"""
Comprehensive benchmark answer generator for Group 2 units:
- CHCCCS031 Part A
- CHCCCS031 Part B
- CHCCCS038
- CHCCCS041
- CHCDIV001
"""
import yaml
import re

def populate_chcccs031_parta(fields):
    for f in fields:
        if f['section'] == 'Assessor Section':
            continue
        t = f['table_idx']
        r = f['row_idx']
        c = f['col_idx']
        idx = f['index_in_cell']
        lbl = f['label'].lower()
        
        # Table 15: Duty of care / Disclosure examples (col 5)
        if t == 15 and c == 5:
            if r in [1, 2]:
                f['value'] = "Promptly notify the client when their personal information must be disclosed under statutory mandatory reporting requirements."
            elif r in [3, 4]:
                f['value'] = "Consistently adhere to individual care plan safety protocols and report emerging hazards to supervisors while supporting client choice."
                
        # Table 30: Life domains (col 2 = how AT helps, col 3 = example)
        elif t == 30:
            if r == 3: # Self-care
                f['value'] = "Assists client to dress, eat, and perform grooming tasks independently without fatigue." if c == 2 else "Button hook and long-handled shoe horn"
            elif r == 4: # Continence
                f['value'] = "Maintains skin dignity and prevents embarrassing leaks or skin breakdown." if c == 2 else "Urinary sheath drainage bags and moisture-wicking mattress protectors"
            elif r == 5: # Hygiene
                f['value'] = "Enables safe, unassisted showering and teeth cleaning." if c == 2 else "Shower chair with backrest and electric toothbrush with wide grip"
            elif r == 6: # Communication
                f['value'] = "Allows non-verbal clients or those with dysarthria to express choices and needs." if c == 2 else "AAC speech-generating tablet device with symbol grid"
            elif r == 7: # Mobility
                f['value'] = "Provides stability and endurance during indoor and outdoor walking." if c == 2 else "4-wheel walker with handbrakes and seat"
            elif r == 8: # Transferring
                f['value'] = "Facilitates safe movement between bed, chair, and wheelchair without manual strain." if c == 2 else "Mechanical mobile standing hoist with harness"

        # Table 31: Life domains
        elif t == 31:
            doms = {
                1: ("Provides visual prompts and task organizers.", "Digital pictorial schedule tablet"),
                2: ("Delivers automated voice reminders for medication and meals.", "Talking digital calendar day clock"),
                3: ("Magnifies text and provides auditory readouts.", "Electronic video magnifier / Screen-reading software"),
                4: ("Amplifies speech sounds and reduces background noise.", "Digital hearing aid with Bluetooth loop connectivity"),
                5: ("Assists with cooking, cleaning, and meal prep.", "Ergonomic easy-grip kitchen utensils"),
                6: ("Allows independent participation in games and hobbies.", "Adaptive card holders and large-print games"),
                7: ("Facilitates reading and audio enjoyment.", "Audiobook player with high-contrast buttons"),
                8: ("Supports digital learning, typing, and research.", "Voice-to-text software and adaptive keyboard"),
                9: ("Enables accessible computer work and workspace ergonomics.", "Adjustable motorized sit-stand desk and trackball mouse")
            }
            if r in doms:
                f['value'] = doms[r][0] if c == 1 else doms[r][1]

        # Table 32: Life domains
        elif t == 32:
            doms2 = {
                1: ("Enables independent home entry and environmental control.", "Smart door lock with sensor and lever door handles"),
                2: ("Provides rapid emergency alerting to support staff.", "Wearable wireless nurse call pendant"),
                3: ("Allows safe navigation of uneven terrain and community spaces.", "All-terrain motorized mobility scooter"),
                4: ("Prevents spills and facilitates self-feeding with tremors.", "Weighted adaptive cutlery and high-rim scooper plate"),
                5: ("Enables controlled fluid intake without neck hyperextension.", "Two-handled weighted mug with dysphagia cut-out lid"),
                6: ("Relieves sustained tissue pressure over bony prominences.", "Alternating air pressure mattress overlay"),
                7: ("Reduces physical lifting strain on informal and formal carers.", "Slide sheets and ceiling track transfer hoist")
            }
            if r in doms2:
                f['value'] = doms2[r][0] if c == 1 else doms2[r][1]

        # Table 33: R4 C0
        elif t == 33 and r == 4:
            f['value'] = "By removing physical, sensory, and cognitive barriers, allowing individuals to engage actively in social, educational, and domestic activities with autonomy and confidence."

        # Table 35: Risk strategies
        elif t == 35:
            if r == 3:
                f['value'] = "Maintain strict adherence to code of conduct, conduct mandatory abuse reporting training, and implement open-door monitoring."
            elif r == 4:
                f['value'] = "Actively involve clients in all care conferences, respect their cultural/lifestyle choices, and uphold dignity of risk."
            elif r == 5:
                f['value'] = "Ensure clear pathways free of clutter, install grab rails in bathrooms, provide adequate lighting, and encourage prescribed mobility aids."

    return fields

