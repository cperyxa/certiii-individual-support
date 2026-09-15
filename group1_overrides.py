"""
Unit-specific benchmark answer dictionaries and overrides for Group 1:
- CHCCCS040
- CHCCOM005
- HLTINF006
- CHCAGE013
"""

CHCCCS040_OVERRIDES = {
    # Table 13: Restrictive practices in Aged Care and Disability Support
    (13, 0, 0, 0): "Aged Care Act 1997 / Quality of Care Principles 2014 (Part 4A)",
    (13, 0, 0, 1): "Restrictive practices must only be used as a last resort, for the shortest possible duration, after exhausting positive behaviour support alternatives. Clinical assessment and informed consent from the consumer or substitute decision-maker are mandatory.",
    (13, 0, 0, 2): "Part 4A, Quality of Care Principles 2014",
    (13, 0, 0, 3): "Care workers must prioritize non-restrictive interventions, adhere strictly to approved behaviour support plans, and maintain constant monitoring and documentation.",
    (13, 0, 0, 4): "National Disability Insurance Scheme (Restrictive Practices and Behaviour Support) Rules 2018",
    (13, 0, 0, 5): "Regulated restrictive practices must be clearly identified, authorised in accordance with state/territory legislation, included in a Behaviour Support Plan lodged with the NDIS Quality and Safeguards Commission, and subject to regular clinical review.",
    (13, 0, 0, 6): "Part 2, Sections 6-12",
    (13, 0, 0, 7): "Workers must only use authorized practices as a last resort, never use prohibited practices, and complete mandatory incident reports to the NDIS Commission if unauthorized use occurs.",
    
    # Table 18: Abuse reporting requirements
    (18, 2, 0): "Workers must immediately report any allegations, disclosures, or reasonable suspicions of abuse, neglect, or exploitation to their supervisor and the relevant statutory authority (e.g. NDIS Commission / Police / NSW Ageing and Disability Commission) within 24 hours in accordance with mandatory reporting policies.",
    
    # Table 20: 8 Aged Care Quality Standards
    (20, 2, 0): "Standard 1: Consumer dignity and choice",
    (20, 3, 0): "Standard 2: Ongoing assessment and planning with consumers",
    (20, 4, 0): "Standard 3: Personal care and clinical care",
    (20, 5, 0): "Standard 4: Services and supports for daily living",
    (20, 6, 0): "Standard 5: Organisation's service environment",
    (20, 7, 0): "Standard 6: Feedback and complaints",
    (20, 8, 0): "Standard 7: Human resources",
    (20, 9, 0): "Standard 8: Organisational governance",
    
    # Table 23: 5 issues impacting health and wellbeing
    (23, 2, 0): "Chronic medical illness and unmanaged physical pain",
    (23, 3, 0): "Social isolation, loneliness, and lack of community engagement",
    (23, 4, 0): "Mental health conditions (e.g. major depression, anxiety disorders)",
    (23, 5, 0): "Cognitive impairment, dementia, or progressive neurological decline",
    (23, 6, 0): "Financial hardship, inadequate housing, or lack of transport access",
    
    # Table 27 & 28: Emotional concerns and issues
    (27, 3, 0): "Anxiety / apprehension",
    (27, 3, 1): "Persistent worry or distress regarding changes in living arrangements, health, or personal safety.",
    (27, 4, 0): "Grief / sadness",
    (27, 4, 1): "Emotional sorrow resulting from the loss of personal independence, loved ones, or familiar routines.",
    (28, 1, 0): "Major depressive disorder",
    (28, 1, 1): "Persistent low mood, profound loss of interest or pleasure, sleep disturbances, and feelings of worthlessness lasting longer than two weeks.",
    (28, 2, 0): "Severe anger / emotional dysregulation",
    (28, 2, 1): "Intense frustration, irritability, or aggressive outbursts arising from unmet needs or cognitive impairment.",
    
    # Table 29, 30, 31: Support strategies, resources, networks
    (29, 3, 0): "Person-centred activity scheduling",
    (29, 3, 1): "Structuring daily routines around individual preferences, hobbies, and strengths to maximize engagement and dignity.",
    (29, 4, 0): "Positive behaviour support",
    (29, 4, 1): "Identifying emotional and environmental triggers and implementing proactive coping mechanisms to reduce distress.",
    (30, 1, 0): "Assistive technology devices",
    (30, 1, 1): "Equipment, communication boards, and mobility aids designed to enhance independent daily living and safety.",
    (30, 2, 0): "Plain-language health educational materials",
    (30, 2, 1): "Written brochures, guides, and visual prompts explaining care procedures and available community services.",
    (31, 1, 0): "Family and informal carer networks",
    (31, 1, 1): "Close relatives, partners, and friends providing ongoing social connection, advocacy, and emotional support.",
    (31, 2, 0): "Community peer support groups",
    (31, 2, 1): "Organised group sessions connecting individuals who share similar lived experiences and challenges."
}

