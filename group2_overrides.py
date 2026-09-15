"""
Benchmark answer dictionaries and overrides for Group 2:
- CHCCCS031 Part A (Knowledge Assessment)
- CHCCCS031 Part B (Simulated / Workplace Assessment)
- CHCCCS038 (Facilitate the empowerment of people receiving support)
- CHCCCS041 (Recognise healthy body systems)
- CHCDIV001 (Work with diverse people)
"""

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

# ==============================================================================
# CHCCCS031 Part A Overrides
# ==============================================================================
CHCCCS031_PARTA_OVERRIDES = {
    # Table 3: Person-centred practices
    (3, 2, 0, 0): "Respect for individual autonomy and personal preferences",
    (3, 2, 0, 1): "Active participation and partnership in all care decision-making",
    (3, 2, 0, 2): "Holistic focus on strengths, abilities, and meaningful community connections",
    (3, 3, 0, 0): "Traditional approach is service-driven, focusing on organisational routines, deficits, and what the service dictates.",
    (3, 3, 0, 1): "Person-centred approach is individual-driven, focusing on client strengths, goals, personal dignity, and self-direction.",
    (3, 4, 0, 0): "A person-centred/self-directed model gives the individual direct control over how their funding and support services are planned and delivered.",
    (3, 4, 0, 1): "An institutional model imposes rigid schedules, standard procedures, and service-directed care with minimal individual choice.",
    
    # Table 4: 3 benefits of person-centred approaches
    (4, 0, 0, 0): "Enhances the individual's sense of self-worth, empowerment, and personal dignity.",
    (4, 0, 0, 1): "Improves overall health, wellbeing, and quality of life outcomes through tailored support.",
    (4, 0, 0, 2): "Fosters greater trust, collaboration, and satisfaction between the person and support workers.",
    
    # Table 5: Strengths-based practices
    (5, 2, 0, 0): "Every individual possesses unique capabilities, competencies, and inherent potential for growth.",
    (5, 2, 0, 1): "Collaboration between worker and client is built on mutual respect rather than expert-client hierarchy.",
    (5, 2, 0, 2): "The environment contains informal networks and community resources that can support individual goals.",
    (5, 3, 0, 0): "Identify and actively acknowledge what the person can do independently before providing assistance.",
    (5, 3, 0, 1): "Support the individual to utilize their existing skills and resources to solve daily challenges.",
    (5, 3, 0, 2): "Structure goals around the person's passions, past experiences, and positive aspirations.",
    (5, 4, 0, 0): "It prevents dependency, builds self-efficacy, and empowers people to lead fulfilling, independent lives.",
    
    # Table 6: Active support
    (6, 2, 0, 0): "Active support is an evidence-based approach that enables people with intellectual and physical disabilities to engage meaningfully in daily domestic, recreational, and vocational activities at home and in the community, regardless of their level of impairment.",
    (6, 3, 0, 0): "Every moment has potential: Using daily routine tasks (cooking, tidying, shopping) as opportunities for engagement and learning.",
    (6, 3, 0, 1): "Little and often: Breaking complex activities down into manageable components so the person can participate frequently without fatigue.",
    (6, 3, 0, 2): "Graded assistance: Providing just the right amount of help (verbal prompts, modelling, physical guidance) to enable success.",
    (6, 3, 0, 3): "Maximising choice and control: Offering continuous opportunities for the person to decide what, when, and how they want to participate.",
    
    # Table 7: Respectful behaviour
    (7, 2, 0, 0): "Unconditional positive regard and preservation of human dignity.",
    (7, 2, 0, 1): "Respect for personal privacy, personal space, and confidentiality.",
    (7, 2, 0, 2): "Non-judgmental acceptance of cultural, religious, and lifestyle choices.",
    (7, 3, 0, 0): "Personal care and grooming preferences (clothing, bathing schedule, hairstyle).",
    (7, 3, 0, 1): "Dietary, mealtime, and recreational choices.",
    (7, 3, 0, 2): "Social, cultural, and spiritual relationships and community participation.",
    (7, 4, 0, 0): "Always knocking and asking for permission before entering private rooms or beginning care routines.",
    (7, 4, 0, 1): "Actively listening without interrupting and using the client's preferred name and title.",
    (7, 4, 0, 2): "Explaining procedures clearly beforehand and seeking ongoing verbal or non-verbal consent.",
    
    # Table 8: Documentation and reports
    (8, 3, 2): "To ensure critical safety events, injuries, or hazards are officially recorded, regulatory reporting duties are fulfilled, and proactive risk controls are established.",
    (8, 3, 3): "Completed objectively, factually, and immediately following an incident using the standard organizational incident report template.",
    (8, 4, 2): "To provide an accurate, legal, and continuous record of client health, wellbeing, support delivered, and progress toward goals.",
    (8, 4, 3): "Written in clear, objective, professional language at the end of each shift in the secure client management database.",
    
    # Table 9: Roles in individualised support
    (9, 3, 2): "Direct own life, articulate preferences, and participate actively in planning.",
    (9, 3, 3): "Express personal goals and collaborate with support workers on daily routines.",
    (9, 3, 4): "Inform workers of changes in feelings, health status, or service satisfaction.",
    (9, 4, 2): "Provide essential historical context, emotional advocacy, and informal care.",
    (9, 4, 3): "Collaborate with care team while respecting the client's independence and choices.",
    (9, 4, 4): "Liaise with providers regarding support plan adjustments and respite needs.",
    (9, 5, 2): "Conduct specialized clinical assessments (physiotherapy, occupational therapy, nursing).",
    (9, 5, 3): "Develop clinical directives, medication regimes, and specialized care plans.",
    (9, 5, 4): "Train and supervise care staff on clinical protocols and equipment use.",
    (9, 6, 2): "Deliver day-to-day person-centred support aligned strictly with the care plan.",
    (9, 6, 3): "Encourage client autonomy, dignity of risk, and skills maintenance.",
    (9, 6, 4): "Monitor, document, and report changes in client health, risks, or wellbeing.",
    (9, 7, 2): "Oversee service coordination, staff allocation, and compliance with standards.",
    (9, 7, 3): "Provide clinical guidance, performance support, and debriefing to workers.",
    (9, 7, 4): "Manage complex client escalations, service agreements, and stakeholder reviews.",
    
    # Table 10: Communication channels
    (10, 2, 0, 0): "Daily activity options, care steps being performed, and seeking consent.",
    (10, 2, 0, 1): "Changes to shift schedules, worker arrivals, or service arrangements.",
    (10, 2, 0, 2): "Encouraging feedback regarding comfort, dignity, and satisfaction with care.",
    (10, 3, 0, 0): "General updates on the client's wellbeing and daily achievements (with client consent).",
    (10, 3, 0, 1): "Notification of scheduled appointments, community outings, or care reviews.",
    (10, 3, 0, 2): "Immediate reporting of any incidents, accidents, or acute health changes.",
    (10, 4, 0, 0): "Personal preferences, dietary choices, and changes in daily routines.",
    (10, 4, 0, 1): "Feedback, compliments, or complaints about service delivery.",
    (10, 4, 0, 2): "Emerging health concerns, pain levels, or emotional distress.",
    (10, 5, 0, 0): "Updated client care plans, risk assessments, and shift instructions.",
    (10, 5, 0, 1): "Policy updates, safety alerts, and organizational compliance procedures.",
    (10, 5, 0, 2): "Constructive performance feedback, training opportunities, and shift debriefs.",
    (10, 6, 0, 0): "Progress notes, goal achievements, and observed behavioral/health changes.",
    (10, 6, 0, 1): "Safety hazards, near misses, incidents, or equipment malfunctions.",
    (10, 6, 0, 2): "Client disclosures, conflicts of interest, or requests for plan variations.",
    (10, 7, 0, 0): "Regular multi-disciplinary team case conferences and care planning meetings.",
    (10, 7, 0, 1): "Secure digital client health records, shift handover logs, and communication books.",
    (10, 7, 0, 2): "Direct phone calls, encrypted emails, and formal progress reviews.",
    
    # Table 11: Service delivery models
    (11, 3, 2): "Residential aged care / supported accommodation: 24/7 onsite lodging, personal care, meals, nursing, and clinical management.",
    (11, 4, 2): "Home care packages / in-home support: Tailored domestic, personal care, nursing, and transport services delivered in the person's own private home.",
    (11, 5, 2): "Community access / day respite: Center-based or community-based social, recreational, and skill-building programs promoting community integration.",
    
    # Table 13: Context of direct support work
    (13, 0, 2): "Aged Care and Disability Support",
    (13, 1, 1): "New South Wales",
    (13, 1, 2): "Support Worker",
    
    # Table 14: Dignity of risk & Human rights (NSW)
    (14, 1, 1): "Aged Care Act 1997 / Quality of Care Principles 2014 / Charter of Aged Care Rights",
    (14, 1, 2): "Schedule 1, Charter of Aged Care Rights (Consumer Rights)",
    (14, 1, 3): "Providers must respect consumer autonomy, support individual choices, and uphold dignity of risk while balancing safety obligations.",
    (14, 1, 4): "Support workers must facilitate informed choices, respect lifestyle decisions, and never impose unnecessary restrictions.",
    (14, 2, 1): "UN Convention on the Rights of Persons with Disabilities (UNCRPD) / Disability Inclusion Act 2014 (NSW)",
    (14, 2, 2): "Section 4, Disability Inclusion Act 2014 (NSW) General Principles",
    (14, 2, 3): "Promotes full inclusion, accessibility, and equality of opportunity for persons with disability across NSW.",
    (14, 2, 4): "Workers must promote inclusion, empower self-advocacy, and treat clients with unconditional dignity and equality.",
    (14, 3, 1): "Disability Discrimination Act 1992 (Cth) / Anti-Discrimination Act 1977 (NSW)",
    (14, 3, 2): "Part 2, Disability Discrimination Act 1992",
    (14, 3, 3): "Prohibits unlawful direct or indirect discrimination in employment, education, and access to premises and services.",
    (14, 3, 4): "Workers must ensure non-discriminatory service delivery and advocate for reasonable adjustments.",
    (14, 4, 1): "NDIS (Quality and Safeguards Commission) Rules 2018",
    (14, 4, 2): "NDIS Code of Conduct Rules 2018",
    (14, 4, 3): "Mandates registered providers and workers uphold rights to freedom of expression, self-determination, and decision-making.",
    (14, 4, 4): "Workers must adhere to ethical codes, avoid conflicts of interest, and deliver high-quality, person-centred support.",
    
    # Table 15: Duty of care & Mandatory reporting (NSW)
    (15, 1, 1): "Civil Liability Act 2002 (NSW) / Common Law Duty of Care",
    (15, 1, 2): "Part 1A, Civil Liability Act 2002 (NSW) Negligence",
    (15, 1, 3): "Workers must take reasonable care to avoid foreseeable acts or omissions that could reasonably cause harm to clients.",
    (15, 1, 4): "Workers must maintain professional competence, balance safety with client choice, and adhere to care plans.",
    (15, 2, 1): "Ageing and Disability Commissioner Act 2019 (NSW)",
    (15, 2, 2): "Part 2, Section 13 Reports of abuse, neglect or exploitation",
    (15, 2, 3): "Establishes powers to investigate allegations of abuse, neglect, and exploitation of older adults and adults with disability.",
    (15, 2, 4): "Workers have a statutory and moral duty to detect, document, and report suspected elder or disability abuse immediately.",
    (15, 3, 1): "Children and Young Persons (Care and Protection) Act 1998 (NSW)",
    (15, 3, 2): "Section 27 Mandatory reporting of children at risk of significant harm",
    (15, 3, 3): "Mandatory reporters must report reasonable grounds to suspect that a child or young person is at risk of significant harm.",
    (15, 3, 4): "Workers must report child protection concerns to the Child Protection Helpline (DCJ NSW) without delay.",
    (15, 4, 1): "Aged Care Quality and Safety Commission Act 2018 / Serious Incident Response Scheme (SIRS)",
    (15, 4, 2): "Part 4B Serious Incident Response Scheme",
    (15, 4, 3): "Mandatory notification of priority incidents (abuse, serious injury, unlawful sexual contact) within prescribed timeframes.",
    (15, 4, 4): "Workers must ensure open disclosure, maintain victim support, and cooperate fully with investigations.",
    
    # Table 16: Privacy and confidentiality
    (16, 1, 1): "Privacy Act 1988 (Cth) / Australian Privacy Principles (APPs)",
    (16, 1, 2): "Schedule 1, Australian Privacy Principles (APPs 1 to 13)",
    (16, 1, 3): "Regulates the collection, storage, use, disclosure, and access to personal and sensitive client information.",
    (16, 1, 4): "Workers must maintain strict confidentiality, obtain consent before sharing, and store records securely.",
    (16, 2, 1): "Health Records and Information Privacy Act 2002 (NSW)",
    (16, 2, 2): "Schedule 1, Health Privacy Principles (HPPs 1 to 15)",
    (16, 2, 3): "Governs the handling of health information by public and private health and community service providers in NSW.",
    (16, 2, 4): "Workers must protect client health records, prevent unauthorized access, and ensure data integrity.",
    (16, 3, 1): "Government Information (Public Access) Act 2009 (NSW) - GIPA Act",
    (16, 3, 2): "Part 1, Public access principles and disclosure frameworks",
    (16, 3, 3): "Facilitates open, transparent access to government-held information while protecting personal privacy rights.",
    (16, 3, 4): "Workers must maintain accurate, objective documentation that can withstand scrutiny and lawful requests for access.",
    (16, 4, 1): "Fair Work Act 2009 (Cth) / Whistleblower Protection Provisions",
    (16, 4, 2): "Part 9.4AAA, Corporations Act 2001 (Whistleblower protection)",
    (16, 4, 3): "Protects workers who make qualifying disclosures regarding breaches of law, systemic abuse, or misconduct.",
    (16, 4, 4): "Workers must act with integrity, expose unlawful practices through protected channels, and protect whistleblowers from detriment.",
    
    # Table 17: Work health and safety (NSW)
    (17, 1, 1): "Work Health and Safety Act 2011 (NSW)",
    (17, 1, 2): "Part 2, Health and Safety Duties (Sections 19, 28)",
    (17, 1, 3): "Workers must take reasonable care for their own health and safety and ensure actions do not adversely affect others.",
    (17, 1, 4): "Workers must follow safety instructions, wear PPE, report hazards, and comply with organizational WHS policies.",
    (17, 2, 1): "Work Health and Safety Regulation 2017 (NSW)",
    (17, 2, 2): "Part 3.2 General workplace management and Part 4.2 Hazardous manual tasks",
    (17, 2, 3): "Mandates risk management controls for hazardous manual tasks, slips, trips, falls, and biological hazards.",
    (17, 2, 4): "Workers must use mechanical hoists, slide sheets, and ergonomic principles during manual handling.",
    (17, 3, 1): "Public Health Act 2010 (NSW)",
    (17, 3, 2): "Part 3 Prevention and control of disease",
    (17, 3, 3): "Requires prevention and control of infectious diseases and compliance with public health infection control protocols.",
    (17, 3, 4): "Workers must perform strict hand hygiene, use appropriate PPE, and adhere to standard and transmission-based precautions.",
    (17, 4, 1): "Workers Compensation Act 1987 (NSW) / Workplace Injury Management Act 1998 (NSW)",
    (17, 4, 2): "Part 3, Workers compensation and return to work obligations",
    (17, 4, 3): "Provides statutory compensation, medical care, and return-to-work rehabilitation for injured workers.",
    (17, 4, 4): "Workers must promptly report all workplace injuries and actively participate in injury management plans.",
    
    # Table 18: Discrimination and Human Rights
    (18, 1, 1): "Racial Discrimination Act 1975 (Cth)",
    (18, 1, 2): "Section 9, Prohibiting discrimination based on race, colour, descent or ethnic origin",
    (18, 1, 3): "Racial discrimination is unlawful across all public, community, and private service operations.",
    (18, 1, 4): "Workers must foster inclusive, culturally safe environments and eliminate racial bias.",
    (18, 2, 1): "Sex Discrimination Act 1984 (Cth)",
    (18, 2, 2): "Part 2, Prohibiting discrimination based on sex, gender identity, intersex status, or relationship status",
    (18, 2, 3): "Guarantees equality of opportunity and protection against sexual harassment and gender-based discrimination.",
    (18, 2, 4): "Workers must provide respectful support to all gender identities and adhere strictly to zero-tolerance harassment policies.",
    (18, 3, 1): "Age Discrimination Act 2004 (Cth)",
    (18, 3, 2): "Part 4, Prohibiting discrimination on the grounds of age in employment and service delivery",
    (18, 3, 3): "Protects individuals from being treated less favourably due to their chronological age.",
    (18, 3, 4): "Workers must counter ageism, treat older people as valued individuals, and promote independent decision-making.",
    (18, 4, 1): "Australian Human Rights Commission Act 1986 (Cth)",
    (18, 4, 2): "Part 2, Australian Human Rights Commission functions and powers",
    (18, 4, 3): "Empowers the Commission to investigate human rights breaches and educate the public.",
    (18, 4, 4): "Workers must champion fundamental human rights and support clients to lodge human rights complaints if infringed.",
    
    # Table 19: Work role boundaries, responsibilities, limitations
    (19, 3, 0): "1. Professional relationship boundaries (maintaining professional detachment; no financial or romantic entanglements).",
    (19, 4, 0): "2. Clinical scope of practice boundaries (performing only delegated, non-clinical tasks; no invasive medical procedures).",
    (19, 5, 0): "3. Working hours and communication boundaries (no private contact or unscheduled service provision outside work hours).",
    (19, 7, 0): "1. Providing person-centred assistance with daily living, mobility, and personal care as outlined in the support plan.",
    (19, 8, 0): "2. Monitoring client safety, documenting progress notes, and reporting any health changes or hazards to the supervisor.",
    (19, 9, 0): "3. Facilitating community engagement, social participation, and respecting client choices and dignity of risk.",
    (19, 11, 0): "1. Not qualified or authorized to alter medication dosages, diagnose conditions, or prescribe medical treatments.",
    (19, 12, 0): "2. Cannot provide legal, financial, or formal psychological counseling advice to clients or family members.",
    (19, 13, 0): "3. Cannot perform specialized nursing or complex manual handling maneuvers without explicit clinical training and delegation.",
    
    # Table 20: Restrictive practices
    (20, 2, 0): "Restrictive practices are any intervention or action that has the effect of restricting the free movement or liberty of a person with disability or an older person.",
    (20, 3, 0, 0): "1. Chemical restraint: Use of medication for the primary purpose of controlling or subduing behaviour.",
    (20, 3, 0, 1): "2. Mechanical restraint: Use of devices or equipment to prevent, restrict, or subdue bodily movement.",
    (20, 3, 0, 2): "3. Physical restraint: Use of physical force to prevent, restrict, or subdue movement of the person's body.",
    (20, 3, 0, 3): "4. Environmental restraint: Restricting free access to all parts of the person's environment or community.",
    (20, 3, 0, 4): "5. Seclusion: Sole confinement of a person in a room or physical space at any hour from which free exit is denied.",
    (20, 4, 0, 0): "National Disability Insurance Scheme (Restrictive Practices and Behaviour Support) Rules 2018",
    (20, 4, 0, 1): "Aged Care Act 1997 / Quality of Care Principles 2014 (Part 4A)",
    (20, 4, 0, 2): "National Framework for Reducing and Eliminating the Use of Restrictive Practices in the Disability Service Sector",
    (20, 5, 0, 0): "1. Used strictly as a last resort after exhausting positive behaviour support alternatives.",
    (20, 5, 0, 1): "2. Must be the least restrictive option available and used for the shortest possible duration.",
    (20, 5, 0, 2): "3. Authorized by a registered behaviour support practitioner and included in a current Behaviour Support Plan.",
    (20, 5, 0, 3): "4. Informed consent obtained from the client or authorized substitute decision-maker (where applicable).",
    (20, 5, 0, 4): "5. Subject to continuous monitoring, strict clinical review, and mandatory reporting.",
    
    # Table 21: National Framework principles
    (21, 0, 0): "1. Person-centred focus. 2. Human rights approach. 3. Proactive positive behaviour support. 4. Elimination as ultimate goal. 5. Evidence-based interventions. 6. Transparency and accountability.",
    (21, 1, 0): "Where an NDIS participant’s behaviours of concern place them or others at risk of harm, a comprehensive Behaviour Support Plan must be developed by a registered practitioner to address the root causes of the behaviour.",
    (21, 2, 0): "1. Regular data logging of usage. 2. Ongoing review of efficacy. 3. Planned strategies for gradual reduction and fading.",
    (21, 3, 0): "Restrictive practices infringe on fundamental human rights to liberty and bodily integrity; ethically, they can only be justified in extreme emergencies to prevent imminent severe harm, with intense oversight.",
    (21, 4, 0): "Registered providers must document every instance of restrictive practice use, maintain detailed evidence of authorization, and submit monthly reporting to the NDIS Quality and Safeguards Commission.",
    (21, 5, 0): "1. Immediate risk assessment demonstrating imminent harm. 2. Authorisation by state authority and inclusion in an approved plan.",
    
    # Table 22: 5 factors affecting clients
    (22, 2, 0): "1. Physical decline, chronic illness, and loss of functional mobility.",
    (22, 3, 0): "2. Cognitive impairment, memory loss, dementia, or sensory loss (vision/hearing).",
    (22, 4, 0): "3. Social isolation, grief, loneliness, and loss of community connections.",
    (22, 5, 0): "4. Mental health conditions such as major depression, anxiety, or trauma.",
    (22, 6, 0): "5. Financial disadvantage, lack of suitable housing, or limited transport options.",
    
    # Table 23: Medication assistance procedures
    (23, 2, 0): "The right medicine must be administered to the [right person], in the [right dose], via the [right route], at the [right time].",
    (23, 3, 0): "1. Checking full legal name and date of birth against care plan. 2. Checking recent photograph. 3. Asking the person to state their full name.",
    (23, 4, 0): "In the client's current Medication Administration Record (MAR) chart and the pharmacist-labelled Dose Administration Aid (DAA).",
    
    # Table 24: Consequences of wrong route & refusal
    (24, 0, 0): "1. Rapid toxicity, adverse physiological shock, or organ failure.",
    (24, 0, 1): "2. Failure to absorb the therapeutic dose, resulting in unmanaged symptoms or deterioration.",
    (24, 0, 2): "3. Local tissue damage, chemical burning, or aspiration into the lungs.",
    (24, 1, 0): "The right to refuse means a competent person has the absolute legal and ethical right to decline any medication or treatment at any time, even if it is against medical advice.",
    (24, 2, 0): "1. Informed (person understands consequences). 2. Voluntary (no coercion). 3. Communicated clearly (verbally or non-verbally).",
    (24, 3, 0): "1. Pause and calmly explain the purpose and benefit of the medication without coercion.",
    (24, 3, 1): "2. Offer the medication again after a short interval (e.g. 15-20 minutes).",
    (24, 3, 2): "3. If still refused, respect the refusal, document on MAR chart, and notify the supervisor/registered nurse immediately.",
    (24, 4, 0): "It empowers the person to make informed choices about their own health, enhances medication adherence, and respects their dignity.",
    
    # Table 25: Right to education & DAA checks
    (25, 0, 0): "1. Provide plain-language information leaflets about the prescribed medications.",
    (25, 0, 1): "2. Facilitate consultations with the dispensing pharmacist or GP to answer questions.",
    (25, 0, 2): "3. Explain what each medication does and potential common side effects prior to assisting.",
    (25, 1, 0): "When inspecting the client's pre-packaged medication, verify that the [packaging is intact and undamaged], and the [blister seals are completely unbroken].",
    (25, 2, 0): "Do not administer the medication; quarantine it immediately, document the issue, notify the supervisor, and contact the dispensing pharmacy for an urgent replacement.",
    (25, 3, 0): "1. Poisons Information Centre (13 11 26). 2. Dispensing Community Pharmacist. 3. Healthdirect Australia (1800 022 222). 4. Triple Zero (000) emergency services.",
    
    # Table 26: Adverse reaction reporting
    (26, 0, 0): "1. Exact date, time, and specific medication administered.",
    (26, 0, 1): "2. Precise physical symptoms and clinical signs observed (rash, breathing difficulty, swelling).",
    (26, 0, 2): "3. Immediate first aid actions taken and emergency medical services contacted.",
    (26, 0, 3): "4. Names of witnesses and staff present.",
    (26, 0, 4): "5. Supervisor notification details and advice received.",
    (26, 1, 0): "1. Cease administration immediately and do not force the client.",
    (26, 1, 1): "2. Ensure the client is comfortable and safe in an upright position.",
    (26, 1, 2): "3. Document the attempted administration and exact reason on the MAR chart.",
    (26, 1, 3): "4. Promptly escalate to the workplace supervisor or registered nurse for medical review.",
    (26, 2, 0): "1. Exact date, time, and medication name/dose refused.",
    (26, 2, 1): "2. Reason given by the client (or non-verbal refusal cues).",
    (26, 2, 2): "3. Actions taken (information provided, alternative timing offered) and supervisor notified.",
    
    # Table 27: Skill development practices
    (27, 2, 0): "1. Task analysis: Breaking down complex daily routines (e.g. making breakfast) into step-by-step components.",
    (27, 3, 0): "2. Prompting and fading: Using verbal prompts, demonstrations, and fading assistance as independence increases.",
    (27, 4, 0): "3. Positive reinforcement: Providing specific praise and encouraging feedback upon successful completion of steps.",
    
    # Table 28: Skills maintenance practices
    (28, 3, 2): "Encouraging regular daily practice of mobility exercises and personal grooming routines to prevent muscle atrophy and preserve existing motor skills.",
    (28, 4, 2): "Facilitating continuous use of assistive technologies (e.g. communication devices, adaptive cutlery) to sustain independence in daily living.",
    (28, 5, 2): "Supporting ongoing participation in familiar social and domestic activities to maintain cognitive engagement and routine memory.",
    
    # Table 29: Unmet needs & behavioural responses
    (29, 2, 0): "Expressing frustration, agitation, restlessness, or verbal aggression when unable to communicate pain or discomfort.",
    (29, 3, 0): "Withdrawing socially, refusing meals, or exhibiting lethargy when experiencing loneliness or lack of mental stimulation.",
    (29, 4, 0): "Identify the underlying trigger (check for pain, hunger, fatigue, toileting needs, or environmental noise) and adapt support accordingly.",
    
    # Tables 30-33: Assistive technologies
    (30, 2, 0): "Mobility: Enables safe, independent movement within the home and community, reducing fall risks and fatigue.",
    (30, 2, 1): "Wheelchair / 4-wheel walker with handbrakes",
    (30, 3, 0): "Communication: Enables non-verbal individuals or those with dysarthria to express desires, choices, and pain.",
    (30, 3, 1): "High-tech AAC speech-generating tablet device / Communication board",
    (30, 4, 0): "Self-care and personal hygiene: Fosters dignity and autonomy during bathing, dressing, and grooming.",
    (30, 4, 1): "Shower chair with armrests / Long-handled sponge / Adaptive button hook",
    (30, 5, 0): "Meal preparation and dining: Facilitates independent eating and drinking despite tremors or reduced grip.",
    (30, 5, 1): "Weighted adaptive cutlery / Non-spill suction bowls / Two-handled mug",
    (30, 6, 0): "Domestic life: Assists with home cleaning, laundry, and daily household maintenance.",
    (30, 6, 1): "Robot vacuum cleaner / Lever-style tap turners",
    (30, 7, 0): "Recreation and leisure: Allows participation in hobbies, reading, and digital entertainment.",
    (30, 7, 1): "Audiobook reader / Adaptive gaming controller / Large-print playing cards",
    (30, 8, 0): "Cognition and memory: Provides automated reminders for medication, appointments, and safety orientation.",
    (30, 8, 1): "Talking digital day clock / Automated pill dispenser with alarms",
    (33, 2, 0): "Assistive technologies compensate for physical, cognitive, or sensory impairments, empowering the client to perform life activities independently without constant reliance on care staff.",
    (33, 3, 0): "1. Client physical and cognitive capability to operate device safely. 2. Ergonomic suitability, fit, and home environment space. 3. Maintenance, battery charging, and cleaning protocols. 4. Training requirements for client and support workers. 5. Cost, funding approval, and ongoing replacement warranty.",
    
    # Tables 34-35: Risk management
    (34, 2, 0): "1. The person's human right to make decisions and experience dignity of risk.",
    (34, 3, 0): "2. The likelihood and potential severity of foreseeable harm to the client or others.",
    (34, 4, 0): "3. Organizational WHS policies, statutory duties of care, and legal liabilities.",
    (34, 5, 0): "4. Environmental hazards within the client's home or facility setting.",
    (34, 6, 0): "5. Available risk mitigation strategies that preserve the client's choice while minimizing danger.",
    (35, 2, 1): "Install non-slip flooring mats, remove clutter/loose rugs, ensure adequate lighting, and encourage use of prescribed mobility aids.",
    (35, 3, 1): "Follow strict speech pathology dysphagia guidelines, provide prescribed texture-modified diets/fluids, and ensure upright posture during meals.",
    (35, 4, 1): "Store medications in a locked cabinet, adhere strictly to 6 rights of administration, and cross-check MAR charts.",
    (35, 5, 1): "Implement proactive positive behaviour support strategies, identify early agitation triggers, and maintain calm sensory environments."
}

