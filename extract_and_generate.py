"""
Extract questions, tables, and input fields from Assessment Workbooks (AWB),
correlate them with benchmark answers in Assessor Guides (AG),
and generate reviewable YAML and JSON answer files.
"""
import os
import re
import json
import yaml
import docx
from extractor_utils import clean_model_answer

W_NS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
W14_NS = 'http://schemas.microsoft.com/office/word/2010/wordml'

NSW_ANSWERS_CHCDIS020 = {
    # Question 18: State/Territory Legislation
    "q18_legislation": "Disability Inclusion Act 2014 No 41 (NSW)",
    "q18_role": "The Disability Inclusion Act 2014 (NSW) acknowledges that people with disability have the same human rights as other members of the community. It promotes their independence and social and economic inclusion, and requires NSW government departments and local councils to develop Disability Inclusion Action Plans (DIAPs).",
    "q18_requirement": "People with disability have the right to participate in and contribute to social and economic life and should be supported to develop and use their skills and to make decisions that affect their lives.",
    "q18_section": "Part 2, Section 4 (General principles)",
    "q18_promote_rights": "Ensuring support workers adhere to this requirement upholds the individual's autonomy, dignity, and active involvement in planning their own care and lifestyle choices, rather than imposing decisions upon them.",
    
    # Question 20: State/Territory Statutory Bodies
    "q20_body_1": "NSW Ageing and Disability Commission (ADC)",
    "q20_role_1": "An independent statutory body established to better protect older adults and adults with disability from abuse, neglect, and exploitation in home and community settings, and to investigate reports of abuse.",
    "q20_promote_1": "Promotes rights by providing a dedicated reporting helpline, independently investigating allegations of abuse, and educating families, service providers, and communities to safeguard vulnerable individuals.",
    "q20_body_2": "Disability Council NSW",
    "q20_role_2": "The official statutory advisory body that advises the NSW Government on public policy, legislation, and services affecting people with disability, their families, and carers.",
    "q20_promote_2": "Promotes rights by ensuring the direct lived experience and human rights of people with disability inform state policies, infrastructure, transport, and community accessibility initiatives.",
    
    # Question 21: Mandatory Reporting
    "q21_legislation": "Children and Young Persons (Care and Protection) Act 1998 No 157 (NSW) and Ageing and Disability Commissioner Act 2019 (NSW)",
    "q21_people_mandatory": "Prescribed mandatory reporters include registered disability support practitioners, healthcare professionals (doctors, registered nurses), teachers, and child protection workers who deliver health care, welfare, education, or disability services to children and young people.",
    "q21_grounds": "A mandatory reporter must make a report if they have reasonable grounds to suspect that a child or young person is at significant harm due to physical abuse, sexual abuse, emotional/psychological abuse, or severe neglect.",
    "q21_statutory_body": "NSW Department of Communities and Justice (Child Protection Helpline) and NSW Ageing and Disability Commission (ADC)",
    
    # Question 22: Privacy and Confidentiality
    "q22_legislation": "Privacy and Personal Information Protection Act 1998 (PPIP Act) (NSW) and Health Records and Information Privacy Act 2002 (HRIP Act) (NSW)",
    "q22_principles": "1. Lawful collection for direct purposes (Information Protection Principle 1)\n2. Secure storage and protection against loss or unauthorized access (Information Protection Principle 4)\n3. Transparency and open access allowing individuals to view and correct their personal health information (Information Protection Principle 6)",
    "q22_consequences": "Breaching privacy laws can result in formal complaints to the NSW Privacy Commissioner, regulatory sanctions, internal disciplinary action including dismissal, civil liability for damages, and loss of organizational accreditation.",
    
    # Question 25: Codes of Conduct
    "q25_code": "NDIS Code of Conduct and NSW Health Code of Conduct for Healthcare and Disability Support Workers",
    "q25_requirement": "Act with integrity, honesty, and transparency; promptly take steps to raise and act on concerns regarding matters that might impact the quality and safety of supports provided to people with disability.",
    "q25_promote_rights": "Ensures that participants receive ethical, safe, and person-centred care, and protects them from fraudulent practices, mistreatment, or negligence."
}

NSW_ANSWERS_CHCPAL003 = {
    # Question 19: State/Territory Medico-Legal Requirements
    "q19_acd_legislation": "Guardianship Act 1987 (NSW) and Advance Care Directives under NSW Common Law",
    "q19_acd_role": "Provides the legal framework for recognizing valid advance care directives (living wills) and appointing enduring guardians to make personal and medical treatment decisions when an individual loses decision-making capacity.",
    "q19_acd_requirements": "1. An Advance Care Directive must be made voluntarily by an adult with decision-making capacity.\n2. It applies only when the individual becomes incapable of giving or withholding consent to treatment.\n3. Healthcare workers and guardians must respect valid refusal of specific medical treatments.",
    "q19_eol_legislation": "Voluntary Assisted Dying Act 2022 No 17 (NSW) and NSW Health End of Life Care Policy",
    "q19_eol_role": "Regulates lawful end-of-life decisions, palliative treatment options, and voluntary assisted dying procedures, establishing strict eligibility, consultation, and conscientious objection standards.",
    "q19_eol_requirements": "1. Palliative care must focus on pain management and comfort care.\n2. Workers must ensure documentation of do-not-resuscitate (DNR) and comfort measures.\n3. All treatments must align with the patient's documented wishes and best clinical practice."
}

def get_all_tables_recursive(container):
    """Recursively collect all top-level and nested tables."""
    tables = []
    for t in container.tables:
        tables.append(t)
        for r in t.rows:
            for c in r.cells:
                if c.tables:
                    tables.extend(get_all_tables_recursive(c))
    return tables