def populate_chcccs031_partb(fields):
    for f in fields:
        if f['section'] == 'Assessor Section':
            continue
        t = f['table_idx']
        r = f['row_idx']
        c = f['col_idx']
        
        # Abraham details (Tables 30-33)
        if t == 30 and c == 1:
            f['value'] = "Abraham C" if r == 0 else "Unit 4, 12 CareConnect Way, Sydney NSW 2000"
        elif t == 31 and c == 1:
            f['value'] = "Alex Chen" if r == 0 else "Support Worker"
        elif t == 32:
            if r == 0: f['value'] = "Abraham confirmed he is pleased with the new mobility equipment and feeling more confident during daily walks."
            elif r == 1: f['value'] = "Abraham requested ongoing assistance with breakfast routines and asked for social group activities on weekends."
            elif r == 2: f['value'] = "Support plan is operating effectively; updated to include weekly community bridge club visits."
        elif t == 33:
            if r == 0: f['value'] = "Alex Chen"
            elif r == 1: f['value'] = "Support Worker"
            elif r == 2: f['value'] = "Alex Chen"
            elif r == 3: f['value'] = "15/09/2026"
            
        # Henry details (Tables 60-63)
        elif t == 60 and c == 1:
            f['value'] = "Henry S" if r == 0 else "Apartment 18, 45 Horizon Street, Sydney NSW 2000"
        elif t == 61 and c == 1:
            f['value'] = "Alex Chen" if r == 0 else "Support Worker"
        elif t == 62:
            if r == 0: f['value'] = "Henry reported that colostomy bag management is stable and skin around stoma remains healthy."
            elif r == 1: f['value'] = "Henry experienced late afternoon fatigue; requested afternoon rest period between 2:00 PM and 3:30 PM."
            elif r == 2: f['value'] = "Care plan adjusted to accommodate afternoon rest. Florence confirmed satisfaction with respite support."
        elif t == 63:
            if r == 0: f['value'] = "Alex Chen"
            elif r == 1: f['value'] = "Support Worker"
            elif r == 2: f['value'] = "Alex Chen"
            elif r == 3: f['value'] = "15/09/2026"
            
    return fields

