import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

def check_preceding_text(awb_path, table_idx):
    doc = docx.Document(awb_path)
    # Search elements before table
    t = doc.tables[table_idx]
    p_prev = t._element.getprevious()
    texts = []
    while p_prev is not None and len(texts) < 5:
        if p_prev.tag.endswith('p'):
            txt = "".join(p_prev.itertext()).strip()
            if txt:
                texts.append(txt)
        elif p_prev.tag.endswith('tbl'):
            break
        p_prev = p_prev.getprevious()
    print(f"Preceding text for Table {table_idx}: {list(reversed(texts))}")

print("CHCCCS040 Table 13:")
check_preceding_text("3. CHCCCS040 - Support independence and wellbeing/CHCCCS040-AWB-F-v1.0.docx", 13)

print("\nHLTINF006 Table 13:")
check_preceding_text("8. HLTINF006 - Apply basic principles and practices of infection prevention and control/HLTINF006-AWB-F-v1.0.docx", 13)

print("\nCHCAGE013 Table 5:")
check_preceding_text("11. CHCAGE013 - Work effectively in aged care/CHCAGE013-AWB-F-v1.0.docx", 5)
