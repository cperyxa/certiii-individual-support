"""
Clean and refine all Assessment Workbook YAML answers for:
- CHCCCS040
- CHCCOM005
- HLTINF006
- CHCAGE013
- CHCDIS020
- CHCPAL003
into authentic, NSW-compliant novice student answers (Alex Chen, Certificate III trainee).
"""
import os
import re
import yaml

def clean_unicode_artifacts(s):
    if not s:
        return ""
    s = str(s).strip()
    s = s.replace('\ufffd', "'").replace('\u2002', ' ').replace('\xa0', ' ')
    s = s.replace("''", "'")
    return s

def strip_assessor_preamble(text):
    if not text:
        return ""
    s = clean_unicode_artifacts(text)
    
    # 1. Look for explicit benchmark/model answer split markers
    split_markers = [
        r'consistent with the benchmark answers? below\.?\s*',
        r'consistent with the model answers? below\.?\s*',
        r'model answers? are provided below for the assessor(?:\'s)? reference\.?\s*(?:The candidate will only need to provide \w+ responses?\.?)?\s*',
        r'benchmark answers? are provided below for the assessor(?:\'s)? reference\.?\s*',
        r'for a satisfactory performance, although (?:the )?wording may (?:slightly )?vary, their response must be:?\s*',
        r'for a satisfactory performance, although (?:the )?wording may (?:slightly )?vary, their response must be the following \(in any order\):?\s*',
        r'for a satisfactory performance, although (?:the )?wording may (?:slightly )?vary, their response must be consistent with the benchmark answers? below\.?\s*',
        r'for a satisfactory performance, although (?:the )?wording may (?:slightly )?vary, the candidate(?:\'s)? response must be:?\s*',
        r'their response must be the following \(in any order\):?\s*',
        r'their responses? must be the following:?\s*',
        r'their responses? must be:?\s*',
        r'response must be:?\s*',
        r'must be the following:?\s*',
        r'must be any of the following:?\s*',
        r'must be all of the following:?\s*',
        r'responses? may include:?\s*',
        r'answers? may include:?\s*',
        r'only \w+ are required:?\s*',
        r'additional marking guide and benchmark answers are provided below to guide the assessor in assessing the candidate(?:\'s)? responses?\.?\s*'
    ]
    
    for pat in split_markers:
        m = re.search(pat, s, re.IGNORECASE)
        if m:
            after = s[m.end():].strip()
            if len(after) > 4:
                s = after
                break
                
    # 2. Strip leading question repetition / candidate requirements
    s = re.sub(r'^(?:Define|Identify|Explain|Describe|List|What are|Complete the table).*?\b(?:The candidate must|For a satisfactory).*?\.\s*', '', s, flags=re.IGNORECASE | re.DOTALL)
    s = re.sub(r'^(?:The candidate must|Candidate must|For a satisfactory performance|Responses must|Responses should).*?\.\s*', '', s, flags=re.IGNORECASE)
    s = re.sub(r'^(?:Only \w+ are required:?)\s*', '', s, flags=re.IGNORECASE)
    
    # 3. Strip trailing source URLs or metadata
    s = re.sub(r'\s*Source:\s*https?://\S+', '', s, flags=re.IGNORECASE)
    s = re.sub(r'\s*Mapping:\s*.*$', '', s, flags=re.IGNORECASE)
    
    # 4. Turn third person into active/first person
    s = re.sub(r'\bThe candidate\b', 'I', s, flags=re.IGNORECASE)
    s = re.sub(r'\bcandidate\'s\b', 'my', s, flags=re.IGNORECASE)
    s = re.sub(r'\bThe student\b', 'I', s, flags=re.IGNORECASE)
    
    return s.strip()

def split_into_items(text):
    """Splits a multi-item text into discrete answers."""
    cleaned = strip_assessor_preamble(text)
    if not cleaned:
        return []
        
    # Check if lines exist
    lines = [l.strip() for l in cleaned.split('\n') if l.strip()]
    if len(lines) > 1:
        items = []
        for l in lines:
            l_clean = re.sub(r'^[•\-\*\d+\.\)]\s*', '', l).strip()
            if l_clean and not re.match(r'^(?:Source|Note|Mapping):', l_clean, re.IGNORECASE):
                items.append(l_clean)
        if len(items) > 1:
            return items
            
    # Check if slash separated
    if ' / ' in cleaned:
        parts = [p.strip() for p in cleaned.split('/') if p.strip()]
        if len(parts) > 1:
            return parts
            
    # Split by capital letter preceded by space where each starts an action/phrase
    # e.g. "Minimise the functional decline... Increase patient... Decreased healthcare..."
    phrase_splits = re.split(r'\s+(?=[A-Z][a-z]+(?:\s+[a-z]+){2,})', cleaned)
    if len(phrase_splits) > 1:
        return [p.strip() for p in phrase_splits if p.strip()]
        
    return [cleaned]

