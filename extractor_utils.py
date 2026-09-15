"""
Core extractor module for extracting fields and answers from CareConnect assessment materials.
"""
import os
import re
import json
import yaml
import docx
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

W_NS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
W14_NS = 'http://schemas.microsoft.com/office/word/2010/wordml'

def get_text(elem):
    return ''.join(elem.itertext()).strip()

def extract_answer_items(raw_text):
    """
    Extracts individual benchmark response items from an Assessor Guide cell.
    Gives strict priority to 'model answers are provided below' / 'benchmark answers are provided below'
    to avoid picking up assessor instructional criteria.
    """
    if not raw_text:
        return []
        
    text = raw_text.strip()
    
    # Priority 1: Text directly following explicit benchmark/model answer headers
    high_priority_pats = [
        r'(?:model answers?|benchmark answers?)(?: are)? provided below[^\n]*[:\.]?\s*(.*)',
        r'consistent with the (?:benchmark|model) answers? below[^\n]*[:\.]?\s*(.*)',
        r'their responses? must be all of the following[^\n]*[:\.]?\s*(.*)',
        r'their responses? must be any of the following[^\n]*[:\.]?\s*(.*)',
        r'their responses? must be[^\n]*[:\.]?\s*(.*)'
    ]
    
    body = None
    for pat in high_priority_pats:
        m = re.search(pat, text, re.IGNORECASE | re.DOTALL)
        if m and m.group(1).strip():
            body = m.group(1).strip()
            break
            
    if body is None:
        body = text
        
    # Cut off trailing mapping metadata if present
    body = re.split(r'\n\s*Mapping:', body, flags=re.IGNORECASE)[0].strip()
    
    lines = [l.strip() for l in body.split('\n') if l.strip()]
    cleaned_items = []
    
    for l in lines:
        l_lower = l.lower()
        # Filter out assessor guidance phrases
        if any(l_lower.startswith(bp) for bp in [
            'mapping:', 'learner guide', 'marking guide', 'for a satisfactory',
            'the candidate must', 'responses may vary', 'responses will vary',
            'for the assessor to determine', 'although wording may', 'tick the box',
            'other responses are acceptable', 'consistent with the given scenario',
            'ways on how anne can communicate', 'visual disability is a result',
            'hearing disability is a result', 'be consistent with the definition',
            'be five examples of information', 'the candidate will only need'
        ]):
            continue
            
        # Strip bullets, numbers, dashes
        l_clean = re.sub(r'^[•\-\*\d+\.\)]\s*', '', l).strip()
        if l_clean and l_clean != '\u2002':
            cleaned_items.append(l_clean)
            
    return cleaned_items

def clean_model_answer(raw_text, item_index=None):
    """
    Returns clean answer string. If item_index is specified, returns item at that index.
    """
    items = extract_answer_items(raw_text)
    if not items:
        return ""
    if item_index is not None:
        if 0 <= item_index < len(items):
            return items[item_index]
        elif items:
            return items[-1]
    return '\n'.join(items)


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

print("Extractor helper functions loaded successfully.")