def populate_chcccs038(fields):
    for f in fields:
        if f['section'] == 'Assessor Section':
            continue
        t = f['table_idx']
        r = f['row_idx']
        c = f['col_idx']
        idx = f['index_in_cell']
        
        # Table 18: Restrictive practices ALRC & human rights (Table 18)
        if t == 18:
            if r == 2: f['value'] = "According to the ALRC, restrictive practices refer to any intervention that has the effect of restricting the free movement or liberty of a person with disability."
            elif r == 3: f['value'] = "Authorised restrictive practices must only be used as a last resort to prevent serious harm after exhausting all positive behaviour support strategies."
            elif r == 4:
                vals = [
                    "Chemical restraint: Using medication for the primary purpose of controlling behaviour.",
                    "Mechanical restraint: Using devices or equipment to restrict free bodily movement.",
                    "Physical restraint: Using physical force to restrict or subdue movement.",
                    "Environmental restraint: Restricting free access to parts of the environment or personal items.",
                    "Seclusion: Confinement of a person alone in a room from which free exit is denied."
                ]
                f['value'] = vals[idx] if idx < len(vals) else vals[-1]
            elif r == 5:
                vals = [
                    "Right to liberty and security of person under Article 14 of the UNCRPD.",
                    "Right to freedom from cruel, inhuman or degrading treatment under Article 15 of the UNCRPD."
                ]
                f['value'] = vals[idx] if idx < len(vals) else vals[-1]
            elif r == 6:
                vals = [
                    "Physical impacts: Muscle deconditioning, pressure sores, loss of functional mobility, and injury.",
                    "Psychological impacts: Trauma, depression, loss of dignity, diminished trust, and heightened anxiety."
                ]
                f['value'] = vals[idx] if idx < len(vals) else vals[-1]
            elif r == 7:
                vals = [
                    "To prevent imminent, serious physical injury to the person or others after all proactive de-escalation strategies have been exhausted.",
                    "During acute, severe behavioral crises as an emergency measure while awaiting clinical assistance."
                ]
                f['value'] = vals[idx] if idx < len(vals) else vals[-1]

        # Table 19: Risks of restrictive practices
        elif t == 19 and r == 2:
            f['value'] = "Risks include physical injury, asphyxiation, cardiovascular distress, severe psychological trauma, and dehumanisation."
            
        # Table 20: Behaviour support plan requirements
        elif t == 20:
            if r == 2: f['value'] = "The Behaviour Support Plan must contain proactive strategies, functional behaviour assessment, explicit authorization, and fading protocols."
            elif r == 3: f['value'] = "1. Authorisation under state legislation. 2. Regular clinical review. 3. Monthly reporting to the NDIS Commission."
            
        # Table 21: Technology & choice
        elif t == 21:
            if r == 2: f['value'] = "Smart home automation, voice-activated environmental controls, and tablet scheduling apps allow individuals to control their own environment and schedule independently."
            elif r == 3: f['value'] = "1. Providing accessible, transparent information about service options. 2. Supporting the individual to run their own care meetings."
            elif r == 4: f['value'] = "Providing choices empowers individuals, validates their identity and preferences, fosters self-esteem, and reduces frustration and feelings of helplessness."
            elif r == 5:
                vals = [
                    "Presenting daily options in accessible formats (visual cards, Easy Read) and explaining the benefits and risks of each option clearly.",
                    "Allowing adequate time for the person to make their own decision without rushing, and upholding their dignity of risk."
                ]
                f['value'] = vals[idx] if idx < len(vals) else vals[-1]
            
        # Table 22: Rights to planning
        elif t == 22:
            if r == 2: f['value'] = "Under the NDIS Act 2013 and UNCRPD Article 12, persons with disability have the right to be central to planning and make decisions about their own lives."
            elif r == 3: f['value'] = "Under the Charter of Aged Care Rights, consumers have the right to have control over and make decisions about their care, personal and social life."
            
        # Table 23: Strategies for planning
        elif t == 23:
            f['value'] = "1. Pre-meeting preparation using visual planning tools. 2. Facilitating independent advocacy support during decision-making."

        # Tables 24-26: Assistive technologies
        elif t in [24, 25, 26]:
            at_dict = {
                "self-care": ("Assists client to dress, eat, and perform grooming tasks independently without fatigue.", "Button hook and long-handled shoe horn"),
                "continence": ("Maintains skin dignity and prevents embarrassing leaks or skin breakdown.", "Urinary sheath drainage bags and moisture-wicking mattress protectors"),
                "hygiene": ("Enables safe, unassisted showering and teeth cleaning.", "Shower chair with backrest and electric toothbrush with wide grip"),
                "communication": ("Allows non-verbal clients or those with dysarthria to express choices and needs.", "AAC speech-generating tablet device with symbol grid"),
                "mobility": ("Provides stability and endurance during indoor and outdoor walking.", "4-wheel walker with handbrakes and seat"),
                "transferring": ("Facilitates safe movement between bed, chair, and wheelchair without manual strain.", "Mechanical mobile standing hoist with harness"),
                "cognition": ("Provides visual prompts and task organizers.", "Digital pictorial schedule tablet"),
                "memory loss": ("Delivers automated voice reminders for medication and meals.", "Talking digital calendar day clock"),
                "vision": ("Magnifies text and provides auditory readouts.", "Electronic video magnifier / Screen-reading software"),
                "hearing": ("Amplifies speech sounds and reduces background noise.", "Digital hearing aid with Bluetooth loop connectivity"),
                "daily living activities": ("Assists with cooking, cleaning, and meal prep.", "Ergonomic easy-grip kitchen utensils"),
                "recreation": ("Allows independent participation in games and hobbies.", "Adaptive card holders and large-print games"),
                "leisure": ("Facilitates reading and audio enjoyment.", "Audiobook player with high-contrast buttons"),
                "education": ("Supports digital learning, typing, and research.", "Voice-to-text software and adaptive keyboard"),
                "employment": ("Enables accessible computer work and workspace ergonomics.", "Adjustable motorized sit-stand desk and trackball mouse"),
                "home": ("Enables independent home entry and environmental control.", "Smart door lock with sensor and lever door handles"),
                "care residence": ("Provides rapid emergency alerting to support staff.", "Wearable wireless nurse call pendant"),
                "outdoors": ("Allows safe navigation of uneven terrain and community spaces.", "All-terrain motorized mobility scooter"),
                "eating": ("Prevents spills and facilitates self-feeding with tremors.", "Weighted adaptive cutlery and high-rim scooper plate"),
                "drinking": ("Enables controlled fluid intake without neck hyperextension.", "Two-handled weighted mug with dysphagia cut-out lid"),
                "pressure area management": ("Relieves sustained tissue pressure over bony prominences.", "Alternating air pressure mattress overlay"),
                "carer support": ("Reduces physical lifting strain on informal and formal carers.", "Slide sheets and ceiling track transfer hoist")
            }
            lbl = f['label'].lower()
            matched = False
            for k, (desc, ex) in at_dict.items():
                if k in lbl:
                    f['value'] = ex if c in [2, 3] and "example" in lbl else desc
                    matched = True
                    break
            if not matched:
                f['value'] = "Adaptive device facilitating client independence and functional autonomy." if c == 1 else "Prescribed assistive aid"

        # Table 27: AT maintaining independence
        elif t == 27:
            f['value'] = "AT compensates for functional impairments, empowering individuals to perform domestic, educational, and vocational tasks on their own terms."

        # Table 28 & 29: Complaints & advocacy
        elif t == 28:
            if r in [4, 5]:
                f['value'] = "People with Disability Australia (PWDA): Free independent advocacy and representation across NSW." if c == 0 else "Accessible via phone 1800 422 015 or online referral at pwd.org.au"
        elif t == 29:
            f['value'] = "Internal Complaint Mechanism: Complete confidential client feedback form; investigated by Quality Manager within 14 days." if c == 0 else "Aged Care Quality and Safety Commission: Phone 1800 951 822 or lodge online complaint."

        # Table 32: Context
        elif t == 32:
            f['value'] = "Aged Care and Disability Support Services"

        # Tables 33-35: Legal & ethical considerations (NSW)
        elif t in [33, 34, 35]:
            leg_map = {
                "discrimination": ("Anti-Discrimination Act 1977 (NSW) / DDA 1992", "Part 4A, Disability Discrimination", "Unlawful to treat persons less favourably based on disability or protected attributes.", "Workers must deliver equitable, non-discriminatory care and support reasonable adjustments."),
                "informed consent": ("Guardianship Act 1987 (NSW) / Common Law", "Part 5, Medical and dental treatment", "Valid consent must be voluntary, informed, and obtained from the person or legal substitute decision-maker.", "Workers must explain procedures clearly and respect the person's right to accept or decline."),
                "duty of care": ("Civil Liability Act 2002 (NSW)", "Part 1A, Negligence", "Workers must take reasonable care to avoid foreseeable harm to clients.", "Maintain professional competence, balance safety with dignity of risk, and follow care plans."),
                "privacy": ("Privacy Act 1988 (Cth) / HRIPA Act 2002 (NSW)", "Health Privacy Principles (HPPs 1-15)", "Strict controls over the collection, storage, and sharing of personal health records.", "Maintain confidentiality, store records securely, and obtain written consent before sharing."),
                "disclosure": ("Ageing and Disability Commissioner Act 2019 (NSW)", "Part 2, Reports of abuse or neglect", "Mandatory statutory duty to disclose and report serious abuse, exploitation, or neglect.", "Report suspected abuse immediately to supervisor and statutory authorities without delay."),
                "whs": ("Work Health and Safety Act 2011 (NSW)", "Part 2, Health and safety duties", "Duty to maintain a safe working environment and follow safe work procedures.", "Comply with manual handling protocols, wear required PPE, and report hazards.")
            }
            lbl = f['label'].lower()
            matched = False
            for k, (act, ref, req, eth) in leg_map.items():
                if k in lbl:
                    if c == 1: f['value'] = act
                    elif c == 2: f['value'] = ref
                    elif c == 3: f['value'] = req
                    elif c == 4: f['value'] = eth
                    matched = True
                    break
            if not matched:
                if c == 1: f['value'] = "Disability Inclusion Act 2014 (NSW)"
                elif c == 2: f['value'] = "Part 1, General principles"
                elif c == 3: f['value'] = "Statutory compliance required across all community support settings."
                elif c == 4: f['value'] = "Maintain person-centred ethics, respect dignity, and champion human rights."

        # Table 37: Boundaries & responsibilities
        elif t == 37:
            if r == 0:
                f['value'] = "Three work role boundaries: 1. No financial transactions/loans with clients. 2. Maintain strict professional detachment (no personal relationships). 3. Only perform delegated tasks within certified competencies."
            elif r == 1:
                f['value'] = "Three responsibilities: 1. Deliver person-centred care aligned with care plan. 2. Maintain accurate daily progress notes. 3. Promptly report health deterioration or hazards."
            elif r == 2:
                f['value'] = "Three limitations: 1. Cannot alter prescribed medications or clinical doses. 2. Cannot provide financial or legal advice. 3. Cannot perform invasive nursing procedures."

        # Table 38: Standards
        elif t == 38:
            if r == 2:
                f['value'] = "8 Aged Care Quality Standards: 1. Consumer dignity and choice. 2. Ongoing assessment and planning. 3. Personal and clinical care. 4. Services and supports for daily living. 5. Organisation's service environment. 6. Feedback and complaints. 7. Human resources. 8. Organisational governance."
            elif r == 3:
                f['value'] = "6 NDIS Code of Conduct Rules: 1. Act with respect for individual rights to freedom of expression and self-determination. 2. Respect privacy of people with disability. 3. Provide supports in a safe and competent manner. 4. Act with integrity, honesty and transparency. 5. Promptly take steps to prevent and respond to violence, abuse, and neglect. 6. Prevent and respond to sexual misconduct."

        # Table 47: Breaches of human rights
        elif t == 47:
            f['value'] = "Breach of Charter of Aged Care Rights: Failing to respect consumer dignity, locking doors to restrict movement without authorization, or ignoring expressed care preferences."

        # Tables 51-55: Incident report for Judith
        elif t == 51:
            if c == 3: f['value'] = "Care Connect Services Residential Care Wing"
            elif r == 3 and c == 1: f['value'] = "Sarah Jenkins (Registered Nurse / Workplace Supervisor)"
        elif t == 52:
            if c == 3: f['value'] = "Judith M (78 years old, Room 14)"
            elif r == 2 and c == 1: f['value'] = "Osteoarthritis, hypertension, and mild cognitive impairment; history of osteoporosis."
            elif r == 3 and c == 1: f['value'] = "Robert M (Son and primary family contact)"
        elif t == 53:
            f['value'] = "Bruising and 3cm skin tear on left forearm; disheveled clothing, pain, and high emotional distress."
        elif t == 54:
            f['value'] = "Judith disclosed rough handling by agency staff during morning transfer; emergency call buzzer was unplugged behind bedside table; client left unattended."
        elif t == 55:
            f['value'] = "Alex Chen (Support Worker) and Sarah Jenkins (Registered Nurse)."

        # Table 67: Matilda strategies
        elif t == 67:
            f['value'] = "Facilitate a consultation with a physiotherapist to design an individualised strength and balance mobility program." if r == 3 else "Encourage Matilda to join the weekly facility gardening group to foster friendships."

    return fields