CHCCOM005_OVERRIDES = {
    # Table 4: Preliminary Task 2
    (4, 7, 1): "Aged Care and Disability Support Services",
    
    # Table 22: Duty of care to a child not primary client
    (22, 0, 0): "Take immediate and reasonable action to protect the child from observable physical hazards or unsafe situations in the facility environment.",
    (22, 1, 0): "Promptly report any suspected abuse, neglect, or child protection concerns to the supervisor and statutory child protection authority (DCJ NSW) in accordance with mandatory reporting legislation.",
    
    # Table 23: 5 authoritative sources of information
    (23, 3, 0): "Australian Government Department of Health and Aged Care (health.gov.au)",
    (23, 3, 1): "National health policies, aged care reform guidelines, quality standards, and funding frameworks.",
    (23, 4, 0): "NSW Health (health.nsw.gov.au)",
    (23, 4, 1): "State clinical guidelines, public health orders, infection control protocols, and statutory health regulations.",
    (23, 5, 0): "Aged Care Quality and Safety Commission (agedcarequality.gov.au)",
    (23, 5, 1): "Aged Care Quality Standards, provider audit reports, compliance notices, and consumer rights documentation.",
    (23, 6, 0): "Australian Commission on Safety and Quality in Health Care (safetyandquality.gov.au)",
    (23, 6, 1): "National safety and quality health service standards, clinical care standards, and accreditation information.",
    (23, 7, 0): "SafeWork NSW (safework.nsw.gov.au)",
    (23, 7, 1): "Work Health and Safety Act regulations, codes of practice, hazard management, and incident reporting guidance.",
    
    # Table 24: Conflicts of interest
    (24, 3, 0): "Accepting substantial personal gifts, money, or bequests from a client",
    (24, 3, 1): "Compromises professional objectivity, creates perceived or actual favouritism, and breaches organisational code of conduct.",
    (24, 4, 0): "Providing private secondary paid care services to a client outside work hours",
    (24, 4, 1): "Creates financial conflicts of interest, blurs professional boundaries, and breaches employment contracts.",
    (24, 5, 0): "Providing professional care to a close family member or relative without declaring it",
    (24, 5, 1): "Impairs clinical objectivity, creates boundary confusion, and may lead to preferential treatment or emotional distress.",
    
    # Table 30: Constraints to effective communication
    (30, 3, 0): "Sensory impairment (e.g. hearing loss, vision loss)",
    (30, 3, 1): "Hinders the client's ability to receive auditory or visual verbal cues, requiring assistive hearing aids or clear enunciation.",
    (30, 4, 0): "Cognitive impairment (e.g. dementia, brain injury)",
    (30, 4, 1): "Limits the client's ability to process complex language, retain information, or express needs coherently.",
    (30, 5, 0): "Language and cultural differences (CALD)",
    (30, 5, 1): "Language barriers and differing communication styles may lead to misunderstandings or misinterpretation of intent.",
    (30, 6, 0): "Emotional distress and high anxiety",
    (30, 6, 1): "High stress or fear reduces concentration and receptiveness during important care discussions.",
    (30, 7, 0): "Environmental noise and lack of privacy",
    (30, 7, 1): "Auditory distractions and lack of confidentiality cause embarrassment and impede open dialogue.",
    
    # Table 47 & 48: Meeting difficulties & client rights
    (47, 2, 0): "Client exhibits visible signs of frustration, agitation, or sudden withdrawal from the conversation.",
    (47, 3, 0): "Client gives conflicting statements or appears confused regarding their care preferences and services.",
    (47, 4, 0): "Family member attempts to speak over the client and dominate the conversation contrary to the client's wishes.",
    (48, 1, 0): "If unaddressed, the client's right to informed consent, autonomy, and dignified decision-making will be violated.",
    (48, 2, 0): "The client may receive services that do not align with their actual needs and preferences, compromising quality of care.",
    (51, 2, 0): "The client has a mild hearing impairment which is exacerbated by background noise in the dining hall.",
    (51, 3, 0): "Lack of an accredited language interpreter during technical discussions about medical treatment.",
    
    # Table 61: Service collaboration & contact frequencies
    (61, 1, 0): "Drug and alcohol services, e.g. Drug Alcohol Services Australia",
    (61, 1, 1): "Dr. Sarah Smith, Clinical Case Manager",
    (61, 1, 2): "Monthly",
    (61, 1, 3): "Client profile, risk assessment, and medical history for referral to accommodation and care",
    (61, 1, 4): "Face-to-face meetings, phone, and email",
    (61, 2, 0): "Aboriginal and Torres Strait Islander Health team",
    (61, 2, 1): "David Wilson, Community Liaison Officer",
    (61, 2, 2): "As-needed basis",
    (61, 2, 3): "Aboriginal and Torres Strait Islander client profile, health risk assessment, hospital access coordination, and medical advice",
    (61, 2, 4): "Face-to-face meetings, phone, and email"
}