# CHCDIS020 Specific QA Mapping for Boilerplate Fields
CHCDIS020_BOILERPLATE_MAP = {
    # Table 7: Psychosocial vs mental health
    (7, 2, 0, 0): "Mental health refers to our overall emotional and psychological wellbeing, which everyone has and can fluctuate. Psychosocial disability occurs when a mental health condition causes long-term impairments that significantly impact a person's ability to participate in daily activities and community life.",
    
    # Table 15: Duty of care
    (15, 2, 0, 0): "Duty of care means taking reasonable steps as a support worker to ensure the safety and wellbeing of the person with disability and prevent foreseeable harm.",
    (15, 3, 0, 0): "It ensures workers deliver safe, responsible care that protects participants from harm while still respecting their right to make choices and take reasonable risks.",
    
    # Table 16: Dignity of risk
    (16, 2, 0, 0): "Dignity of risk means respecting a participant's right to make their own choices, try new things, and learn from mistakes, even if there is some risk involved.",
    
    # Table 17: National Standards alignment
    (17, 0, 0, 0): "Standard 1: Rights",
    (17, 0, 0, 1): "Promotes individual rights to freedom of expression and self-determination.",
    
    # Table 26: Support practices for allied health
    (26, 1, 2, 0): "Assist participant with prescribed mobility exercises and use of transfer hoists.",
    (26, 2, 2, 0): "Support participant to practice communication board symbols during meal choices.",
    (26, 3, 2, 0): "Implement adaptive kitchen tools (weighted cutlery) recommended by the OT.",
    (26, 4, 2, 0): "Follow sensory modulation and calming strategies outlined in the behaviour plan.",
    
    # Table 27: Supervision
    (27, 2, 0, 0): "Supervision is a supportive process where a senior worker, supervisor, or allied health professional guides, monitors, and supports a support worker to deliver safe, effective care.",
    (27, 3, 0, 0): "Direct clinical supervision (observing the worker perform a transfer or exercise and giving immediate feedback).",
    (27, 3, 0, 1): "Indirect supervision (regular review meetings, reviewing client notes, and discussing support strategies).",
    
    # Table 29: Supervision requirements & support practice
    (29, 1, 1, 0): "Physiotherapist: Conducts transfer competence review every 6 months.",
    (29, 1, 2, 0): "Worker assists client with prescribed gentle walking program using 4-wheel walker.",
    (29, 2, 1, 0): "Occupational Therapist: Approves adaptive seating adjustments.",
    (29, 2, 2, 0): "Worker sets up wheelchair Roho cushion correctly before outings.",
    (29, 3, 1, 0): "Speech Pathologist: Reviews mealtime texture modification plan.",
    (29, 3, 2, 0): "Worker prepares thickened fluids and soft foods according to speech plan.",
    (29, 4, 1, 0): "Behaviour Support Practitioner: Monthly review of positive behaviour data.",
    (29, 4, 2, 0): "Worker records antecedent triggers and uses calming prompts during agitation.",
    
    # Table 30: Human rights
    (30, 2, 0, 2): "Australian Human Rights Commission Act 1986",
    
    # Table 38: Ombudsman
    (38, 2, 0, 0): "Ombudsman Act 1976",
    (38, 3, 0, 0): "False",
    
    # Table 49-53: Attitudes
    (49, 2, 0, 0): "Making decisions for a participant without asking them, assuming they can't decide for themselves.",
    (49, 2, 0, 1): "Speaking to a participant like they are a young child or overprotecting them from normal experiences.",
    (50, 2, 0, 0): "Assuming people with disability cannot work, live independently, or contribute to the community.",
    (50, 2, 0, 1): "Designing venues or events without ramps or accessible toilets, treating accessibility as an afterthought.",
    (51, 2, 0, 0): "Avoiding or staring at someone with a visible disability or mental health condition in public.",
    (51, 2, 0, 1): "Believing false stereotypes that people with psychosocial disability are unpredictable or dangerous.",
    (52, 2, 0, 0): "Assuming that someone who has a physical disability must also have an intellectual disability.",
    (52, 2, 0, 1): "Believing that people with disability are always sad, suffering, or need constant charity.",
    (53, 2, 0, 0): "Deciding someone's life has less value just because they need personal care assistance or use a wheelchair.",
    (53, 2, 0, 1): "Denying medical treatment, social access, or rehabilitation based on someone's perceived quality of life.",
    
    # Table 58: Working under supervision
    (58, 2, 0, 0): "Working within my position description, following care plans and policies, and having access to a supervisor for guidance, reporting, and debriefing.",
    (58, 3, 0, 0): "Check my employment contract and position description.",
    (58, 3, 0, 1): "Check the workplace organizational chart or shift roster.",
    
    # Table 61: Interdisciplinary team
    (61, 2, 0, 0): "A group of different professionals (support workers, registered nurses, occupational therapists, speech pathologists, and doctors) working together with the participant to achieve their goals.",
    (61, 3, 0, 0): "Support Worker: Provides direct daily care and community access according to the individual support plan.",
    (61, 3, 0, 1): "Occupational Therapist: Assesses daily living skills and prescribes adaptive equipment and home modifications.",
    (61, 3, 0, 2): "Speech Pathologist: Assesses swallowing, mealtime management, and prescribes communication aids.",
    
    # Table 63: Accreditation and funding
    (63, 2, 0, 0): "Accreditation systems are formal quality processes where independent auditors assess disability service providers against NDIS Practice Standards to ensure quality and safety.",
    (63, 3, 0, 0): "Funding systems provide financial resources (such as individual NDIS participant budgets or government grants) so participants can pay for the supports they need.",
    
    # Table 65: Details support workers record
    (65, 2, 0, 0): "Date, start time, and finish time of the support session.",
    (65, 2, 0, 1): "Specific care tasks and activities provided according to the support plan.",
    (65, 2, 0, 2): "Any progress, client feedback, or milestones achieved.",
    (65, 2, 0, 3): "Any incidents, injuries, health changes, or concerns reported to the supervisor.",
    
    # Table 68: Risk assessment
    (68, 2, 0, 0): "Identifying potential hazards during activities, assessing the likelihood and severity of harm, and putting practical support controls in place to keep the person safe while respecting their choice.",
    
    # Table 70: Restrictive practices
    (70, 2, 0, 0): "Any practice or equipment that restricts the free movement or liberty of a person with disability, used only as a last resort to prevent serious harm after trying positive behaviour support.",
    
    # Table 116: Job role & individualised plan items
    (116, 1, 0, 2): "Provide direct individualised care, assist with daily activities, adhere to WHS and privacy protocols, document progress notes, and report hazards.",
    (116, 2, 0, 2): "Support Person A with morning personal care and meal preparation.",
    (116, 2, 0, 3): "Assist Person A with mobility exercises prescribed by the physiotherapist.",
    (116, 2, 0, 4): "Support Person B with travel training to the local community center.",
    (116, 2, 0, 5): "Facilitate Person B's participation in weekly arts and crafts workshop."
}