# ==============================================================================
# CHCCCS031 Part B Overrides (Simulated Assessment Tasks)
# ==============================================================================
CHCCCS031_PARTB_OVERRIDES = {
    # Abraham Case Study Review / Meeting (Tables 29-33)
    (29, 1, 0): "15/09/2026 10:30 AM",
    (30, 1, 0): "Abraham C",
    (30, 1, 1): "Unit 4, 12 CareConnect Way, Sydney NSW 2000",
    (31, 1, 0): "Alex Chen",
    (31, 1, 1): "Support Worker",
    (32, 1, 0): "Abraham expressed satisfaction with his new hearing aid and mobility equipment. He noted improved confidence during morning walks.",
    (32, 1, 1): "Abraham requested continued assistance with breakfast preparation and asked for community social outing options on weekends.",
    (32, 1, 2): "Support plan is effective; recommended introducing a weekly senior community bridge club visit to enhance social connection.",
    (33, 1, 0): "Alex Chen",
    (33, 1, 1): "Support Worker",
    (33, 1, 2): "Alex Chen",
    (33, 1, 3): "15/09/2026",
    
    # Henry Case Study Review / Meeting (Tables 59-63)
    (59, 1, 0): "15/09/2026 02:00 PM",
    (60, 1, 0): "Henry S",
    (60, 1, 1): "Apartment 18, 45 Horizon Street, Sydney NSW 2000",
    (61, 1, 0): "Alex Chen",
    (61, 1, 1): "Support Worker",
    (62, 1, 0): "Henry and Florence reported that the colostomy care routine is operating smoothly and skin around the stoma remains healthy and intact.",
    (62, 1, 1): "Henry expressed fatigue in the late afternoons; requested adjustments to afternoon walking schedule to allow a 1-hour rest period.",
    (62, 1, 2): "Care plan adjusted to accommodate afternoon rest. Florence confirmed feeling well-supported with respite arrangements.",
    (63, 1, 0): "Alex Chen",
    (63, 1, 1): "Support Worker",
    (63, 1, 2): "Alex Chen",
    (63, 1, 3): "15/09/2026",
    
    # Personal Care & Mobility Demonstrations (Tables 69-74)
    (69, 1, 0): "1. Review client care plan and verify preferences for bathing.",
    (69, 2, 0): "2. Wash hands and gather clean linens, warm water basin, soap, washcloths, and towels.",
    (69, 3, 0): "3. Explain procedure, seek client consent, and ensure door/curtains are closed for privacy.",
    (69, 4, 0): "4. Check water temperature using the inside of the wrist or thermometer (38-40°C).",
    (69, 5, 0): "5. Don disposable apron and gloves, and adjust bed to safe working ergonomic height.",
    
    (70, 1, 0): "1. Cover client with a bath blanket and expose only the body section currently being washed.",
    (70, 2, 0): "2. Wash face with water only (no soap around eyes), wiping from inner canthus outwards.",
    (70, 3, 0): "3. Wash, rinse, and gently pat dry upper limbs, trunk, abdomen, and lower limbs in sequence.",
    (70, 4, 0): "4. Assist client to turn onto side to wash and dry back, inspecting pressure areas for redness.",
    (70, 5, 0): "5. Perform perineal hygiene from front to back, apply moisturizer, dress in clean clothes, and dispose of soiled water safely.",
    
    (71, 1, 0): "1. Confirm client consent, preferences for wet shaving with safety razor, and ensure comfortable upright positioning.",
    (71, 2, 0): "2. Apply a warm, moist towel to face for 2-3 minutes to soften facial hair follicles.",
    (71, 3, 0): "3. Apply shaving foam or cream evenly across jawline, cheeks, and neck.",
    (71, 4, 0): "4. Hold skin taut and shave in the direction of hair growth using short, gentle strokes, rinsing razor frequently.",
    (71, 5, 0): "5. Rinse face thoroughly with warm water, pat dry with soft towel, and apply soothing non-alcohol post-shave balm.",
    
    (72, 1, 0): "1. Position wheelchair adjacent to the vehicle passenger door at a 45-degree angle.",
    (72, 2, 0): "2. Lock wheelchair wheel brakes securely and fold away or remove both footrests.",
    (72, 3, 0): "3. Open passenger door fully, adjust vehicle seat as far back as possible, and recline slightly.",
    (72, 4, 0): "4. Assist client to stand using transfer belt or steadying technique, ensuring non-slip footwear.",
    (72, 5, 0): "5. Pivot client carefully so their back faces the car seat, and guide them to sit down gently.",
    
    (73, 1, 0): "1. Park on level ground, open car door fully, and position wheelchair beside the car with brakes locked.",
    (73, 2, 0): "2. Assist client to swivel their legs out of the vehicle so both feet are flat and stable on the ground.",
    (73, 3, 0): "3. Move car seat forward slightly if needed to assist client with forward leaning weight transfer.",
    (73, 4, 0): "4. On count of three, assist client to stand upright while steadying balance.",
    (73, 5, 0): "5. Pivot client toward wheelchair, guide them to sit back securely, and replace footrests.",
    
    (74, 1, 0): "1. Immediately assess fallen client for consciousness, breathing, visible injury, pain, or bleeding; do not move client if fracture or spinal injury is suspected.",
    (74, 2, 0): "2. If no injury, reassure client, keep them calm and warm, and call for a registered nurse or second worker to assist.",
    (74, 3, 0): "3. Bring a sturdy chair or mechanical mobile floor hoist with appropriate sling to the client's side.",
    (74, 4, 0): "4. Assist client to roll onto side, onto hands and knees, and rest arms on the chair seat before stepping up, or use hoist according to care plan.",
    (74, 5, 0): "5. Take baseline vital signs, document fall incident in full on organizational Incident Report Form, and notify supervisor and family."
}

