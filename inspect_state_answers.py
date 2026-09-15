import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

def inspect_q(code, ag_path, terms):
    print(f"\n{'='*25} {code} {'='*25}")
    ag = docx.Document(ag_path)
    for i, t in enumerate(ag.tables):
        txt = " ".join([c.text for r in t.rows for c in r.cells])
        if any(term.lower() in txt.lower() for term in terms):
            print(f"AG Table {i}:")
            for r_i, r in enumerate(t.rows[:8]):
                cells = [" ".join(c.text.split()) for c in r.cells]
                print(f"  R{r_i}: {cells[:2]}")

inspect_q('CHCCCS040', 'Assignment Materials-20260915 (3)/CHCCCS040-AG-F-v1.0.docx', ['Question 20', 'Question 19', 'legislation, standards and codes'])
inspect_q('CHCCOM005', 'Assignment Materials-20260915 (5)/CHCCOM005-AG-F-v1.1.docx', ['Question 1', 'legal and ethical requirements'])
inspect_q('HLTINF006', 'Assignment Materials-20260915 (8)/HLTINF006-AG-F-v1.0.docx', ['Question 36', 'contaminated waste'])
inspect_q('CHCAGE013', 'Assignment Materials-20260915 (11)/CHCAGE013-AG-F-v1.1.docx', ['Question 9', 'Question 11', 'Question 13'])
