"""
Populate benchmark answers for all Group 3 units:
- CHCLEG001: Work legally and ethically
- HLTWHS002: Follow safe work practices for direct client care
- CHCAGE011: Provide support to people living with dementia
- CHCDIS011: Contribute to ongoing skills development using a strengths-based approach
- CHCDIS012: Support community participation and social inclusion
"""
import os
import sys
import yaml
import re

from group3_overrides import CANDIDATE_DETAILS

def populate_chcleg001(fields):
    for f in fields:
        if f['section'] == 'Assessor Section':
            continue
        if f.get('type') == 'checkbox':
            if f['table_idx'] == 68 and "new south wales" in f.get('label', '').lower():
                f['value'] = True
            elif f['table_idx'] == 36 and f['row_idx'] in [10, 11] and f['index_in_cell'] == 0:
                f['value'] = True
            continue
        t = f['table_idx']
        r = f['row_idx']
        c = f['col_idx']
        idx = f['index_in_cell']
        p = f.get('prompt', '').lower()
        
        # Table 3: Candidate Declaration
        if t == 3:
            f['value'] = CANDIDATE_DETAILS["candidate_name"] if c == 0 or r in [0, 1] else CANDIDATE_DETAILS["date"]

        # Table 5 & 6: Children in the workplace legislation (NSW)
        elif t == 5:
            f['value'] = "Child Protection (Working with Children) Act 2012 (NSW)"
        elif t == 6:
            if r == 1: f['value'] = "Holding a valid Working with Children Check (WWCC) before starting work."
            elif r == 2: f['value'] = "Reporting any suspected risk of significant harm to children to my supervisor and the Child Protection Helpline."
            elif r == 3: f['value'] = "Keeping children supervised at all times and making sure the workplace environment is safe."
            elif r == 4: f['value'] = "Fines, losing your job, and being banned from working with children."
            elif r == 5: f['value'] = "NSW Office of the Children's Guardian"
            elif r == 6: f['value'] = "https://www.ocg.nsw.gov.au"
            elif r == 7: f['value'] = "NSW Child Safe Standards"
            elif r == 8: f['value'] = "Making sure organisations have clear rules and a safe culture to protect children from harm."

        # Table 8: Ethical considerations - children in workplace
        elif t == 8:
            if r == 1: f['value'] = "Always putting the child's safety and wellbeing first, with zero tolerance for any abuse or neglect."
            elif r == 2: f['value'] = "Keeping personal details confidential, except when I need to report safety concerns by law."
            elif r == 3: f['value'] = "Treating every child with respect, kindness, and fairness regardless of their background."
            elif r == 4: f['value'] = "Disciplinary action, losing your job, and being deregistered."

        # Table 10: National Code of Conduct for Health Care Workers
        elif t == 10:
            if r == 1: f['value'] = "National Code of Conduct for Health Care Workers (NSW Health Care Complaints Act 1993)."
            elif r == 2: f['value'] = "Giving care safely and ethically, respecting client choices, dignity, and privacy."
            elif r == 3: f['value'] = "Never having sexual, romantic, or financial relationships with clients."
            elif r == 4: f['value'] = "Being banned from practice by the HCCC, losing your job, and formal warnings."
            elif r == 5: f['value'] = "Health Care Complaints Commission (HCCC) NSW"
            elif r == 6: f['value'] = "https://www.hccc.nsw.gov.au"
            elif r == 7: f['value'] = "Australian Charter of Healthcare Rights"
            elif r == 8: f['value'] = "Gives clients the right to safe care, respect, clear information, privacy, and being listened to."

        # Table 12: First aid in the workplace
        elif t == 12:
            if r == 1: f['value'] = "First Aid in the Workplace Code of Practice (SafeWork NSW)"
            elif r == 2: f['value'] = "Keeping first aid kits fully stocked and easy to reach in an emergency."
            elif r == 3: f['value'] = "Having trained staff with current HLTAID011 first aid certificates on every shift."
            elif r == 4: f['value'] = "Breaching WHS duty of care, safety warning notices from SafeWork NSW, and fines."
            elif r == 5: f['value'] = "SafeWork NSW"

        # Table 14: Managing noise in the workplace
        elif t == 14:
            if r == 1: f['value'] = "Managing Noise and Preventing Hearing Loss at Work Code of Practice (SafeWork NSW)"
            elif r == 2: f['value'] = "Keeping noise levels below 85 decibels over an 8-hour shift so hearing is not damaged."
            elif r == 3: f['value'] = "Using hearing protection (like earplugs or earmuffs) and maintaining quiet equipment."
            elif r == 4: f['value'] = "Permanent hearing loss for workers, safety notices, and compensation claims."
            elif r == 5: f['value'] = "SafeWork NSW"

        # Table 16 & 17: Complaints handling
        elif t == 16:
            if r == 1: f['value'] = "AS/NZS 10002:2014 Guidelines for complaint management in organizations"
            elif r == 2: f['value'] = "Listening to complaints, acknowledging them within 24 to 48 hours, and fixing issues fairly."
            elif r == 3: f['value'] = "Writing down complaints accurately and passing them to management to investigate."
            elif r == 4: f['value'] = "Escalation to the Aged Care Quality and Safety Commission or NDIS Commission."
            elif r == 5: f['value'] = "Australian Human Rights Commission / ACQSC"
        elif t == 17:
            if r == 1: f['value'] = "Confidentiality: Protecting the client's privacy and not gossiping about the complaint."
            elif r == 2: f['value'] = "Fairness: Listening to everyone involved calmly and without taking sides."
            elif r == 3: f['value'] = "Loss of client trust, anger, and damaged relationships between clients and staff."
            elif r == 4: f['value'] = "Formal warning and disciplinary action for breach of workplace confidentiality."

        # Table 18 & 19: Mandatory CPD
        elif t == 18:
            if r == 1: f['value'] = "Regular training helps us keep our skills up to date, learn best practices, and deliver safe care."
            elif r == 2: f['value'] = "Completing at least 20 hours of training and professional development each year."
            elif r == 3: f['value'] = "Cannot renew registration, suspension from work, and failing audit checks."
            elif r == 4: f['value'] = "Aged Care Quality and Safety Commission / AHPRA"
            elif r == 5:
                cpds = [
                    "Attending workshops on dementia care and infection control refreshers.",
                    "Completing online training modules on manual handling and mandatory reporting.",
                    "Joining practical skills practice sessions and CPR refreshers with my team."
                ]
                f['value'] = cpds[idx] if idx < len(cpds) else cpds[-1]
            elif r == 6:
                f['value'] = "Not being allowed to work with clients until training is completed, plus formal warnings."
        elif t == 19:
            f['value'] = "Do annual CPR updates, infection control refreshers, medication safety training, and dementia workshops."

        # Table 21-35: Duty of care, dignity of risk, negligence, privacy, human rights
        elif t == 21:
            f['value'] = "Duty of care means taking reasonable steps as a support worker to keep clients safe and avoid doing anything that could cause foreseeable harm."
        elif t == 23:
            f['value'] = "Dignity of risk means respecting a client's right to make their own choices and try new things, even if there is some risk involved, so they can live independently."
        elif t == 24:
            if r == 1: f['value'] = "Aged Care Act 1997 / Quality of Care Principles 2014 (Aged Care Quality Standard 1)"
            elif r == 2: f['value'] = "https://www.legislation.gov.au/Details/F2018L01519"
            elif r == 3: f['value'] = "Consumer dignity and choice: Upholds the consumer's right to make decisions about their care, including taking calculated risks."
            elif r == 4: f['value'] = "Standard 1 (3)(a) and (d)"
            elif r == 6: f['value'] = "Support workers should talk with the client about risks and find safe ways to support their wishes, rather than just saying no."
            elif r == 7: f['value'] = "Taking away client independence, breaching Aged Care Quality Standards, and sanctions."
        elif t == 25:
            f['value'] = "Negligence happens when a worker fails to take proper care (by doing something wrong or forgetting to do something they should have), leading to harm or injury to the client."
        elif t == 27:
            f['value'] = "Informed consent means explaining what you plan to do, the benefits, and any risks in simple terms, and making sure the client willingly agrees before you start."
        elif t == 29:
            f['value'] = "Privacy Act 1988 (Cth) and Australian Privacy Principles (APPs); Health Records and Information Privacy Act 2002 (NSW)."
        elif t == 30:
            if r == 1: f['value'] = "Article 1 and Article 5 of the Universal Declaration of Human Rights"
            elif r == 2: f['value'] = "All human beings are born free and equal in dignity and rights; no one shall be subjected to torture or to cruel, inhuman or degrading treatment."
            elif r == 4: f['value'] = "Treating every client with dignity, never humiliating or talking down to them, and protecting them from harm or rough treatment."
            elif r == 5: f['value'] = "Immediate dismissal, loss of certificate/registration, and possible police investigation."
        elif t == 31:
            f['value'] = "Mandatory reporting means by law I must immediately report any suspected physical, emotional, or sexual abuse, neglect, or financial exploitation to my supervisor and reporting bodies."
        elif t == 33:
            f['value'] = "Anti-Discrimination Act 1977 (NSW) and Disability Discrimination Act 1992 (Cth) make it unlawful to discriminate against clients or workers."
        elif t == 35:
            f['value'] = "Freedom to make your own choices, freedom of speech, right to privacy, and protection from abuse or degrading treatment."
        elif t == 36:
            if r == 2: f['value'] = "Employers must not coerce an employee to exercise or not exercise a workplace right under Part 3-1 (General Protections)."
            elif r == 3: f['value'] = "Adverse action claims, substantial civil monetary penalties, and orders to compensate the employee."
            elif r == 4: f['value'] = "Employers must give pay slips within one working day of paying an amount to the employee, containing prescribed details (hours, gross/net pay, superannuation)."
            elif r == 5: f['value'] = "Fair Work Ombudsman compliance notices, infringement notices, and court-imposed civil penalties up to $66,600."
            elif r == 7: f['value'] = "Reinstatement of the employee and payment of compensation for lost remuneration up to 6 months' salary."
            elif r == 8: f['value'] = "When an employee cannot be usefully employed because of industrial action, machinery breakdown, or a stoppage of work for which the employer cannot reasonably be held responsible (Section 524)."
            elif r == 9: f['value'] = "Employer remains legally liable to pay the employee their full wages for the stand-down period."
            elif r == 10: f['value'] = "The employer must refuse the fraudulent request, report the conduct to senior management/HR, and initiate formal misconduct disciplinary procedures."
        elif t == 37:
            f['value'] = "Autonomy (respecting choices), Beneficence (doing good), Non-maleficence (doing no harm), and Justice (treating everyone fairly)."
        elif t == 38:
            if c == 1:
                if r == 2: f['value'] = "Mandatory Reporting of Child Abuse (Children and Young Persons Care and Protection Act 1998 NSW)"
                elif r == 4: f['value'] = "Support workers must report any suspected risk of significant harm to the Child Protection Helpline right away."
                elif r == 5: f['value'] = "Fines, losing registration, and immediate termination of employment."
            elif c == 2:
                if r == 2: f['value'] = "Privacy and Confidentiality (Privacy Act 1988 Cth / APPs)"
                elif r == 4: f['value'] = "Keep client information private and secure, only sharing details when required by law or with client consent."
                elif r == 5: f['value'] = "Disciplinary action, complaints to the Privacy Commissioner, and dismissal."
        elif t == 39:
            f['value'] = "An ethical dilemma happens when you face a tough choice between two principles, like respecting a client's choice to do something versus your duty to keep them safe from harm."
        elif t == 41:
            f['value'] = "Talk to my supervisor, check workplace policies, discuss options with the care team, and find safe ways to support the client's choice."
        elif t == 43:
            f['value'] = "Whistleblowing means reporting serious wrongdoing, illegal acts, or dangerous abuse to external authorities when management fails to fix the issue."
        elif t == 44:
            if r == 1: f['value'] = "NDIS Practice Standards (Quality Indicators) - Person-Centred Supports"
            elif r == 2: f['value'] = "https://www.ndiscommission.gov.au/providers/provider-obligations/ndis-practice-standards"
            elif r == 3: f['value'] = "Each participant receives support that respects their dignity and right to make their own choices."
            elif r == 4: f['value'] = "Core Module 1: Rights and Responsibilities"
            elif r == 6: f['value'] = "Support workers should actively involve participants in daily decisions and respect their personal and cultural choices."
            elif r == 7: f['value'] = "Warning notice from the NDIS Commission, losing approved provider status, and staff retraining."
        elif t == 45:
            f['value'] = "Public Interest Disclosures Act 2022 (NSW) protects workers from being bullied or punished when reporting serious workplace wrongdoing."
        elif t == 47:
            f['value'] = "Keep professional boundaries by politely declining personal gifts, avoiding personal relationships outside work, and never sharing bank or personal contact details."
        elif t == 49:
            f['value'] = "Advocacy means supporting a client and standing up for their rights so their voice and wishes are heard in all care decisions."
        elif t == 51:
            f['value'] = "Self-advocacy, family advocacy, independent advocacy, and systemic advocacy."
        elif t == 52:
            if r == 2: f['value'] = "ISO 15489-1:2016 Information and documentation - Records management"
            elif r == 3: f['value'] = "Records must be kept for the required legal period (such as 7 years for adult health records, or until age 25 for children)."
            elif r == 5: f['value'] = "Write clear, objective progress notes promptly after care and store them in secure, password-protected systems or locked filing cabinets."
            elif r == 6: f['value'] = "Loss of important medical history, privacy breaches, regulatory fines, and inability to defend against complaints."
        elif t == 53:
            f['value'] = "Access and equity means making sure everyone has fair and equal access to community services regardless of their background, language, or abilities."
        elif t == 54:
            roles_levels = {
                3: ("Help with basic household tasks like cleaning, meal prep, and companionship under supervision.", "Cannot administer medications or perform complex client transfers."),
                4: ("Provide direct personal care like showering, dressing, and following care plans under general supervision.", "Cannot alter care plan goals or assess complex wounds."),
                5: ("Coordinate daily shift rosters, guide junior support workers, and assist with medication administration.", "Cannot conduct registered nurse clinical assessments."),
                6: ("Oversee team operations, manage client services, coordinate with doctors and allied health, and supervise staff.", "Cannot make medical diagnoses or prescribe medications.")
            }
            if r in roles_levels:
                f['value'] = roles_levels[r][0] if c == 2 else roles_levels[r][1]
        elif t == 55:
            f['value'] = "Using TIS National interpreters for clients who speak limited English, providing wheelchair ramps, and respecting cultural backgrounds."
        elif t == 56:
            if r == 2:
                b_practices = [
                    "Never accept cash, personal loans, or expensive gifts from clients or their families.",
                    "Never share personal mobile numbers, home address, or social media accounts with clients.",
                    "Only perform care tasks listed in the client's care plan during scheduled shift hours."
                ]
                f['value'] = b_practices[idx] if idx < len(b_practices) else b_practices[-1]
            elif r == 3:
                f['value'] = "Unhealthy dependency, loss of professional objectivity, conflict of interest, complaints, and dismissal."

        # Tables 57-87: Human Rights & PANEL Principles
        elif t in range(57, 88):
            panel_dict = {
                "p": "Participation: Clients actively participate in all decisions affecting their health, care, and daily life.",
                "a": "Accountability: Duty-bearers are answerable for the observance and protection of human rights standards.",
                "n": "Non-discrimination: Ensuring equitable service delivery without distinction based on age, race, gender, or disability.",
                "e": "Empowerment: Building client capacities, self-advocacy skills, and independence to claim their rights.",
                "l": "Legality: Aligning all service policies and practices strictly with international and domestic human rights legislation."
            }
            if 'p:' in p: f['value'] = panel_dict['p']
            elif 'a:' in p: f['value'] = panel_dict['a']
            elif 'n:' in p: f['value'] = panel_dict['n']
            elif 'e:' in p: f['value'] = panel_dict['e']
            elif 'l:' in p: f['value'] = panel_dict['l']
            elif 'instrument' in p or 'rights' in p:
                f['value'] = "Universal Declaration of Human Rights (UDHR) and UN Convention on the Rights of Persons with Disabilities (CRPD)."
            elif 'consequence' in p:
                f['value'] = "Disciplinary reprimand, suspension, loss of professional registration, and potential civil litigation."
            elif 'individual workers' in p:
                f['value'] = "Workers must integrate human rights principles into everyday client interactions, dignity of risk, and care planning."
            else:
                f['value'] = "Ensures full compliance with the Australian Human Rights Framework through active rights protection and transparent practice."

        # Tables 88-100: Instruments & Rights
        elif t in [88, 89]:
            if r == 0: f['value'] = "UN Convention on the Rights of Persons with Disabilities (CRPD)" if t == 88 else "Aged Care Quality and Safety Commission Act 2018"
            elif r == 1: f['value'] = "Mandates respect for inherent dignity, individual autonomy, and full participation in society."
            elif r == 2: f['value'] = "Participation: Involving clients directly in formulating their individual support goals."
            elif r == 3: f['value'] = "Accountability: Maintaining open documentation and clear reporting channels."
            elif r == 4: f['value'] = "Non-discrimination: Offering equal access and dignity to all clients."
            elif r == 5: f['value'] = "Empowerment: Supporting client decision-making through choice and skill-building."
            elif r == 6: f['value'] = "Legality: Ensuring care delivery conforms strictly with Australian statutory standards."
            elif r == 7: f['value'] = "Workers must respect client choices, promote independence, and avoid restrictive practices."
            elif r == 8: f['value'] = "Sanctions by regulatory bodies, organizational dismissal, and possible civil action."

        elif t in [91, 92, 93, 94]:
            if t in [91, 93]:
                if r == 0: f['value'] = "Fair Work Act 2009 (Cth)" if t == 91 else "Work Health and Safety Act 2011 (NSW)"
                elif r == 2: f['value'] = "Fair Work Ombudsman website (www.fairwork.gov.au)"
                elif r == 3: f['value'] = "Legislative database: Federal Register of Legislation"
                else: f['value'] = "Updated modern awards and employment agreements."
            elif t in [92, 94]:
                if c == 0: f['value'] = "Right to a safe working environment free of bullying and physical hazards." if r in [1, 2] else "Right to fair pay, rest breaks, and modern award employment conditions."
                elif c == 1: f['value'] = "Statutory protection under WHS and employment legislation."
                elif c == 2: f['value'] = "Applies to all workers, contractors, and volunteers across the organization."

        elif t in [96, 97, 98, 99]:
            if t in [96, 98]:
                if r == 0: f['value'] = "Australian Community Workers Association (ACWA) Code of Ethics" if t == 96 else "Code of Conduct for Aged Care / NDIS Code of Conduct"
                elif r == 2: f['value'] = "ACWA professional standards documentation"
                elif r == 3: f['value'] = "NDIS Quality and Safeguards Commission regulatory portal"
                else: f['value'] = "Annual professional ethics guidelines."
            elif t in [97, 99]:
                if c == 0: f['value'] = "Right to practice with professional integrity and moral independence." if r in [1, 2] else "Right to be treated with dignity, respect, and professional collegiality."
                elif c == 1: f['value'] = "Ethical standard established by professional association codes."
                elif c == 2: f['value'] = "Encompasses all support worker interactions with clients, families, and colleagues."

        # Tables 104-117: Workplace activities, breaches, issues log
        elif t == 104:
            if r == 1: f['value'] = "Care Connect Services"
            elif r == 2: f['value'] = "Sarah Jenkins (Workplace Supervisor / Registered Nurse)"
            elif r == 3: f['value'] = "Sarah Jenkins, RN"
            elif r == 4: f['value'] = "David Wilson, Quality & Compliance Manager"
            elif r == 5: f['value'] = "Emily Taylor, Senior Support Worker"
            elif r == 6: f['value'] = "Mark Roberts, Care Team Leader"
        elif t == 105:
            acts = {
                1: "Reviewing client consent documentation prior to providing personal hygiene support.",
                2: "Reporting an observed medication non-compliance incident to the workplace supervisor.",
                3: "Facilitating a client choice meeting respecting dignity of risk in meal selection."
            }
            if r in acts: f['value'] = acts[r]
        elif t == 111:
            f['value'] = "Privacy and Confidentiality Protocol: Client health summary left unattended on nurse station counter." if r == 4 else "Breach of Australian Privacy Principle 11 and Health Records and Information Privacy Act 2002 (NSW)."
        elif t == 112:
            f['value'] = "Implement automatic screen locking on all shared workstations and enforce clean desk protocols with secure lockable storage for physical files."
        elif t == 113:
            f['value'] = "Support worker accepting high-value cash gifts from an older client with mild cognitive impairment." if r == 2 else "Breach of organizational Code of Conduct and Ethical Conflict of Interest Guidelines."
        elif t == 114:
            f['value'] = "Provide refresher training on gift and benefit policies and establish an open workplace gift register with mandatory manager notification."
        elif t == 117:
            unaddressed = {
                1: ("Lack of clear protocol on supported decision-making for clients with fluctuating capacity.", "Supported Decision-Making Policy & Procedure"),
                2: ("Delayed mandatory reporting of minor client abrasions to the incident management system.", "Incident and Mandatory Reporting Policy"),
                3: ("Inconsistent staff recording of restrictive practice authorization.", "Positive Behaviour Support and Restrictive Practices Manual"),
                4: ("Inadequate multilingual information sheets for non-English speaking clients.", "Cultural Diversity and Communication Guidelines")
            }
            if r in unaddressed:
                f['value'] = unaddressed[r][0] if c == 0 else unaddressed[r][1]

    return fields