# ==============================================================================
# CHCCCS038 Overrides (Empowerment of people receiving support)
# ==============================================================================
CHCCCS038_OVERRIDES = {
    # Table 3: History & recent developments in disability and ageing
    (3, 3, 2): "Disability Services Act 1986: Shifted funding from institutional segregation toward community-based integration and individual rights.",
    (3, 4, 2): "Disability Discrimination Act 1992: Made discrimination unlawful in employment, education, transport, and public accommodation across Australia.",
    (3, 5, 2): "Aged Care Act 1997: Established national framework, user rights, funding principles, and quality standards for residential and home aged care.",
    (3, 6, 2): "National Disability Strategy 2010-2020: Ten-year national policy framework driving systemic inclusion and barrier removal across government sectors.",
    (3, 7, 2): "National Disability Insurance Scheme Act 2013: Created the NDIS, shifting funding control directly into participants' hands via individualised budgets.",
    (3, 8, 2): "Royal Commission into Aged Care Quality and Safety (2018-2021): Highlighted rights-based care, leading to comprehensive sector-wide quality reforms.",
    
    # Table 4: Differentiating concepts
    (4, 2, 0): "Enablement is a collaborative approach that assists individuals to do things for themselves to maintain autonomy, while reablement focuses on intensive, time-limited interventions to regain lost physical and social skills following an acute illness or injury.",
    (4, 2, 1): "Enablement promotes ongoing self-care and decision-making, whereas reablement targets specific functional rehabilitation goals over a set period.",
    (4, 3, 0): "An institutional model enforces uniform schedules, medical routines, and provider dominance, treating individuals as passive care recipients.",
    (4, 3, 1): "A person-centred, self-directed model places the individual at the center, empowering them to direct their own lifestyle, care routines, and funding.",
    
    # Table 5: Barriers to empowerment
    (5, 3, 2): "Individual barrier: Low self-confidence or internalized defeatism resulting from prolonged dependency on care providers.",
    (5, 3, 3): "Strategy: Utilize positive reinforcement and incremental skill-building to celebrate small achievements and foster self-efficacy.",
    (5, 4, 2): "Emotional barrier: Fear of failure, anxiety, or vulnerability when attempting new tasks independently.",
    (5, 4, 3): "Strategy: Provide empathetic active listening, reassurance, and a supportive safety net without judgment.",
    (5, 5, 2): "Physical environmental barrier: Lack of wheelchair ramps, narrow doorways, or inaccessible bathroom facilities.",
    (5, 5, 3): "Strategy: Advocate for home modifications, install grab rails, and remove environmental obstacles.",
    (5, 6, 2): "Social environmental barrier: Negative public stereotypes, ageism, or patronizing societal attitudes.",
    (5, 6, 3): "Strategy: Educate community members, promote positive representation, and facilitate inclusive community participation.",
    (5, 7, 2): "Communication barrier: Complex jargon, fine print documents, or lack of assistive communication aids.",
    (5, 7, 3): "Strategy: Provide materials in Easy Read formats, visual communication charts, and utilize accredited interpreters.",
    
    # Tables 6-7: Structural and systemic power
    (6, 2, 0): "Structural power refers to the formal institutional hierarchies, legal frameworks, and organizational rules that dictate how resources, privileges, and authority are distributed across a system.",
    (6, 3, 0): "Systemic power is the pervasive, entrenched set of cultural norms, policies, and societal practices that systematically advantage certain dominant social groups while marginalizing others.",
    (6, 4, 0, 0): "1. Legislative and regulatory policies established by government.",
    (6, 4, 0, 1): "2. Economic resource allocation and funding distribution models.",
    (6, 4, 0, 2): "3. Institutional leadership structures and professional hierarchies.",
    (6, 4, 0, 3): "4. Societal culture, historical traditions, and prevailing media narratives.",
    (6, 5, 0, 0): "1. Service access and funding eligibility determinations.",
    (6, 5, 0, 1): "2. Personal decision-making capacity and legal guardianship arrangements.",
    (6, 5, 0, 2): "3. Daily routine scheduling and freedom of movement within facilities.",
    (7, 3, 2): "Health and community services: Rigid provider schedules can override individual preferences, dictating when clients wake, eat, and shower.",
    (7, 4, 2): "Education and employment: Systemic entry barriers and inflexible workplaces exclude people with disability from career progression.",
    (7, 5, 2): "Housing and accommodation: Lack of accessible social housing forces individuals into restrictive group homes or residential care.",
    (7, 6, 2): "Legal and justice systems: Complex legal language and lack of communication supports deny marginalized individuals equal standing.",
    (7, 7, 2): "Financial services: Strict banking criteria and risk models restrict independent management of personal finances.",
    (7, 8, 2): "Public transport and infrastructure: Inaccessible buses, trains, and urban footpaths severely restrict independent mobility.",
    (7, 9, 2): "Social and civic participation: Physical and attitudinal barriers exclude individuals from voting, volunteering, and community governance.",
    
    # Table 8: Social constructs of ageing and disability
    (8, 2, 0): "Older people often construct ageing as a natural life stage characterized by wisdom, continued personal growth, resilience, and valuable life experience, while seeking continued dignity and autonomy.",
    (8, 3, 0): "Younger people often view ageing through an ageist deficit lens, associating it primarily with physical decay, cognitive decline, burden, and technological irrelevance.",
    (8, 4, 0): "The medical model views disability as an individual physical or psychological pathology or defect that resides within the person and must be cured or medically managed by experts.",
    (8, 5, 0): "The social model views disability as the result of physical, systemic, and attitudinal barriers created by society, which disadvantage and exclude people with impairments.",
    
    # Table 9: Working with people with disabilities
    (9, 0, 0): "I feel passionate and deeply committed to working collaboratively with people with disabilities, viewing them as equal rights-holders who possess distinct strengths, goals, and rights to full self-determination.",
    (9, 1, 0, 0): "1. Positive attitude: Believing every individual has inherent worth and capacity for lifelong learning and growth.",
    (9, 1, 0, 1): "Impact: Encourages proactive support that promotes independence, active support, and dignity of risk.",
    (9, 1, 0, 2): "2. Unconscious paternalism: Feeling an instinct to protect or do things for the person to save time or avoid struggle.",
    (9, 1, 0, 3): "Impact: Risks disempowering the client; must be actively managed by stepping back and providing graded guidance.",
    
    # Table 10: Experienced and qualified staff
    (10, 2, 0): "An experienced staff member possesses extensive practical on-the-job history, seasoned situational judgment, and deep practical problem-solving skills developed over years of client support.",
    (10, 3, 0): "A qualified staff member holds recognized formal tertiary or vocational credentials (e.g. Registered Nurse, Occupational Therapist, Behaviour Support Practitioner) granting clinical and legal authority.",
    (10, 4, 0, 0): "1. Identify and clarify the specific issue, boundary limitation, or emerging challenge encountered.",
    (10, 4, 0, 1): "2. Check relevant client care plans, organizational procedures, and emergency guidelines.",
    (10, 4, 0, 2): "3. Approach the qualified colleague in a timely, professional manner and explain the situation clearly.",
    (10, 4, 0, 3): "4. Receive clinical directives or mentoring instructions and apply them carefully to support the client.",
    (10, 4, 0, 4): "5. Document the discussion, outcome, and actions taken in the client management record.",
    (10, 5, 0, 0): "1. When a client exhibits acute physical deterioration, unmanaged pain, or signs of a serious medical emergency.",
    (10, 5, 0, 1): "2. When encountering complex behaviours of concern or suspected abuse that exceed the worker's training and scope of practice.",
    
    # Table 11: Support practices for conditions
    (11, 3, 2, 0): "Sensory disability (Vision loss): Verbally describe surroundings, announce entrances/exits, and ensure hallways are well-lit and clear of obstacles.",
    (11, 3, 2, 1): "Sensory disability (Hearing loss): Maintain clear face-to-face eye contact, speak clearly without shouting, and utilize hearing loop systems or visual communication aids.",
    (11, 4, 2, 0): "Intellectual disability: Break instructions down into simple, concrete steps, use visual prompt cards, and allow ample time for responses.",
    (11, 4, 2, 1): "Intellectual disability: Implement active support techniques to engage the person in everyday tasks using consistent routines and positive reinforcement.",
    (11, 5, 2, 0): "Physical disability (Mobility impairment): Ensure ergonomic physical access, position transfer equipment correctly, and support client to use adaptive cutlery/aids.",
    (11, 5, 2, 1): "Physical disability (Cerebral palsy): Encourage comfortable positioning, allow extra time for speech, and collaborate with speech/physiotherapy directives.",
    (11, 6, 2, 0): "Acquired brain injury: Maintain a predictable, calm daily schedule, use written checklist organizers, and avoid over-stimulating environments.",
    (11, 6, 2, 1): "Acquired brain injury: Use gentle verbal cues for redirection and support memory through digital calendar reminders.",
    (11, 7, 2, 0): "Mental health condition (Depression): Provide empathetic, non-judgmental active listening and support engagement in small, meaningful social activities.",
    (11, 7, 2, 1): "Mental health condition (Anxiety): Implement grounding and relaxation strategies, validate feelings, and maintain a quiet, predictable atmosphere.",
    (11, 8, 2, 0): "Dementia (Cognitive decline): Use reminiscence therapy, validate emotional reality rather than arguing, and provide clear environmental signage.",
    (11, 8, 2, 1): "Dementia (Wandering risk): Facilitate purposeful movement within secure, pleasant garden spaces and maintain familiar comforting objects.",
    (11, 9, 2, 0): "Autism spectrum condition: Respect sensory sensitivities (lighting, noise), provide clear advance notice of routine changes, and use structured visual timetables.",
    (11, 9, 2, 1): "Autism spectrum condition: Support special interests and accommodate preferred communication styles without forcing direct eye contact.",
    
    # Tables 12-17: Principles of support & human rights
    (12, 2, 0): "Empowerment is the process of enabling individuals to gain greater control, choice, and influence over decisions, actions, and services that affect their lives.",
    (12, 3, 0, 0): "1. Self-determination: Recognizing the individual as the rightful director of their own choices and goals.",
    (12, 3, 0, 1): "2. Capacity building: Equipping the person with information, skills, and tools to advocate for themselves.",
    (12, 3, 0, 2): "3. Participation: Ensuring active inclusion in planning, community life, and policy feedback.",
    (12, 3, 0, 3): "4. Equality and dignity: Treating the person with respect, removing attitudinal barriers, and upholding dignity of risk.",
    (12, 4, 0): "A rights-based approach integrates international human rights principles into everyday service delivery, viewing clients as entitlement holders rather than objects of charity.",
    (13, 0, 0, 0): "1. Participation: Everyone has the right to participate in decisions that affect their lives.",
    (13, 0, 0, 1): "2. Accountability: Providers and governments must be answerable for the realization of rights.",
    (13, 0, 0, 2): "3. Non-discrimination: Equal treatment without distinction based on disability, age, or background.",
    (13, 0, 0, 3): "4. Empowerment: People must be supported to claim their rights independently.",
    (13, 0, 0, 4): "5. Legality: Care practices must comply with statutory human rights frameworks.",
    (13, 1, 0, 0): "1. Right to equality before the law and non-discrimination.",
    (13, 1, 0, 1): "2. Right to personal liberty, security, and freedom from torture or degrading treatment.",
    (13, 1, 0, 2): "3. Right to live independently and be included in the community.",
    (13, 2, 0, 0): "1. Right to protection from all forms of physical or mental violence, injury, or neglect.",
    (13, 2, 0, 1): "2. Right to participate and have their views given due weight in all matters affecting them.",
    (13, 3, 0, 0): "1. Safe and high-quality care and services.",
    (13, 3, 0, 1): "2. Be treated with dignity and respect.",
    (13, 3, 0, 2): "3. Have my identity, culture and diversity valued and supported.",
    (13, 3, 0, 3): "4. Live without abuse and neglect.",
    (13, 3, 0, 4): "5. Exercise choice and make decisions about my care, including personal relationships and financial affairs.",
    (14, 0, 0): "Person-centred practice is an approach where the individual leads the planning and delivery of their own support, ensuring their goals, preferences, and rights direct every aspect of care.",
    (14, 1, 0, 0): "1. Knowing the person deeply (biography, values, relationships).",
    (14, 1, 0, 1): "2. Fostering genuine partnership and collaboration.",
    (14, 1, 0, 2): "3. Respecting autonomy and dignity of risk.",
    (14, 1, 0, 3): "4. Recognizing and utilizing existing strengths and capabilities.",
    (14, 1, 0, 4): "5. Continuous communication, responsiveness, and flexibility.",
    (14, 2, 0, 0): "1. Ensuring that the individual's informed consent is sought and respected.",
    (14, 2, 0, 1): "2. Maintaining confidentiality and upholding privacy rights throughout all interactions.",
    (14, 3, 0): "Self-advocacy is the ability of an individual to effectively speak up, negotiate, and assert their own rights, choices, and interests without relying on an intermediary.",
    (14, 4, 0, 0): "1. Facilitating participation in independent self-advocacy peer groups and workshops.",
    (14, 4, 0, 1): "2. Providing accessible information and coaching clients to express their preferences at care planning meetings.",
    (15, 0, 0, 0): "1. Every moment has potential: Turning ordinary daily routines into opportunities for learning and engagement.",
    (15, 0, 0, 1): "2. Little and often: Breaking tasks down so the person participates frequently across the day.",
    (15, 0, 0, 2): "3. Graded assistance: Providing precisely the right level of prompting and physical support.",
    (15, 0, 0, 3): "4. Maximising choice and control: Offering ongoing, meaningful choices during activities.",
    (15, 1, 0, 0): "1. Attentive non-verbal cues: Maintaining open body posture, nodding, and gentle eye contact.",
    (15, 1, 0, 1): "2. Paraphrasing and reflecting: Summarizing what the client expressed in your own words to verify understanding.",
    (15, 1, 0, 2): "3. Empathetic validation: Acknowledging and validating the person's emotions without judging or dismissing them.",
    (16, 0, 0): "Social justice is the fair and equitable distribution of resources, opportunities, rights, and privileges within a society.",
    (16, 1, 0, 0): "1. Access: Fair and equal opportunity to access health services, education, transport, and community infrastructure.",
    (16, 1, 0, 1): "2. Equity: Additional resources and personalized support allocated to overcome disadvantage.",
    (16, 1, 0, 2): "3. Participation: Meaningful involvement in decision-making and civic society.",
    (16, 1, 0, 3): "4. Rights: Full statutory protection against discrimination and guarantee of human rights.",
    (17, 0, 0, 0): "1. Prevents generic stereotyping and ensures care plans address true individual needs.",
    (17, 0, 0, 1): "2. Builds authentic trust and empowers the person to lead a fulfilling life on their own terms.",
    (17, 1, 0, 0): "1. Affirms their inherent human dignity, self-worth, and cultural identity.",
    (17, 1, 0, 1): "2. Enhances emotional wellbeing and reduces feelings of depersonalization in care systems.",
    (17, 2, 0): "Strengths-based practice focuses on recognizing, utilizing, and expanding an individual's existing abilities and resources rather than focusing primarily on their deficits.",
    (17, 3, 0, 0): "1. Goal-directed and forward-looking.",
    (17, 3, 0, 1): "2. Collaborative partnership between worker and client.",
    (17, 3, 0, 2): "3. Treating the person as the expert in their own life.",
    
    # Tables 18-20: Restrictive practices in CHCCCS038
    (18, 0, 0): "Restrictive practices are interventions that have the effect of restricting the free movement or liberty of a person, classified into chemical, mechanical, physical, environmental, and seclusion.",
    (19, 0, 0, 0): "1. Used only as a last resort.",
    (19, 0, 0, 1): "2. Proportional to the potential harm.",
    (19, 0, 0, 2): "3. Least restrictive option available.",
    (19, 0, 0, 3): "4. Used for the shortest time possible.",
    (19, 0, 0, 4): "5. Included in a Behaviour Support Plan.",
    (19, 0, 0, 5): "6. Authorized under state/territory legislation.",
    (19, 0, 0, 6): "7. Subject to regular monitoring and review.",
    (19, 1, 0, 0): "1. Leadership towards organizational cultural change.",
    (19, 1, 0, 1): "2. Use of data to inform practice.",
    (19, 1, 0, 2): "3. Workforce development and trauma-informed training.",
    (19, 1, 0, 3): "4. Inclusion of individual debriefing techniques.",
    (19, 1, 0, 4): "5. Meaningful consumer and carer participation.",
    (19, 1, 0, 5): "6. Rigorous prevention tools (sensory modulation, positive behaviour support).",
    (20, 0, 0, 0): "1. Any unauthorized use of a restrictive practice.",
    (20, 0, 0, 1): "2. Any use of a prohibited restrictive practice (e.g. prone or supine restraint).",
    (20, 1, 0): "must be reported to the NDIS Quality and Safeguards Commission within 5 business days.",
    
    # Table 22: 13 Australian Privacy Principles
    (22, 0, 0, 0): "APP 1 — Open and transparent management of personal information",
    (22, 0, 0, 1): "APP 2 — Anonymity and pseudonymity",
    (22, 0, 0, 2): "APP 3 — Collection of solicited personal information",
    (22, 0, 0, 3): "APP 4 — Dealing with unsolicited personal information",
    (22, 0, 0, 4): "APP 5 — Notification of the collection of personal information",
    (22, 0, 0, 5): "APP 6 — Use or disclosure of personal information",
    (22, 0, 0, 6): "APP 7 — Direct marketing",
    (22, 0, 0, 7): "APP 8 — Cross-border disclosure of personal information",
    (22, 0, 0, 8): "APP 9 — Adoption, use or disclosure of government related identifiers",
    (22, 0, 0, 9): "APP 10 — Quality of personal information",
    (22, 0, 0, 10): "APP 11 — Security of personal information",
    (22, 0, 0, 11): "APP 12 — Access to personal information",
    (22, 0, 0, 12): "APP 13 — Correction of personal information",
    (22, 1, 0, 0): "1. Storing hard-copy client files in locked filing cabinets and digital records behind two-factor password protection.",
    (22, 1, 0, 1): "2. Never discussing client details in public areas or with unauthorized third parties without signed consent.",
    
    # Tables 28-29: Advocacy & complaint mechanisms
    (28, 3, 2): "People with Disability Australia (PWDA): Free independent advocacy, advice, and human rights representation across NSW.",
    (28, 3, 3): "Aged Rights Advocacy Service (ARAS) / Older Persons Advocacy Network (OPAN): Dedicated advocacy supporting aged care consumers to assert rights.",
    (29, 3, 2): "Internal complaints process: Formal grievance forms submitted directly to service management, followed by documented investigation and feedback within 14 days.",
    (29, 3, 3): "External statutory complaints: Lodging complaints with the NDIS Quality and Safeguards Commission or Aged Care Quality and Safety Commission for independent statutory resolution.",
    
    # Table 30: Abuse, neglect, exploitation
    (30, 2, 0): "1. Unexplained bruising, welts, abrasions, or fearfulness in the presence of specific persons.",
    (30, 3, 0): "2. Sudden changes in financial assets, missing property, or unauthorized bank account withdrawals.",
    (30, 4, 0): "3. Untreated pressure ulcers, severe malnutrition, poor hygiene, or unaddressed medical conditions.",
    
    # Tables 51-55: Incident Report for Judith
    (51, 1, 0): "Care Connect Services - Residential Care Facility",
    (51, 1, 1): "15/09/2026",
    (51, 1, 2): "09:30 AM",
    (51, 2, 0): "Judith M",
    (51, 2, 1): "78",
    (51, 2, 2): "Resident, Room 14",
    (52, 1, 0): "Bruising and mild skin tear on left forearm; disheveled clothing and emotional distress.",
    (52, 1, 1): "First aid applied (wound cleansed and dressed with sterile dressing); vital signs checked; client reassured.",
    (53, 1, 0): "Support worker observed Judith crying in her room; Judith disclosed that an agency staff member roughly pulled her arm when transferring her and neglected her call buzzer.",
    (54, 1, 0): "Factual details: Disclosed rough handling by agency staff; visible skin tear and 3cm contusion observed; buzzer found unplugged behind the bedside table.",
    (55, 1, 0): "Alex Chen (Support Worker) and Sarah Jenkins (Registered Nurse).",
    
    # Table 59: Neglect indicators for Judith
    (59, 2, 0): "1. Judith was left in soiled clothing for an extended period despite calling for assistance.",
    (59, 3, 0): "2. Her emergency call buzzer was unplugged and out of physical reach.",
    (59, 4, 0): "3. Prescribed morning medication and fluids were missed on the morning shift.",
    
    # Table 67: Strategies for Matilda
    (67, 1, 0): "Facilitate a consultation with a physiotherapist to design an individualised strength and balance mobility program.",
    (67, 2, 0): "Encourage Matilda to join the weekly facility gardening group to foster friendships and community connection."
}

