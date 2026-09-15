"""
Process and generate YAML answers for Group 1 units:
- CHCCCS040
- CHCCOM005
- HLTINF006
- CHCAGE013
"""
import os
import sys
import re
import yaml
import docx
from extractor_utils import extract_answer_items, get_all_tables_recursive

def clean_text(s):
    if not s: return ""
    return " ".join(str(s).replace('\u2002', ' ').split())

W_NS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
W14_NS = 'http://schemas.microsoft.com/office/word/2010/wordml'

CANDIDATE_DETAILS = {
    "candidate_name": "Alex Chen",
    "candidate_phone": "0412 345 678",
    "candidate_email": "alex.chen@email.com.au",
    "date": "15/09/2026",
    "state": "New South Wales",
    "workplace": "Care Connect Services",
    "rto": "Care Connect College",
    "rto_phone": "1300 123 456",
    "rto_email": "info@careconnectcollege.edu.au"
}

def build_ag_index(ag_docx_path):
    doc = docx.Document(ag_docx_path)
    all_tables = get_all_tables_recursive(doc)
    index = []
    
    for t_idx, t in enumerate(all_tables):
        rows_data = []
        full_text = []
        for r_idx, r in enumerate(t.rows):
            cells_text = [" ".join(c.text.split()) for c in r.cells]
            rows_data.append(cells_text)
            full_text.append(" ".join(cells_text))
            
        t_text = " ".join(full_text)
        
        # Check mapping or question header
        m_q = re.search(r'(Question\s+\d+|Task\s+[\d\.]+|Preliminary Task|Scenario\s+\d+|Complete the table|Case Study)', t_text, re.IGNORECASE)
        q_label = m_q.group(1) if m_q else f"Table_{t_idx}"
        
        index.append({
            "table_idx": t_idx,
            "q_label": q_label,
            "text": t_text,
            "rows": rows_data,
            "table_obj": t
        })
    return index

def find_best_ag_match(ag_index, prompt, row_header="", col_header="", item_idx=0):
    prompt_clean = clean_text(prompt).lower()
    row_clean = clean_text(row_header).lower()
    col_clean = clean_text(col_header).lower()
    
    # Priority 1: Match by row_header + col_header in table rows
    if row_clean and len(row_clean) > 3:
        for entry in ag_index:
            for r in entry["rows"]:
                if len(r) > 1:
                    r_text = " ".join(r).lower()
                    if row_clean in r[0].lower() or row_clean in r_text:
                        # Return answer cell
                        ans_cand = r[-1] if len(r) > 1 else r[0]
                        items = extract_answer_items(ans_cand)
                        if items:
                            return items[item_idx] if item_idx < len(items) else items[-1]
                        if len(clean_text(ans_cand)) > 5:
                            return clean_text(ans_cand)
                            
    # Priority 2: Match by prompt keywords
    words = [w for w in re.findall(r'\b[a-zA-Z]{4,}\b', prompt_clean) if w not in ['candidate', 'satisfactory', 'performance', 'must', 'below', 'response']]
    best_entry = None
    best_score = 0
    for entry in ag_index:
        score = sum(1 for w in words if w in entry["text"].lower())
        if score > best_score:
            best_score = score
            best_entry = entry
            
    if best_entry and best_score >= 2:
        # Search rows in best_entry
        for r in best_entry["rows"]:
            r_str = " ".join(r)
            items = extract_answer_items(r_str)
            if items:
                return items[item_idx] if item_idx < len(items) else items[-1]
        items = extract_answer_items(best_entry["text"])
        if items:
            return items[item_idx] if item_idx < len(items) else items[-1]
            
    return ""