def populate_hltwhs002(fields):
    for f in fields:
        if f['section'] == 'Assessor Section':
            continue
        if f.get('type') == 'checkbox':
            if f['table_idx'] == 5 and f['row_idx'] == 10 and f['index_in_cell'] == 1:
                f['value'] = True
            continue
        t = f['table_idx']
        r = f['row_idx']
        c = f['col_idx']
        idx = f['index_in_cell']
        p = f.get('prompt', '').lower()

        # Table 4: WHS legislation (NSW)
        if t == 4:
            f['value'] = "Work Health and Safety Act 2011 (NSW)" if r == 1 else "Sets out the main safety laws in NSW to protect the health, safety, and welfare of workers, clients, and visitors."
        
        # Table 5: WHS Regulations (NSW)
        elif t == 5:
            if r == 1: f['value'] = "Work Health and Safety Regulation 2017 (NSW)"
            elif r == 2: f['value'] = "Gives practical legal rules for managing manual tasks, hazardous chemicals, first aid, and emergency plans."
            elif r == 3: f['value'] = "Part 4.2 - Hazardous Manual Tasks"
            elif r == 4: f['value'] = "Sets out duties to identify and control risks of musculoskeletal disorders."
            elif r == 5: f['value'] = "Part 3.2 - General Working Environment (First aid, emergency plans, and PPE)"
            elif r == 6: f['value'] = "Requires employers to provide first aid facilities, emergency evacuation plans, and proper PPE."
            elif r == 7: f['value'] = "SafeWork NSW"
            elif r == 8: f['value'] = "be approved by the relevant Minister and published in the NSW Government Gazette."
            elif r == 10: f['value'] = "False. Approved codes of practice are not law themselves, but they are admissible in court proceedings as evidence of whether or not a duty or obligation under the WHS Act has been complied with."

        # Table 6: Codes of practice
        elif t == 6:
            if r == 1: f['value'] = "Hazardous Manual Tasks Code of Practice (SafeWork NSW)"
            elif r == 2: f['value'] = "https://www.safework.nsw.gov.au/resource-library/list-of-all-codes-of-practice/hazardous-manual-tasks"
            elif r == 3: f['value'] = "Provides practical guidance to spot dangerous lifting, pulling, and bending postures, and use mechanical hoists to prevent back and muscle injuries."
            elif r == 4: f['value'] = "Managing the Risk of Falls at Workplaces Code of Practice"
            elif r == 5: f['value'] = "https://www.safework.nsw.gov.au/resource-library/list-of-all-codes-of-practice/managing-the-risk-of-falls-at-workplaces"
            elif r == 6: f['value'] = "Explains how to prevent slips, trips, and falls during showering, mobility transfers, and walking on wet floors."
            elif r == 7: f['value'] = "How to Manage Work Health and Safety Risks Code of Practice"
            elif r == 8: f['value'] = "https://www.safework.nsw.gov.au/resource-library/list-of-all-codes-of-practice/how-to-manage-work-health-and-safety-risks"
            elif r == 9: f['value'] = "Explains the 4-step risk management process: 1. Spot hazards, 2. Assess risks, 3. Control risks, 4. Review controls."

        # Table 7: Industry standards
        elif t == 7:
            if r == 1: f['value'] = "Industry standards are established guidelines and rules developed by standards bodies (like Standards Australia) setting out best practice safety and quality for equipment and care."
            elif r == 2: f['value'] = "AS/NZS ISO 45001:2018 Occupational health and safety management systems."
            elif r == 3: f['value'] = "Provides organizations with a structured system to improve employee safety, reduce hazards, and prevent injuries."

        # Table 8: WHS Authorities
        elif t == 8:
            if r == 1: f['value'] = "SafeWork NSW"
            elif r == 2: f['value'] = "Inspects workplaces, gives improvement and prohibition notices, investigates serious workplace accidents, and enforces WHS laws in NSW."
            elif r == 3: f['value'] = "Health and Safety Representative (HSR) and Workplace Health and Safety Committee."
            elif r == 4: f['value'] = "Helps workers and management talk about safety issues, does workplace safety checks, and assists in incident reviews."
            elif r == 5: f['value'] = "Right to stop unsafe work and right to be consulted on safety matters affecting our work."

        # Table 9 & 10: Rights and responsibilities
        elif t == 9:
            if r == 1: f['value'] = "Primary duty of care (Section 19): Ensure, so far as is reasonably practicable, the health and safety of workers and clients in the workplace."
            elif r == 2: f['value'] = "Provide and maintain safe equipment, safe work procedures, clean facilities, and first aid kits."
            elif r == 3: f['value'] = "Provide necessary safety training, clear instructions, and adequate supervision."
            elif r == 4: f['value'] = "Section 28 Worker Duties: Take reasonable care for my own health and safety and make sure my actions don't harm others."
            elif r == 5: f['value'] = "Follow any reasonable safety instruction and follow workplace WHS policies and procedures."
            elif r == 6: f['value'] = "Report hazards, injuries, near misses, and faulty equipment immediately to my supervisor."
            elif r == 8: f['value'] = "Section 28 of the Work Health and Safety Act 2011 (NSW)."
        elif t == 10:
            if r == 1: f['value'] = "Right to work in a safe, healthy environment where hazards are properly controlled."
            elif r == 2: f['value'] = "Right to stop work or refuse dangerous work if there is a serious imminent risk to my health or safety."
            elif r == 3: f['value'] = "Right to elect Health and Safety Representatives and speak up about safety concerns."
            elif r == 4: f['value'] = "Right to receive proper PPE, first aid supplies, and safety training free of charge."
            elif r == 5: f['value'] = "Responsibility to wear and take care of provided PPE properly (gloves, masks, eye protection)."
            elif r == 6: f['value'] = "Responsibility not to damage, misuse, or interfere with safety equipment."
            elif r == 7: f['value'] = "Responsibility to take part in workplace safety meetings and training sessions."
            elif r == 8: f['value'] = "Responsibility to follow infection control rules and safe manual handling guidelines."

        # Table 11: Officers duties
        elif t == 11:
            officer_vals = [
                "Keep up-to-date knowledge of work health and safety laws and practices.",
                "Understand the work operations and the hazards involved in client care.",
                "Make sure the organisation provides and uses proper safety equipment and resources.",
                "Make sure there are clear processes to receive and respond to incident and hazard reports.",
                "Ensure the organisation complies with all obligations under the WHS Act.",
                "Verify that safety resources and procedures are actually being followed through audits and reviews."
            ]
            f['value'] = officer_vals[idx] if idx < len(officer_vals) else officer_vals[-1]

        # Tables 12-25: Hazards, Risk assessment, Manual tasks, Emergencies
        elif t == 12:
            f['value'] = "A hazard is something with potential to cause harm (like a wet floor). A risk is the chance and how badly someone could get hurt by that hazard."
        elif t == 13:
            vals = ["Elimination", "Substitution", "Isolation", "Engineering controls", "Administrative controls", "Personal Protective Equipment (PPE)"]
            f['value'] = vals[idx] if idx < len(vals) else vals[-1]
        elif t == 14:
            f['value'] = "Spot the hazards, assess the risk level (likelihood and consequence), put control measures in place using the hierarchy of controls, and review controls regularly."
        elif t == 15:
            f['value'] = "Musculoskeletal disorders (MSD) like lower back strains, shoulder injuries, or wrist pain from heavy lifting, awkward bending, or pushing heavy wheelchairs."
        elif t == 16:
            f['value'] = "Use mechanical hoists, slide sheets, height-adjustable beds, and always get a second support worker to help with heavy or difficult transfers."
        elif t == 17:
            f['value'] = "Check the client's transfer plan, clear any clutter from the floor, adjust bed height, lock wheels, explain what you are doing to the client, and keep a good posture."
        elif t == 18:
            f['value'] = "R - Remove people in immediate danger; A - Alert emergency services (000) and sound the alarm; C - Contain smoke and fire by closing doors; E - Evacuate to the assembly area."
        elif t == 19:
            f['value'] = "Follow DRSABCD: Danger, Response, Send for help (000), Airway, Breathing, CPR (30 compressions : 2 breaths), Defibrillation (AED)."
        elif t == 20:
            f['value'] = "Blood-borne viruses (HBV, HCV, HIV), respiratory infections (COVID-19, Influenza, colds), and stomach bugs (Norovirus, gastroenteritis)."
        elif t == 21:
            f['value'] = "Wash hands before and after client contact, wear PPE (gloves, aprons, masks), dispose of sharps safely, clean up spills immediately, and disinfect surfaces."
        elif t == 22:
            f['value'] = "A notifiable incident under WHS Act Section 38 is a death, serious injury or illness needing immediate hospital treatment, or a dangerous incident (like a fire, explosion, or gas leak)."
        elif t == 23:
            f['value'] = "Call SafeWork NSW immediately on 13 10 50 and follow up with written notice within 48 hours; do not disturb the incident site."
        elif t == 24:
            f['value'] = "Fill out the workplace Incident/Accident Report Form, write down factual details, note vital signs and first aid given, and report to the supervisor."
        elif t == 25:
            f['value'] = "Debriefing gives emotional support to workers, reduces stress or trauma after a crisis, identifies what happened, and helps prevent it happening again."
        elif t == 26:
            if r == 2: f['value'] = "Illnesses caused by germs like bacteria or viruses that pass from person to person or from dirty surfaces, causing illnesses like gastroenteritis, the flu, or skin infections."
            elif r == 3:
                sources = [
                    "High-touch surfaces like door handles, bathroom taps, and bedside tables.",
                    "Client body fluids like blood, urine, vomit, or soiled personal laundry.",
                    "Improperly stored or prepared food, unwashed hands, and pests."
                ]
                f['value'] = sources[idx] if idx < len(sources) else sources[-1]
            elif r == 4:
                minims = [
                    "Washing hands thoroughly with soap and water or using alcohol-based hand rub.",
                    "Wearing proper PPE (gloves, apron, mask) whenever exposed to body fluids or soiled laundry.",
                    "Wiping down surfaces with hospital-grade disinfectant and bagging dirty linen immediately."
                ]
                f['value'] = minims[idx] if idx < len(minims) else minims[-1]
        elif t == 27:
            if r == 2: f['value'] = "The musculoskeletal system is made up of our bones, joints, muscles, tendons, and ligaments that support the body and help us move."
            elif r == 3:
                msds = [
                    "Lower back strain or muscle spasm from lifting or bending.",
                    "Wrist strain or carpal tunnel from repetitive tasks.",
                    "Shoulder strain or rotator cuff pain from pulling clients or equipment."
                ]
                f['value'] = msds[idx] if idx < len(msds) else msds[-1]
        elif t == 28:
            if r == 3: f['value'] = "Identify manual tasks that involve awkward postures, heavy lifting, or repetitive movements."
            elif r == 4: f['value'] = "Assess the risk level using the manual handling risk assessment matrix."
            elif r == 6: f['value'] = "Put controls in place like hoists, slide sheets, and asking a colleague to help."
            elif r == 7: f['value'] = "Check controls regularly and update the client's care plan if their mobility changes."
        elif t == 30:
            if r == 0: f['value'] = "Support Worker / Care Assistant"
            elif r == 1: f['value'] = "Providing personal care, helping with client transfers, following WHS procedures, and reporting hazards."
            elif r == 3: f['value'] = "Residential Aged Care Facility / Community Home-based Care"
            elif r == 4: f['value'] = "Aged Care and Disability Support Sector"

        # Tables 33-53: Case study tasks
        elif t in [33, 34, 35]:
            if r == 1: f['value'] = "Client Lucy slipped from wheelchair onto bathroom floor; floor was wet from shower and the bathmat slid."
            elif r == 2: f['value'] = "Lucy had a small skin tear and bruising on her left elbow and complained of pain in her right hip."
            elif r == 3: f['value'] = "Assisted Lucy calmly, applied first aid with an ice pack on hip and sterile dressing on elbow, called RN Sarah Jenkins, and checked vital signs."
            else: f['value'] = "Reported immediately to supervisor Sarah Jenkins and filled out the workplace Incident Report Form."
        elif t in [36, 37, 38]:
            if r == 1: f['value'] = "Worker strained lower back while trying to reposition client Lucy in bed without using a slide sheet."
            elif r == 2: f['value'] = "Sharp lower back pain, muscle stiffness, and difficulty standing straight."
            elif r == 3: f['value'] = "Stopped task immediately, notified supervisor Sarah Jenkins, applied cold pack, rested, and saw doctor."
            else: f['value'] = "Lodged worker injury report, reviewed safe manual handling, and scheduled slide sheet refresher training for staff."
        elif t in range(39, 54):
            f['value'] = "Reported hazard immediately to supervisor Sarah Jenkins, put up warning signs to keep area clear, and logged details in the hazard register."

    return fields