# ==============================================================================
# CHCCCS041 Overrides (Recognise healthy body systems)
# ==============================================================================
CHCCCS041_OVERRIDES = {
    # Table 3: Functions of cells
    (3, 2, 0): "1. Cellular metabolism and energy generation (producing ATP via cellular respiration).",
    (3, 3, 0): "2. Protein and enzyme synthesis to support growth, structural maintenance, and repair.",
    (3, 4, 0): "3. Cellular reproduction and tissue regeneration through mitosis.",
    
    # Table 4: Functions of tissues
    (4, 2, 0): "1. Epithelial tissue: Provides protective barriers against pathogens, chemical wear, and absorbs nutrients.",
    (4, 3, 0): "2. Connective tissue: Supports, binds, and cushions other tissues and organs (bones, cartilage, adipose).",
    (4, 4, 0): "3. Muscle tissue: Generates mechanical force to produce voluntary and involuntary bodily movement.",
    (4, 5, 0): "4. Nervous tissue: Transmits electrical and chemical nerve impulses throughout the central and peripheral nervous system.",
    (4, 6, 0): "5. Fluid tissue (blood/lymph): Transports oxygen, nutrients, hormones, and immune cells while removing metabolic wastes.",
    
    # Table 5 & 6: 11 Organ systems
    (5, 3, 2): "Cardiovascular system: Circulates oxygenated blood, nutrients, and hormones to cells throughout the body while transporting carbon dioxide and wastes to excretory organs via heart pumping action.",
    (5, 4, 2): "Respiratory system: Facilitates gas exchange by bringing oxygen into the body through inhalation and eliminating metabolic carbon dioxide through exhalation.",
    (5, 5, 2): "Musculoskeletal system: Provides structural framework, protects internal organs, produces red blood cells, stores calcium, and enables voluntary locomotion through muscle-bone contraction.",
    (5, 6, 2): "Digestive system: Breaks down food mechanically and chemically, absorbs essential nutrients, vitamins, and water into the bloodstream, and expels solid waste.",
    (5, 7, 2): "Urinary/Renal system: Filters metabolic wastes and toxins from blood, regulates systemic fluid and electrolyte balance, and maintains blood pH through urine excretion.",
    (5, 8, 2): "Endocrine system: Synthesizes and secretes chemical messengers (hormones) directly into blood to regulate metabolism, growth, mood, and reproduction.",
    (6, 3, 2): "Female reproductive system: Produces female gametes (ova), secretes estrogen and progesterone, facilitates conception, and sustains foetal development.",
    (6, 4, 2): "Male reproductive system: Produces, maintains, and transports sperm and protective seminal fluid, and secretes male sex hormones (testosterone).",
    (6, 5, 2): "Integumentary system: Forms a waterproof outer protective barrier against environmental pathogens, UV radiation, and dehydration; houses sensory receptors; and regulates body temperature.",
    (6, 6, 2): "Lymphatic system: Returns leaked interstitial fluid to the circulatory system, absorbs dietary fats, and filters foreign pathogens through lymph nodes.",
    (6, 7, 2): "Nervous system: Rapidly detects internal and external sensory stimuli, processes cognitive information, and coordinates voluntary and involuntary physiological responses.",
    (6, 8, 2): "Immune system: Defends the body against infectious microorganisms (bacteria, viruses, fungi) and abnormal cells using innate physical barriers and adaptive antibody/cellular responses.",
    
    # Table 7: Sensory organs
    (7, 3, 2): "Eyes: Photoreceptor organs that detect light waves and transmit electrical impulses via the optic nerve to the brain for visual processing.",
    (7, 4, 2): "Ears: Mechanoreceptors that detect acoustic sound waves for hearing and fluid movements in semicircular canals to maintain balance and spatial equilibrium.",
    (7, 5, 2): "Nose: Houses olfactory receptors that detect airborne chemical odor molecules and filters/warms inhaled air.",
    (7, 6, 2): "Tongue: Features gustatory papillae taste buds that detect basic chemical tastes (sweet, salty, sour, bitter, umami) and assists with mastication and swallowing.",
    (7, 7, 2): "Skin: Houses cutaneous thermoreceptors, mechanoreceptors (touch/pressure), and nociceptors (pain) to perceive external tactile stimuli.",
    
    # Tables 37-47: Interactions, regulation & homeostasis
    (37, 2, 0): "cardiovascular",
    (37, 2, 1): "respiratory",
    (37, 3, 0): "muscular",
    (37, 3, 1): "skeletal",
    (38, 2, 0): "Through cutaneous sensory nerve endings and receptors embedded in the dermis and epidermis.",
    (38, 3, 0): "sensory",
    (38, 3, 1): "central nervous",
    (39, 2, 0): "Gonads (testes in males and ovaries in females)",
    (39, 3, 0): "endocrine",
    (39, 3, 1): "bloodstream",
    (41, 1, 1): "Transmit visual light information to the occipital lobe of the brain.",
    (41, 1, 2): "Transmit auditory vibrations and maintain vestibular equilibrium.",
    (41, 1, 3): "Detect airborne chemical odorants through the olfactory bulb.",
    (41, 1, 4): "Detect food flavours and initiate digestive salivary secretions.",
    (42, 2, 0): "Hypothalamus acts as the body's internal thermostat, initiating sweating/vasodilation to cool down or shivering/vasoconstriction to warm up.",
    (43, 2, 0): "sweat normally",
    (43, 2, 1): "sweat glands",
    (44, 2, 0): "The kidneys regulate fluid volume, blood osmolality, and electrolytes by reabsorbing or excreting sodium, potassium, and water under the influence of aldosterone and antidiuretic hormone (ADH).",
    (45, 2, 0): "kidney",
    (45, 2, 1): "large intestine",
    (46, 2, 0): "Baroreceptors in the carotid sinuses and aortic arch monitor arterial stretch and signal the autonomic nervous system to adjust heart rate and vascular tone.",
    (47, 2, 0): "Innate immunity provides non-specific physical barriers (skin, mucous membranes) and phagocytes, while adaptive immunity produces specific T-lymphocytes and B-lymphocyte antibodies.",
    
    # Tables 48-53: Physical activity & movement
    (48, 2, 0): "accumulate at least 30 minutes of moderate-intensity physical activity on most, preferably all, days.",
    (49, 2, 0): "Active exercise involves voluntary muscle contraction performed by the client independently (e.g. walking), whereas passive exercise involves gentle external movement of joints by a carer or therapist without client effort (e.g. passive range of motion).",
    (50, 2, 0): "Encouraging regular daily walking, gentle chair yoga, and balanced hydration to maintain functional mobility and prevent joint stiffness.",
    (51, 1, 0): "Adequate nutrition provides the fuel, vitamins, and minerals necessary to sustain skin integrity, cell repair, and immune defence against infection, while hygienic food handling prevents gastrointestinal illness.",
    (52, 1, 0): "Poor oral hygiene leads to dental caries, periodontitis, and missing teeth, causing oral pain and chewing difficulty, which results in reduced food intake, weight loss, and malnutrition.",
    (53, 2, 0): "Ageing causes sarcopenia (loss of muscle mass), reduced joint cartilage, and slower neural reflexes, while disabilities may cause paresis, spasticity, or ataxia, increasing fall risks and reducing endurance.",
    
    # Tables 54-63: Indicators, ageing, and pain
    (54, 2, 0): "Dysphagia: Coughing, throat clearing, or choking during meals, and pocketing food in cheeks.",
    (54, 3, 0): "Bone health: Gradual loss of height, stooped kyphotic posture, or fracture resulting from minor trips.",
    (54, 4, 0): "Food intolerance: Abdominal bloating, flatulence, nausea, diarrhea, or rash following dairy/gluten intake.",
    (54, 5, 0): "Dementia: Progressive short-term memory loss, disorientation to time/place, and difficulty with familiar routines.",
    (54, 6, 0): "Cognitive impairment: Impaired executive functioning, confusion, and poor decision-making capacity.",
    (56, 3, 2): "Bone health: Decreased bone mineral density (osteopenia/osteoporosis), increasing fracture vulnerability.",
    (56, 4, 2): "Skin integrity: Thinning epidermis, loss of collagen and subcutaneous fat, delayed healing, and heightened risk of tears.",
    (56, 5, 2): "Pressure point injuries: Compromised microcirculation and reduced mobility lead to rapid tissue ischemia over bony prominences.",
    (58, 2, 1): "Mental health: Increased susceptibility to depressive episodes, grief from bereavement, anxiety, and social isolation.",
    (60, 1, 0): "Physical illness produces pain, fatigue, and immobility, which can trigger severe psychological distress, loss of independence, social withdrawal, and reduced quality of life.",
    (61, 1, 0): "By comparing the client's current baseline against their documented normal profile: noticing sudden changes in appetite, facial expression, gait speed, sleeping patterns, or sudden confusion/irritability.",
    (62, 2, 0): "1. Non-verbal facial expressions: Grimacing, furrowed brow, clenching teeth.",
    (62, 3, 0): "2. Vocalisations: Moaning, whimpering, grunting, or calling out.",
    (62, 4, 0): "3. Body language and behaviours: Guarding painful areas, restlessness, agitation, or sudden withdrawal.",
    (63, 2, 0): "Abbey Pain Scale",
    (63, 2, 1): "Wong-Baker FACES Pain Rating Scale",
    
    # Tables 64-73: Diseases, disabilities, medical terminology
    (64, 2, 0): "Cardiovascular disease (Heart failure): Causes impaired myocardial pumping, fluid retention, pulmonary edema, dyspnea, and extreme fatigue.",
    (64, 2, 1): "Type 2 Diabetes Mellitus: Impairs insulin secretion and glucose uptake, causing hyperglycemia, vascular damage, neuropathy, and slow wound healing.",
    (65, 1, 0): "Severe oral pain, bad breath, and loss of teeth cause social embarrassment, speech difficulties, inability to enjoy meals, and significant depression.",
    (66, 2, 0): "1. Refusing hard food textures or wincing while drinking cold/hot liquids.",
    (66, 3, 0): "2. Frequent touching of the mouth, cheek, or pulling at jaw.",
    (66, 4, 0): "3. Increased agitation, refusal of oral hygiene assistance, or foul mouth odor with swollen gums.",
    (67, 2, 0): "Physical disability: Impairment of the musculoskeletal, neurological, or circulatory systems resulting in limited physical functioning and mobility.",
    (67, 2, 1): "Sensory disability: Impairment affecting one or more senses, most commonly hearing (deafness) or vision (blindness).",
    (67, 2, 2): "Intellectual disability: Significantly reduced capacity to understand new or complex information, learn new skills, and cope independently.",
    (68, 2, 0): "1. Review client individualised care plan and identify specific recommendations from allied health professionals.",
    (68, 3, 0): "2. Attend multi-disciplinary case conferences to discuss client goals and progress.",
    (68, 4, 0): "3. Implement prescribed therapeutic exercises and assistive devices under professional guidance.",
    (68, 5, 0): "4. Document daily outcomes and report any client difficulties or setbacks to the health professional.",
    
    (70, 2, 1): "Abrasion: Superficial damage to the skin caused by friction or scraping.",
    (70, 3, 1): "Cardi- or cardio-: Relating to the heart.",
    (70, 4, 1): "Cephalgia: Headache or pain in the head.",
    (70, 5, 1): "Contusion: A bruise caused by blunt force trauma causing ruptured subcutaneous capillaries.",
    (71, 2, 1): "Febrile: Having or showing symptoms of a fever (elevated body temperature).",
    (71, 3, 1): "Pathogen: A biological agent (bacterium, virus, fungus) that can cause disease.",
    (73, 2, 1): "Complete Blood Count",
    (73, 2, 2): "A diagnostic blood test measuring red cells, white cells, hemoglobin, and platelets to detect anemia or infection.",
    
    # Tables 91-102: Case Study 2 - Madge Fall Incident Report
    (91, 2, 0): "Notify the workplace supervisor/registered nurse immediately and assist in stabilizing the client within scope of practice.",
    (92, 2, 0): "1. Deep hematoma on right hip with severe pain upon palpation.",
    (92, 3, 0): "2. Suspected hip fracture with leg shortening and external rotation.",
    (92, 4, 0): "3. Acute hypotension (blood pressure 90/60 mmHg) and tachycardia.",
    (93, 1, 0): "Madge became severely distressed, disoriented, tearful, and fearful of being left alone.",
    (95, 1, 0): "CareConnect College Aged Care Wing - Room 22",
    (95, 1, 1): "Sarah Jenkins, RN",
    (95, 1, 2): "02 9876 5432",
    (95, 1, 3): "Residential Aged Care Facility",
    (96, 1, 0): "Friday",
    (96, 1, 1): "11/03/2026",
    (96, 1, 2): "08:15 AM",
    (96, 1, 3): "Alex Chen, Support Worker",
    (97, 1, 0): "Client slip and fall while attempting unassisted transfer from bed to walker.",
    (98, 1, 0): "Right hip, right elbow abrasion, and lower back.",
    (99, 1, 0): "First aid administered; Registered Nurse called immediately; ambulance dispatched; family contacted.",
    (100, 1, 0): "Alex Chen (Support Worker) and Maria Santos (Personal Care Assistant).",
    (101, 1, 0): "At 08:00 AM, worker entered Room 22 and discovered resident Madge seated on the floor beside her bed. Madge stated she slipped while reaching for her glasses. Resident was assessed, vital signs taken, first aid provided, and RN took clinical charge.",
    (102, 1, 0): "Alex Chen, Support Worker, Care Connect Services",
    (102, 1, 1): "11/03/2026 08:45 AM",
    (102, 1, 2): "Alex Chen"
}