def populate_chcccs041(fields):
    for f in fields:
        if f['section'] == 'Assessor Section':
            continue
        t = f['table_idx']
        r = f['row_idx']
        c = f['col_idx']
        idx = f['index_in_cell']
        
        # Table 5 & 6: Organ systems
        if t == 5 and r == 9 and c == 2:
            f['value'] = "Produces female gametes (ova), secretes estrogen and progesterone, facilitates fertilization, and supports foetal gestation."
        elif t == 6 and c == 1:
            systems = {
                1: "Produces, maintains, and transports sperm and protective seminal fluid, and secretes male sex hormones (testosterone).",
                2: "Forms a waterproof outer protective barrier against environmental pathogens, UV radiation, and dehydration; houses sensory receptors; and regulates body temperature.",
                3: "Returns leaked interstitial fluid to the circulatory system, absorbs dietary fats, and filters foreign pathogens through lymph nodes.",
                4: "Rapidly detects internal and external sensory stimuli, processes cognitive information, and coordinates voluntary and involuntary physiological responses.",
                5: "Defends the body against infectious microorganisms (bacteria, viruses, fungi) and abnormal cells using innate physical barriers and adaptive antibody/cellular responses.",
                6: "Filters metabolic wastes and toxins from blood, regulates systemic fluid and electrolyte balance, and maintains blood pH through urine excretion."
            }
            if r in systems: f['value'] = systems[r]

        # Tables 37-39: System interactions & hormones
        elif t == 37:
            vals = ["cardiovascular", "respiratory", "muscular", "skeletal"]
            f['value'] = vals[idx] if idx < len(vals) else vals[-1]
        elif t == 38:
            if idx == 0: f['value'] = "Through cutaneous sensory nerve endings and mechanoreceptors embedded in the dermis and epidermis."
            elif idx == 1: f['value'] = "sensory"
            elif idx == 2: f['value'] = "central nervous"
        elif t == 39:
            vals = ["Gonads (testes in males and ovaries in females)", "endocrine", "bloodstream", "target tissues", "homeostasis", "metabolic", "growth"]
            f['value'] = vals[idx] if idx < len(vals) else vals[-1]

        # Table 41: Sensory organs
        elif t == 41:
            exps = {
                1: "Photoreceptors in the retina convert light waves into electrical nerve impulses sent to the visual cortex.",
                2: "Mechanoreceptors in the cochlea translate acoustic vibrations into auditory signals, and semicircular canals maintain balance.",
                3: "Chemoreceptors in the olfactory epithelium bind airborne odorant molecules, transmitting smell signals to the olfactory bulb.",
                4: "Gustatory taste receptor cells detect dissolved chemical tastants (sweet, salty, sour, bitter, umami) and stimulate salivation."
            }
            if r in exps: f['value'] = exps[r]

        # Tables 42-47: Homeostasis
        elif t == 42:
            f['value'] = "The body promotes heat loss through cutaneous vasodilation (flushing) and eccrine sweating; when exposed to cold, it initiates peripheral vasoconstriction and shivering thermogenesis."
        elif t == 43:
            vals = ["sweat normally", "sweat glands", "heat exhaustion", "hyperthermia", "core body temperature"]
            f['value'] = vals[idx] if idx < len(vals) else vals[-1]
        elif t == 44:
            f['value'] = "The kidneys selectively reabsorb or excrete water, sodium, potassium, and chloride ions under the hormonal regulation of aldosterone, antidiuretic hormone (ADH), and atrial natriuretic peptide."
        elif t == 45:
            vals = ["kidney", "large intestine", "lungs", "skin", "sweat", "urea", "carbon dioxide", "feces", "urine", "filtration"]
            f['value'] = vals[idx] if idx < len(vals) else vals[-1]
        elif t == 46:
            f['value'] = "Systolic pressure is the maximum arterial pressure during ventricular myocardial contraction; diastolic pressure is the minimum resting pressure during ventricular relaxation. Regulated by baroreceptors."
        elif t == 47:
            f['value'] = "White blood cells destroy invading pathogens via phagocytosis (neutrophils and macrophages) and antibody-mediated neutralization (B-lymphocytes)."

        # Tables 48-53: Physical activity & movement
        elif t == 48:
            f['value'] = "Older adults with poor mobility should perform balance exercises, seated resistance training, and gentle walking for at least 30 minutes on most days to reduce fall risks."
        elif t == 49:
            f['value'] = "Active exercise is recommended for clients with voluntary muscle control to improve cardiovascular fitness; passive exercise is recommended for bedbound, paralyzed, or post-stroke clients to maintain joint range of motion."
        elif t == 50:
            f['value'] = "Providing balanced, nutrient-dense meals tailored to clinical dietary requirements, and supporting daily oral and personal hygiene routines."
        elif t == 51:
            f['value'] = "Nutrition supplies the essential proteins, vitamins, and fluids needed for tissue repair and immune vitality, while strict personal and food hygiene prevents pathogenic infection."
        elif t == 52:
            f['value'] = "Poor oral hygiene causes periodontitis, tooth loss, and severe mouth pain, making chewing difficult, leading to food avoidance, poor nutritional intake, and unintentional weight loss."
        elif t == 53:
            f['value'] = "Disabilities such as hemiplegia, paraplegia, spasticity, or severe arthritis restrict physical mobility, requiring assistive mobility devices and regular passive/active physical support."

        # Tables 54-58: Indicators of issues & ageing
        elif t == 54:
            inds = {
                1: "Malnutrition: Unintentional clothes loosening, noticeable muscle wasting, lethargy, and dull skin/hair.",
                2: "Dehydration: Dry cracked lips, sunken eyes, dark concentrated urine, and sudden postural dizziness.",
                3: "Skin tear / wound: Epidermal separation, localized bleeding, erythema, and purulent exudate.",
                4: "Incontinence: Strong ammonia odor, wet bedding/clothing, and excoriated perineal skin.",
                5: "Respiratory infection: Productive cough with yellow/green sputum, wheezing, and fever.",
                6: "Oral health: Bleeding swollen gums, loose teeth, severe halitosis, or painful mouth ulcers.",
                7: "Appetite regulation: Unexplained sudden loss of appetite, skipping multiple meals consecutively, or leaving more than half of meal portions untouched."
            }
            if r in inds: f['value'] = inds[r]
        elif t == 55:
            inds2 = {
                1: "Dysphagia: Persistent coughing, throat clearing, or choking during meals, and pocketing food.",
                2: "Bone health: Gradual loss of height, stooped kyphotic posture, or fracture from minor bumps.",
                3: "Food intolerance: Abdominal cramps, flatulence, nausea, diarrhea, or urticaria following meal intake.",
                4: "Dementia: Disorientation to familiar surroundings, losing track of conversations, and impaired judgment.",
                5: "Cognitive decline: Difficulty following multi-step instructions and sudden personality changes."
            }
            if r in inds2: f['value'] = inds2[r]
        elif t == 56:
            if r == 6:
                f['value'] = "Ageing causes dry mouth (xerostomia), receding gums, brittle teeth, and reduced taste bud sensitivity."
            elif r == 7:
                f['value'] = "Dysphagia: Age-related pharyngeal muscle weakness, xerostomia (dry mouth), and delayed swallowing reflexes increase coughing and aspiration risks."
        elif t == 57:
            f['value'] = "Decreased bone mineral density (osteopenia/osteoporosis), increasing vulnerability to low-trauma fractures." if r == 1 else "Age-related structural skin thinning, loss of subcutaneous fat, and impaired collagen synthesis."
        elif t == 58:
            f['value'] = "Increased risk of depression, anxiety, social isolation, and grief associated with loss of independence and peers."

        # Tables 59-65: Wellbeing, pain, diseases
        elif t == 59:
            f['value'] = "Reduced physical mobility reduces caloric expenditure, while certain psychiatric medications cause appetite stimulation, leading to weight gain and secondary cardiovascular strain."
        elif t == 60:
            f['value'] = "Chronic physical illness induces ongoing pain, fatigue, and frustration, which can erode self-esteem and lead to depression, anxiety, and social withdrawal."
        elif t == 61:
            f['value'] = "By observing deviations from the client's documented baseline: changes in posture, facial expressions, speech speed, appetite, gait balance, or sudden agitation."
        elif t == 62 and r == 5:
            f['value'] = "Cognitive or communicative disability can impair the ability to articulate pain verbally, leading to behavioural expressions such as aggression, grimacing, or withdrawal."
        elif t == 63:
            vals = ["Abbey Pain Scale", "Wong-Baker FACES Pain Rating Scale", "facial expression", "vocalisation", "body language", "physiological changes", "physical changes"]
            f['value'] = vals[idx] if idx < len(vals) else vals[-1]
        elif t == 64:
            f['value'] = "Coronary heart disease: Narrowing of coronary arteries impairs myocardial blood supply, causing angina, shortness of breath, and risk of acute myocardial infarction."
        elif t == 65:
            f['value'] = "Poor oral hygiene produces constant dental pain, difficulty chewing, bad breath, and loss of teeth, destroying self-esteem, social confidence, and enjoyment of eating."
        elif t == 67:
            exps = {
                1: "Physical disability: Long-term impairment of the musculoskeletal or neurological systems limiting mobility or dexterity.",
                2: "Sensory disability: Impairment affecting visual or auditory perception.",
                3: "Intellectual disability: Significantly reduced ability to understand new concepts, solve problems, and learn new skills.",
                4: "Cognitive disability: Impairment in memory, attention, executive functioning, or perception.",
                5: "Psychiatric disability: Mental health conditions such as schizophrenia or bipolar disorder impacting emotion, thought, and behaviour.",
                6: "Neurological disability: Damage to the central or peripheral nervous system (e.g. stroke, multiple sclerosis, Parkinson's disease).",
                7: "Hearing impairment: Partial or total inability to perceive acoustic sounds due to damage to the auditory nerve, cochlea, or middle ear.",
                8: "Vision impairment: Significant loss of sight not fully correctable by standard glasses (e.g. macular degeneration, cataracts, glaucoma)."
            }
            if r in exps: f['value'] = exps[r]

        # Tables 70-73: Medical terminology & abbreviations
        elif t == 70 and r == 1:
            f['value'] = "Abrasion: A superficial rubbing or scraping of the surface layers of the skin."
        elif t == 71 and r == 1:
            f['value'] = "Febrile: Showing symptoms of a fever; having an abnormally high body temperature above 37.5°C."
        elif t == 73:
            abbs = {
                1: "Complete Blood Count: Measures red cells, white cells, hemoglobin, and platelets to detect infection or anemia.",
                2: "Blood Pressure: Measures the pressure exerted by circulating blood against arterial walls.",
                3: "Pro re nata (As needed): Medication taken only when required for specific symptoms.",
                4: "Activities of Daily Living: Basic daily self-care tasks (bathing, dressing, eating, mobility).",
                5: "Upper Respiratory Infection: An acute infection affecting the nose, throat, sinuses, or larynx (e.g. common cold, pharyngitis, sinusitis)."
            }
            if r in abbs: f['value'] = abbs[r]

        # Tables 78-87: Case study 1 health monitoring
        elif t in range(78, 88):
            f['value'] = "Follow organizational clinical protocols, check vital signs, report abnormal readings to the Registered Nurse, and record findings in the client health chart."

        # Tables 91-102: Case study 2 Madge fall report
        elif t == 91:
            if r == 3:
                f['value'] = "To the Registered Nurse / Workplace Supervisor immediately, followed by the facility manager and treating doctor."
            elif r == 4:
                f['value'] = "Verbally in person or via telephone immediately, followed by formal written documentation in the organizational Incident Report Form."
            elif r == 5:
                f['value'] = "Immediately upon discovery or stabilization of the client, without delay."
        elif t == 93:
            f['value'] = "Madge exhibited acute distress, confusion, crying, and severe anxiety about falling again."
        elif t == 95:
            f['value'] = "CareConnect College Aged Care Facility - Room 22"
        elif t == 96:
            f['value'] = "Alex Chen, Support Worker"
        elif t == 97:
            f['value'] = "Madge Thompson (Resident, Room 22)"
        elif t == 98:
            f['value'] = "Right hip contusion and hematoma, right elbow abrasion, and lower back tenderness."
        elif t == 99:
            f['value'] = "First aid provided; Registered Nurse attended immediately; Triple Zero (000) dispatched; family notified."
        elif t == 101:
            f['value'] = "At 08:00 AM on 11/03/2026, worker entered Room 22 and found resident Madge on the floor beside her bed. Madge stated she slipped while reaching for her glasses. First aid was administered, vital signs checked (BP 95/60, Pulse 92), RN took clinical charge, and ambulance arrived at 08:35 AM."
        elif t == 102:
            f['value'] = "Alex Chen, Support Worker, Care Connect Services"

    return fields