HLTINF006_OVERRIDES = {
    # Table 13: Infectious agents and transmission
    (13, 0, 0, 0): "Influenza virus / Staphylococcus aureus",
    (13, 0, 0, 1): "Airborne droplet spray from coughing/sneezing, or direct skin-to-skin contact.",
    (13, 0, 0, 2): "Toxoplasma gondii / Ringworm (Microsporum canis)",
    (13, 0, 0, 3): "Direct contact with animal fur/lesions, or handling contaminated litter/feces.",
    (13, 0, 0, 4): "Chlamydia psittaci (Psittacosis) / Cryptococcus neoformans",
    (13, 0, 0, 5): "Inhalation of desiccated bird droppings, respiratory secretions, or feather dust.",
    (13, 0, 0, 6): "Hepatitis B virus (HBV) / Hepatitis C virus (HCV) / HIV",
    (13, 0, 0, 7): "Percutaneous sharps injury (needlestick), or direct contact of non-intact skin/mucous membranes with blood.",
    (13, 0, 0, 8): "Norovirus / Rotavirus / Clostridioides difficile",
    (13, 0, 0, 9): "Faecal-oral route via contaminated hands, or contact with contaminated surfaces/vomitus.",
    (13, 0, 0, 10): "Salmonella enterica / Campylobacter jejuni",
    (13, 0, 0, 11): "Ingestion of contaminated, improperly cooked, or cross-contaminated food items.",
    (13, 0, 0, 12): "Legionella pneumophila / Pseudomonas aeruginosa",
    (13, 0, 0, 13): "Inhalation of contaminated water aerosols (cooling towers, warm water systems) or wound exposure.",
    (13, 0, 0, 14): "Clostridium tetani (Tetanus) / Bacillus anthracis",
    (13, 0, 0, 15): "Inoculation of bacterial spores from soil into broken skin or penetrating wounds.",
    (13, 0, 0, 16): "Multi-drug resistant organisms (MDROs) / Enterococci",
    (13, 0, 0, 17): "Direct contact with improperly disposed clinical waste, contaminated dressings, or body fluid receptacles.",
    
    # Table 24: Steps for handwashing
    (24, 2, 0): "1. Wet hands thoroughly with clean, warm running water.",
    (24, 3, 0): "2. Apply an adequate amount of liquid soap to cover all hand surfaces.",
    (24, 4, 0): "3. Rub hands together vigorously (palm to palm, between fingers, backs of hands, and thumbs) for at least 20 seconds.",
    (24, 5, 0): "4. Rinse hands thoroughly under clean running water until all soap residue is removed.",
    (24, 6, 0): "5. Dry hands completely using a clean, single-use disposable paper towel.",
    (24, 7, 0): "6. Turn off the tap using the paper towel to prevent re-contaminating clean hands.",
    
    # Table 26: Five moments of hand hygiene
    (26, 2, 0): "Moment 1: Before touching a patient / client",
    (26, 3, 0): "Moment 2: Before a clean or aseptic procedure",
    (26, 4, 0): "Moment 3: After body fluid exposure risk",
    (26, 5, 0): "Moment 4: After touching a patient / client",
    (26, 6, 0): "Moment 5: After touching patient / client surroundings",
    
    # Table 27: Alcohol-based hand rub steps
    (27, 2, 0): "1. Apply a palmful of alcohol-based hand rub into a cupped hand to cover all surfaces.",
    (27, 3, 0): "2. Rub hands palm to palm.",
    (27, 4, 0): "3. Rub right palm over left dorsum with interlaced fingers, and vice versa.",
    (27, 5, 0): "4. Rub palm to palm with fingers interlaced.",
    (27, 6, 0): "5. Rub backs of fingers to opposing palms with fingers interlocked.",
    (27, 7, 0): "6. Rotational rubbing of left thumb clasped in right palm, and vice versa.",
    (27, 8, 0): "7. Rotational rubbing backwards and forwards with clasped fingers in palm until completely dry (20-30 seconds).",
    
    # Table 28: Alcohol concentration
    (28, 1, 0): "60% to 80% v/v (volume/volume) ethanol or isopropanol (as recommended by the Australian Guidelines for the Prevention and Control of Infection in Healthcare).",
    (28, 2, 0): "At least 60% (between 60% and 80% v/v alcohol concentration).",
    
    # Table 30: Hand hygiene precautions for skin breaks / skin conditions
    (30, 3, 0): "Open cuts, sores, or abrasions should be covered with waterproof bandages/dressings prior to starting work.",
    (30, 4, 0): "Consider wearing gloves to protect breaks in the skin from exposure to blood or bodily fluids.",
    (30, 6, 0): "Wash with mild soap or with moisturizer and water, then moisturize regularly.",
    (30, 7, 0): "Use an alcohol-based hand rub that contains skin emollient to minimise the risk of skin irritation and drying.",
    
    # Table 36: PPE donning & doffing order
    (36, 3, 0): "Gowns and aprons",
    (36, 4, 0): "Masks",
    (36, 5, 0): "Protective eyewear and face shields",
    (36, 6, 0): "Gloves",
    (36, 8, 0): "Gloves",
    (36, 9, 0): "Protective eyewear and face shields",
    (36, 10, 0): "Gowns and aprons",
    (36, 11, 0): "Masks",
    
    # Table 37: 3 steps for mask fitting
    (37, 2, 0): "Position the mask over your mouth and nose.",
    (37, 3, 0): "Fasten the ties or tapes above and below your ears at the back of your head.",
    (37, 4, 0): "Fit flexible band to nose bridge.",
    
    # Table 38: 3 steps for removing & disposing mask
    (38, 2, 0): "Using clean hands, untie or break the ties at the back of your head without touching the front of the mask.",
    (38, 3, 0): "Touch only the ties of the mask and discard it into the designated waste disposal container.",
    (38, 4, 0): "Perform hand hygiene immediately after disposal.",
    
    # Table 39: 5 steps for putting on gloves
    (39, 2, 0): "Perform hand hygiene before putting on gloves.",
    (39, 3, 0): "Remove gloves one at a time from the box or packaging, holding the top of the cuff.",
    (39, 4, 0): "Put your hand through the glove opening and pull it up to the wrist.",
    (39, 5, 0): "Repeat the same procedure with the second hand.",
    (39, 6, 0): "Adjust gloves to cover wrists or gown cuffs as required.",
    
    # Table 40: 5 steps for removing & disposing gloves
    (40, 2, 0): "Using a gloved hand, grasp the palm area of the other gloved hand and peel off the first glove.",
    (40, 3, 0): "Hold the removed glove in the remaining gloved hand.",
    (40, 4, 0): "Slide fingers of ungloved hand under the remaining glove at the wrist and peel off the second glove over the first glove.",
    (40, 5, 0): "Discard gloves into a designated clinical waste container.",
    (40, 6, 0): "Perform hand hygiene immediately.",
    
    # Table 41: 3 steps for putting on face shield
    (41, 2, 0): "Bending forward, hold on to the straps of the face shield with both hands without touching the front.",
    (41, 3, 0): "Place the elastic behind your head, so that the foam rests comfortably on your forehead.",
    (41, 4, 0): "Check the face shield to make sure it covers the front and sides of the face with no areas left uncovered.",
    
    # Table 42: 3 steps for putting on protective eyewear
    (42, 2, 0): "Pick up the eyewear using the temples.",
    (42, 3, 0): "Use both hands to open the temples.",
    (42, 4, 0): "Place the eyewear over your eyes, making sure that the bridge rests comfortably on your nose and temple tips hook securely over your ears.",
    
    # Table 43: 3 steps for removing & disposing protective eyewear & face shield
    (43, 2, 0): "Remove goggles or face shield from the back by lifting the headband or temples without touching the front surface.",
    (43, 3, 0): "If reusable, place in designated receptacle for reprocessing; otherwise, discard in a waste container.",
    (43, 4, 0): "Perform hand hygiene afterwards.",
    
    # Table 49: 6 guidelines for managing spills
    (49, 2, 0): "Blood and body fluid/substance spills should be dealt with as soon as possible.",
    (49, 3, 0): "In operating rooms or during care procedures, spills should be attended to as soon as it is safe to do so.",
    (49, 4, 0): "Care should be taken to thoroughly clean and dry areas where there is any possibility of bare skin contact with the surface.",
    (49, 5, 0): "PPE should be used for all cleaning procedures and disposed of or sent for reprocessing after use.",
    (49, 6, 0): "Where a spill occurs on a carpet, shampoo or steam clean as soon as possible; do not use bleach or chlorine disinfectant directly.",
    (49, 7, 0): "Wash and dry hands thoroughly after cleaning is completed.",
    
    # Table 50: 5 steps for managing spills
    (50, 2, 0): "Wear appropriate personal protective equipment (gloves, gown, eye protection, mask).",
    (50, 3, 0): "Confine the spill and wipe it up immediately with absorbent paper towels, cloths, or spill granules, then dispose into clinical waste.",
    (50, 4, 0): "Clean thoroughly using neutral detergent and warm water solution.",
    (50, 5, 0): "Disinfect by using a facility-approved intermediate-level disinfectant (e.g. 1000 ppm sodium hypochlorite solution).",
    (50, 6, 0): "Immediately send all reusable supplies and equipment (e.g., mop heads, cloths) for reprocessing and perform hand hygiene.",
    
    # Table 51: Principles of asepsis
    (51, 2, 2): "Support worker",
    (51, 4, 0): "Hand hygiene",
    (51, 4, 2): "Hand washing must be done regularly following the five moments of hand hygiene and correct hand washing procedures to reduce the risk of infection and cross-contamination.",
    (51, 5, 0): "Personal protective equipment (PPE)",
    (51, 5, 2): "PPE must be worn during clinical or care interactions involving potential contact with blood or body fluids to protect both worker and client, and removed correctly.",
    
    # Table 58: 4 characteristics of sharps containers
    (58, 2, 0): "Made of heavy-duty, puncture-resistant plastic.",
    (58, 3, 0): "Can be closed securely with a tight-fitting, puncture-proof lid.",
    (58, 4, 0): "Sharps cannot easily fall out or puncture through the container walls.",
    (58, 5, 0): "Leak-resistant on the sides and bottom, and clearly labelled with the biohazard symbol.",
    
    # Table 59: 4 things to avoid when handling needles & sharps
    (59, 2, 0): "Re-capping or bending used needles.",
    (59, 3, 0): "Removing needles from syringes by hand.",
    (59, 4, 0): "Placing used sharps in general waste or recycling bins.",
    (59, 5, 0): "Leaving sharps unattended or in areas accessible to unauthorised persons or children.",
    
    # Table 78: Infection hazards & risks
    (78, 3, 0): "COVID-19 (SARS-CoV-2)",
    (78, 3, 2): "Close contact with infected client and inhaling respiratory droplets or airborne aerosols during personal care assistance.",
    (78, 4, 0): "Influenza virus",
    (78, 4, 2): "Exposure to infectious respiratory secretions when assisting coughing clients without adequate PPE.",
    (78, 5, 0): "Blood-borne pathogens (Hepatitis B / C)",
    (78, 5, 2): "Direct skin or mucous membrane contact with blood or body fluids during wound care or sharps management."
}