def extract_all_ag_text(ag_doc):
    """Pre-extract all tables (including all nested tables) and cells in AG doc."""
    ag_index = []
    for t_idx, t in enumerate(get_all_tables_recursive(ag_doc)):
        table_rows = []
        for r in t.rows:
            row_cells = [c.text.strip() for c in r.cells]
            table_rows.append(row_cells)
        table_text = ' '.join(c for r in table_rows for c in r if c)
        ag_index.append({
            'table_idx': t_idx,
            'text': table_text,
            'rows': table_rows
        })
    return ag_index

def find_best_ag_answer_for_cell(ag_index, question_hint, prompt_hint, row_header, col_header, item_index=0):
    """Fast search across pre-extracted AG table data for the corresponding model answer."""
    # 1. Exact row header match
    if row_header and len(row_header) > 4:
        row_h_lower = row_header.lower()
        for item in ag_index:
            rows = item['rows']
            for r in rows:
                if len(r) >= 2:
                    first_cell = r[0]
                    if row_h_lower in first_cell.lower():
                        if col_header and len(rows) > 0 and len(rows[0]) > 1:
                            header_row = [c.lower() for c in rows[0]]
                            for c_i, h_txt in enumerate(header_row):
                                if col_header.lower() in h_txt and c_i < len(r):
                                    ans = r[c_i]
                                    if ans and ans != first_cell:
                                        res = clean_model_answer(ans, item_index=item_index)
                                        if res: return res
                                        return ans.strip()
                        ans = r[1]
                        if ans and ans != first_cell:
                            res = clean_model_answer(ans, item_index=item_index)
                            if res: return res
                            return ans.strip()

    # 2. Prompt hint match in question tables
    if prompt_hint and len(prompt_hint) > 10:
        cleaned_prompt = prompt_hint.lower().replace('\n', ' ')[:30]
        for item in ag_index:
            if cleaned_prompt in item['text'].lower():
                for r in item['rows']:
                    for c in r:
                        c_lower = c.lower()
                        if any(k in c_lower for k in ['benchmark answer', 'model answer', 'satisfactory performance']):
                            cleaned = clean_model_answer(c, item_index=item_index)
                            if cleaned and len(cleaned) > 10:
                                return cleaned

    return ""



