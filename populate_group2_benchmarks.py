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
                f['value'] = "Tell the client gently if I have to report safety or abuse concerns by law."
            elif r in [3, 4]:
                f['value'] = "Always follow the client's care plan, support their choices safely, and report any hazards to my supervisor."
                
        # Table 30: Life domains (col 2 = how AT helps, col 3 = example)
        elif t == 30:
            if r == 3: # Self-care
                f['value'] = "Helps the client dress, eat, and groom themselves independently without getting tired." if c == 2 else "Button hook and long-handled shoe horn"
            elif r == 4: # Continence
                f['value'] = "Protects skin, prevents leaks, and preserves personal dignity." if c == 2 else "Urinary drainage bags and waterproof mattress protector"
            elif r == 5: # Hygiene
                f['value'] = "Enables safe, unassisted showering and teeth cleaning." if c == 2 else "Shower chair with backrest and easy-grip toothbrush"
            elif r == 6: # Communication
                f['value'] = "Helps clients who have trouble speaking to express their needs and choices." if c == 2 else "Communication tablet with picture symbols"
            elif r == 7: # Mobility
                f['value'] = "Gives balance and support when walking indoors or outside." if c == 2 else "4-wheel walker with handbrakes and seat"
            elif r == 8: # Transferring
                f['value'] = "Helps move safely between bed, chair, and wheelchair without back strain." if c == 2 else "Mobile standing hoist with sling"

        # Table 31: Life domains
        elif t == 31:
            doms = {
                1: ("Gives visual reminders and helps organise daily routines.", "Digital pictorial schedule tablet"),
                2: ("Gives spoken reminders for medication and meal times.", "Talking digital calendar day clock"),
                3: ("Magnifies small text and reads words aloud.", "Electronic video magnifier / Screen-reading software"),
                4: ("Makes voices clearer and cuts down background noise.", "Digital hearing aid with Bluetooth connectivity"),
                5: ("Makes cooking, peeling, and cutting food easier and safer.", "Ergonomic easy-grip kitchen utensils"),
                6: ("Allows playing cards and board games independently.", "Adaptive card holders and large-print games"),
                7: ("Lets the client listen to audiobooks easily.", "Audiobook player with high-contrast buttons"),
                8: ("Helps with reading, typing, and using a computer.", "Voice typing software and adaptive keyboard"),
                9: ("Makes desk work comfortable and accessible.", "Adjustable sit-stand desk and trackball mouse")
            }
            if r in doms:
                f['value'] = doms[r][0] if c == 1 else doms[r][1]

        # Table 32: Life domains
        elif t == 32:
            doms2 = {
                1: ("Lets the client unlock doors and enter home easily.", "Smart door lock with sensor and lever handles"),
                2: ("Calls support staff quickly in an emergency.", "Wearable wireless call pendant"),
                3: ("Helps travel safely around paths and the neighbourhood.", "Motorized mobility scooter"),
                4: ("Steadies shaky hands so food doesn't spill.", "Weighted cutlery and high-rim scooper plate"),
                5: ("Allows drinking comfortably without tilting the head back.", "Two-handled mug with nose cut-out lid"),
                6: ("Relieves pressure on skin to prevent bedsores.", "Alternating air pressure mattress overlay"),
                7: ("Stops back strain for carers when repositioning clients.", "Slide sheets and transfer hoist")
            }
            if r in doms2:
                f['value'] = doms2[r][0] if c == 1 else doms2[r][1]

        # Table 33: R4 C0
        elif t == 33 and r == 4:
            f['value'] = "By removing physical and communication barriers, assistive technology helps clients join in everyday activities and hobbies with confidence and independence."

        # Table 35: Risk strategies
        elif t == 35:
            if r == 3:
                f['value'] = "Follow the workplace code of conduct, complete mandatory reporting training, and keep my supervisor informed."
            elif r == 4:
                f['value'] = "Involve the client in all care discussions, respect their cultural background, and support their choices."
            elif r == 5:
                f['value'] = "Keep walkways clear of clutter, make sure lighting is good, install grab rails, and ensure mobility aids are within reach."

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
            if r == 2: f['value'] = "Restrictive practices are actions or equipment that stop a person from moving freely or doing what they want, used only as a last resort to keep them or others safe after positive support strategies have been tried."
            elif r == 3: f['value'] = "Authorised restrictive practices must only be used as a last resort to prevent serious harm after trying positive behaviour support strategies."
            elif r == 4:
                vals = [
                    "Chemical restraint: Using medication for the primary purpose of controlling behaviour.",
                    "Mechanical restraint: Using devices or straps to restrict free movement of the body.",
                    "Physical restraint: Using hands or physical force to hold or restrict movement.",
                    "Environmental restraint: Locking doors or restricting access to parts of the home or personal belongings.",
                    "Seclusion: Keeping someone alone in a room that they are not free to leave."
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
                    "Physical impacts: Bruising, pressure sores, loss of muscle strength, and injuries.",
                    "Psychological impacts: Fear, trauma, depression, loss of dignity, and losing trust in carers."
                ]
                f['value'] = vals[idx] if idx < len(vals) else vals[-1]
            elif r == 7:
                vals = [
                    "Only to prevent immediate, serious physical injury to the person or others after all calming strategies have been tried.",
                    "During an acute crisis as an emergency safety measure while waiting for clinical help."
                ]
                f['value'] = vals[idx] if idx < len(vals) else vals[-1]

        # Table 19: Risks of restrictive practices
        elif t == 19 and r == 2:
            f['value'] = "Risks include physical injury, cuts and bruises, breathing difficulties, severe emotional distress, and loss of dignity."
            
        # Table 20: Behaviour support plan requirements
        elif t == 20:
            if r == 2: f['value'] = "The Behaviour Support Plan must contain proactive strategies, functional assessment, clear authorization, and steps to reduce and eliminate the restraint."
            elif r == 3: f['value'] = "1. Authorisation under state legislation. 2. Regular clinical review. 3. Monthly reporting to the NDIS Commission."
            
        # Table 21: Technology & choice
        elif t == 21:
            if r == 2: f['value'] = "Smart home automation, voice-controlled lights, and picture schedule apps allow people to control their own room and daily routine independently."
            elif r == 3: f['value'] = "1. Providing clear, easy-to-understand information about care options. 2. Supporting the client to run their own care meetings."
            elif r == 4: f['value'] = "Giving clients choices validates their preferences, builds self-esteem, and helps them feel in control of their own life, reducing frustration."
            elif r == 5:
                vals = [
                    "Presenting daily options in simple formats (visual cards, Easy Read) and explaining benefits and risks clearly.",
                    "Giving the person enough time to make their own decision without rushing them."
                ]
                f['value'] = vals[idx] if idx < len(vals) else vals[-1]
            
        # Table 22: Rights to planning
        elif t == 22:
            if r == 2: f['value'] = "Under the NDIS Act 2013 and UNCRPD Article 12, people with disability have the right to be central to planning and make decisions about their own lives."
            elif r == 3: f['value'] = "Under the Charter of Aged Care Rights, consumers have the right to have control over and make decisions about their care, personal and social life."
            
        # Table 23: Strategies for planning
        elif t == 23:
            f['value'] = "1. Preparing before meetings using visual tools. 2. Involving an independent advocate to support the client's decisions."

        # Tables 24-26: Assistive technologies
        elif t in [24, 25, 26]:
            at_dict = {
                "self-care": ("Helps client dress, eat, and perform grooming independently.", "Button hook and long-handled shoe horn"),
                "continence": ("Protects skin, prevents leaks, and maintains personal dignity.", "Urinary drainage bags and waterproof mattress protector"),
                "hygiene": ("Enables safe, unassisted showering and teeth cleaning.", "Shower chair with backrest and easy-grip toothbrush"),
                "communication": ("Helps clients who have trouble speaking to express choices.", "Communication tablet with symbol grid"),
                "mobility": ("Provides balance and support during indoor and outdoor walking.", "4-wheel walker with handbrakes and seat"),
                "transferring": ("Helps move safely between bed and wheelchair without back strain.", "Mobile standing hoist with harness"),
                "cognition": ("Provides visual reminders and daily task organizers.", "Digital pictorial schedule tablet"),
                "memory loss": ("Gives spoken reminders for medication and meal times.", "Talking digital calendar day clock"),
                "vision": ("Magnifies small text and reads words aloud.", "Electronic video magnifier / Screen-reading software"),
                "hearing": ("Makes voices clearer and cuts down background noise.", "Digital hearing aid with Bluetooth loop connectivity"),
                "daily living activities": ("Assists with cooking, cleaning, and meal prep.", "Ergonomic easy-grip kitchen utensils"),
                "recreation": ("Allows independent participation in games and hobbies.", "Adaptive card holders and large-print games"),
                "leisure": ("Lets the client listen to audiobooks easily.", "Audiobook player with high-contrast buttons"),
                "education": ("Supports reading, typing, and using a computer.", "Voice typing software and adaptive keyboard"),
                "employment": ("Makes desk work comfortable and accessible.", "Adjustable sit-stand desk and trackball mouse"),
                "home": ("Lets the client unlock doors and enter home easily.", "Smart door lock with sensor and lever door handles"),
                "care residence": ("Calls support staff quickly in an emergency.", "Wearable wireless nurse call pendant"),
                "outdoors": ("Helps travel safely around paths and the neighbourhood.", "All-terrain motorized mobility scooter"),
                "eating": ("Steadies shaky hands so food doesn't spill.", "Weighted adaptive cutlery and high-rim scooper plate"),
                "drinking": ("Allows drinking comfortably without tilting the head back.", "Two-handled mug with dysphagia cut-out lid"),
                "pressure area management": ("Relieves pressure on skin to prevent bedsores.", "Alternating air pressure mattress overlay"),
                "carer support": ("Stops back strain for carers when repositioning clients.", "Slide sheets and ceiling track transfer hoist")
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
            f['value'] = "Assistive technology helps people overcome physical limitations so they can do daily tasks, hobbies, and work on their own terms."

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
                f['value'] = "Three work boundaries: 1. Never accept gifts of money or lend money to clients. 2. Keep relationships strictly professional (not friends outside of work). 3. Only do tasks I have been trained and certified to perform."
            elif r == 1:
                f['value'] = "Three responsibilities: 1. Deliver care following the client's care plan. 2. Write clear, accurate daily progress notes. 3. Report any changes in client health or hazards to my supervisor."
            elif r == 2:
                f['value'] = "Three limitations: 1. Cannot alter prescribed medications or dosages. 2. Cannot give legal or financial advice. 3. Cannot perform invasive nursing procedures."

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
            f['value'] = "Bruising and a small skin tear on left forearm; Judith was very upset, crying, and in pain."
        elif t == 54:
            f['value'] = "Judith stated she was handled roughly by agency staff during morning transfer; call buzzer was left unplugged behind the bed."
        elif t == 55:
            f['value'] = "Alex Chen (Support Worker) and Sarah Jenkins (Registered Nurse)."

        # Table 67: Matilda strategies
        elif t == 67:
            f['value'] = "Arrange for a physiotherapist to assess Matilda and design a gentle walking and balance exercise program." if r == 3 else "Invite Matilda to join the weekly facility gardening group to make friends and enjoy the outdoors."

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
            f['value'] = "Produces eggs (ova), makes female hormones (estrogen and progesterone), and carries and nourishes a baby during pregnancy."
        elif t == 6 and c == 1:
            systems = {
                1: "Produces and carries sperm and makes male sex hormones (testosterone).",
                2: "Protects the body against germs and dirt, helps control body temperature through sweating, and senses touch, heat, and pain.",
                3: "Drains extra fluid from body tissues back to the blood and helps filter out germs through lymph nodes.",
                4: "Senses changes inside and outside the body, sends messages through nerves to the brain, and controls our movements and reactions.",
                5: "Fights off harmful germs like bacteria and viruses to protect the body from illness and infections.",
                6: "Filters waste from the blood, balances fluid levels in the body, and gets rid of extra water and waste as urine."
            }
            if r in systems: f['value'] = systems[r]

        # Tables 37-39: System interactions & hormones
        elif t == 37:
            vals = ["cardiovascular", "respiratory", "muscular", "skeletal"]
            f['value'] = vals[idx] if idx < len(vals) else vals[-1]
        elif t == 38:
            if idx == 0: f['value'] = "Through tiny sensory nerve endings in the skin that detect touch, pressure, temperature, and pain."
            elif idx == 1: f['value'] = "sensory"
            elif idx == 2: f['value'] = "central nervous"
        elif t == 39:
            vals = ["Gonads (testes in males and ovaries in females)", "endocrine", "bloodstream", "target tissues", "homeostasis", "metabolic", "growth"]
            f['value'] = vals[idx] if idx < len(vals) else vals[-1]

        # Table 41: Sensory organs
        elif t == 41:
            exps = {
                1: "Light enters the eye and hits the retina, which sends visual messages through the optic nerve to the brain.",
                2: "Sound waves enter the ear canal and make the eardrum vibrate, sending sound signals to the brain and helping us keep our balance.",
                3: "Scent molecules in the air are detected by nerve cells in the nose, sending smell signals to the brain.",
                4: "Taste buds on the tongue detect sweet, salty, sour, bitter, and savoury tastes and trigger saliva."
            }
            if r in exps: f['value'] = exps[r]

        # Tables 42-47: Homeostasis
        elif t == 42:
            f['value'] = "When the body is hot, blood vessels widen (flushing) and we sweat so the skin cools down as sweat evaporates. When cold, blood vessels narrow to keep heat in and muscles shiver to create warmth."
        elif t == 43:
            vals = ["sweat normally", "sweat glands", "heat exhaustion", "hyperthermia", "core body temperature"]
            f['value'] = vals[idx] if idx < len(vals) else vals[-1]
        elif t == 44:
            f['value'] = "The kidneys balance water and minerals in the body, holding onto fluid if we are dehydrated or making more urine if we drink extra water."
        elif t == 45:
            vals = ["kidney", "large intestine", "lungs", "skin", "sweat", "urea", "carbon dioxide", "feces", "urine", "filtration"]
            f['value'] = vals[idx] if idx < len(vals) else vals[-1]
        elif t == 46:
            f['value'] = "Systolic is the higher pressure when the heart contracts and pumps blood out. Diastolic is the lower resting pressure when the heart relaxes between beats."
        elif t == 47:
            f['value'] = "White blood cells fight off infections by swallowing up germs or making antibodies to destroy harmful bacteria and viruses."

        # Tables 48-53: Physical activity & movement
        elif t == 48:
            f['value'] = "Older adults with poor mobility should do gentle balance exercises, seated exercises, and short walks for about 30 minutes on most days to prevent falls."
        elif t == 49:
            f['value'] = "Active exercise is when the client moves their own body to stay fit. Passive exercise is when a carer gently moves a client's joints (for someone who is bedbound or had a stroke) to keep joints from getting stiff."
        elif t == 50:
            f['value'] = "Giving balanced healthy meals that meet the client's dietary needs, and helping with daily teeth brushing and personal washing."
        elif t == 51:
            f['value'] = "Good nutrition gives the body vitamins and protein to heal skin and stay strong, while good hygiene stops germs from spreading."
        elif t == 52:
            f['value'] = "Tooth decay and sore gums cause severe mouth pain, making it difficult to chew, leading to food avoidance, poor nutrition, and weight loss."
        elif t == 53:
            f['value'] = "Disabilities like stroke paralysis, arthritis, or muscle weakness make it hard to move around, needing walking aids, wheelchairs, and carer help."

        # Tables 54-58: Indicators of issues & ageing
        elif t == 54:
            inds = {
                1: "Malnutrition: Clothes fitting loosely, noticeable weight loss, low energy, and tired appearance.",
                2: "Dehydration: Dry cracked lips, dark strong-smelling urine, sunken eyes, and feeling dizzy.",
                3: "Skin tear / wound: A cut, scrape, redness, or bleeding on fragile skin.",
                4: "Incontinence: Wet clothes or bedding, strong urine smell, and red sore skin around the groin.",
                5: "Respiratory infection: Coughing with yellow or green phlegm, wheezing, shortness of breath, and fever.",
                6: "Oral health: Bleeding or swollen gums, loose teeth, bad breath, or painful mouth ulcers.",
                7: "Appetite: Leaving most food untouched, skipping meals, or refusing to eat."
            }
            if r in inds: f['value'] = inds[r]
        elif t == 55:
            inds2 = {
                1: "Dysphagia: Coughing or choking while eating or drinking, clearing throat often, or holding food in cheeks.",
                2: "Bone health: Loss of height, stooped posture, or fractures from minor bumps.",
                3: "Food intolerance: Stomach cramps, bloating, nausea, or diarrhoea after eating certain foods.",
                4: "Dementia: Getting lost in familiar places, forgetting recent conversations, and confusion with daily tasks.",
                5: "Cognitive decline: Trouble following simple instructions, forgetting names, or sudden confusion."
            }
            if r in inds2: f['value'] = inds2[r]
        elif t == 56:
            if r == 6:
                f['value'] = "Ageing causes dry mouth, receding gums, brittle teeth, and reduced taste bud sensitivity."
            elif r == 7:
                f['value'] = "Weakening throat muscles, dry mouth, and slower swallowing reflexes make older people more likely to cough or choke on food."
        elif t == 57:
            f['value'] = "Thinning bones (osteoporosis), making bones break easily from minor falls." if r == 1 else "Skin becomes thinner, drier, and loses fat padding, making it tear easily."
        elif t == 58:
            f['value'] = "Feeling lonely, anxious, or depressed after losing independence, moving out of home, or losing loved ones."

        # Tables 59-65: Wellbeing, pain, diseases
        elif t == 59:
            f['value'] = "Less physical activity burns fewer calories, while some medications increase appetite, leading to weight gain and extra strain on the heart and joints."
        elif t == 60:
            f['value'] = "Living with constant pain or sickness makes people feel tired and frustrated, which can lead to feeling down, anxious, or withdrawing from friends."
        elif t == 61:
            f['value'] = "By watching for changes from the client's normal behaviour: looking pale or tired, grimacing, moving slower than usual, eating less, or sudden confusion."
        elif t == 62 and r == 5:
            f['value'] = "Clients who have trouble speaking or memory loss might not be able to say they are in pain, so they might show it by crying, grimacing, withdrawing, or becoming restless and agitated."
        elif t == 63:
            vals = ["Abbey Pain Scale", "Wong-Baker FACES Pain Rating Scale", "facial expression", "vocalisation", "body language", "physiological changes", "physical changes"]
            f['value'] = vals[idx] if idx < len(vals) else vals[-1]
        elif t == 64:
            f['value'] = "Coronary heart disease: Fatty deposits build up in the blood vessels supplying the heart, reducing blood flow and causing chest pain (angina) or a heart attack."
        elif t == 65:
            f['value'] = "Tooth decay and mouth pain make eating uncomfortable, cause bad breath, and stop people from smiling or socializing because of embarrassment."
        elif t == 67:
            exps = {
                1: "Physical disability: Long-term physical condition that limits movement, strength, or coordination.",
                2: "Sensory disability: Loss of sight or hearing that affects how someone takes in information.",
                3: "Intellectual disability: Difficulty learning new things, understanding complex concepts, and problem-solving.",
                4: "Cognitive disability: Impairment affecting memory, concentration, thinking, and planning.",
                5: "Psychiatric disability: Mental health conditions (like depression, bipolar, or schizophrenia) that affect mood and daily functioning.",
                6: "Neurological disability: Conditions affecting the brain and nerves, such as stroke, Parkinson's disease, or multiple sclerosis.",
                7: "Hearing impairment: Partial or total hearing loss in one or both ears.",
                8: "Vision impairment: Significant loss of eyesight that cannot be fully fixed by glasses."
            }
            if r in exps: f['value'] = exps[r]

        # Tables 70-73: Medical terminology & abbreviations
        elif t == 70 and r == 1:
            f['value'] = "Abrasion: A graze or scrape on the surface of the skin."
        elif t == 71 and r == 1:
            f['value'] = "Febrile: Having a fever; body temperature above 37.5°C."
        elif t == 73:
            abbs = {
                1: "Full Blood Count: Blood test checking red and white blood cells and platelets to look for infection or anaemia.",
                2: "Blood Pressure: Measures the pressure of blood pumping through the arteries.",
                3: "PRN (Pro re nata): Medication given only when needed for specific symptoms.",
                4: "ADLs (Activities of Daily Living): Everyday tasks like showering, dressing, eating, and walking.",
                5: "URI: Upper Respiratory Infection (like a head cold, sinus infection, or sore throat)."
            }
            if r in abbs: f['value'] = abbs[r]

        # Tables 78-87: Case study 1 health monitoring
        elif t in range(78, 88):
            f['value'] = "Follow workplace care procedures, check vital signs, report unusual readings to the Registered Nurse, and record notes in the client's chart."

        # Tables 91-102: Case study 2 Madge fall report
        elif t == 91:
            if r == 3:
                f['value'] = "Report immediately in person to RN Sarah Jenkins, followed by the facility manager and treating doctor."
            elif r == 4:
                f['value'] = "Verbally in person immediately, followed by completing the workplace Incident Report Form."
            elif r == 5:
                f['value'] = "Immediately as soon as Madge is made safe and attended to."
        elif t == 93:
            f['value'] = "Madge was shaken up, crying, and anxious about falling again."
        elif t == 95:
            f['value'] = "CareConnect College Aged Care Facility - Room 22"
        elif t == 96:
            f['value'] = "Alex Chen, Support Worker"
        elif t == 97:
            f['value'] = "Madge Thompson (Resident, Room 22)"
        elif t == 98:
            f['value'] = "Bruising on right hip and a small graze on right elbow."
        elif t == 99:
            f['value'] = "Gave first aid, called RN Sarah Jenkins immediately, checked vitals (BP 95/60, Pulse 92), made Madge comfortable, and called 000 ambulance."
        elif t == 101:
            f['value'] = "At 08:00 AM on 11/03/2026, I walked into Room 22 and found resident Madge sitting on the floor beside her bed. She told me she slipped while reaching for her glasses. I stayed with her, called RN Sarah Jenkins, checked vital signs, applied first aid to her elbow graze, and ambulance arrived at 08:35 AM."
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
            if r == 3: f['value'] = "Cultural awareness is being aware of my own cultural background and values, and respecting that others have different cultures and ways of life."
            elif r == 4: f['value'] = "Cultural safety means creating a welcoming environment where clients feel respected, safe, and comfortable to be themselves without experiencing judgment or discrimination."
            elif r == 5: f['value'] = "Cultural competence is the ability to communicate, work effectively, and build respectful relationships with people from all different cultural and language backgrounds."

        # Table 7: Policies
        elif t == 7:
            if r == 1:
                f['value'] = "National Agreement on Closing the Gap (closingthegap.gov.au): Aims to overcome health, education, and social gaps for Aboriginal and Torres Strait Islander peoples."
            elif r == 2:
                f['value'] = "National Settlement Framework (homeaffairs.gov.au): Provides support for humanitarian refugees to settle, learn English, and join the community."

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
                f['value'] = "Workers must be given equal opportunities, reasonable workplace adjustments, and an environment free from harassment."
            elif "penalty" in lbl or "consequence" in lbl:
                f['value'] = "Fines, paying compensation, formal conciliation meetings, and workplace equity audits."
            elif "anti-discrimination law" in lbl:
                if "disability" in lbl: f['value'] = "Disability Discrimination Act 1992 (Cth)"
                elif "race" in lbl: f['value'] = "Racial Discrimination Act 1975 (Cth)"
                elif "sex" in lbl: f['value'] = "Sex Discrimination Act 1984 (Cth)"
                else: f['value'] = "Anti-Discrimination Act 1977 (NSW)"

        # Tables 26-28: Human rights & UDHR
        elif t == 26:
            f['value'] = "Human needs are basic things required to survive (like food, clean water, shelter, and medical care), while human rights are the legal protections ensuring everyone is treated fairly and with dignity."
        elif t == 27:
            vals = [
                "Universal Declaration of Human Rights (UDHR) Article 23 (Right to work and protection against unemployment).",
                "UDHR Article 18 (Freedom of thought, conscience and religion).",
                "UDHR Article 25 (Right to an adequate standard of living and health care)."
            ]
            f['value'] = vals[idx] if idx < len(vals) else vals[-1]
        elif t == 28:
            f['value'] = "1. Write down factual notes of what happened. 2. Make sure the client is safe. 3. Report to supervisor. 4. Escalate to Anti-Discrimination NSW or AHRC if unresolved."

        # Table 30: Legal/ethical human rights framework
        elif t == 30:
            f['value'] = "Charter of Human Rights and Principles of Social Justice (AHRC / UN Treaties): Protecting equality, dignity, participation, and non-discrimination."

        # Tables 33, 35, 38: Human rights principles
        elif t == 33:
            vals = ["Reaffirm: Upholding human rights in all care.", "Educate: Completing workplace diversity training.", "Engage: Involving diverse community groups."]
            f['value'] = vals[idx] if idx < len(vals) else vals[-1]
        elif t == 35:
            vals = ["Protect: Zero tolerance for harassment or discrimination.", "Respect: Valuing individual cultural and lifestyle choices."]
            f['value'] = vals[idx] if idx < len(vals) else vals[-1]
        elif t == 38:
            vals = ["Participation", "Accountability", "Non-discrimination and Equality", "Empowerment", "Legality"]
            f['value'] = vals[idx] if idx < len(vals) else vals[-1]

        # Tables 41-44: Diversity areas & terms
        elif t == 41:
            f['value'] = "Shared values, traditions, language, and ancestral background passed down through generations."
        elif t == 42:
            f['value'] = "Beliefs, spiritual traditions, and values that guide daily life and rituals."
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
            f['value'] = "1. Health gaps and shorter life expectancy. 2. High rates of child removal and over-representation in the justice system."
        elif t in [46, 47]:
            f['value'] = "Past policies stopped First Nations children from speaking their language and practicing traditions, causing loss of language and deep disadvantage across generations."
        elif t in [48, 49]:
            f['value'] = "European religious rules banned traditional ceremonies, broke kinship ties, and disconnected people from Country and culture."

        # Tables 51-56: Marginalised groups
        elif t == 51:
            f['value'] = "Accessible sports clubs, inclusive job programs, and disability peer advocacy groups."
        elif t in [53, 54]:
            f['value'] = "Feeling anxious, depressed, and isolated from community barriers; supported by accessible counselling and peer mentoring."
        elif t in [55, 56]:
            f['value'] = "Intergenerational trauma from historical dispossession; supported through culturally safe community yarning circles and ACCHO services."

        # Tables 57-59: Trauma & stigma
        elif t == 57:
            f['value'] = "Trauma from war experiences means workers need to provide a calm, predictable environment and explain what they are doing before touching the person."
        elif t == 58:
            f['value'] = "Use trauma-informed care: avoid loud sudden noises, explain care steps clearly, and respect personal space and boundaries."
        elif t == 59:
            f['value'] = "Making separate spaces for Indigenous clients is unlawful racial segregation that creates stigma and breaches anti-discrimination laws."

        # Tables 62-67: Influences, changing practices, reflection
        elif t == 62:
            f['value'] = "Migration has made Australia very diverse, so support workers need to understand different cultures and support clients who speak other languages."
        elif t == 63:
            f['value'] = "Focusing on consumer-directed care and using phone interpreters (like TIS National) and multilingual signs."
        elif t in [65, 67]:
            f['value'] = "Attending cultural diversity training builds empathy, challenges unconscious bias, and improves teamwork."
        elif t == 69:
            vals = ["Australian multicultural background", "Support Worker", "Providing direct personal care and community access", "Care Connect Services"]
            f['value'] = vals[idx] if idx < len(vals) else vals[-1]
        elif t == 72:
            f['value'] = "Support Worker: Applies cultural safety in everyday care; Care Coordinator: Organises culturally appropriate support packages."
        elif t == 73:
            f['value'] = "1. We celebrate and respect diverse cultural identities. 2. We provide culturally safe care. 3. We uphold equal opportunity for all."
        elif t in [76, 77, 78, 81, 82]:
            f['value'] = "Being aware that speaking too directly might seem rude to some cultural groups, while being too indirect might confuse others; adjusting my style politely."
        elif t == 84:
            f['value'] = "Treating all clients with kindness and respect, challenging unfair stereotypes, and supporting their choices."
        elif t == 86:
            f['value'] = "Anti-Discrimination Act 1977 (NSW) (https://legislation.nsw.gov.au/view/html/inforce/current/act-1977-048)"
        elif t in [87, 88, 89]:
            f['value'] = "Right to work without discrimination; responsibility to treat others with respect and follow equity policies."
        elif t == 91:
            f['value'] = "Care Connect Services Diversity and Inclusion Policy v1.2"
        elif t in [92, 93, 94]:
            f['value'] = "Right to equal treatment and respect; responsibility to comply with professional codes of conduct."
        elif t in [96, 97, 98, 99]:
            f['value'] = "Self-reflection helps me notice my own assumptions, keep an open mind, and give culturally respectful care to every person."
        elif t == 101:
            f['value'] = "Limitation: Limited foreign language skills; Improvement: Use professional TIS National interpreters."
        elif t in [103, 104, 105, 106]:
            f['value'] = "Language misunderstanding resolved by using an accredited TIS National interpreter and checking client comfort."
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