CHCAGE013_OVERRIDES = {
    # Table 5: Person-centred approach in Aged Care
    (5, 0, 0, 0): "Respects the older person's independence and acknowledges their legal and moral right to make decisions regarding their own lifestyle, care routines, and personal goals.",
    (5, 0, 0, 1): "Consult the older person directly before providing any assistance, actively listen to their choices, and support them to perform tasks independently whenever possible.",
    (5, 0, 0, 2): "Empowers the individual by providing clear information and meaningful options, enabling them to control their daily schedule and care arrangements.",
    (5, 0, 0, 3): "Offer genuine choices regarding meal options, clothing, waking and bedtime, and recreational activities, supporting their dignity of risk.",
    (5, 0, 0, 4): "Ensures the older person remains the active director of their life and care journey rather than a passive recipient of services.",
    (5, 0, 0, 5): "Actively include the older person in all care planning conferences, support plan updates, and case reviews, ensuring their expressed wishes guide the care plan.",
    
    # Table 15: Legislation and Statutory Bodies in Aged Care (NSW)
    (15, 0, 0, 0): "Aged Care Act 1997 (Cth)",
    (15, 0, 0, 1): "Regulates commonwealth-funded aged care services, establishes provider obligations, protects consumer rights, and sets out the Aged Care Quality Standards.",
    (15, 0, 0, 2): "Aged Care Quality and Safety Commission Act 2018",
    (15, 0, 0, 3): "Establishes the Aged Care Quality and Safety Commission to protect and promote the health, safety, and wellbeing of aged care consumers and handle complaints.",
    (15, 0, 0, 4): "Guardianship Act 1987 (NSW)",
    (15, 0, 0, 5): "Provides statutory frameworks for substitute decision-making, enduring guardianships, and financial management for individuals lacking decision-making capacity.",
    (15, 0, 0, 6): "Public Health Act 2010 (NSW)",
    (15, 0, 0, 7): "Protects public health and prevents the spread of infectious and notifiable diseases within healthcare and residential care facilities.",
    
    # Table 17: Supervision requirements & support practices for health professionals
    (17, 0, 0, 0): "Ensure that the worker develops a positive and caring relationship with the person they are supporting.",
    (17, 0, 0, 1): "Use encouragement to boost a person’s self-esteem and make them feel capable.",
    (17, 0, 0, 2): "Ensure that the person is closely monitored after taking pain medications.",
    (17, 0, 0, 3): "Regularly check the person’s vital signs after they take pain medication.",
    (17, 0, 0, 4): "Ensure informed consent is given before asking for the person’s medical background from their family or carer.",
    (17, 0, 0, 5): "Ask for the person’s consent to collect information regarding their medical background.",
    (17, 0, 0, 6): "Ensure that the standards for providing psychotherapy are being observed.",
    (17, 0, 0, 7): "Follow codes of practice for delivering psychotherapy support services.",
    
    # Table 48: Mental health condition / Psychosocial disability (Bipolar disorder)
    (48, 0, 1): "Bipolar disorder",
    (48, 2, 0): "Manic episode",
    (48, 2, 1): "This is a period of at least one week during which a person has more energy than normal, is extremely elated or agitated most of the time, and exhibits at least three of the behavioural changes: decreased need for sleep, increased or faster speech, racing thoughts, distractibility, increased activity, or risky behaviour.",
    (48, 2, 2): "Introduce relaxation strategies to the person.",
    (48, 2, 3): "Educate the person’s carer about the relaxation strategies that they can assist the person in doing when they have manic episodes.",
    (48, 3, 0): "Depressive episode",
    (48, 3, 1): "This is a period of at least two weeks during which a person has at least five symptoms: intense sadness or despair, loss of interest in activities once enjoyed, feelings of worthlessness or guilt, fatigue, sleep changes, appetite changes, restlessness or slowed movement, difficulty concentrating, or frequent thoughts of death.",
    (48, 3, 2): "Encourage the person to join social activities in their local community.",
    (48, 3, 4): "Provide a list of same-interest groups that the person can participate in so they can make connections with people who have similar or shared experiences."
}