def populate_chcage011(fields):
    for f in fields:
        if f['section'] == 'Assessor Section':
            continue
        if f.get('type') == 'checkbox':
            if f['table_idx'] == 3 and f['row_idx'] == 3 and f['index_in_cell'] == 1:
                f['value'] = True
            elif f['table_idx'] == 54:
                # Type of incident: injury / medical condition
                if f['row_idx'] == 1 and f['col_idx'] in [0, 2]:
                    f['value'] = True
                elif f['row_idx'] == 4 and f['index_in_cell'] in [0, 3]:
                    f['value'] = True
            elif f['table_idx'] == 55:
                # Response to incident: First aid / clean linen provided, supervisor notified
                if f['row_idx'] == 1 and f['col_idx'] == 0:
                    f['value'] = True
                elif f['row_idx'] == 3 and f['col_idx'] in [0, 1]:
                    f['value'] = True
            continue
        t = f['table_idx']
        r = f['row_idx']
        c = f['col_idx']
        idx = f['index_in_cell']
        p = f.get('prompt', '').lower()

        # Table 3: Dementia research & testing
        if t == 3:
            if r == 2:
                # 3 diagnostic tests
                diag_tests = [
                    "Mini-Mental State Examination (MMSE): A short set of questions testing memory, attention, and language.",
                    "Montreal Cognitive Assessment (MoCA): Tests short-term memory, planning, problem-solving, and orientation.",
                    "Rowland Universal Dementia Assessment Scale (RUDAS): A screening tool designed to be fair for people from different language and cultural backgrounds."
                ]
                f['value'] = diag_tests[idx] if idx < len(diag_tests) else diag_tests[-1]
            elif r == 4:
                # 3 current treatments
                treatments = [
                    "Medicines that target amyloid plaques to help slow down damage to brain cells.",
                    "Treatments targeting tau tangles to protect brain cells from breaking down.",
                    "Programs focusing on brain training, physical exercise, and healthy diet to support brain health."
                ]
                f['value'] = treatments[idx] if idx < len(treatments) else treatments[-1]
            elif r == 5:
                f['value'] = "Person-centred care, improving quality of life, and avoiding restrictive practices through gentle activities and clear communication."
            elif r == 6:
                early_methods = [
                    "Brain scans like MRI or PET scans that can show physical changes or shrinkage in the brain.",
                    "Biomarker tests using blood samples or spinal fluid to look for specific proteins linked to dementia."
                ]
                f['value'] = early_methods[idx] if idx < len(early_methods) else early_methods[-1]
            elif r == 7:
                f['value'] = "Getting diagnosed early gives the person and their family time to plan ahead, make legal and care choices, and start support services early."
            elif r == 8:
                therapies = [
                    "Reminiscence therapy: Talking about happy past memories using old photos, music, or familiar objects.",
                    "Music therapy: Playing calming, familiar songs to help reduce anxiety and improve mood."
                ]
                f['value'] = therapies[idx] if idx < len(therapies) else therapies[-1]

        # Table 4: Causes of dementia
        elif t == 4:
            if r == 1:
                f['value'] = "Dementia is caused by progressive damage to brain cells, which stops them from working properly and leads to ongoing memory loss and confusion."
            elif r == 2:
                causes = [
                    "Strokes and damaged blood vessels in the brain that stop oxygen from reaching brain cells.",
                    "Inherited genetic conditions passed down through families (like familial Alzheimer's genes).",
                    "Severe head injuries from falls or accidents that damage brain tissue.",
                    "Getting older, which is the biggest risk factor as brain cells naturally become more fragile over time."
                ]
                f['value'] = causes[idx] if idx < len(causes) else causes[-1]

        # Table 5 & 6: Types of dementia
        elif t == 5:
            types_d = {
                1: "Alzheimer's Disease: The most common type of dementia. It starts with mild memory loss and gradually makes it harder to remember recent events, find words, or complete everyday tasks.",
                2: "Vascular Dementia: Caused by reduced blood flow or mini-strokes in the brain. Cognitive decline often happens in steps, where thinking and planning drop after each stroke.",
                3: "Frontotemporal Dementia: Affects the front parts of the brain, causing noticeable changes in personality, social behavior, and loss of speech or language understanding.",
                4: "Vascular dementia: Caused by poor blood flow in the brain due to strokes, leading to problems with planning, walking, and thinking.",
                5: "Multi-infarct dementia: A form of vascular dementia caused by multiple small mini-strokes that damage small areas across the brain over time."
            }
            if r in types_d: f['value'] = types_d[r]
        elif t == 6:
            types_d2 = {
                1: "Lewy Body Dementia: Causes memory problems along with visual hallucinations, fluctuating alertness, and tremors or stiffness similar to Parkinson's disease.",
                2: "Korsakoff Syndrome: A severe memory condition caused by a lack of vitamin B1 (thiamine), usually linked to long-term alcohol misuse. It makes it very hard to learn new information.",
                3: "Frontotemporal lobar degeneration: Brain shrinkage in the front and temporal lobes, leading to major changes in social behaviour or difficulty speaking and understanding words.",
                4: "Huntington's disease: An inherited genetic condition that causes involuntary jerky movements, mood swings, and gradual loss of thinking and memory skills.",
                5: "Parkinson's Disease: A condition affecting brain cells that control movement, leading to shaking, stiff muscles, slow movements, and in later stages, dementia.",
                6: "Younger onset dementia: Any form of dementia diagnosed in people under the age of 65, which often has a big impact on family, work, and finances."
            }
            if r in types_d2: f['value'] = types_d2[r]

        # Table 7 & 8: Pathological features & plaques/tangles
        elif t == 7:
            if r == 1: f['value'] = "Dementia physically damages and destroys brain cells and their connections, causing different areas of the brain to shrink over time."
            elif r == 2: f['value'] = "Amyloid plaques are abnormal protein build-ups that form in the spaces between brain cells."
            elif r == 3: f['value'] = "They block messages from passing between brain cells and trigger inflammation that damages surrounding brain tissue."
            elif r == 4: f['value'] = "Plaques build up between brain cells, stopping normal communication and causing nearby nerve cells to weaken and die."
        elif t == 8:
            if r in [0, 1]: f['value'] = "Neurofibrillary tangles are twisted strands of tau protein that form inside brain cells."
            elif r == 2: f['value'] = "Tau protein detaches from the cell structure and tangles up, destroying the transport system inside the brain cell so it cannot survive."
            elif r == 3: f['value'] = "The overall shrinkage of brain tissue and loss of brain cells as dementia progresses."
            elif r == 4: f['value'] = "It reduces brain size and destroys the connections needed for memory, speech, and everyday tasks."

        # Table 9: Symptoms and indicators
        elif t == 9:
            symps = {
                1: "Memory loss: Forgetting recent events, repeating the same question, or losing track of the day.",
                2: "Communication difficulty: Struggling to find common words, losing train of thought, and speaking in short phrases.",
                3: "Disorientation: Getting confused about the time of day, date, or getting lost in familiar surroundings.",
                4: "Indicator: Neglecting personal hygiene, wearing unwashed or mismatched clothes, and skipping meals.",
                5: "Indicator: Uncharacteristic mood swings, sudden withdrawal from family and friends, or feeling anxious.",
                6: "Indicator: Struggling to complete familiar everyday tasks, like making a cup of tea or buttoning a shirt.",
                7: "Progressive aphasia: Difficulty finding words to speak or understanding what others are saying.",
                8: "Apraxia: Trouble carrying out purposeful physical movements (like using a fork) even though muscles are healthy.",
                9: "Agnosia: Not recognizing familiar everyday objects, sounds, or faces (for example, not recognizing a comb or a close relative)."
            }
            if r in symps: f['value'] = symps[r]

        # Table 10: Behaviours of concern
        elif t == 10:
            behs = {
                1: "Wandering: Walking around without a clear destination, often looking for home or feeling restless.",
                2: "Agitation: Feeling restless, anxious, or irritable, often triggered by too much noise, clutter, or feeling rushed.",
                3: "Sundowning: Becoming more confused, anxious, or agitated in the late afternoon and evening as the sun goes down.",
                4: "Vocal disruption: Calling out loudly, groaning, or repeating words because of pain, loneliness, or distress.",
                5: "Resistance to care: Refusing assistance with showering or dressing because the person feels scared, cold, or embarrassed.",
                6: "Physical aggression: Lashing out, hitting, or pushing away when feeling cornered, frightened, or misunderstood.",
                7: "Hiding items: Stashing away clothes, food, or cutlery in cupboards or under pillows because of feeling insecure.",
                8: "Disinhibition: Saying inappropriate comments or undressing in public areas due to loss of social filters."
            }
            if r in behs: f['value'] = behs[r]

        # Tables 11-25: Communication, validation, pain, environment
        elif t == 11:
            f['value'] = "Behaviours are often a way of communicating an unmet need (like pain, hunger, cold, or fear) when the person can no longer explain it in words. For example, a resident pushing staff away during a shower because the water is too hot, or pacing because they have a painful urinary infection."
        elif t == 12:
            f['value'] = "Restrictive practices are actions or devices that stop a person from moving freely or making their own choices (like locking doors, using bed rails, or giving sedating medications). They should only ever be used as a last resort when there is immediate danger, and for the shortest possible time."
        elif t == 13:
            f['value'] = "Restrictive practices must only be used as a last resort, for the shortest possible time, and after all positive and gentle support strategies have been tried."
        elif t == 14:
            f['value'] = "1. Right to freedom of movement and dignity. 2. Right to make personal choices. 3. Right to be treated with respect and live free from abuse."
        elif t == 15:
            f['value'] = "Non-verbal pain signs include facial grimacing, groaning, guarding a painful body part, clenching fists, or sudden withdrawal. Two pain tools are the Abbey Pain Scale (for non-verbal clients) and the Wong-Baker FACES scale."
        elif t == 16:
            f['value'] = "Undetected pain or an infection (like a UTI) can cause sudden confusion (delirium), make the resident very agitated, stop them from eating, or increase their risk of falling."
        elif t in [17, 18, 19]:
            f['value'] = "Dementia causes physical loss of coordination and balance, while emotionally it can cause fear, anxiety, and frustration. For family carers, it causes high emotional stress, physical exhaustion, and grief as the person's memory fades."
        elif t == 20:
            f['value'] = "1. Feelings of grief and loss over losing his driving licence. 2. Loneliness from not seeing his friends. 3. Frustration and lower self-confidence."
        elif t == 21:
            f['value'] = "Support the person empathetically by listening without judgment, encouraging them to join enjoyable social activities, and treating them with dignity and respect."
        elif t == 22:
            f['value'] = "1. Seeing the person first, not their dementia diagnosis. 2. Involving the person in decisions about their daily routine. 3. Respecting their personal life history, habits, and cultural background."
        elif t == 23:
            f['value'] = "Looking through family photo albums, watering plants in the garden, listening to favorite music from their youth, or folding warm towels together."
        elif t == 24:
            f['value'] = "Good, glare-free lighting to prevent scary shadows; clear picture signage on bathroom doors at eye level; and keeping noise low by reducing loud TV or radio sounds."
        elif t == 25:
            f['value'] = "Physical abuse (hitting/rough handling), emotional abuse (yelling/belittling), financial abuse (misusing money/cards), and neglect (leaving someone in soiled bedding or ignoring hygiene). Report immediately to the supervisor and under SIRS guidelines."
        elif t == 27:
            comm_methods = {
                1: ("Speak clearly, use simple everyday words, and give one instruction at a time.", "Example: 'Good morning, Madge. Let's put on your warm cardigan.'"),
                2: ("Use warm eye contact, smile, and keep an open, relaxed posture.", "Example: Sitting down beside the resident so you are at eye level and smiling warmly."),
                3: ("Respecting the person's cultural customs, language preferences, and traditions.", "Example: Using preferred greetings or simple words in the resident's first language."),
                4: ("Creating a comfortable space where the person feels safe and valued.", "Example: Arranging a bilingual worker or interpreter if the resident prefers their native tongue."),
                5: ("Using gentle environment cues like large clocks and calendars to help orientate without arguing.", "Example: Placing a large-print day/night clock on the bedside table."),
                6: ("Using comforting, reassuring words to make the person feel safe.", "Example: 'You are safe here with me, Madge. I am right here to help you.'")
            }
            if r in comm_methods:
                f['value'] = comm_methods[r][0] if c == 1 else comm_methods[r][1]
        elif t == 28:
            comm_methods2 = {
                1: ("Open arm posture, gentle unhurried movements, and warm eye contact.", "Example: Placing a gentle, reassuring hand on the resident's arm when they seem anxious."),
                2: ("Accepting the person's feelings and their version of reality instead of arguing.", "Example: If a resident is worried about getting her children from school, saying: 'You are such a caring mother, tell me about your kids.'"),
                3: ("Recognizing and acknowledging how the person is feeling.", "Example: 'I can see you are feeling upset and worried right now. I understand.'"),
                4: ("Letting the person cry or express frustration without shushing them or walking away.", "Example: Sitting quietly with a crying resident, holding their hand, and offering a tissue."),
                5: ("Talking about happy past memories, achievements, and family life.", "Example: Looking through a photo album together and asking about their wedding day or old job.")
            }
            if r in comm_methods2:
                f['value'] = comm_methods2[r][0] if c == 1 else comm_methods2[r][1]
        elif t == 29:
            if r == 2:
                stressors = [
                    "Environmental stressors: Loud TV sounds, bright flashing lights, or crowded rooms that overwhelm the senses.",
                    "Physical stressors: Undetected pain, feeling cold, constipation, or needing the toilet.",
                    "Emotional stressors: Feeling rushed, disorientated, or misunderstood by carers."
                ]
                f['value'] = stressors[idx] if idx < len(stressors) else stressors[-1]
            elif r == 3:
                examples = [
                    "A noisy, busy dining room makes the resident anxious and refuse to eat their meal.",
                    "Being rushed through morning showering causes frustration that leads to an angry reaction."
                ]
                f['value'] = examples[idx] if idx < len(examples) else examples[-1]
            elif r == 4:
                f['value'] = "Small stresses build up across the day until the person reaches a breaking point, leading to crying, shouting, or withdrawing completely."

        # Tables 31-37: Assistive technologies
        elif t in range(31, 38):
            if "example" in p or c in [2, 3]:
                at_examples = [
                    "Easy-grip adaptive cutlery and high-rim scooped plate for eating.",
                    "Shower chair with armrests and non-slip floor mat for bathing.",
                    "Large-print digital day clock showing morning, afternoon, and night.",
                    "Bed sensor mat that gently alerts care staff if the resident gets out of bed at night.",
                    "4-wheel mobility walker with handbrakes and padded seat."
                ]
                f['value'] = at_examples[idx % len(at_examples)]
            else:
                at_descs = [
                    "Helps the resident eat meals independently with less spilling and fatigue.",
                    "Allows the resident to sit safely while showering, reducing the risk of falls.",
                    "Helps orientate the resident to the day and time, reducing anxiety about schedules.",
                    "Protects resident safety by notifying carers promptly if they wander at night.",
                    "Provides physical stability and confidence while walking indoors and outdoors."
                ]
                f['value'] = at_descs[idx % len(at_descs)]

        # Tables 38-44: Legal and ethical requirements (NSW)
        elif t in range(38, 45):
            if "legislation" in p or "legal" in p or r in [1, 2]:
                if "whs" in p or "safety" in p or t in [40, 44]:
                    f['value'] = "Work Health and Safety Act 2011 (NSW): I must take reasonable care of my own safety and the safety of clients, use hoists properly, and report hazards."
                elif "privacy" in p or "confidentiality" in p or t in [42, 43]:
                    f['value'] = "Privacy Act 1988 (Cth): I must keep client personal and health information secure, not share files with unauthorized people, and only discuss care with the care team."
                elif "mandatory" in p or "reporting" in p or t in [41, 44]:
                    f['value'] = "Aged Care Act 1997 / Serious Incident Response Scheme (SIRS): I must immediately report any suspected physical abuse, sexual abuse, or neglect to my supervisor."
                else:
                    f['value'] = "Aged Care Quality Standards (Standard 1: Consumer Dignity and Choice): I must treat residents with respect and support their right to make everyday choices."
            elif "ethical" in p:
                f['value'] = "Treat every resident with kindness and dignity, maintain professional boundaries, never accept gifts or money, and always prioritize resident safety and comfort."
            else:
                f['value'] = "In my daily work, I always knock before entering a room, explain what I am doing before assisting, keep curtains closed for privacy, and report any health changes to the nurse."

        # Table 49: Three conditions beyond support worker role (Madge)
        elif t == 49:
            if r == 3:
                f['value'] = "Severe unexplained weight loss and dehydration over the past two months."
            elif r == 4:
                f['value'] = "Painful urination (dysuria) and no bowel movement for two days (suspected UTI and severe constipation)."

        # Table 50: Signs of abuse and neglect (Madge)
        elif t == 50:
            if r in [3, 4]:
                abuse_signs = [
                    "Madge showed visible fear, hesitation, and anxiety when nurse Olivia's name was mentioned.",
                    "Reluctance to ask for pain relief or help because she 'did not want to bother the nurse', and changing her story claiming the pain was gone."
                ]
                f['value'] = abuse_signs[idx] if idx < len(abuse_signs) else abuse_signs[-1]
            elif r in [7, 8]:
                neglect_signs = [
                    "Stained bedsheets smelling of faeces and urine that had not been changed or checked for at least a day or two.",
                    "Being left in bed for two days without repositioning, resulting in an open bleeding pressure wound on her buttocks and purple marks on her shoulders."
                ]
                f['value'] = neglect_signs[idx] if idx < len(neglect_signs) else neglect_signs[-1]

        # Tables 52-57: Incident Report Form for Madge
        elif t == 52:
            if r == 2: f['value'] = "CareConnect Residential Aged Care - Room 14 (Madge's Room)"
            elif r == 3: f['value'] = "Sarah Jenkins (Registered Nurse / Supervisor)"
            elif r == 4: f['value'] = "0412 345 678"
            elif r == 5: f['value'] = "Residential Aged Care Facility"
        elif t == 53:
            if "day" in p or c == 0: f['value'] = "Friday"
            elif "date" in p or c == 1: f['value'] = "11/03/2026"
            elif "time" in p or c == 2: f['value'] = "08:00 AM"
            elif "completed by" in p or r == 2: f['value'] = "Alex Chen (Individual Support Worker)"
        elif t == 54:
            if r == 2: f['value'] = "Madge Thompson (Resident)"
            elif r == 3: f['value'] = "Upper buttocks, both shoulders, and backside of head"
            elif r == 4: f['value'] = "Stage 2 open pressure wound with bleeding, and purple discoloured pressure spots"
            elif r == 5: f['value'] = "2cm open red wound with bleeding on upper buttocks; 8cm purple marks on both shoulders; 3cm mark on head"
            elif r == 6: f['value'] = "Bedsheets stained and smelling of urine and faeces; resident in pain, anxious, and expressed fear of nurse Olivia"
        elif t == 55:
            if r == 1: f['value'] = "Gently helped Madge into comfortable position, provided clean bed linen, stayed with her to provide reassurance, and reported immediately to RN Sarah Jenkins"
            elif r == 2: f['value'] = "RN supervisor Sarah Jenkins attended Room 14 immediately to inspect wounds, provide wound care, and arrange urgent GP review"
            elif r == 3: f['value'] = "Registered Nurse supervisor Sarah Jenkins and Facility Clinical Manager"
        elif t == 56:
            if r == 1: f['value'] = "Alex Chen (Support Worker) and co-worker support worker assisting with transfer"
            elif r == 2: f['value'] = "At 8:00 AM on 11/03/2026, during transfer to wheelchair, I observed a 2cm open bleeding bedsore on Madge's buttocks and 8cm purple pressure marks on both shoulders. Bed linen was soiled with urine and faeces and appeared unchanged for at least 1-2 days. Madge was in pain and distressed. I provided clean sheets, reassured her, and reported immediately to RN Sarah Jenkins."
        elif t == 57:
            if r == 1 and c == 0: f['value'] = "Alex Chen, Individual Support Worker, Phone: 0412 345 678"
            elif r == 1 and c == 1: f['value'] = "11/03/2026, 08:30 AM"
            elif r == 2: f['value'] = "Alex Chen"

    return fields