def process_chcdis020(awb_path, ag_path):
    print(f"Processing {awb_path}...")
    awb = docx.Document(awb_path)
    ag = docx.Document(ag_path)
    ag_index = extract_all_ag_text(ag)
    
    data = {
        "unit": "CHCDIS020",
        "title": "Work effectively in disability support",
        "candidate_details": {
            "candidate_name": "Alex Chen",
            "candidate_phone": "0412 345 678",
            "candidate_email": "alex.chen@careconnectcollege.edu.au",
            "rto_name": "CareConnect College",
            "trainer_assessor_name": "Assessment Assessor",
            "date": "15/09/2026",
            "candidate_declaration_agreed": True
        },
        "preliminary_task": {
            "selected_state": "New South Wales",
            "notes": "State selected for Questions 18, 20, 21, 22, 25"
        },
        "fields": []
    }
    
    field_counter = 1
    
    for t_idx, t in enumerate(awb.tables):
        # Determine section
        table_text = ' '.join(c.text.strip().replace('\n', ' ') for r in t.rows for c in r.cells if c.text.strip())
        
        section = "Unknown"
        if t_idx in [1, 2]:
            section = "Cover Sheet"
        elif t_idx == 3:
            section = "Preliminary Task"
        elif 4 <= t_idx <= 71:
            section = "Knowledge Assessment"
        elif 72 <= t_idx <= 124:
            section = "Practical Assessment"
        elif 125 <= t_idx <= 127:
            section = "Candidate Checklist"
        elif t_idx >= 128:
            section = "Assessor Section"
            
        # Detect Question header in or before table
        q_ref = f"Table_{t_idx}"
        if section == "Knowledge Assessment":
            # search for question indicator
            m = re.search(r'(Question\s+\d+|Complete the table|Answer the following|Read the scenario|Briefly define|Which standard)', table_text)
            if m:
                q_ref = m.group(1)
        elif section == "Practical Assessment":
            m = re.search(r'(Scenario\s+\d+|Task\s+[\d\.]+|Incident Report|CareConnect)', table_text)
            if m:
                q_ref = m.group(1)
                
        # Iterate cells
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
                
                # Check for form text fields
                ff_list = cell_elem.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}ffData')
                # Check for checkboxes
                cb_list = cell_elem.findall('.//{http://schemas.microsoft.com/office/word/2010/wordml}checkbox')
                
                if not ff_list and not cb_list:
                    continue
                
                # Checkbox handling
                for cb_i, cb in enumerate(cb_list):
                    sdt = cb
                    # find parent sdt
                    curr = cb
                    while curr is not None and not curr.tag.endswith('sdt'):
                        curr = curr.getparent()
                    sdt_id = ""
                    if curr is not None:
                        id_el = curr.find('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}id')
                        if id_el is not None:
                            sdt_id = id_el.get(f'{{{W_NS}}}val')
                            
                    # Determine label and value
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
                        # Candidate confirms Yes for all items
                        if "yes" in cb_label.lower() or "tick" in cb_label.lower() or c_idx == 1:
                            cb_value = True
                    elif section == "Knowledge Assessment":
                        # Check if True/False question
                        if "false" in cb_label.lower() and t_idx in [7, 30, 38, 43]:
                            cb_value = True
                    elif section == "Practical Assessment":
                        # Abuse indicator checkboxes
                        if t_idx in [78, 79, 80, 81, 95, 96, 97, 98]:
                            # mark confirmed indicators
                            if any(w in cb_label.lower() for w in ['bruise', 'burn', 'fear', 'withdrawn', 'injury', 'depression', 'anxiety']):
                                cb_value = True
                                
                    field_id = f"CHCDIS020_CB_{t_idx}_{r_idx}_{c_idx}_{cb_i+1}"
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
                    
                # Text form field handling
                for ff_i, ff in enumerate(ff_list):
                    # Get paragraph id
                    curr = ff
                    while curr is not None and not curr.tag.endswith('p'):
                        curr = curr.getparent()
                    para_id = ""
                    if curr is not None:
                        para_id = curr.get(f'{{{W14_NS}}}paraId', '')
                        
                    prompt_snippet = c.text.strip().replace('\u2002', '').strip()
                    if not prompt_snippet:
                        prompt_snippet = f"{row_header} - {col_header}".strip(" -")
                    if not prompt_snippet:
                        prompt_snippet = f"Table {t_idx} Row {r_idx} Col {c_idx}"
                        
                    # Find answer from AG
                    answer = ""
                    if section == "Cover Sheet":
                        if t_idx == 1:
                            if r_idx == 2:
                                answer = data["candidate_details"]["candidate_name"]
                            elif r_idx == 3:
                                answer = data["candidate_details"]["candidate_phone"]
                            elif r_idx == 4:
                                answer = data["candidate_details"]["candidate_email"]
                        elif t_idx == 2:
                            if c_idx == 0:
                                answer = data["candidate_details"]["candidate_name"]
                            elif c_idx == 1:
                                answer = data["candidate_details"]["candidate_name"]
                            elif c_idx == 2:
                                answer = data["candidate_details"]["date"]
                    elif section == "Knowledge Assessment":
                        # Specific multi-part questions handling
                        if t_idx == 9: # Q3 Bipolar disorder
                            if r_idx == 0:
                                answer = "Bipolar disorder"
                            elif r_idx == 2:
                                if c_idx == 0: answer = "Manic episode"
                                elif c_idx == 1: answer = "This is a period of at least one week during which a person has more energy than usual, feels unusually elated, irritable, or agitated."
                                elif c_idx == 2: answer = "Introduce relaxation strategies to the person"
                                elif c_idx >= 3: answer = "Educate the person’s carer about the relaxation strategies that they can assist the person with"
                            elif r_idx == 4:
                                if c_idx == 0: answer = "Depressive episode"
                                elif c_idx == 1: answer = "This is a period of at least two weeks during which a person has at least five symptoms: feeling sad/miserable most of the time, loss of interest/pleasure, sleep changes, fatigue, feelings of worthlessness, or difficulty concentrating."
                                elif c_idx == 2: answer = "Encourage the person to join social activities in their local community"
                                elif c_idx >= 3: answer = "Provide a list of same-interest groups that the person can participate to make connections with others"
                        elif t_idx == 10: # Q4 Anne scenario
                            if r_idx == 2: # Rachel - visual
                                visual_ways = [
                                    "Anne can provide a clear word picture when describing things to them. This includes details such as colour, texture, shape and landmarks.",
                                    "Anne can greet Rachel as she enters a room or location to let them know they are there."
                                ]
                                answer = visual_ways[ff_i] if ff_i < len(visual_ways) else visual_ways[-1]
                            elif r_idx == 3: # Carla - hearing
                                hearing_ways = [
                                    "Anne can maintain eye contact while communicating with Carla.",
                                    "Anne can use gestures and clear facial expressions to help Carla understand what she is saying."
                                ]
                                answer = hearing_ways[ff_i] if ff_i < len(hearing_ways) else hearing_ways[-1]
                        elif t_idx == 12: # Q5 Individualised plans
                            if r_idx == 2:
                                answer = "Individualised care plans serve as a guide in providing the appropriate strategies to meet the person’s goals and needs."
                            elif r_idx == 3:
                                plan_contents = [
                                    "The person’s basic information (name, history, condition, allergies if any).",
                                    "The person’s holistic needs (physical, emotional, psychological, and spiritual).",
                                    "The person’s wants and preferences.",
                                    "The person’s goals in terms of their holistic needs.",
                                    "The person’s support schedule, which includes tasks, frequency of tasks, and equipment needed."
                                ]
                                answer = plan_contents[ff_i] if ff_i < len(plan_contents) else plan_contents[-1]
                        elif t_idx == 13: # Q6 Person-centred approach
                            if r_idx == 2:
                                answer = "The person-centred approach in disability focuses on improving the person’s overall quality of life based on personal goals and preferences. On the contrary, the traditional approach focuses on managing the person’s illness and medical condition based on clinical or medical advice."
                            elif r_idx == 3:
                                pc_benefits = [
                                    "PWDs will generally have an easier time trusting those who apply person-centred approaches.",
                                    "PWDs will be more compliant with routines, activities, and programs designed based on their needs and wants.",
                                    "Support workers will not have difficulty creating support strategies or complicated care procedures."
                                ]
                                answer = pc_benefits[ff_i] if ff_i < len(pc_benefits) else pc_benefits[-1]
                        elif t_idx == 32: # Q17 DDA
                            if r_idx == 3:
                                answer = "To ensure, as far as practicable, that persons with disabilities have the same rights to equality before the law as the rest of the community."
                            elif r_idx == 5:
                                if c_idx == 0:
                                    if ff_i == 0:
                                        answer = "A person (the discriminator) discriminates against another person (the aggrieved person) on the ground of a disability of the aggrieved person if, because of the disability, the discriminator treats, or proposes to treat, the aggrieved person less favourably than the discriminator would treat a person without the disability in circumstances that are not materially different."
                                    else:
                                        answer = "Section 5 (1)"
                                elif c_idx >= 3:
                                    answer = "Treating a person with disability the same way as others without disability will make them feel respected and valued as individuals."
                        elif t_idx == 33: # Q18 NSW legislation
                            if "legislation" in prompt_snippet.lower() or r_idx == 2:
                                answer = NSW_ANSWERS_CHCDIS020["q18_legislation"]
                            elif "role" in prompt_snippet.lower() or r_idx == 3:
                                answer = NSW_ANSWERS_CHCDIS020["q18_role"]
                            elif "requirement" in prompt_snippet.lower() or r_idx == 4:
                                answer = NSW_ANSWERS_CHCDIS020["q18_requirement"]
                            elif "section" in prompt_snippet.lower() or r_idx == 5:
                                answer = NSW_ANSWERS_CHCDIS020["q18_section"]
                            else:
                                answer = NSW_ANSWERS_CHCDIS020["q18_promote_rights"]
                        elif t_idx in [36, 37]: # Q20 NSW statutory bodies
                            if r_idx == 1 or "1" in prompt_snippet:
                                answer = NSW_ANSWERS_CHCDIS020["q20_body_1"] if c_idx == 0 else NSW_ANSWERS_CHCDIS020["q20_role_1"]
                            else:
                                answer = NSW_ANSWERS_CHCDIS020["q20_body_2"] if c_idx == 0 else NSW_ANSWERS_CHCDIS020["q20_role_2"]
                        elif t_idx in [39, 40]: # Q21 NSW mandatory reporting
                            if "legislation" in prompt_snippet.lower() or r_idx == 1:
                                answer = NSW_ANSWERS_CHCDIS020["q21_legislation"]
                            elif "mandatory" in prompt_snippet.lower() or r_idx == 2:
                                answer = NSW_ANSWERS_CHCDIS020["q21_people_mandatory"]
                            elif "grounds" in prompt_snippet.lower() or r_idx == 3:
                                answer = NSW_ANSWERS_CHCDIS020["q21_grounds"]
                            else:
                                answer = NSW_ANSWERS_CHCDIS020["q21_statutory_body"]
                        elif t_idx in [41, 42]: # Q22 Privacy & 13 APPs
                            if r_idx == 3: # 13 APPs
                                apps = [
                                    "APP 1: Open and transparent management of personal information",
                                    "APP 2: Anonymity and pseudonymity",
                                    "APP 3: Collection of solicited personal information",
                                    "APP 4: Dealing with unsolicited personal information",
                                    "APP 5: Notification of the collection of personal information",
                                    "APP 6: Use or disclosure of personal information",
                                    "APP 7: Direct marketing",
                                    "APP 8: Cross-border disclosure of personal information",
                                    "APP 9: Adoption, use or disclosure of government related identifiers",
                                    "APP 10: Quality of personal information",
                                    "APP 11: Security of personal information",
                                    "APP 12: Access to personal information",
                                    "APP 13: Correction of personal information"
                                ]
                                answer = apps[ff_i] if ff_i < len(apps) else apps[-1]
                            elif "legislation" in prompt_snippet.lower() or r_idx == 1:
                                answer = NSW_ANSWERS_CHCDIS020["q22_legislation"]
                            elif "principles" in prompt_snippet.lower() or r_idx == 2:
                                answer = NSW_ANSWERS_CHCDIS020["q22_principles"]
                            else:
                                answer = NSW_ANSWERS_CHCDIS020["q22_consequences"]
                        elif t_idx == 43: # Q23 Consent
                            if r_idx == 2:
                                answer = "The Partnering with Consumers Standard aims to ensure that consumers are involved in the planning, design, delivery and evaluation of systems and services."
                            elif r_idx == 3:
                                answer = "False. Informed consent is not always needed; it may be overridden in emergency situations where life-saving care is immediately required."
                            elif r_idx == 4:
                                consent_elements = [
                                    "The person must have decision-making capacity to give consent.",
                                    "Consent must be given freely and voluntarily without pressure or coercion.",
                                    "Consent must be informed with full disclosure of benefits, risks, and alternatives."
                                ]
                                answer = consent_elements[ff_i] if ff_i < len(consent_elements) else consent_elements[-1]
                            else:
                                answer = "Informed consent promotes rights by upholding the individual's autonomy, bodily integrity, and right to self-determination."
                        elif t_idx == 45: # Q25 Codes of conduct
                            if r_idx == 2:
                                answer = "To set clear standards and expectations for ethical conduct and safe, high-quality service delivery."
                            elif r_idx == 3:
                                answer = "https://www.ndiscommission.gov.au/providers/ndis-code-conduct"
                            elif r_idx == 4:
                                coc_reqs = [
                                    "Act with respect for individual rights to freedom of expression, self-determination and decision-making.",
                                    "Respect the privacy of people with disability.",
                                    "Provide supports and services in a safe and competent manner with care and skill."
                                ]
                                answer = coc_reqs[ff_i] if ff_i < len(coc_reqs) else coc_reqs[-1]
                            else:
                                answer = NSW_ANSWERS_CHCDIS020["q25_promote_rights"]
                        elif t_idx == 54: # Philosophies
                            if r_idx == 4: answer = "Social Role Valorisation is the use of culturally valued means to enable people with disability to live culturally valued lives and assume socially valued roles."
                            elif r_idx == 6: answer = "Social model of disability"
                            elif r_idx == 7: answer = "It views disability as a consequence of environmental, social, and attitudinal barriers rather than an individual's medical deficit or personal impairment."
                            else: answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                        elif t_idx == 55: # Trauma-informed practice principles
                            if r_idx == 2:
                                ti_principles = ["Safety", "Trust", "Choice", "Collaboration", "Empowerment", "Respect for Diversity"]
                                answer = ti_principles[ff_i] if ff_i < len(ti_principles) else ti_principles[-1]
                            else:
                                answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                        elif t_idx == 56: # Wellbeing
                            if r_idx == 2: answer = "Social and emotional wellbeing refers to a positive state of mental health that enables people to function effectively in everyday life, cope with stress, and engage with their communities."
                            elif r_idx == 3: answer = "By providing access to inclusive community activities, supporting self-advocacy, and maintaining strong relationships with family, friends, and support networks."
                            else: answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                        elif t_idx == 60: # Reporting lines
                            if r_idx == 2: answer = "Reporting lines define authority, escalation pathways, accountability, and communication flows within the organization."
                            elif r_idx == 3: answer = "Direct Supervisor / Team Leader"
                            elif r_idx == 4: answer = "Disability Support Service Manager"
                            elif r_idx == 5: answer = "Chief Executive Officer (CEO) / Executive Director"
                            else: answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                        elif t_idx == 62: # Key organisations in disability support sector
                            if r_idx == 3:
                                if c_idx == 0: answer = "Australian Council of Social Services (ACOSS)"
                                else: answer = "The Australian Council of Social Service is a national advocate supporting people affected by poverty, disadvantage and inequality, and the peak council for community services nationally."
                            elif r_idx == 4:
                                if c_idx == 0: answer = "Aged and Community Services Australia (ACSA)"
                                else: answer = "ACSA exists to support an equitable and just aged care and disability support sector that Australians can trust to offer quality of life, choice and accessibility."
                            elif r_idx == 5:
                                if c_idx == 0: answer = "Children with Disability Australia (CDA)"
                                else: answer = "CYDA's purpose is to ensure governments, communities and families, are empowering children and young people with disability to fully exercise their rights and aspirations."
                            else:
                                answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                        elif t_idx == 68: # Risk assessment
                            if r_idx == 3:
                                risk_phases = ["1. Risk identification", "2. Risk analysis", "3. Risk evaluation"]
                                answer = risk_phases[ff_i] if ff_i < len(risk_phases) else risk_phases[-1]
                            else:
                                answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                        else:
                            # General lookup from AG
                            answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                    elif section == "Practical Assessment":
                        if t_idx == 112: # Workplace details
                            if r_idx == 0: answer = "Care Connect Disability Services"
                            elif r_idx == 1: answer = "Sarah Jenkins, RN / Care Coordinator"
                        elif t_idx == 113: # Persons A and B
                            if c_idx == 1:
                                if r_idx == 1: answer = "John"
                                elif r_idx == 2: answer = "Mary Smith (Spouse)"
                            elif c_idx == 2:
                                if r_idx == 1: answer = "David"
                                elif r_idx == 2: answer = "Robert Brown (Son / Enduring Guardian)"
                        elif t_idx == 119: # Assist interdisciplinary team members
                            if r_idx == 2: answer = "Collect information about the person’s health and diet as requested by the clinical dietitian/nurse."
                            elif r_idx == 3: answer = "Monitor and record the effects and side effects of pain medications for the person with disability as requested by the Registered Nurse."
                        else:
                            answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                        if not answer:
                            # Fallback for incident reports
                            if "client" in prompt_snippet.lower() or "name" in prompt_snippet.lower():
                                answer = "Jenny Smith" if t_idx < 90 else "John Doe"
                            elif "date" in prompt_snippet.lower():
                                answer = "15/09/2026"
                            elif "location" in prompt_snippet.lower():
                                answer = "CareConnect Community Centre, Hurstville NSW"
                            elif "worker" in prompt_snippet.lower() or "reporter" in prompt_snippet.lower():
                                answer = "Alex Chen, Disability Support Worker"
                    elif section == "Candidate Checklist":
                        if "date" in prompt_snippet.lower():
                            answer = "15/09/2026"
                        elif "signature" in prompt_snippet.lower() or "name" in prompt_snippet.lower():
                            answer = "Alex Chen"
                    elif section == "Assessor Section":
                        if t_idx == 133: # Record of Assessment candidate info
                            if r_idx == 1: answer = "Alex Chen"
                            elif r_idx == 2: answer = "Care Connect College"
                            elif r_idx == 3: answer = "1300 123 456"
                            elif r_idx == 4: answer = "info@careconnectcollege.edu.au"
                            
                    field_id = f"CHCDIS020_TXT_{t_idx}_{r_idx}_{c_idx}_{ff_i+1}"
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
                    field_counter += 1
                    
    print(f"Total fields extracted for CHCDIS020: {len(data['fields'])}")
    return data