# ==============================================================================
# CHCDIV001 Overrides (Work with diverse people)
# ==============================================================================
CHCDIV001_OVERRIDES = {
    # Table 4: Diversity concepts
    (4, 2, 0): "Culture encompasses the shared beliefs, values, customs, language, social practices, and ways of life passed down through generations within a specific community.",
    (4, 2, 1): "Cultural competence is the ability of individuals and systems to effectively interact, communicate, and work respectfully with people across diverse cultural and linguistic backgrounds.",
    (4, 3, 0): "Cultural awareness is acknowledging cultural differences and being aware of one's own cultural beliefs.",
    (4, 3, 1): "Cultural safety is an environment that is spiritually, socially, and emotionally safe, where there is no assault, challenge, or denial of client identity.",
    
    # Tables 7-18: Policies and Anti-Discrimination Laws (Cth & NSW)
    (7, 2, 1): "National Agreement on Closing the Gap: Policy driving transformative change in health, housing, and justice equity for First Nations peoples.",
    (7, 2, 2): "https://www.closingthegap.gov.au",
    (7, 3, 1): "National Settlement Framework: Outlines comprehensive settlement support, language programs, and social integration for refugees.",
    (7, 3, 2): "https://www.homeaffairs.gov.au",
    
    (11, 2, 0): "Disability Discrimination Act 1992 (Cth)",
    (12, 1, 0): "Disability Discrimination Act 1992 (Cth)",
    (12, 1, 1): "https://www.legislation.gov.au/Details/C2016C00763",
    (12, 1, 2): "Part 2, Division 1 (Discrimination in work): Unlawful to discriminate against an employee on the ground of disability in hiring, promotion, or working conditions.",
    (12, 1, 3): "Workers must be provided with reasonable workplace adjustments and protection against discriminatory conduct.",
    (12, 1, 4): "Substantial civil penalties, compensation orders, mandatory conciliation, and organizational compliance audits.",
    
    (13, 1, 0): "Racial Discrimination Act 1975 (Cth)",
    (13, 1, 1): "https://www.legislation.gov.au/Details/C2016C00089",
    (13, 1, 2): "Section 9 (Racial discrimination to be unlawful): Prohibits discrimination based on race, colour, descent, or national/ethnic origin.",
    (13, 1, 3): "Ensures an inclusive workplace where workers are treated equally regardless of race or cultural origin.",
    (13, 1, 4): "Statutory damages, civil compensation, public apology orders, and workplace anti-racism training mandates.",
    
    (14, 1, 0): "Sex Discrimination Act 1984 (Cth)",
    (14, 1, 1): "https://www.legislation.gov.au/Details/C2021C00420",
    (14, 1, 2): "Part 2, Division 1 (Discrimination in work): Unlawful to discriminate on grounds of sex, sexual orientation, gender identity, intersex status, or marital status.",
    (14, 1, 3): "Workers have the right to a workplace free from sexual harassment, gender pay disparities, and gender bias.",
    (14, 1, 4): "Vicarious liability for employers, compensation awards, and enforcement actions by the AHRC and Fair Work Commission.",
    
    (15, 2, 0): "UN Convention on the Rights of Persons with Disabilities (UNCRPD)",
    (16, 1, 0): "UN Convention on the Rights of Persons with Disabilities (UNCRPD)",
    (16, 1, 1): "https://www.un.org/development/desa/disabilities/convention-on-the-rights-of-persons-with-disabilities.html",
    (16, 1, 2): "Article 27 (Work and employment): Recognizing the right of persons with disabilities to work on an equal basis with others.",
    (16, 1, 3): "Guides domestic disability policies, equal remuneration, and vocational rehabilitation programs.",
    (16, 1, 4): "International diplomatic scrutiny, periodic shadow reports to the UN Committee, and domestic policy reform pressure.",
    
    (17, 1, 0): "International Convention on the Elimination of All Forms of Racial Discrimination (ICERD)",
    (17, 1, 1): "https://www.ohchr.org/en/instruments-mechanisms/instruments/international-convention-elimination-all-forms-racial",
    (17, 1, 2): "Article 5: Guaranteeing equality without distinction as to race, colour, or ethnic origin in the enjoyment of economic and social rights.",
    (17, 1, 3): "Establishes global benchmarks implemented in Australian domestic anti-racism legislation.",
    (17, 1, 4): "UN Treaty Body review findings, adverse human rights reports, and international legal standing implications.",
    
    (18, 1, 0): "Convention on the Elimination of All Forms of Discrimination Against Women (CEDAW)",
    (18, 1, 1): "https://www.un.org/womenwatch/daw/cedaw/",
    (18, 1, 2): "Article 11: Elimination of discrimination against women in employment to ensure equal rights and benefits.",
    (18, 1, 3): "Mandates maternity protection, pay equity, and non-discriminatory hiring and promotion across the workforce.",
    (18, 1, 4): "International reporting citations, government review hearings, and pressure to align domestic workplace legislation.",
    
    # State Anti-Discrimination Law (NSW)
    (22, 1, 0): "Anti-Discrimination Act 1977 (NSW)",
    (23, 1, 0): "Anti-Discrimination Act 1977 (NSW)",
    (23, 1, 1): "Part 4A, Discrimination on the ground of disability (Sections 49A-49V)",
    (23, 1, 2): "Workers in NSW cannot be treated less favourably in hiring, terms of employment, or dismissal due to past, present, or future disability.",
    (23, 1, 3): "Complaints investigated by Anti-Discrimination NSW; conciliation orders, compensation up to $100,000, and NCAT hearings.",
    
    (24, 1, 0): "Anti-Discrimination Act 1977 (NSW)",
    (24, 1, 1): "Part 2, Racial discrimination (Sections 6-22)",
    (24, 1, 2): "Protects workers in NSW from direct or indirect racial discrimination, segregation, and racial vilification in the workplace.",
    (24, 1, 3): "Investigation by Anti-Discrimination NSW, legally binding conciliation, compensation awards, and public apologies.",
    
    (25, 1, 0): "Anti-Discrimination Act 1977 (NSW)",
    (25, 1, 1): "Part 3, Sex discrimination (Sections 23-38B)",
    (25, 1, 2): "Prohibits discriminatory treatment and sexual harassment in employment and provision of goods and services in NSW.",
    (25, 1, 3): "Formal hearings before the NSW Civil and Administrative Tribunal (NCAT) and enforceable monetary compensation.",
    
    # Tables 26-28: Human rights and human needs
    (26, 1, 0): "Human needs are fundamental biological, emotional, and social requirements (food, shelter, safety, belonging) necessary for human survival, while human rights are the legal, moral, and universal entitlements (enshrined in law) that protect and guarantee access to meeting those fundamental needs with dignity.",
    (27, 2, 0): "Universal Declaration of Human Rights (UDHR) Article 23 (Right to desirable work and protection against unemployment).",
    (27, 3, 0): "UDHR Article 18 (Freedom of thought, conscience and religion).",
    (27, 4, 0): "UDHR Article 25 (Right to an adequate standard of living and medical care).",
    (28, 1, 0): "1. Immediately document the incident factually. 2. Support and protect the affected worker or client. 3. Follow the internal grievance policy by notifying management. 4. If unaddressed, escalate to external bodies (Anti-Discrimination NSW, Fair Work Ombudsman, or AHRC).",
    
    # Tables 33-38: Human rights principles & PANEL
    (33, 1, 0): "Reaffirm: Re-establishing commitment to fundamental human rights in all organizational values and mission statements.",
    (33, 1, 1): "Educate: Providing ongoing cultural competence, diversity, and human rights training to all staff and clients.",
    (33, 1, 2): "Engage: Actively involving diverse community groups, elders, and clients in organizational co-design and policy reviews.",
    (35, 1, 0): "Protect: Organizations must maintain active safety measures, anti-harassment policies, and hazard controls to safeguard workers and clients from harm.",
    (35, 1, 1): "Respect: Support workers and managers must refrain from interfering with the enjoyment of rights and accept diverse cultural practices.",
    (38, 1, 0): "Participation: Involving clients directly in all planning and service decisions.",
    (38, 1, 1): "Accountability: Clear monitoring, transparent complaints processes, and answerability to regulatory standards.",
    (38, 1, 2): "Non-discrimination: Proactive inclusion and equal access for all diversity groups.",
    (38, 1, 3): "Empowerment: Building skills and knowledge so individuals can claim their rights.",
    (38, 1, 4): "Legality: Ensuring all actions align strictly with domestic and international human rights law.",
    
    # Tables 41-44: Areas of diversity & definitions
    (41, 1, 0): "Shared historical background, cultural practices, language, and ancestral heritage.",
    (41, 1, 1): "Long-term physical, cognitive, sensory, or neurological impairments.",
    (41, 1, 2): "Structured systems of faith and spiritual rituals (e.g. Christianity, Islam, Buddhism).",
    (41, 1, 3): "Socially constructed roles, behaviours, and personal gender identity.",
    (44, 2, 0): "Lesbian: A woman who is emotionally, romantically, or sexually attracted to other women.",
    (44, 2, 1): "Gay: A person who is emotionally, romantically, or sexually attracted to people of the same sex/gender.",
    (44, 2, 2): "Bisexual: A person who is attracted to people of more than one gender.",
    (44, 2, 3): "Heterosexual: A person who is attracted to people of a different gender.",
    (44, 2, 4): "Intersex: A person born with physical, hormonal, or genetic sex characteristics that do not fit typical definitions of male or female.",
    (44, 2, 5): "Transgender: A person whose gender identity differs from the sex assigned to them at birth.",
    
    # Tables 45-49: Aboriginal and Torres Strait Islander perspectives
    (45, 2, 0): "1. Historical disenfranchisement and underrepresentation in political decision-making bodies.",
    (45, 2, 1): "2. Lack of constitutional recognition and ongoing advocacy for the Voice and regional treaties.",
    (45, 3, 0): "1. Lower life expectancy and higher burden of chronic disease (Closing the Gap health disparities).",
    (45, 3, 1): "2. Systemic child removal trauma and over-representation in the juvenile and criminal justice systems.",
    (45, 4, 0): "1. Significant income gaps and higher rates of intergenerational poverty.",
    (45, 4, 1): "2. Limited employment opportunities and housing shortages in rural and remote communities.",
    (46, 1, 0): "Imposed English-only schooling suppressed traditional languages, eroded cultural knowledge transmission, and created intergenerational educational disadvantage.",
    (47, 1, 0): "Historical institutionalization within mission schools stripped young Indigenous people of family ties, contributing to systemic trauma and mistrust of authority.",
    (48, 1, 0): "Missionary settlements banned sacred ceremonies, disrupted Dreamtime spiritual connections to Country, and enforced patriarchal Western social structures.",
    (49, 1, 0): "Forced conversion undermined traditional kinship obligations, ancestral spiritual beliefs, and community lore.",
    
    # Tables 51-56: Marginalised groups, trauma, stigma
    (51, 2, 1): "Risk factor: Lack of physical activity due to inaccessible public gyms, sports facilities, or transport options.",
    (51, 2, 2): "Protective factor: Access to adaptive recreational sports programs, peer support networks, and community gyms with hoist equipment.",
    (54, 2, 0): "Anxiety and depressive symptoms resulting from social isolation and physical barriers in the community.",
    (54, 2, 1): "Need for accessible psychological counselling, supportive workplace adjustments, and peer mentoring.",
    (54, 3, 0): "Feelings of frustration, loss of autonomy, and distress when encountering inaccessible public environments.",
    (54, 3, 1): "Need for empathetic support, validation of lived experience, and empowerment to direct personal goals.",
    (55, 2, 0): "Intergenerational and complex trauma stemming from historical dispossession, Stolen Generations policies, and systemic racism.",
    (55, 2, 1): "Need for culturally safe mental health support provided by Aboriginal Community Controlled Health Services (ACCHOs).",
    (56, 2, 0): "Grief, identity distress, and loss of connection to Country, culture, and kinship networks.",
    (56, 2, 1): "Need for yarning circles, connection with local community elders, and engagement in cultural ceremonies.",
    (58, 1, 0): "The former army medic may experience hypervigilance, distress from loud noises, or flashbacks triggered by medical equipment.",
    (58, 1, 1): "Adopt trauma-informed care: provide a quiet, predictable workspace, explain procedures before acting, and avoid sudden loud alarms.",
    (59, 1, 0): "Creating segregated spaces reinforces racial stereotypes, dehumanizes clients, and constitutes unlawful racial discrimination.",
    
    # Tables 61-67: Resources, cultural influences, and practices
    (61, 2, 1): "National Multicultural Health Care Framework: Helps providers deliver linguistically accessible and culturally tailored health services.",
    (61, 2, 2): "Australian Human Rights Commission Workplace Cultural Diversity Tool: Provides self-assessment metrics for organizations to improve equity.",
    (62, 2, 0): "Migration waves have enriched Australian society with diverse languages, cuisines, and cultural perspectives, requiring support workers to adapt to varied communication norms.",
    (63, 2, 0): "Shift toward person-centred care, consumer choice under NDIS/Aged Care reforms, and increasing utilization of digital translation technologies.",
    (65, 2, 0): "Actively checking personal biases ensures respectful, patient communication and prevents cross-cultural misunderstandings.",
    (65, 2, 1): "Fosters inclusive teamwork, mutual appreciation of diverse skills, and open dialogue between colleagues of different backgrounds.",
    (67, 2, 0): "Challenging ethnocentric views allows workers to understand clients' perspectives without imposing dominant Western cultural assumptions.",
    (67, 2, 1): "Encourages society to celebrate cultural diversity, respect linguistic differences, and support equal rights.",
    
    # Tables 69-106: Practical Assessment (Cultural self-reflection & CareConnect profile)
    (69, 1, 0): "Australian with diverse multicultural heritage; values egalitarianism, active listening, and inclusive community support.",
    (69, 1, 1): "Support Worker",
    (69, 1, 2): "Providing person-centred daily support, facilitating social inclusion, and assisting clients with mobility and personal care.",
    (69, 1, 3): "Care Connect Services / Care Connect College",
    (72, 1, 0): "Support Worker: Applies cultural safety by asking clients about their preferred cultural traditions and honoring them in daily care routines.",
    (72, 1, 1): "Care Coordinator: Designs service packages that incorporate culturally specific meals, bilingual support staff, and family consultations.",
    (73, 1, 0): "1. We celebrate and respect the unique cultural, linguistic, and spiritual identity of every client and staff member.",
    (73, 1, 1): "2. We provide culturally safe care free from discrimination, stereotyping, or bias.",
    (73, 1, 2): "3. We actively foster equal opportunity, reasonable adjustments, and accessible communication across all service environments.",
    (76, 1, 0): "Direct verbal communication style: May be appreciated by Anglo-Australian clients for clarity, but perceived as blunt or disrespectful by clients from indirect, high-context cultures.",
    (84, 1, 0): "Racial discrimination violates ethical principles of human dignity and equity; must be addressed by proactive inclusion and reporting.",
    (84, 1, 1): "Disability discrimination undermines autonomy and rights; requires mandatory reasonable adjustments and accessible communication.",
    (84, 1, 2): "Sex discrimination creates hostile environments; requires zero-tolerance harassment policies and gender-affirming support.",
    (84, 1, 3): "Age discrimination perpetuates harmful stereotypes; requires empowerment, dignity of risk, and valuing older people's autonomy.",
    (86, 1, 0): "Anti-Discrimination Act 1977 (NSW)",
    (86, 1, 1): "https://legislation.nsw.gov.au/view/html/inforce/current/act-1977-048",
    (87, 1, 0): "Right to a safe workplace free from unlawful discrimination and harassment.",
    (87, 1, 1): "Lodge a formal internal grievance or external complaint to Anti-Discrimination NSW.",
    (87, 1, 2): "Responsibility to treat all clients, colleagues, and visitors with respect and avoid discriminatory conduct.",
    (87, 1, 3): "Cooperate with workplace equity investigations and attend mandatory diversity training.",
    (88, 1, 0): "Right to expect employees to comply with organizational codes of conduct and diversity policies.",
    (88, 1, 1): "Initiate formal disciplinary action or performance management for staff who breach policies.",
    (88, 1, 2): "Responsibility to take all reasonable steps to prevent discrimination (vicarious liability) and provide reasonable adjustments.",
    (88, 1, 3): "Conduct regular workplace culture reviews and implement anti-discrimination policies.",
    (89, 1, 0): "Right to receive high-quality, culturally safe services that respect individual identity, beliefs, and language.",
    (89, 1, 1): "Submit a complaint to service management, the Aged Care Quality and Safety Commission, or the NDIS Commission.",
    (89, 1, 2): "Responsibility to treat care workers and other clients with courtesy and mutual respect.",
    (89, 1, 3): "Engage constructively with the provider to resolve service disagreements.",
    (96, 1, 0): "Valuing individual autonomy and egalitarianism; ensures clients are treated as equals and empowered to direct their own support routines.",
    (97, 1, 0): "Recognizing that fast assumptions based on age or disability can lead to low expectations; overcoming this by focusing on individual strengths.",
    (98, 1, 0): "Acknowledging that my Western communication style prioritizes direct eye contact, whereas some First Nations and Asian cultures view prolonged eye contact as intrusive; adjusting body language accordingly.",
    (99, 1, 0): "Cultural bias can cause workers to view their own customs as the default standard; reflecting helps me embrace varied dietary, spiritual, and family practices.",
    (101, 1, 0): "Limitation: Limited conversational proficiency in languages other than English.",
    (101, 1, 1): "Improvement: Engage professional TIS National accredited interpreters and learn key greeting phrases in clients' primary languages.",
    (103, 1, 0): "Client became distressed when a worker attempted to enter their room without waiting for a verbal response; resolved by apologizing, stepping outside, and waiting for an invitation.",
    (104, 1, 0): "Client declined food that had touched pork products on the kitchen bench; resolved by implementing separate halal-designated cutting boards and cooking utensils.",
    (105, 1, 0): "Difficulty understanding a client's specific dialect during an initial assessment; resolved by booking an accredited phone interpreter through TIS National.",
    (106, 1, 0): "Family member wished to speak on behalf of the female client contrary to the client's non-verbal discomfort; resolved by gently explaining organizational policy of direct client consultation while honoring family involvement."
}