def populate_chcdis011(fields):
    for f in fields:
        if f['section'] == 'Assessor Section':
            continue
        if f.get('type') == 'checkbox':
            if f['table_idx'] in [87, 89, 113, 115] and f['col_idx'] == 2 and f['index_in_cell'] == 0:
                f['value'] = True
            continue
        t = f['table_idx']
        r = f['row_idx']
        c = f['col_idx']
        idx = f['index_in_cell']
        p = f.get('prompt', '').lower()

        # Table 2 & 3: NDIS Quality & Safeguarding Framework & Risk
        if t == 2:
            if r == 1: f['value'] = "Developmental: Building participant skills and community connections to help them stay safe and speak up for themselves."
            elif r == 2: f['value'] = "Preventive: Worker screening checks, NDIS Code of Conduct training, and clear service quality standards."
            elif r == 3: f['value'] = "Corrective: Handling complaints fairly, investigating incidents, and taking action when providers break rules."
            elif r == 4: f['value'] = "NDIS Practice Standards: Sets out the quality rules that providers must follow to protect human rights."
            elif r == 5: f['value'] = "NDIS Code of Conduct: The ethical rules and standards all disability support workers must follow."
            elif r == 6: f['value'] = "Positive Behaviour Support Capability Framework: Guides workers on how to support positive behaviour and reduce restrictive practices."
            elif r == 7: f['value'] = "NDIS Quality and Safeguards Commission"
            elif r == 8: f['value'] = "https://www.ndiscommission.gov.au"
            elif r == 9: f['value'] = "Protects the rights and safety of NDIS participants and handles complaints about service quality."
            elif r == 10: f['value'] = "Requires workers to immediately report serious reportable incidents (death, serious injury, abuse, neglect, unauthorized restrictive practices)."
        elif t == 3:
            f['value'] = "Involving participants in decisions, talking through risks and benefits in simple language, finding safe alternatives, and respecting their right to take reasonable risks."

        # Table 4 & 5: Social devaluation & Social Role Valorisation (SRV)
        elif t == 4:
            if r == 1: f['value'] = "Social devaluation happens when society looks down on people with disability or treats them as having less worth, which leads to being excluded or treated unfairly."
            elif r == 2: f['value'] = "Low expectations from others, losing independence, being left out of community activities, and loneliness."
            elif r == 3: f['value'] = "Support workers challenge devaluation by focusing on people's strengths, treating them with respect, and helping them join in community life."
            elif r == 4: f['value'] = "Helping people get jobs, volunteer, join clubs, and be visible and active in their neighbourhood."
        elif t == 5:
            f['value'] = "Social Role Valorisation (SRV) means helping people with disability take on valued roles in the community (like employee, student, volunteer, friend, club member) so they are respected and valued by others."

        # Table 6-8: Strengths-based practice
        elif t == 6:
            practices = {
                1: "Finding out what the participant is good at, what they enjoy doing, and building on those strengths.",
                2: "Listening to the participant as the main decision-maker in their own life and support plan.",
                3: "Helping the person learn new practical skills to grow their independence, rather than focusing on what they can't do.",
                4: "Supporting the person to make choices about their daily routines, hobbies, and activities."
            }
            if r in practices: f['value'] = practices[r]
        elif t == 7:
            f['value'] = "Strengths-based practice looks at what a person can do, their talents, and what they enjoy, instead of just seeing their medical diagnosis or limitations."
        elif t == 8:
            prin = [
                "Focus on abilities and talents rather than medical labels or deficits.",
                "The participant is the expert in their own life and knows what they want.",
                "Working as partners together to help the person build independence.",
                "Using local community groups and connections to support inclusion."
            ]
            f['value'] = prin[idx] if idx < len(prin) else prin[-1]

        # Table 9 & 10: Positive behaviour support & Active support
        elif t == 9:
            pbs = {
                1: "Positive Behaviour Support (PBS) is a person-centred way of helping someone when they show behaviours of concern by finding out why the behaviour happens (the trigger or unmet need), changing the environment, and teaching new skills rather than punishing them.",
                2: "Human rights-based approach: PBS respects the person's dignity and rights, aiming to eliminate the need for restrictive practices.",
                3: "Functional Behaviour Assessment (FBA): Finds out what triggers the behaviour and what the person is trying to communicate.",
                4: "Proactive strategies like setting a calm routine, changing the environment, and teaching positive ways to express feelings."
            }
            if r in pbs: f['value'] = pbs[r]
        elif t == 10:
            act = {
                1: "Person-Centred Active Support (PCAS) is a way of supporting people with disability to be involved in everyday tasks (like cooking, shopping, laundry) by breaking tasks into small steps and giving just enough help so they can do it themselves.",
                2: "Every moment has potential: Turning everyday tasks into fun opportunities to learn and join in.",
                3: "Little and often: Breaking activities into small steps so the person can participate throughout the day without getting tired.",
                4: "Graded assistance: Giving just the right amount of help (ask, prompt, show, guide) without taking over."
            }
            if r in act: f['value'] = act[r]

        # Tables 11-30: Task analysis, chaining, goals, AT
        elif t == 11:
            f['value'] = "Task analysis means breaking down a big task (like making a cup of tea or doing laundry) into small, step-by-step instructions so it is easier to teach and learn."
        elif t == 12:
            f['value'] = "Forward chaining teaches step 1 first and moves forward. Backward chaining has the worker do all the steps except the last one, so the client does the final step and feels success right away."
        elif t == 13:
            f['value'] = "Positive reinforcement means praising or rewarding a person right after they do a good job (like saying 'well done!' or high fives), which encourages them to do it again."
        elif t == 14:
            f['value'] = "SMART goals are Specific (clear), Measurable (can track progress), Achievable (realistic), Relevant (important to the person), and Time-bound (has a target date)."
        elif t == 15:
            f['value'] = "Communication tablets (AAC apps), picture boards (PECS), easy-grip kitchen utensils, and electric wheelchairs."
        elif t == 16:
            f['value'] = "Regular check-ins, tracking how many steps the client can do on their own, and updating support steps with the supervisor when needed."
        elif t == 17:
            f['value'] = "Doing a risk assessment to balance safety (duty of care) with letting the client try new things and make choices (dignity of risk)."
        elif t == 18:
            f['value'] = "Working together with allied health specialists (like Speech Pathologists and Occupational Therapists) to follow their advice and exercises."
        elif t == 19:
            discrim = {
                1: ("People depending on and supporting each other equally in the community.", "Helps the person build friendships, teamwork skills, and feel like an equal part of the community."),
                2: ("Unfair treatment directed at a person with disability by someone else due to bias.", "Hurts their self-confidence and makes them feel afraid or embarrassed to go out and try new things."),
                3: ("Rules, policies, or physical barriers that disadvantage people with disability.", "Stops people from getting jobs, learning at school, or using public transport.")
            }
            if r in discrim:
                f['value'] = discrim[r][0] if c == 1 else discrim[r][1]

        # Tables 20-70: Skills development plans, Erik & Sam case studies
        elif t in range(20, 71):
            if "participant" in p or "client" in p:
                f['value'] = "Erik (24 years old, ASD Level 2) / Sam (38 years old, acquired brain injury)"
            elif "goal" in p:
                f['value'] = "Develop independent travel skills to catch the public bus to community college three times weekly."
            elif "strength" in p:
                f['value'] = "Excellent memory for timetables, highly motivated, punctual, and possesses strong smartphone literacy."
            elif "barrier" in p:
                f['value'] = "Anxiety in crowded environments and difficulty managing unexpected bus delays."
            elif "strategy" in p or "support" in p:
                f['value'] = "Implement graded task analysis, practice journey routes during off-peak hours, provide visual cue cards, and roleplay asking driver for assistance."
            elif "review" in p or "monitoring" in p:
                f['value'] = "Weekly progress tracking in collaboration with supervisor, reviewing anxiety management techniques, and gradually fading worker physical presence."
            else:
                f['value'] = "Factual observation documented in skill progress notes, supervisor briefed, and positive reinforcement provided to the participant."

        # Tables 71-118: Workplace tasks, observations, evidence
        elif t in range(71, 119):
            if "signature" in p or "name" in p:
                f['value'] = CANDIDATE_DETAILS["candidate_name"]
            elif "date" in p:
                f['value'] = CANDIDATE_DETAILS["date"]
            elif "supervisor" in p:
                f['value'] = "Sarah Jenkins (Registered Nurse / Workplace Supervisor)"
            elif "feedback" in p:
                f['value'] = "Participant successfully completed 4 of 5 steps independently; showed high enthusiasm; continues to develop self-confidence in public settings."
            else:
                f['value'] = "Conducted skill development session using Person-Centred Active Support; adhered strictly to WHS and privacy guidelines; documented outcomes accurately."

    return fields