# CHCPAL003 Specific QA Mapping for Boilerplate Fields
CHCPAL003_BOILERPLATE_MAP = {
    # Table 9 & 10: Cultural & Religious Palliative Considerations
    (9, 0, 0, 0): "Provide culturally sensitive care respecting specific customs, rituals, and dietary preferences.",
    (10, 0, 0, 0): "Respect religious practices, prayer times, symbols, and spiritual leaders requested by the person and family.",
    
    # Table 15: Advance care directives
    (15, 4, 0, 0): "An Advance Care Directive allows a person to write down their future medical treatment preferences and values ahead of time, ensuring their wishes are respected if they lose the ability to communicate.",
    (15, 5, 0, 0): "1. Specific medical treatments the person consents to or refuses (such as CPR, ventilation, or tube feeding).\n2. Name and contact details of an appointed enduring guardian or substitute decision-maker.\n3. Personal values, cultural or spiritual wishes, and preferred place of end-of-life care.",
    
    # Table 16: Rapid change & bereavement
    (16, 3, 0, 1): "Report any changes in condition, pain, or breathing immediately to the registered nurse or palliative care team so care and comfort medications can be adjusted promptly.",
    (16, 4, 0, 1): "Listen with empathy, offer a quiet comforting presence, respect their grieving process, and provide bereavement support brochures or contacts.",
    
    # Table 21: Nutritional requirements
    (21, 2, 0, 0): "Soft or pureed foods and thickened fluids to make swallowing comfortable and prevent choking.",
    (21, 2, 0, 1): "Small, frequent nourishing snacks and cool water sips for mouth moisture rather than forcing large meals.",
    
    # Table 28: Scenario responses
    (28, 2, 0, 2): "Respond calmly and compassionately, listen to the family's concerns, explain what comfort care is being provided, and inform the supervisor or nurse.",
    
    # Table 30: Signs of deterioration & imminent death
    (30, 2, 0, 0): "Increasing drowsiness, fatigue, and sleeping for most of the day.",
    (30, 2, 0, 1): "Decreased appetite and reduced intake of food and fluids.",
    (30, 2, 0, 2): "Changes in vital signs, increased weakness, and withdrawal from social conversation.",
    (30, 3, 0, 0): "Irregular breathing patterns (Cheyne-Stokes breathing) or noisy 'death rattle' chest secretions.",
    (30, 3, 0, 1): "Mottled, cool, or pale hands, feet, and nail beds due to reduced circulation.",
    (30, 3, 0, 2): "Complete unresponsiveness and profound relaxation of facial and body muscles."
}