def process_unit(unit_code, awb_path, ag_path, output_yaml, specific_overrides=None):
    print(f"\n{'='*30} Processing {unit_code} {'='*30}")
    print(f"AWB: {awb_path}")
    print(f"AG:  {ag_path}")
    
    awb_doc = docx.Document(awb_path)
    ag_index = build_ag_index(ag_path)
    
    data = {
        "unit": unit_code,
        "candidate_details": CANDIDATE_DETAILS,
        "fields": []
    }
    
    total_tables = len(awb_doc.tables)
    
    cand_start = None
    assessor_start = None
    for i, t in enumerate(awb_doc.tables):
        txt = " ".join(c.text.strip() for r in t.rows for c in r.cells).lower()
        if 'to the candidate' in txt and cand_start is None:
            cand_start = i
        if ('to the assessor' in txt or 'record of assessment' in txt) and assessor_start is None and cand_start is not None:
            assessor_start = i

    for t_idx, t in enumerate(awb_doc.tables):
        t_text = " ".join([c.text.strip().replace('\u2002', '') for r in t.rows for c in r.cells if c.text.strip()])
        t_text_lower = t_text.lower()
        
        # Section detection
        if t_idx in [1, 2]:
            section = "Cover Sheet"
        elif "preliminary task" in t_text_lower or (cand_start is not None and t_idx < 5 and "state" in t_text_lower):
            section = "Preliminary Task"
        elif "to be completed by the manager" in t_text_lower or (assessor_start is not None and t_idx >= assessor_start) or "record of assessment" in t_text_lower:
            section = "Assessor Section"
        elif cand_start is not None and t_idx >= cand_start:
            section = "Candidate Checklist"
        elif "case study" in t_text_lower or "workplace assessment" in t_text_lower or "incident report" in t_text_lower or "client information" in t_text_lower:
            section = "Practical Assessment"
        else:
            section = "Knowledge Assessment"
            
        m_q = re.search(r'(Question\s+\d+|Task\s+[\d\.]+|Complete the table|Answer the following|Read the scenario|Briefly define|List down|Identify)', t_text, re.IGNORECASE)
        q_ref = m_q.group(1) if m_q else f"Table_{t_idx}"
        
        for r_idx, r in enumerate(t.rows):
            row_header = r.cells[0].text.strip().replace('\u2002', '').strip() if len(r.cells) > 0 else ""
            seen_tc = set()
            for c_idx, c in enumerate(r.cells):
                if id(c._tc) in seen_tc:
                    continue
                seen_tc.add(id(c._tc))
                
                col_header = ""
                if len(t.rows) > 0 and c_idx < len(t.rows[0].cells):
                    col_header = t.rows[0].cells[c_idx].text.strip().replace('\u2002', '').strip()
                cell_elem = c._element
                
                ff_list = cell_elem.findall(f'.//{{{W_NS}}}ffData')
                cb_list = cell_elem.findall(f'.//{{{W14_NS}}}checkbox')
                
                if not ff_list and not cb_list:
                    continue
                    
                # Handle checkboxes
                for cb_i, cb in enumerate(cb_list):
                    curr = cb
                    while curr is not None and not curr.tag.endswith('sdt'):
                        curr = curr.getparent()
                    sdt_id = ""
                    if curr is not None:
                        id_el = curr.find(f'.//{{{W_NS}}}id')
                        if id_el is not None:
                            sdt_id = id_el.get(f'{{{W_NS}}}val')
                            
                    cb_label = c.text.strip().replace('\n', ' ')
                    if not cb_label and c_idx + 1 < len(r.cells):
                        cb_label = r.cells[c_idx + 1].text.strip()
                    if not cb_label:
                        cb_label = f"Row {r_idx} Col {c_idx}"
                        
                    cb_value = False
                    if section == "Preliminary Task":
                        if "new south wales" in cb_label.lower():
                            cb_value = True
                    elif section == "Candidate Checklist":
                        if re.search(r'\bno\b', cb_label.lower()):
                            cb_value = False
                        else:
                            cb_value = True
                    elif section == "Practical Assessment":
                        # Check abuse/injury indicators or standard checkboxes
                        if any(w in cb_label.lower() for w in ['bruise', 'burn', 'fear', 'withdrawn', 'injury', 'depression', 'anxiety', 'yes']):
                            cb_value = True
                    elif section == "Assessor Section":
                        cb_value = False
                            
                    field_id = f"{unit_code}_CB_{t_idx}_{r_idx}_{c_idx}_{cb_i+1}"
                    data["fields"].append({
                        "field_id": field_id,
                        "type": "checkbox",
                        "section": section,
                        "question_ref": q_ref,
                        "label": cb_label[:100],
                        "table_idx": t_idx,
                        "row_idx": r_idx,
                        "col_idx": c_idx,
                        "index_in_cell": cb_i,
                        "sdt_id": sdt_id,
                        "value": cb_value
                    })
                    
                # Handle text fields
                for ff_i, ff in enumerate(ff_list):
                    curr = ff
                    while curr is not None and not curr.tag.endswith('p'):
                        curr = curr.getparent()
                    para_id = curr.get(f'{{{W14_NS}}}paraId', '') if curr is not None else ""
                    
                    prompt_snippet = c.text.strip().replace('\u2002', '').strip()
                    if not prompt_snippet:
                        prompt_snippet = f"{row_header} - {col_header}".strip(" -")
                    if not prompt_snippet:
                        prompt_snippet = f"Table {t_idx} Row {r_idx} Col {c_idx}"
                        
                    answer = ""
                    if section == "Cover Sheet":
                        if t_idx == 1:
                            if r_idx == 2: answer = CANDIDATE_DETAILS["candidate_name"]
                            elif r_idx == 3: answer = CANDIDATE_DETAILS["candidate_phone"]
                            elif r_idx == 4: answer = CANDIDATE_DETAILS["candidate_email"]
                        elif t_idx == 2:
                            if c_idx == 0: answer = CANDIDATE_DETAILS["candidate_name"]
                            elif c_idx == 1: answer = CANDIDATE_DETAILS["candidate_name"]
                            elif c_idx == 2: answer = CANDIDATE_DETAILS["date"]
                    elif section == "Candidate Checklist":
                        if "date" in prompt_snippet.lower():
                            answer = CANDIDATE_DETAILS["date"]
                        elif "signature" in prompt_snippet.lower() or "name" in prompt_snippet.lower():
                            answer = CANDIDATE_DETAILS["candidate_name"]
                    elif section == "Assessor Section":
                        if "candidate" in prompt_snippet.lower():
                            answer = CANDIDATE_DETAILS["candidate_name"]
                        elif "rto name" in prompt_snippet.lower():
                            answer = CANDIDATE_DETAILS["rto"]
                        elif "rto contact" in prompt_snippet.lower():
                            answer = CANDIDATE_DETAILS["rto_phone"]
                        elif "rto email" in prompt_snippet.lower():
                            answer = CANDIDATE_DETAILS["rto_email"]
                    else:
                        # Check specific overrides first
                        if specific_overrides and (t_idx, r_idx, c_idx, ff_i) in specific_overrides:
                            answer = specific_overrides[(t_idx, r_idx, c_idx, ff_i)]
                        elif specific_overrides and (t_idx, r_idx, c_idx) in specific_overrides:
                            answer = specific_overrides[(t_idx, r_idx, c_idx)]
                        elif specific_overrides and (t_idx, r_idx) in specific_overrides:
                            val = specific_overrides[(t_idx, r_idx)]
                            if isinstance(val, list):
                                answer = val[ff_i] if ff_i < len(val) else val[-1]
                            else:
                                answer = val
                        else:
                            answer = find_best_ag_match(ag_index, prompt_snippet, row_header, col_header, ff_i)
                            
                        # Practical Assessment generic defaults if AG lookup was empty
                        if not answer and section == "Practical Assessment":
                            if "workplace" in prompt_snippet.lower() or "organisation" in prompt_snippet.lower():
                                answer = CANDIDATE_DETAILS["workplace"]
                            elif "supervisor" in prompt_snippet.lower():
                                answer = "Sarah Jenkins, RN / Care Coordinator"
                            elif "date" in prompt_snippet.lower():
                                answer = CANDIDATE_DETAILS["date"]
                            elif "signature" in prompt_snippet.lower():
                                answer = CANDIDATE_DETAILS["candidate_name"]
                                
                    field_id = f"{unit_code}_TXT_{t_idx}_{r_idx}_{c_idx}_{ff_i+1}"
                    data["fields"].append({
                        "field_id": field_id,
                        "type": "text",
                        "section": section,
                        "question_ref": q_ref,
                        "label": prompt_snippet[:100],
                        "table_idx": t_idx,
                        "row_idx": r_idx,
                        "col_idx": c_idx,
                        "index_in_cell": ff_i,
                        "para_id": para_id,
                        "value": answer
                    })
                    
    print(f"Total fields extracted for {unit_code}: {len(data['fields'])}")
    with open(output_yaml, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)
    print(f"Saved {output_yaml}")
    
    # Check empty candidate fields
    empty_cand = [f for f in data['fields'] if f['type'] == 'text' and f['section'] != 'Assessor Section' and (not f['value'] or not str(f['value']).strip())]
    print(f"Empty candidate text fields in {unit_code}: {len(empty_cand)}")
    for ec in empty_cand[:10]:
        print(f"   * Table {ec['table_idx']} Row {ec['row_idx']} Col {ec['col_idx']} idx{ec['index_in_cell']}: {ec['label'][:60]}")
    return data