def populate_chcdis012(fields):
    for f in fields:
        if f['section'] == 'Assessor Section' or f.get('type') != 'text':
            continue
        t = f['table_idx']
        r = f['row_idx']
        c = f['col_idx']
        idx = f['index_in_cell']
        p = f.get('prompt', '').lower()

        # Table 3 & 4: CRPD & Responsibilities
        if t == 3:
            if r == 1: f['value'] = "Article 19 - Living independently and being included in the community: People have the right to choose where and with whom they live, and be included in community life."
            elif r == 2: f['value'] = "Article 27 - Work and employment: People with disability have the right to work on an equal basis with others in open, fair workplaces."
            elif r == 3: f['value'] = "Article 30 - Joining in cultural life, recreation, and sports: Equal access to community sports, entertainment, and hobbies."
            elif r == 4: f['value'] = "Treats people with disability with dignity, respects their choices, and makes sure they aren't left out."
        elif t == 4:
            if r == 3:
                f['value'] = "Telling workers what food, routines, and support they prefer." if c == 0 else "Helps workers give personalised support based on what the client actually wants."
            elif r == 4:
                f['value'] = "Treating staff, other participants, and the public with respect." if c == 0 else "Keeps everyone safe and creates a friendly, welcoming environment."

        # Table 5 & 6: Strengths-based & Person-centred principles
        elif t == 5:
            if r == 3:
                f['value'] = "Focusing on what the person is good at instead of their limitations." if c == 0 else "Boosts confidence and encourages them to try new community activities."
            elif r == 4:
                f['value'] = "Working together with the participant as a partner in their care." if c == 0 else "Makes sure goals are what the person truly wants."
        elif t == 6:
            if r == 3:
                f['value'] = "Respecting the person's right to make their own choices in daily life." if c == 0 else "Lets the person choose their own hobbies, groups, and friends."
            elif r == 4:
                f['value'] = "Looking at the whole person including emotional, physical, and cultural needs." if c == 0 else "Makes sure activities fit well with the person's lifestyle and wellbeing."

        # Table 8-10: Human rights & Community inclusion
        elif t == 8:
            if r == 1:
                f['value'] = "Dignity and personal choice: Respecting the person's freedom to decide for themselves." if c == 0 else "Ensures community activities match the person's real interests."
            elif r == 2:
                f['value'] = "Equal opportunity and fairness: Equal access to public services and facilities." if c == 0 else "Helps stop stigma and opens up community places for everyone."
        elif t == 9:
            if r == 3:
                f['value'] = "Universal accessibility: Making sure buildings, transport, and info are easy to access." if c == 0 else "Lets people with mobility, sensory, or learning needs join in independently."
            elif r == 4:
                f['value'] = "Real community belonging: Being an active member of mainstream community groups." if c == 0 else "Builds genuine friendships and stops feelings of loneliness."
        elif t == 10:
            f['value'] = "Partnering with local sports clubs and art centres, and doing travel training to get there." if r == 2 else "Connecting with community buddy programs and supported volunteering."

        # Table 11 & 12: Social & emotional wellbeing
        elif t == 11:
            if r == 2: f['value'] = "a state of complete physical, mental and social well-being and not merely the absence of disease or infirmity."
            elif r == 3: f['value'] = "Having good friends, feeling like you belong, doing meaningful activities, and having choices in your life."
        elif t == 12:
            negs = {
                0: "Chronic loneliness, feeling down, and losing self-esteem.",
                1: "Feeling judged, unwelcome, or embarrassed to go out in public due to negative attitudes.",
                2: "Not being able to visit friends, work, or attend activities due to lack of accessible transport.",
                3: "Missing out on social activities and fun outings because of cost or lack of money.",
                4: "Feeling frustrated, stuck, and excluded when buildings have steps and no ramps or accessible toilets."
            }
            f['value'] = negs[idx] if idx < len(negs) else negs[0]

        # Table 13-16: Strategies, Networks, Services
        elif t == 13:
            if r == 4:
                f['value'] = "Helping the person join local hobby clubs (like a pottery class or choir)." if c == 0 else "Lets them meet people with the same interests and build natural friendships."
            elif r == 5:
                f['value'] = "Doing bus and train travel training so they can get around independently." if c == 0 else "Gives the person freedom to travel without always relying on support workers."
        elif t == 14:
            if r == 2:
                f['value'] = "Local disability sports clubs (like Wheelchair Sports NSW)." if c == 0 else "Offers fun accessible sports, exercise, and great team friendships."
            elif r == 3:
                f['value'] = "Neighbourhood community centre activity groups." if c == 0 else "Offers weekly social gatherings, art classes, computing, and social events."
        elif t == 15:
            if r == 2:
                f['value'] = "NDIS Local Area Coordinator (LAC)." if c == 0 else "Helps link participants with local community programs, groups, and funded supports."
            elif r == 3:
                f['value'] = "Community transport services." if c == 0 else "Provides accessible door-to-door transport for people who cannot use standard buses or trains."

        # Table 17-23: Active citizenship, adjustments
        elif t == 17:
            strat = ["Community awareness talks", "Advocating for better access", "Accessibility checks of local venues", "Joining local council access committees"]
            f['value'] = strat[idx] if idx < len(strat) else strat[-1]
        elif t == 18:
            sport_vals = [
                "Wheelchair basketball / boccia clubs", "Fun physical exercise, teamwork, and making good friends.",
                "Community walking groups", "Gentle exercise outdoors in the fresh air and chatting with others.",
                "Local Men's Shed / woodwork club", "Building practical skills, working on projects, and making mates.",
                "Community garden groups", "Growing plants, fresh air, and enjoying teamwork in the garden.",
                "Library book clubs", "Reading interesting books and sharing thoughts with other members.",
                "Amateur theatre and drama workshops", "Building self-confidence, having fun, and acting."
            ]
            f['value'] = sport_vals[idx] if idx < len(sport_vals) else sport_vals[-1]
        elif t == 19:
            f['value'] = "Active citizenship means everyone has the right and opportunity to take part in community life, share their views, and have a say in society." if r == 2 else "It lets people with disability vote, attend local council meetings, and speak up about issues that matter to them."
        elif t == 20:
            if r == 3:
                f['value'] = "Helping the person attend local council forums and community meetings." if c == 0 else "Makes sure their voice and real-life experiences help shape local community decisions."
            elif r == 4:
                f['value'] = "Helping the person register to vote with the Australian Electoral Commission and practice voting." if c == 0 else "Protects their democratic right to have their vote counted just like everyone else."
        elif t == 21:
            if r == 3:
                f['value'] = "Connecting with independent disability advocacy groups (like PWDA)." if c == 0 else "Gives the person support to resolve housing, funding, or service problems."
            elif r == 4:
                f['value'] = "Running self-advocacy practice sessions on speaking up and asking for help." if c == 0 else "Builds confidence to speak up during doctor visits and care planning meetings."
        elif t == 22:
            if r == 3:
                f['value'] = "Giving info in Easy Read, large print, or screen-reader formats." if c == 0 else "Makes sure the person can read and understand documents on their own."
            elif r == 4:
                f['value'] = "Helping the person prepare questions and goals before meetings." if c == 0 else "Ensures the meeting focuses on what is most important to the person."
        elif t == 23:
            if r == 3:
                f['value'] = "Adding wheelchair ramps, wide automatic doors, and height-adjustable desks." if c == 0 else "Removes physical barriers so people can move around the building easily."
            elif r == 4:
                f['value'] = "Offering flexible times and quiet break rooms in community centres." if c == 0 else "Helps clients manage fatigue or sensory overload comfortably."

        # Tables 24-33: Assistive Technology across domains
        elif t in range(24, 34):
            at_dict = {
                24: ("Dressing stick and button hook", "Helps the person do up buttons and pull on clothes independently.", "Long-handled reacher", "Lets the person pick things up off the floor without bending or losing balance."),
                25: ("Swivel shower chair with backrest", "Lets the person sit down safely while showering, preventing slips and falls.", "Long-handled sponge", "Lets the person wash their back and legs without straining."),
                26: ("Slide transfer board", "Helps transfer smoothly between wheelchair and bed without standing up.", "Mobile hoist with sling", "Lifts non-weight-bearing clients safely between bed and chair without hurting the worker's back."),
                27: ("Screen-reading software (like NVDA)", "Reads out text on the computer screen for people with vision loss.", "Handheld digital magnifier", "Enlarges small text on restaurant menus, bus timetables, and books."),
                28: ("All-terrain electric wheelchair", "Lets the person travel over grass, gravel, and park paths for outdoor outings.", "Adaptive bowling ramp", "Helps people with limited arm strength roll bowling balls."),
                29: ("Ergonomic mouse and split keyboard", "Stops hand and wrist fatigue during office work.", "Voice typing software", "Allows writing emails and documents by speaking instead of typing."),
                30: ("Weighted cutlery with thick rubber handles", "Steadies shaking hands so food doesn't spill while eating.", "Scoop plate with high curved rim", "Makes it easy to push food onto a spoon or fork with one hand."),
                31: ("Alternating air mattress", "Shifts pressure across the body to stop painful pressure sores from forming in bed.", "Roho air cushion for wheelchair", "Protects the client's bottom and hips from sores when sitting for hours."),
                32: ("Automatic pill dispenser with timer", "Beeps and opens at the right time so pills aren't missed or mixed up.", "Voice-activated smart lighting", "Lets someone with limited mobility turn lights and heating on or off by voice."),
                33: ("Smartphone bus transit app with voice directions", "Speaks directions so the person knows when their bus stop is coming up.", "Vibrating digital watch with reminders", "Gives discreet vibration reminders for appointments and medication.")
            }
            if t in at_dict:
                vals = at_dict[t]
                f['value'] = vals[idx] if idx < len(vals) else vals[-1]

        # Tables 35-39: Barriers (Physical, Skill, Structural, Psychological, Discrimination, Resources)
        elif t in [35, 36, 37]:
            barrier_responses = {
                35: [
                    "Entrance steps without an accompanying access ramp.", "Prevents wheelchair users from entering venue.", "Creates feelings of exclusion and second-class citizenship.",
                    "Lack of money management and public transit navigation skills.", "Restricts ability to travel independently to activities.", "Limits personal autonomy and forces reliance on carers."
                ],
                36: [
                    "Inadequate scheduled weekend accessible public transport routes.", "Prevents attending social gatherings after standard business hours.", "Isolates individuals within residential facilities on weekends.",
                    "Severe social anxiety and fear of negative public judgment.", "Causes withdrawal and reluctance to leave home.", "Erodes self-confidence and prevents forming new peer relationships."
                ],
                37: [
                    "Community venue refusing entry to a person with an assistance animal.", "Directly blocks participation in public events and services.", "Reinforces social stigma and causes intense emotional humiliation.",
                    "Lack of personal financial funds for venue admission fees and equipment.", "Prevents participation in paid community activities (gyms, cinemas).", "Creates economic segregation from mainstream leisure pursuits."
                ]
            }
            if t in barrier_responses:
                blist = barrier_responses[t]
                f['value'] = blist[idx] if idx < len(blist) else blist[-1]

        elif t in [38, 39]:
            if t == 38:
                roles = [
                    "Provides vital insight into participant routines and comforting communication cues.", "Worker consults carer to understand sensory triggers and favorite leisure interests.",
                    "Offers long-term natural emotional support and social continuity.", "Worker keeps family informed of community outings and celebrates participant milestones."
                ]
                f['value'] = roles[idx] if idx < len(roles) else roles[-1]
            elif t == 39:
                roles2 = [
                    "Support worker / Key worker", "Facilitates travel, assists with mobility, and implements active support during outings.",
                    "Allied Health Professional (Occupational Therapist)", "Prescribes adaptive equipment and advises on environmental modifications."
                ]
                f['value'] = roles2[idx] if idx < len(roles2) else roles2[-1]

        # Tables 42-66: Case study tasks (Person A & Person B)
        elif t in range(42, 68):
            if "person with disability a" in p:
                f['value'] = "Person A (James, 28 years old, cerebral palsy, passionate about community radio and swimming)"
            elif "person with disability b" in p:
                f['value'] = "Person B (Maria, 45 years old, mild intellectual disability, interested in cooking and botanical gardening)"
            elif "network" in p or "service" in p:
                f['value'] = "Local community center arts group, YMCA accessible hydrotherapy pool, and volunteer radio station."
            elif "feedback" in p:
                f['value'] = "Participant expressed high satisfaction with swimming sessions; felt energized and welcomed by instructors; requested to increase attendance to twice weekly."
            elif "barrier" in p:
                f['value'] = "Heavy manual entrance doors at pool; worker arranged with facility management for automatic sensor button installation."
            elif "minutes" in p or "meeting" in p:
                f['value'] = "Support planning review meeting held on 15/09/2026 with participant, support worker Alex Chen, and supervisor Sarah Jenkins. Agreed to maintain weekly community radio volunteering."
            else:
                f['value'] = "Support provided using person-centred active support principles; participant goals reviewed and updated in the individualised plan."

    return fields

def process_all_benchmarks():
    configs = [
        ("answers_CHCLEG001.yaml", populate_chcleg001),
        ("answers_HLTWHS002.yaml", populate_hltwhs002),
        ("answers_CHCAGE011.yaml", populate_chcage011),
        ("answers_CHCDIS011.yaml", populate_chcdis011),
        ("answers_CHCDIS012.yaml", populate_chcdis012),
    ]

    for yml_path, pop_func in configs:
        with open(yml_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            
        data['fields'] = pop_func(data['fields'])
        
        # Check remaining empties
        empty_cand = [f for f in data['fields'] if f['section'] != 'Assessor Section' and f['type'] == 'text' and not str(f.get('value', '')).strip()]
        
        with open(yml_path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, sort_keys=False, allow_unicode=True, width=1000)
            
        print(f"{yml_path}: empty candidate text fields = {len(empty_cand)}")

if __name__ == "__main__":
    process_all_benchmarks()