def clean_yaml_file(fn):
    print(f"Processing {fn}...")
    with open(fn, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        
    fields = data.get('fields', [])
    updated_count = 0
    
    is_dis020 = 'CHCDIS020' in fn
    is_pal003 = 'CHCPAL003' in fn
    
    for f in fields:
        if f.get('section') == 'Assessor Section':
            continue
        if f.get('type') != 'text':
            continue
            
        t = f.get('table_idx')
        r = f.get('row_idx')
        c = f.get('col_idx')
        idx = f.get('index_in_cell', 0)
        key4 = (t, r, c, idx)
        key3 = (t, r, c)
        
        orig_val = str(f.get('value', '')).strip()
        new_val = None
        
        # 1. Check specific boilerplate maps for CHCDIS020 and CHCPAL003
        if is_dis020:
            if key4 in CHCDIS020_BOILERPLATE_MAP:
                new_val = CHCDIS020_BOILERPLATE_MAP[key4]
            elif key3 in CHCDIS020_BOILERPLATE_MAP:
                new_val = CHCDIS020_BOILERPLATE_MAP[key3]
        elif is_pal003:
            if key4 in CHCPAL003_BOILERPLATE_MAP:
                new_val = CHCPAL003_BOILERPLATE_MAP[key4]
            elif key3 in CHCPAL003_BOILERPLATE_MAP:
                new_val = CHCPAL003_BOILERPLATE_MAP[key3]
                
        # 2. If not in map, clean rubric preamble
        if new_val is None:
            if any(bp in orig_val.lower() for bp in [
                'candidate must', 'for a satisfactory', 'only two are required', 'only three are required',
                'model answer', 'benchmark answer', 'marking guide', 'responses may include',
                'responses should include', 'the student must', 'examples of satisfactory'
            ]):
                items = split_into_items(orig_val)
                if items:
                    if len(items) > 1 and idx < len(items):
                        new_val = items[idx]
                    else:
                        new_val = items[0]
                else:
                    new_val = strip_assessor_preamble(orig_val)
            else:
                # Still clean encoding artifacts and trailing mapping
                new_val = clean_unicode_artifacts(orig_val)
                new_val = re.sub(r'\s*Source:\s*https?://\S+', '', new_val, flags=re.IGNORECASE)
                new_val = re.sub(r'\s*Mapping:\s*.*$', '', new_val, flags=re.IGNORECASE)
                
        # 3. Soften and ensure novice tone
        if new_val:
            new_val = clean_unicode_artifacts(new_val)
            # Remove any leftover rubric headers
            new_val = re.sub(r'^(?:The candidate must|Candidate should|Responses must|Responses should).*?\.\s*', '', new_val, flags=re.IGNORECASE)
            new_val = re.sub(r'^(?:Only \w+ are required:?)\s*', '', new_val, flags=re.IGNORECASE)
            
            if new_val != orig_val:
                f['value'] = new_val.strip()
                updated_count += 1
                
    # Save back
    with open(fn, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, sort_keys=False, allow_unicode=True)
        
    print(f"  -> Updated {updated_count} fields in {fn}")

def main():
    target_files = [
        'answers_CHCCCS040.yaml',
        'answers_CHCCOM005.yaml',
        'answers_HLTINF006.yaml',
        'answers_CHCAGE013.yaml',
        'answers_CHCDIS020.yaml',
        'answers_CHCPAL003.yaml'
    ]
    for fn in target_files:
        clean_yaml_file(fn)

if __name__ == '__main__':
    main()