def populate_chcdiv001(fields):
    for f in fields:
        if f['section'] == 'Assessor Section':
            continue
        t = f['table_idx']
        r = f['row_idx']
        c = f['col_idx']
        idx = f['index_in_cell']
        
        # Table 4: Definitions
        if t == 4:
            if r == 3: f['value'] = "Cultural awareness is the self-examination and understanding of one's own cultural beliefs and an openness to recognizing and respecting differences in others."
            elif r == 4: f['value'] = "Cultural safety is an environment that is spiritually, socially, and emotionally safe, where there is no assault, challenge, or denial of an individual's cultural identity."
            elif r == 5: f['value'] = "Cultural competence is the ability of individuals and systems to effectively communicate and collaborate with people across diverse cultural, ethnic, and linguistic backgrounds."

        # Table 7: Policies
        elif t == 7:
            if r == 1:
                f['value'] = "National Agreement on Closing the Gap (closingthegap.gov.au): Aims to overcome systemic health, justice, and economic inequality for First Nations peoples."
            elif r == 2:
                f['value'] = "National Settlement Framework (homeaffairs.gov.au): Provides support for humanitarian refugees to integrate socially, economically, and linguistically."

        # Tables 12-18 & 22-25: Anti-discrimination legislation
        elif t in [12, 13, 14, 15, 16, 17, 18, 22, 23, 24, 25]:
            lbl = f['label'].lower()
            if "link" in lbl:
                if "disability" in lbl: f['value'] = "https://www.legislation.gov.au/Details/C2016C00763"
                elif "race" in lbl: f['value'] = "https://www.legislation.gov.au/Details/C2016C00089"
                elif "sex" in lbl: f['value'] = "https://www.legislation.gov.au/Details/C2021C00420"
                else: f['value'] = "https://www.legislation.gov.au"
            elif "provision" in lbl or "clause" in lbl:
                if "disability" in lbl: f['value'] = "Part 2, Division 1 (Discrimination in work): Unlawful to discriminate against an employee based on disability."
                elif "race" in lbl: f['value'] = "Section 9: Unlawful to discriminate based on race, colour, descent, or ethnic origin in employment."
                elif "sex" in lbl: f['value'] = "Part 2, Division 1: Unlawful to discriminate on grounds of sex, gender identity, or marital status."
                else: f['value'] = "Part 2, General prohibitions against discrimination in the workplace."
            elif "impact" in lbl:
                f['value'] = "Workers must be provided with equal opportunities, reasonable adjustments, and an inclusive workplace free from harassment."
            elif "penalty" in lbl or "consequence" in lbl:
                f['value'] = "Civil financial penalties, formal compensation orders, mandatory conciliation, and workplace equity audits."
            elif "anti-discrimination law" in lbl:
                if "disability" in lbl: f['value'] = "Disability Discrimination Act 1992 (Cth)"
                elif "race" in lbl: f['value'] = "Racial Discrimination Act 1975 (Cth)"
                elif "sex" in lbl: f['value'] = "Sex Discrimination Act 1984 (Cth)"
                else: f['value'] = "Anti-Discrimination Act 1977 (NSW)"

        # Tables 26-28: Human rights & UDHR
        elif t == 26:
            f['value'] = "Human needs are fundamental biological and emotional necessities (food, water, safety, shelter), whereas human rights are the legal entitlements that guarantee access to meeting those needs with dignity and equality."
        elif t == 27:
            vals = [
                "Universal Declaration of Human Rights (UDHR) Article 23 (Right to work and protection against unemployment).",
                "UDHR Article 18 (Freedom of thought, conscience and religion).",
                "UDHR Article 25 (Right to an adequate standard of living and health care)."
            ]
            f['value'] = vals[idx] if idx < len(vals) else vals[-1]
        elif t == 28:
            f['value'] = "1. Document the human rights breach factually. 2. Ensure victim safety. 3. Report to supervisor under grievance policy. 4. Escalate to Anti-Discrimination NSW or AHRC if unresolved."

        # Table 30: Legal/ethical human rights framework
        elif t == 30:
            f['value'] = "Charter of Human Rights and Principles of Social Justice (AHRC / UN Treaties): Mandating equality, dignity, participation, and protection against discrimination."

        # Tables 33, 35, 38: Human rights principles
        elif t == 33:
            vals = ["Reaffirm: Commitment to human rights.", "Educate: Mandatory staff cultural training.", "Engage: Involving diverse communities."]
            f['value'] = vals[idx] if idx < len(vals) else vals[-1]
        elif t == 35:
            vals = ["Protect: Enforcing zero-tolerance harassment.", "Respect: Valuing cultural and lifestyle choices."]
            f['value'] = vals[idx] if idx < len(vals) else vals[-1]
        elif t == 38:
            vals = ["Participation", "Accountability", "Non-discrimination and Equality", "Empowerment", "Legality"]
            f['value'] = vals[idx] if idx < len(vals) else vals[-1]

        # Tables 41-44: Diversity areas & terms
        elif t == 41:
            f['value'] = "Shared values, traditions, language, and ancestral background passed through generations."
        elif t == 42:
            f['value'] = "Structured systems of faith, ethical rituals, and core spiritual beliefs that guide daily life."
        elif t == 44:
            defs = {
                1: "Lesbian: A woman who is emotionally, romantically, or sexually attracted to other women.",
                2: "Gay: A person who is attracted to people of the same sex or gender.",
                3: "Bisexual: A person who is attracted to more than one gender.",
                4: "Heterosexual: A person who is attracted to people of a different gender.",
                5: "Intersex: A person born with reproductive or physical sex characteristics that do not fit typical male or female norms.",
                6: "Transgender: A person whose gender identity differs from the sex assigned to them at birth."
            }
            if r in defs: f['value'] = defs[r]

        # Tables 45-49: First Nations issues & systems
        elif t == 45:
            f['value'] = "1. Gaps in health outcomes and life expectancy. 2. High rates of child removal and over-representation in the justice system."
        elif t in [46, 47]:
            f['value'] = "Western education suppressed native languages and culture, disrupting traditional knowledge transmission and causing intergenerational educational disadvantage."
        elif t in [48, 49]:
            f['value'] = "Imposed Western religious institutions banned traditional ceremonies, disrupted kinship lore, and severed ancestral spiritual connections to Country."

        # Tables 51-56: Marginalised groups
        elif t == 51:
            f['value'] = "Accessible adaptive sports clubs, inclusive employment programs, and peer advocacy networks."
        elif t in [53, 54]:
            f['value'] = "Anxiety, depression, and social isolation resulting from environmental barriers; supported by accessible counselling and peer mentoring."
        elif t in [55, 56]:
            f['value'] = "Intergenerational trauma from historical dispossession; supported through culturally safe community yarning circles and ACCHO services."

        # Tables 57-59: Trauma & stigma
        elif t == 57:
            f['value'] = "Trauma from war experiences requires a calm, predictable environment and clear communication before initiating tasks."
        elif t == 58:
            f['value'] = "Adopt trauma-informed practice, avoid loud sudden alarms, explain care steps clearly, and respect personal boundaries."
        elif t == 59:
            f['value'] = "Creating separate spaces for Indigenous clients is unlawful racial segregation that perpetuates deep stigma and breaches anti-discrimination laws."

        # Tables 62-67: Influences, changing practices, reflection
        elif t == 62:
            f['value'] = "Multicultural migration has diversified Australian society, requiring healthcare workers to adapt to multilingual and diverse cultural care expectations."
        elif t == 63:
            f['value'] = "Shift toward consumer-directed care and adoption of professional telephone and digital translation services."
        elif t in [65, 67]:
            f['value'] = "Attending cultural diversity training enhances empathy, challenges unconscious bias, and strengthens respectful teamwork."
        elif t == 69:
            vals = ["Australian multicultural background", "Support Worker", "Providing direct personal care and community access", "Care Connect Services"]
            f['value'] = vals[idx] if idx < len(vals) else vals[-1]
        elif t == 72:
            f['value'] = "Support Worker: Applies cultural safety in everyday routines; Care Coordinator: Designs culturally tailored service packages."
        elif t == 73:
            f['value'] = "1. We celebrate and respect diverse cultural identities. 2. We provide culturally safe care. 3. We uphold equal opportunity for all."
        elif t in [76, 77, 78, 81, 82]:
            f['value'] = "Direct communication style: Appreciated by low-context cultures for clarity, but may be perceived as abrupt by high-context cultures; adjusted accordingly."
        elif t == 84:
            f['value'] = "Treating all individuals with unconditional positive regard, challenging stereotypes, and promoting self-determination."
        elif t == 86:
            f['value'] = "Anti-Discrimination Act 1977 (NSW) (https://legislation.nsw.gov.au/view/html/inforce/current/act-1977-048)"
        elif t in [87, 88, 89]:
            f['value'] = "Right to a workplace free from discrimination; responsibility to treat others with respect and follow equity policies."
        elif t == 91:
            f['value'] = "Care Connect Services Diversity and Inclusion Policy v1.2"
        elif t in [92, 93, 94]:
            f['value'] = "Right to equal treatment and respect; responsibility to comply with professional codes of conduct."
        elif t in [96, 97, 98, 99]:
            f['value'] = "Self-reflection helps identify unconscious biases, enabling me to listen actively and avoid imposing Western assumptions onto clients."
        elif t == 101:
            f['value'] = "Limitation: Limited foreign language skills; Improvement: Utilize professional TIS National interpreters."
        elif t in [103, 104, 105, 106]:
            f['value'] = "Language misunderstanding resolved by engaging an accredited TIS National interpreter and verifying client comfort."
        elif t == 115:
            f['value'] = "Cultural misinterpretation of non-verbal cues (e.g. eye contact); resolved by apologizing and clarifying preferences respectfully."

    return fields

def process_group2_all():
    files = [
        ("answers_CHCCCS031_PartA.yaml", populate_chcccs031_parta),
        ("answers_CHCCCS031_PartB.yaml", populate_chcccs031_partb),
        ("answers_CHCCCS038.yaml", populate_chcccs038),
        ("answers_CHCCCS041.yaml", populate_chcccs041),
        ("answers_CHCDIV001.yaml", populate_chcdiv001),
    ]
    for filename, pop_fn in files:
        with open(filename, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        data['fields'] = pop_fn(data['fields'])
        with open(filename, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, allow_unicode=True, sort_keys=False)
            
        empty = [f for f in data['fields'] if f['type'] == 'text' and f['section'] != 'Assessor Section' and (not f['value'] or not str(f['value']).strip())]
        print(f"{filename}: empty candidate text fields = {len(empty)}")
        if empty:
            for e in empty[:5]:
                print(f"  T{e['table_idx']} R{e['row_idx']} C{e['col_idx']} idx{e['index_in_cell']}: {e['label'][:60]}")

if __name__ == "__main__":
    process_group2_all()