from group1_overrides import CHCCCS040_OVERRIDES, CHCCOM005_OVERRIDES, HLTINF006_OVERRIDES, CHCAGE013_OVERRIDES

def main():
    units = [
        ("CHCCCS040", "3. CHCCCS040 - Support independence and wellbeing/CHCCCS040-AWB-F-v1.0.docx", "3. CHCCCS040 - Support independence and wellbeing/CHCCCS040-AG-F-v1.0.docx", "answers_CHCCCS040.yaml", CHCCCS040_OVERRIDES),
        ("CHCCOM005", "5. CHCCOM005 - Communicate and work in health or community services/CHCCOM005-AWB-F-v1.1.docx", "5. CHCCOM005 - Communicate and work in health or community services/CHCCOM005-AG-F-v1.1.docx", "answers_CHCCOM005.yaml", CHCCOM005_OVERRIDES),
        ("HLTINF006", "8. HLTINF006 - Apply basic principles and practices of infection prevention and control/HLTINF006-AWB-F-v1.0.docx", "8. HLTINF006 - Apply basic principles and practices of infection prevention and control/HLTINF006-AG-F-v1.0.docx", "answers_HLTINF006.yaml", HLTINF006_OVERRIDES),
        ("CHCAGE013", "11. CHCAGE013 - Work effectively in aged care/CHCAGE013-AWB-F-v1.0.docx", "11. CHCAGE013 - Work effectively in aged care/CHCAGE013-AG-F-v1.1.docx", "answers_CHCAGE013.yaml", CHCAGE013_OVERRIDES)
    ]
    for code, awb_p, ag_p, out_yaml, overrides in units:
        process_unit(code, awb_p, ag_p, out_yaml, overrides)

if __name__ == "__main__":
    main()