def process_chcpal003(awb_path, ag_path):
    print(f"Processing {awb_path}...")
    awb = docx.Document(awb_path)
    ag = docx.Document(ag_path)
    ag_index = extract_all_ag_text(ag)
    
    data = {
        "unit": "CHCPAL003",
        "title": "Deliver care services using a palliative approach",
        "candidate_details": {
            "candidate_name": "Alex Chen",
            "candidate_phone": "0412 345 678",
            "candidate_email": "alex.chen@careconnectcollege.edu.au",
            "rto_name": "CareConnect College",
            "trainer_assessor_name": "Assessment Assessor",
            "date": "15/09/2026",
            "candidate_declaration_agreed": True
        },
        "preliminary_task": {
            "selected_state": "New South Wales",
            "notes": "State selected for Question 19"
        },
        "fields": []
    }
    
    field_counter = 1
    
    for t_idx, t in enumerate(awb.tables):
        table_text = ' '.join(c.text.strip().replace('\n', ' ') for r in t.rows for c in r.cells if c.text.strip())
        
        section = "Unknown"
        if t_idx in [1, 2]:
            section = "Cover Sheet"
        elif t_idx == 3:
            section = "Preliminary Task"
        elif 4 <= t_idx <= 40:
            section = "Knowledge Assessment"
        elif 41 <= t_idx <= 120:
            section = "Practical Assessment"
        elif 121 <= t_idx <= 124:
            section = "Candidate Checklist"
        elif t_idx >= 125:
            section = "Assessor Section"
            
        q_ref = f"Table_{t_idx}"
        if section == "Knowledge Assessment":
            m = re.search(r'(Question\s+\d+|Complete the table|Answer the following|Read the scenario|Briefly define|List down|Identify)', table_text)
            if m:
                q_ref = m.group(1)
        elif section == "Practical Assessment":
            m = re.search(r'(James\s+D|Task\s+[\d\.]+|Case Study|Progress Notes)', table_text)
            if m:
                q_ref = m.group(1)
                
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
                
                ff_list = cell_elem.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}ffData')
                cb_list = cell_elem.findall('.//{http://schemas.microsoft.com/office/word/2010/wordml}checkbox')
                
                if not ff_list and not cb_list:
                    continue
                    
                # Checkbox handling
                for cb_i, cb in enumerate(cb_list):
                    curr = cb
                    while curr is not None and not curr.tag.endswith('sdt'):
                        curr = curr.getparent()
                    sdt_id = ""
                    if curr is not None:
                        id_el = curr.find('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}id')
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
                        if "yes" in cb_label.lower() or "tick" in cb_label.lower() or c_idx == 1:
                            cb_value = True
                    elif section == "Knowledge Assessment":
                        if t_idx == 58: # multiple choice
                            if any(w in cb_label.lower() for w in ['all of the above', 'palliative', 'comfort']):
                                cb_value = True
                                
                    field_id = f"CHCPAL003_CB_{t_idx}_{r_idx}_{c_idx}_{cb_i+1}"
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
                    
                # Text form field handling
                for ff_i, ff in enumerate(ff_list):
                    curr = ff
                    while curr is not None and not curr.tag.endswith('p'):
                        curr = curr.getparent()
                    para_id = ""
                    if curr is not None:
                        para_id = curr.get(f'{{{W14_NS}}}paraId', '')
                        
                    prompt_snippet = c.text.strip().replace('\u2002', '').strip()
                    if not prompt_snippet:
                        prompt_snippet = f"{row_header} - {col_header}".strip(" -")
                    if not prompt_snippet:
                        prompt_snippet = f"Table {t_idx} Row {r_idx} Col {c_idx}"
                        
                    answer = ""
                    if section == "Cover Sheet":
                        if t_idx == 1:
                            if r_idx == 2:
                                answer = data["candidate_details"]["candidate_name"]
                            elif r_idx == 3:
                                answer = data["candidate_details"]["candidate_phone"]
                            elif r_idx == 4:
                                answer = data["candidate_details"]["candidate_email"]
                        elif t_idx == 2:
                            if c_idx == 0:
                                answer = data["candidate_details"]["candidate_name"]
                            elif c_idx == 1:
                                answer = data["candidate_details"]["candidate_name"]
                            elif c_idx == 2:
                                answer = data["candidate_details"]["date"]
                    elif section == "Knowledge Assessment":
                        if t_idx == 5: # Irreversible illnesses
                            illnesses = [
                                "Advanced Metastatic Cancer",
                                "Dementia (including Alzheimer's disease)",
                                "Chronic Obstructive Pulmonary Disease (COPD)",
                                "Motor Neurone Disease (MND)"
                            ]
                            answer = illnesses[ff_i] if ff_i < len(illnesses) else illnesses[-1]
                        elif t_idx == 7: # Emotional impact
                            answer = "Intense grief, anxiety, shock, depression, and fear of pain or loss of independence."
                        elif t_idx == 12: # Unconscious bias
                            answer = "Unconscious bias can cause workers to make unfounded assumptions about a client's cognitive ability or quality of life, leading to patronising communication or undertreatment of pain."
                        elif t_idx == 14: # 4 personal strategies
                            strategies = [
                                "Participating in formal clinical debriefing sessions with colleagues and supervisors.",
                                "Accessing confidential counseling through the Employee Assistance Program (EAP).",
                                "Engaging in regular mindfulness, reflection, or journaling.",
                                "Maintaining physical self-care, exercise, adequate sleep, and work-life boundaries."
                            ]
                            answer = strategies[ff_i] if ff_i < len(strategies) else strategies[-1]
                        elif t_idx == 18: # Pain relief and comfort
                            if r_idx == 1:
                                p_relief = [
                                    "Administering prescribed analgesics on time according to the medication chart.",
                                    "Repositioning the client gently with supportive pillows.",
                                    "Applying warm or cool compresses as approved in the care plan."
                                ]
                                answer = p_relief[ff_i] if ff_i < len(p_relief) else p_relief[-1]
                            elif r_idx == 2:
                                c_promo = [
                                    "Providing regular mouth care and applying lip balm to prevent dry mucous membranes.",
                                    "Ensuring comfortable ambient room temperature, gentle lighting, and quiet environment.",
                                    "Assisting with personal hygiene and fresh, smooth bed linen."
                                ]
                                answer = c_promo[ff_i] if ff_i < len(c_promo) else c_promo[-1]
                            else:
                                answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                        elif t_idx == 22: # Duty of care
                            if r_idx == 2:
                                answer = "The legal and professional obligation to take reasonable care to avoid causing foreseeable harm or injury to clients in care."
                            elif r_idx == 3:
                                duties = [
                                    "Following organizational policies, procedures, and care plans.",
                                    "Maintaining required certifications and clinical skills.",
                                    "Reporting hazards, incidents, and client deterioration promptly.",
                                    "Respecting client confidentiality and dignity at all times.",
                                    "Working within the boundaries of the job role and seeking supervision when required."
                                ]
                                answer = duties[ff_i] if ff_i < len(duties) else duties[-1]
                            else:
                                answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                        elif t_idx == 23: # Aged care quality standards
                            if r_idx == 0:
                                answer = "Aged Care Act 1997 (Cth)"
                            elif r_idx == 3:
                                ways = [
                                    "Actively consulting the client on their daily preferences and routines.",
                                    "Supporting the client's dignity of risk while putting reasonable safety measures in place.",
                                    "Treating the client with kindness, courtesy, and respect at all times."
                                ]
                                answer = ways[ff_i] if ff_i < len(ways) else ways[-1]
                            else:
                                answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                        elif t_idx == 25: # RDA, DDA, SDA, Diversity Framework
                            if r_idx == 0:
                                rda_acts = ["Distinction", "Exclusion", "Restriction", "Preference"]
                                answer = rda_acts[ff_i] if ff_i < len(rda_acts) else rda_acts[-1]
                            elif r_idx == 1:
                                dda_types = [
                                    "Physical", "Intellectual", "Sensory", "Neurological",
                                    "Learning and psychosocial disabilities", "Diseases or illnesses",
                                    "Physical disfigurement", "Medical conditions", "Work-related injuries"
                                ]
                                answer = dda_types[ff_i] if ff_i < len(dda_types) else dda_types[-1]
                            elif r_idx == 2:
                                sda_types = ["Direct discrimination", "Indirect discrimination", "Sexual harassment"]
                                answer = sda_types[ff_i] if ff_i < len(sda_types) else sda_types[-1]
                            elif r_idx == 3:
                                answer = "Aged Care Diversity Framework"
                            elif r_idx == 4:
                                div_aims = [
                                    "To ensure aged care services are accessible and meet the diverse needs of older Australians.",
                                    "To promote inclusive, respectful, and culturally safe care that embraces individuality and dignity."
                                ]
                                answer = div_aims[ff_i] if ff_i < len(div_aims) else div_aims[-1]
                        elif t_idx == 26: # Privacy & 13 APPs
                            if r_idx == 2:
                                answer = "Collection, storage, use, and disclosure of personal and health information."
                            elif r_idx == 3:
                                apps = [
                                    "APP 1: Open and transparent management of personal information",
                                    "APP 2: Anonymity and pseudonymity",
                                    "APP 3: Collection of solicited personal information",
                                    "APP 4: Dealing with unsolicited personal information",
                                    "APP 5: Notification of the collection of personal information",
                                    "APP 6: Use or disclosure of personal information",
                                    "APP 7: Direct marketing",
                                    "APP 8: Cross-border disclosure of personal information",
                                    "APP 9: Adoption, use or disclosure of government related identifiers",
                                    "APP 10: Quality of personal information",
                                    "APP 11: Security of personal information",
                                    "APP 12: Access to personal information",
                                    "APP 13: Correction of personal information"
                                ]
                                answer = apps[ff_i] if ff_i < len(apps) else apps[-1]
                            else:
                                answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                        elif t_idx == 36: # Medico-legal requirements (NSW)
                            if r_idx == 2:
                                mccd_reqs = [
                                    "Issued by the attending medical practitioner within 48 hours of death.",
                                    "Must accurately state the direct cause of death and contributing medical conditions."
                                ]
                                answer = mccd_reqs[ff_i] if ff_i < len(mccd_reqs) else mccd_reqs[-1]
                            elif r_idx == 3:
                                coronial_reasons = [
                                    "Sudden, unexpected, or violent death.",
                                    "Death occurring during or as a result of a medical/surgical procedure or anesthesia.",
                                    "Death in care or custody where the person was under state protection."
                                ]
                                answer = coronial_reasons[ff_i] if ff_i < len(coronial_reasons) else coronial_reasons[-1]
                            elif r_idx == 4:
                                answer = "NSW State Coroner's Court (Coroners Court of New South Wales) / NSW Police Force."
                            elif "advance care" in prompt_snippet.lower() or r_idx in [1, 2]:
                                answer = NSW_ANSWERS_CHCPAL003["q19_acd_legislation"] if "legislation" in prompt_snippet.lower() else NSW_ANSWERS_CHCPAL003["q19_acd_requirements"]
                            else:
                                answer = NSW_ANSWERS_CHCPAL003["q19_eol_legislation"] if "legislation" in prompt_snippet.lower() else NSW_ANSWERS_CHCPAL003["q19_eol_requirements"]
                        else:
                            answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                    elif section == "Practical Assessment":
                        if t_idx == 56: # James physical needs
                            if r_idx == 3: answer = "Assistance with ADLs (e.g. showering, walking up the stairs)"
                            elif r_idx == 4: answer = "Assistance with mobility"
                            elif r_idx == 5: answer = "Assistance with addressing pain that prevents him from sleeping"
                            else: answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                        elif t_idx == 59: # James changing needs
                            changing_needs = [
                                "James’s pain is worsening",
                                "Pain medication is not enough to manage his pain",
                                "James’s appetite is poor",
                                "He tires easily and has difficulty in breathing",
                                "He has insomnia",
                                "He may need additional assistance from other ADLs"
                            ]
                            if 2 <= r_idx <= 7:
                                answer = changing_needs[r_idx - 2]
                            else:
                                answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                        elif t_idx == 70: # Medication concerns
                            if r_idx == 2: answer = "James still feeling the same pain despite increasing the pain medication dosage"
                            elif r_idx == 3: answer = "James’ request to have the pain medication replaced"
                            else: answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                        elif t_idx == 73: # Quality of life
                            if r_idx == 2: answer = "James feels happy that his son John, with whom he had disagreements in the past, is coming to visit him."
                            elif r_idx == 3: answer = "James expressed enjoyment in conversing with Lily about similar interests (i.e. a book they both have finished reading)"
                            else: answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                        elif t_idx == 74: # Experiences of physical pain
                            if r_idx == 2: answer = "James’s feeling of tightening in the chest has become worse, especially when he coughs."
                            elif r_idx == 3: answer = "James experiences headaches several times a day."
                            else: answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                        elif t_idx == 75: # Comfort needs
                            if r_idx == 2: answer = "Air conditioning set to a lower temperature to alleviate his headache"
                            else: answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                        elif t_idx == 82: # Signs of deterioration
                            signs = [
                                "James has become less responsive",
                                "James cannot eat food or take oral medication anymore",
                                "James is restless at times"
                            ]
                            answer = signs[r_idx] if r_idx < len(signs) else signs[-1]
                        elif t_idx == 93:
                            if r_idx == 0: answer = "Care Connect Aged Care & Palliative Services"
                            else: answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                        elif t_idx == 94: # Person 1
                            if r_idx == 0: answer = "Arthur Pendelton"
                            elif r_idx == 1: answer = "Advanced Chronic Obstructive Pulmonary Disease (COPD) and Heart Failure"
                            elif r_idx == 2: answer = "Dorothy Pendelton (Wife)"
                            elif r_idx == 3: answer = "Dorothy Pendelton"
                            elif r_idx == 4: answer = "Clinical care team, palliative physician, community nurse"
                            else: answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                        elif t_idx == 95: # Person 2
                            if r_idx == 0: answer = "Margaret Sullivan"
                            elif r_idx == 1: answer = "Metastatic Breast Cancer (Stage IV)"
                            elif r_idx == 2: answer = "James Sullivan (Son)"
                            elif r_idx == 3: answer = "James Sullivan"
                            elif r_idx == 4: answer = "Palliative care team, general practitioner, physiotherapist"
                            else: answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                        elif t_idx == 106: # ACDs - job role
                            if r_idx == 1:
                                if c_idx == 0: answer = "Refusal of Cardiopulmonary Resuscitation (CPR / DNR)"
                                elif c_idx == 1: answer = "Support Worker / Care Assistant"
                                elif c_idx == 2: answer = "Respect the client's decision not to receive CPR, ensure the palliative care team and supervisor are informed, and provide comfort care instead of initiating resuscitation."
                            elif r_idx == 2:
                                if c_idx == 0: answer = "Refusal of artificial nutrition and hydration via tube feeding"
                                elif c_idx == 1: answer = "Support Worker / Care Assistant"
                                elif c_idx == 2: answer = "Support oral comfort care and mouth hygiene rather than artificial feeding, ensuring the client is comfortable and moistening lips as per care plan."
                            else: answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                        elif t_idx == 108: # ACDs - legislative requirements
                            if r_idx == 1:
                                if c_idx == 0: answer = "Refusal of Cardiopulmonary Resuscitation (CPR / DNR)"
                                elif c_idx == 1: answer = "Guardianship Act 1987 (NSW) / Advance Care Directives Common Law: A valid advance care directive refusing medical treatment is legally binding and must be respected by care staff."
                                elif c_idx == 2: answer = "Adhere to the client's legally binding refusal of life-sustaining treatment by not initiating CPR and immediately alerting the supervising registered nurse."
                            elif r_idx == 2:
                                if c_idx == 0: answer = "Refusal of artificial nutrition and hydration via tube feeding"
                                elif c_idx == 1: answer = "Consent to Medical and Dental Treatment (Guardianship Act 1987 NSW): Competent adults have the right to refuse medical interventions including artificial nutrition."
                                elif c_idx == 2: answer = "Comply with the client's refusal of invasive artificial nutrition while continuing to offer palliative comfort measures and oral hydration."
                            else: answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                        elif t_idx == 110: # ACDs - ethical requirements
                            if r_idx == 1:
                                if c_idx == 0: answer = "Refusal of Cardiopulmonary Resuscitation (CPR / DNR)"
                                elif c_idx == 1: answer = "Code of Conduct for Aged Care: Principle of respecting individual autonomy, dignity, and self-determination in end-of-life choices."
                                elif c_idx == 2: answer = "Uphold the client's autonomous choice by ensuring care aligns with their expressed wishes and dignity is maintained."
                            elif r_idx == 2:
                                if c_idx == 0: answer = "Refusal of artificial nutrition and hydration via tube feeding"
                                elif c_idx == 1: answer = "Beneficence and Non-maleficence: Providing compassionate comfort care while avoiding non-beneficial, burdensome interventions."
                                elif c_idx == 2: answer = "Provide palliative comfort, oral moistening, and emotional support without imposing unwanted invasive procedures."
                            else: answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                        else:
                            answer = find_best_ag_answer_for_cell(ag_index, q_ref, prompt_snippet, row_header, col_header, item_index=ff_i)
                        if not answer:
                            if "james" in prompt_snippet.lower() or "client" in prompt_snippet.lower():
                                answer = "James D."
                            elif "date" in prompt_snippet.lower():
                                answer = "15/09/2026"
                            elif "location" in prompt_snippet.lower():
                                answer = "CareConnect College Facility, Hurstville NSW"
                            elif "worker" in prompt_snippet.lower() or "carer" in prompt_snippet.lower():
                                answer = "Alex Chen, Palliative Care Support Worker"
                    elif section == "Candidate Checklist":
                        if "date" in prompt_snippet.lower():
                            answer = "15/09/2026"
                        elif "signature" in prompt_snippet.lower() or "name" in prompt_snippet.lower():
                            answer = "Alex Chen"
                    elif section == "Assessor Section":
                        if t_idx == 131: # Record of Assessment candidate info
                            if r_idx == 1: answer = "Alex Chen"
                            elif r_idx == 2: answer = "Care Connect College"
                            elif r_idx == 3: answer = "1300 123 456"
                            elif r_idx == 4: answer = "info@careconnectcollege.edu.au"
                            
                    field_id = f"CHCPAL003_TXT_{t_idx}_{r_idx}_{c_idx}_{ff_i+1}"
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
                    field_counter += 1
                    
    print(f"Total fields extracted for CHCPAL003: {len(data['fields'])}")
    return data

def main():
    # 1. CHCDIS020
    awb1 = "Assignment Materials-20260914/CHCDIS020-AWB-F-v1.0.docx"
    ag1 = "Assignment Materials-20260914/CHCDIS020-AG-F-v1.0.docx"
    chcdis_data = process_chcdis020(awb1, ag1)
    
    with open("answers_CHCDIS020.yaml", "w", encoding="utf-8") as f:
        yaml.dump(chcdis_data, f, allow_unicode=True, sort_keys=False)
    print("Saved answers_CHCDIS020.yaml")
    
    # 2. CHCPAL003
    awb2 = "Assignment Materials-20260915/CHCPAL003-AWB-F-v1.0 .docx"
    ag2 = "Assignment Materials-20260915/CHCPAL003-AG-F-v1.0 .docx"
    chcpal_data = process_chcpal003(awb2, ag2)
    
    with open("answers_CHCPAL003.yaml", "w", encoding="utf-8") as f:
        yaml.dump(chcpal_data, f, allow_unicode=True, sort_keys=False)
    print("Saved answers_CHCPAL003.yaml")

if __name__ == "__main__":
    main()
