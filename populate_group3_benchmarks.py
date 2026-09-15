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
            if r == 1: f['value'] = "Working with Children Check (WWCC) clearance and verification of ongoing clearance status."
            elif r == 2: f['value'] = "Mandatory reporting of suspected risk of significant harm under Section 27 of the Children and Young Persons (Care and Protection) Act 1998 (NSW)."
            elif r == 3: f['value'] = "Supervising children at all times and ensuring child-safe environment policies are enforced."
            elif r == 4: f['value'] = "Criminal penalties, fines up to $11,000 for employers/workers, immediate termination, and prohibition from child-related work."
            elif r == 5: f['value'] = "NSW Office of the Children's Guardian"
            elif r == 6: f['value'] = "https://www.ocg.nsw.gov.au"
            elif r == 7: f['value'] = "NSW Child Safe Standards"
            elif r == 8: f['value'] = "Requires organizations to implement leadership, governance, and culture promoting child safety and preventing abuse."

        # Table 8: Ethical considerations - children in workplace
        elif t == 8:
            if r == 1: f['value'] = "Prioritizing the best interests of the child and upholding zero tolerance for emotional, physical, or neglectful abuse."
            elif r == 2: f['value'] = "Ensuring child confidentiality while balancing child protection disclosure duties."
            elif r == 3: f['value'] = "Treating all children with dignity, respect, and fairness regardless of background."
            elif r == 4: f['value'] = "Formal disciplinary action, professional deregistration, and workplace dismissal."

        # Table 10: National Code of Conduct for Health Care Workers
        elif t == 10:
            if r == 1: f['value'] = "National Code of Conduct for Health Care Workers (NSW Health Care Complaints Act 1993)."
            elif r == 2: f['value'] = "Provide services in a safe and ethical manner, respecting client autonomy and privacy."
            elif r == 3: f['value'] = "Prohibition of sexual or financial relationships between workers and clients."
            elif r == 4: f['value'] = "Prohibition order by the Health Care Complaints Commission (HCCC), public warning, and employment termination."
            elif r == 5: f['value'] = "Health Care Complaints Commission (HCCC) NSW"
            elif r == 6: f['value'] = "https://www.hccc.nsw.gov.au"
            elif r == 7: f['value'] = "Australian Charter of Healthcare Rights"
            elif r == 8: f['value'] = "Guarantees access, safety, respect, partnership, information, privacy, and feedback for all care recipients."

        # Table 12: First aid in the workplace
        elif t == 12:
            if r == 1: f['value'] = "First Aid in the Workplace Code of Practice (SafeWork NSW)"
            elif r == 2: f['value'] = "Providing accessible, fully stocked first aid kits tailored to workplace hazards."
            elif r == 3: f['value'] = "Maintaining trained first aiders with current HLTAID011 certification on duty."
            elif r == 4: f['value'] = "Breach of WHS Act duty of care, regulatory improvement notices, and monetary fines."
            elif r == 5: f['value'] = "SafeWork NSW"

        # Table 14: Managing noise in the workplace
        elif t == 14:
            if r == 1: f['value'] = "Managing Noise and Preventing Hearing Loss at Work Code of Practice (SafeWork NSW)"
            elif r == 2: f['value'] = "Ensuring occupational noise exposure does not exceed 85 dB(A) over an 8-hour shift."
            elif r == 3: f['value'] = "Implementing acoustic engineering controls and providing appropriate hearing PPE."
            elif r == 4: f['value'] = "Irreversible noise-induced hearing loss, SafeWork NSW prohibition notices, and worker compensation claims."
            elif r == 5: f['value'] = "SafeWork NSW"

        # Table 16 & 17: Complaints handling
        elif t == 16:
            if r == 1: f['value'] = "AS/NZS 10002:2014 Guidelines for complaint management in organizations"
            elif r == 2: f['value'] = "Acknowledging complaints within 24–48 hours and resolving them without victimisation."
            elif r == 3: f['value'] = "Documenting and investigating grievances transparently and fairly."
            elif r == 4: f['value'] = "Escalation to the Aged Care Quality and Safety Commission or NDIS Quality and Safeguards Commission."
            elif r == 5: f['value'] = "Australian Human Rights Commission / ACQSC"
        elif t == 17:
            if r == 1: f['value'] = "Confidentiality: Protecting the identity of complainants and details of the grievance."
            elif r == 2: f['value'] = "Procedural fairness: Giving all involved parties the opportunity to respond."
            elif r == 3: f['value'] = "Loss of client trust, internal organizational conflict, and staff grievances."
            elif r == 4: f['value'] = "Disciplinary action for breach of confidentiality and professional conduct policy."

        # Table 18 & 19: Mandatory CPD
        elif t == 18:
            if r == 1: f['value'] = "Ongoing training ensures workers maintain up-to-date evidence-based clinical skills and comply with sector standards."
            elif r == 2: f['value'] = "Minimum 20 hours of validated continuing professional development per registration year."
            elif r == 3: f['value'] = "Inability to re-register, suspension from practice, and non-compliance findings during audits."
            elif r == 4: f['value'] = "Aged Care Quality and Safety Commission / AHPRA"
            elif r == 5:
                cpds = [
                    "Attending accredited seminars on dementia care and infection control.",
                    "Completing workplace e-learning modules on positive behaviour support and mandatory reporting.",
                    "Participating in peer practice review workshops and clinical skill simulations."
                ]
                f['value'] = cpds[idx] if idx < len(cpds) else cpds[-1]
            elif r == 6:
                f['value'] = "Inability to renew annual professional registration, mandatory supervision requirements, formal disciplinary review, and potential suspension from client-facing care duties."
        elif t == 19:
            f['value'] = "Undertake annual CPR updates, infection control refreshers, medication administration competencies, and dementia care seminars."

        # Table 21-35: Duty of care, dignity of risk, negligence, privacy, human rights
        elif t == 21:
            f['value'] = "Duty of care is the legal and moral obligation of care workers to take reasonable care to avoid causing foreseeable harm or injury to clients."
        elif t == 23:
            f['value'] = "Dignity of risk recognizes a client's fundamental right to make choices and take calculated risks to achieve personal growth and independence."
        elif t == 24:
            if r == 1: f['value'] = "Aged Care Act 1997 / Quality of Care Principles 2014 (Aged Care Quality Standard 1)"
            elif r == 2: f['value'] = "https://www.legislation.gov.au/Details/F2018L01519"
            elif r == 3: f['value'] = "Consumer dignity and choice: Upholds the consumer's right to exercise choice and make decisions about their care, including taking calculated risks."
            elif r == 4: f['value'] = "Standard 1 (3)(a) and (d)"
            elif r == 6: f['value'] = "Workers must balance duty of care with client autonomy, conducting risk assessments collaboratively rather than imposing blanket restrictions."
            elif r == 7: f['value'] = "Unreasonable denial of client autonomy, breach of Aged Care Quality Standards, and sanctions against the provider."
        elif t == 25:
            f['value'] = "Negligence occurs when a worker breaches their duty of care through act or omission, causing actual, foreseeable harm or loss to the client."
        elif t == 27:
            f['value'] = "Informed consent requires providing comprehensive, understandable information regarding benefits, risks, and alternatives before obtaining voluntary agreement."
        elif t == 29:
            f['value'] = "Privacy Act 1988 (Cth) and Australian Privacy Principles (APPs); Health Records and Information Privacy Act 2002 (NSW)."
        elif t == 30:
            if r == 1: f['value'] = "Article 1 and Article 5 of the Universal Declaration of Human Rights"
            elif r == 2: f['value'] = "All human beings are born free and equal in dignity and rights; no one shall be subjected to torture or to cruel, inhuman or degrading treatment."
            elif r == 4: f['value'] = "Workers must treat every client with profound respect, avoid degrading or humiliating practices, and ensure zero tolerance for mistreatment."
            elif r == 5: f['value'] = "Breach of professional code of ethics, immediate termination of employment, and potential human rights commission investigation."
        elif t == 31:
            f['value'] = "Mandatory reporting requires workers to report suspected physical abuse, sexual abuse, severe neglect, or financial exploitation to supervisors and statutory bodies."
        elif t == 33:
            f['value'] = "Anti-Discrimination Act 1977 (NSW) and Disability Discrimination Act 1992 (Cth) prohibit direct and indirect discrimination in community services."
        elif t == 35:
            f['value'] = "Freedom of association, freedom of speech, right to personal autonomy, and protection against degrading treatment."
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
            f['value'] = "Beneficence (acting in the client's best interest), Non-maleficence (doing no harm), Autonomy (respecting self-determination), and Justice (fairness)."
        elif t == 38:
            if c == 1:
                if r == 2: f['value'] = "Mandatory Reporting of Child Abuse (Children and Young Persons Care and Protection Act 1998 NSW)"
                elif r == 4: f['value'] = "Workers must notify the Child Protection Helpline immediately if they suspect child is at risk of significant harm."
                elif r == 5: f['value'] = "Criminal penalties, fines, professional deregistration, and workplace dismissal."
            elif c == 2:
                if r == 2: f['value'] = "Privacy and Confidentiality (Privacy Act 1988 Cth / APPs)"
                elif r == 4: f['value'] = "Workers must handle personal and sensitive client information securely and only disclose with consent or under law."
                elif r == 5: f['value'] = "Disciplinary action, investigation by the Office of the Australian Information Commissioner (OAIC), and civil damages."
        elif t == 39:
            f['value'] = "An ethical dilemma arises when a worker faces two competing ethical principles, such as client autonomy versus protecting them from potential harm."
        elif t == 41:
            f['value'] = "Consult organizational policies, discuss with the clinical supervisor, engage the multidisciplinary team, and explore supported decision-making options."
        elif t == 43:
            f['value'] = "Whistleblowing involves reporting illegal, fraudulent, or hazardous workplace practices to appropriate authorities when internal channels fail."
        elif t == 44:
            if r == 1: f['value'] = "NDIS Practice Standards (Quality Indicators) - Person-Centred Supports"
            elif r == 2: f['value'] = "https://www.ndiscommission.gov.au/providers/provider-obligations/ndis-practice-standards"
            elif r == 3: f['value'] = "Each participant accesses supports that respect and protect their dignity and right to freedom of expression."
            elif r == 4: f['value'] = "Core Module 1: Rights and Responsibilities"
            elif r == 6: f['value'] = "Support workers must actively involve participants in decisions and deliver care that honors individual cultural, spiritual, and personal values."
            elif r == 7: f['value'] = "Non-compliance notice by the NDIS Commission, loss of approved provider status, and worker retraining."
        elif t == 45:
            f['value'] = "Public Interest Disclosures Act 2022 (NSW) protects workers from detrimental reprisal or workplace bullying when reporting serious wrongdoing."
        elif t == 47:
            f['value'] = "Maintain professional boundaries by declining personal gifts, avoiding dual relationships, and never sharing personal financial details."
        elif t == 49:
            f['value'] = "Advocacy represents and defends the client's rights, choices, and interests, ensuring their voice is heard in all care decisions."
        elif t == 51:
            f['value'] = "Independent advocacy, family advocacy, self-advocacy, and legal/systemic advocacy."
        elif t == 52:
            if r == 2: f['value'] = "ISO 15489-1:2016 Information and documentation - Records management"
            elif r == 3: f['value'] = "Records must be retained for the minimum statutory periods prescribed by law (e.g. 7 years for financial/health records, or until age 25 for paediatric records)."
            elif r == 5: f['value'] = "Workers must record accurate, contemporaneous clinical notes and file them promptly in authorized secure storage systems."
            elif r == 6: f['value'] = "Inability to defend against malpractice claims, privacy breaches, regulatory fines, and organizational compliance sanctions."
        elif t == 53:
            f['value'] = "Access and equity ensures that all individuals have fair and equal opportunity to access health and community services regardless of background."
        elif t == 54:
            roles_levels = {
                3: ("Perform basic routine domestic and kitchen assistance under direct supervision.", "Cannot administer medications or perform complex clinical transfers."),
                4: ("Deliver personal care (showering, dressing) following established care plans under routine supervision.", "Cannot alter care plan goals or assess complex wound care."),
                5: ("Coordinate daily work rosters, supervise junior support staff, and administer prescribed oral medications.", "Cannot conduct comprehensive clinical assessments reserved for Registered Nurses."),
                6: ("Oversee team performance, manage service budgets, liaise with allied health specialists, and conduct staff appraisals.", "Cannot make medical diagnoses or prescribe pharmaceutical regimens.")
            }
            if r in roles_levels:
                f['value'] = roles_levels[r][0] if c == 2 else roles_levels[r][1]
        elif t == 55:
            f['value'] = "Eliminate language barriers by using TIS National interpreters, providing wheelchair-accessible facilities, and delivering culturally safe care."
        elif t == 56:
            if r == 2:
                b_practices = [
                    "Never accept personal money, loans, or expensive gifts from clients or their families.",
                    "Avoid sharing personal phone numbers, home addresses, or social media profiles with clients.",
                    "Limit care activities strictly to the documented support plan and shift hours."
                ]
                f['value'] = b_practices[idx] if idx < len(b_practices) else b_practices[-1]
            elif r == 3:
                f['value'] = "Development of client dependency, loss of objectivity, conflict of interest, emotional exploitation, and professional dismissal."

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
            f['value'] = "Work Health and Safety Act 2011 (NSW)" if r == 1 else "Provides a balanced and nationally consistent framework to secure the health and safety of workers and workplaces in NSW."
        
        # Table 5: WHS Regulations (NSW)
        elif t == 5:
            if r == 1: f['value'] = "Work Health and Safety Regulation 2017 (NSW)"
            elif r == 2: f['value'] = "Specifies practical legal requirements for managing hazardous manual tasks, hazardous chemicals, infection control, and emergency plans."
            elif r == 3: f['value'] = "Part 4.2 - Hazardous Manual Tasks"
            elif r == 4: f['value'] = "Mandates duty to identify, manage, and control risks associated with musculoskeletal disorders."
            elif r == 5: f['value'] = "Part 3.2 - General Working Environment (First aid, emergency plans, and PPE)"
            elif r == 6: f['value'] = "Requires duty-holders to provide first aid facilities, emergency evacuation procedures, and suitable PPE."
            elif r == 7: f['value'] = "SafeWork NSW"
            elif r == 8: f['value'] = "be approved by the relevant Minister and published in the NSW Government Gazette."
            elif r == 10: f['value'] = "False. Approved codes of practice are not law themselves, but they are admissible in court proceedings as evidence of whether or not a duty or obligation under the WHS Act has been complied with."

        # Table 6: Codes of practice
        elif t == 6:
            if r == 1: f['value'] = "Hazardous Manual Tasks Code of Practice (SafeWork NSW)"
            elif r == 2: f['value'] = "https://www.safework.nsw.gov.au/resource-library/list-of-all-codes-of-practice/hazardous-manual-tasks"
            elif r == 3: f['value'] = "Provides practical guidance to identify postures, movements, and forces that produce musculoskeletal strain and implement mechanical controls."
            elif r == 4: f['value'] = "Managing the Risk of Falls at Workplaces Code of Practice"
            elif r == 5: f['value'] = "https://www.safework.nsw.gov.au/resource-library/list-of-all-codes-of-practice/managing-the-risk-of-falls-at-workplaces"
            elif r == 6: f['value'] = "Outlines risk management for slips, trips, and falls during client mobility transfers and wet area maintenance."
            elif r == 7: f['value'] = "How to Manage Work Health and Safety Risks Code of Practice"
            elif r == 8: f['value'] = "https://www.safework.nsw.gov.au/resource-library/list-of-all-codes-of-practice/how-to-manage-work-health-and-safety-risks"
            elif r == 9: f['value'] = "Sets out the four-step risk management process: identify hazards, assess risks, control risks, and review control measures."

        # Table 7: Industry standards
        elif t == 7:
            if r == 1: f['value'] = "Industry standards are established guidelines and technical specifications developed by standards bodies (e.g. Standards Australia) detailing best practices for equipment, safety, and service quality."
            elif r == 2: f['value'] = "AS/NZS ISO 45001:2018 Occupational health and safety management systems."
            elif r == 3: f['value'] = "Provides organizations with a structured framework to improve employee safety, reduce workplace risks, and create safer working environments."

        # Table 8: WHS Authorities
        elif t == 8:
            if r == 1: f['value'] = "SafeWork NSW"
            elif r == 2: f['value'] = "Inspects workplaces, issues improvement and prohibition notices, investigates serious workplace incidents, and enforces WHS laws in NSW."
            elif r == 3: f['value'] = "Health and Safety Representative (HSR) and Workplace Health and Safety Committee."
            elif r == 4: f['value'] = "Facilitates consultation between workers and management, conducts hazard inspections, and assists in incident reviews."
            elif r == 5: f['value'] = "Right to cease unsafe work and right to be consulted on matters affecting workplace safety."

        # Table 9 & 10: Rights and responsibilities
        elif t == 9:
            if r == 1: f['value'] = "Primary duty of care (Section 19): Ensure, so far as is reasonably practicable, the health and safety of workers and other persons in the workplace."
            elif r == 2: f['value'] = "Provide and maintain safe plant, structures, safe systems of work, and adequate facilities for worker welfare."
            elif r == 3: f['value'] = "Provide necessary information, training, instruction, and supervision to protect workers from risks."
            elif r == 4: f['value'] = "Section 28 Worker Duties: Take reasonable care for own health and safety and ensure actions do not adversely affect others."
            elif r == 5: f['value'] = "Comply with any reasonable instruction and cooperate with reasonable WHS policies and procedures."
            elif r == 6: f['value'] = "Report hazards, injuries, and unsafe work practices immediately to the workplace supervisor."
            elif r == 8: f['value'] = "Section 28 of the Work Health and Safety Act 2011 (NSW)."
        elif t == 10:
            if r == 1: f['value'] = "Right to a safe and healthy workplace with effective risk controls in place."
            elif r == 2: f['value'] = "Right to cease work or refuse to carry out work if there is a reasonable concern of serious imminent risk to health or safety."
            elif r == 3: f['value'] = "Right to elect Health and Safety Representatives and be represented in safety consultation."
            elif r == 4: f['value'] = "Right to access adequate first aid, personal protective equipment, and WHS training free of charge."
            elif r == 5: f['value'] = "Responsibility to wear and maintain required PPE properly in accordance with manufacturer instructions."
            elif r == 6: f['value'] = "Responsibility not to intentionally or recklessly interfere with or misuse safety equipment."
            elif r == 7: f['value'] = "Responsibility to actively participate in workplace health and safety consultation and debriefing sessions."
            elif r == 8: f['value'] = "Responsibility to follow infection prevention protocols and manual handling guidelines."

        # Table 11: Officers duties
        elif t == 11:
            officer_vals = [
                "Acquire and maintain up-to-date knowledge of work health and safety matters.",
                "Gain an understanding of the nature of operations and hazards and risks associated with work.",
                "Ensure the PCBU has and uses appropriate resources and processes to eliminate or minimize risks.",
                "Ensure the PCBU has appropriate processes for receiving and considering information regarding incidents and hazards.",
                "Ensure the PCBU implements processes for complying with any duty or obligation under the WHS Act.",
                "Verify the provision and use of resources and processes through routine audits and executive safety reviews."
            ]
            f['value'] = officer_vals[idx] if idx < len(officer_vals) else officer_vals[-1]

        # Tables 12-25: Hazards, Risk assessment, Manual tasks, Emergencies
        elif t == 12:
            f['value'] = "Hazard is a situation or thing with potential to cause harm; Risk is the likelihood and consequence that harm will occur from exposure to the hazard."
        elif t == 13:
            vals = ["Elimination", "Substitution", "Isolation", "Engineering controls", "Administrative controls", "Personal Protective Equipment (PPE)"]
            f['value'] = vals[idx] if idx < len(vals) else vals[-1]
        elif t == 14:
            f['value'] = "Identify hazards, assess the risk level (likelihood x consequence), implement control measures following the hierarchy of controls, and review controls regularly."
        elif t == 15:
            f['value'] = "Musculoskeletal disorders (MSD) caused by repetitive bending, twisting, lifting heavy clients without mechanical aids, or pushing wheelchairs over rough ground."
        elif t == 16:
            f['value'] = "Use electric client hoists, slide sheets, height-adjustable beds, and ensure two care workers are present for bariatric or complex transfers."
        elif t == 17:
            f['value'] = "Perform a preliminary dynamic risk assessment, clear obstacles, check client mobility plan, adjust bed height, lock wheels, and communicate each step."
        elif t == 18:
            f['value'] = "R - Remove people in immediate danger; A - Alert emergency services (000) and sound alarm; C - Contain smoke and fire by closing doors; E - Evacuate to designated assembly area."
        elif t == 19:
            f['value'] = "Check DRSABCD: Danger, Response, Send for help (000), Airway, Breathing, CPR (30 compressions : 2 breaths), Defibrillation (AED)."
        elif t == 20:
            f['value'] = "Blood-borne viruses (HBV, HCV, HIV), respiratory pathogens (COVID-19, Influenza), and enteric pathogens (Norovirus)."
        elif t == 21:
            f['value'] = "Hand hygiene before and after client contact, correct PPE usage, safe sharps handling, prompt spill clean-up, and routine environmental disinfection."
        elif t == 22:
            f['value'] = "A notifiable incident under WHS Act Section 38 involves death of a person, serious injury/illness requiring immediate hospital treatment, or a dangerous incident (e.g. fire/gas leak)."
        elif t == 23:
            f['value'] = "Notify SafeWork NSW immediately via telephone (13 10 50) and follow up with written notice within 48 hours; preserve incident site."
        elif t == 24:
            f['value'] = "Complete the organizational Incident/Accident Report Form, document factual objective observations, record vital signs and first aid given, and notify the RN."
        elif t == 25:
            f['value'] = "Workplace debriefings provide emotional support to workers, reduce psychological distress/trauma, identify root causes, and prevent recurrence."
        elif t == 26:
            if r == 2: f['value'] = "Illnesses caused by pathogenic microorganisms (bacteria, viruses, fungi, parasites) that can be transmitted directly or indirectly from one person to another or from environmental vectors."
            elif r == 3:
                sources = [
                    "Contaminated household surfaces and high-touch areas (door handles, bathroom taps, bedside tables).",
                    "Client bodily fluids and soiled personal laundry or linen.",
                    "Improperly stored or prepared food and domestic pets/pest vectors."
                ]
                f['value'] = sources[idx] if idx < len(sources) else sources[-1]
            elif r == 4:
                minims = [
                    "Performing strict hand hygiene using soap and water or alcohol-based hand rub.",
                    "Wearing appropriate personal protective equipment (gloves, aprons, masks) when exposed to fluids.",
                    "Cleaning and disinfecting touch points with hospital-grade disinfectant and bagging soiled linen immediately."
                ]
                f['value'] = minims[idx] if idx < len(minims) else minims[-1]
        elif t == 27:
            if r == 2: f['value'] = "The complex bodily system comprising bones, joints, muscles, tendons, ligaments, and cartilage that provides form, support, stability, and movement to the body."
            elif r == 3:
                msds = [
                    "Lumbar spinal disc herniation or acute low back muscle strain.",
                    "Carpal tunnel syndrome or repetitive wrist tendonitis.",
                    "Rotator cuff tendinopathy or shoulder impingement syndrome."
                ]
                f['value'] = msds[idx] if idx < len(msds) else msds[-1]
        elif t == 28:
            if r == 3: f['value'] = "Identify hazardous manual tasks involving repetitive, awkward, or high-force movements."
            elif r == 4: f['value'] = "Assess the risk using the Hazardous Manual Tasks risk assessment matrix."
            elif r == 6: f['value'] = "Implement control measures following the hierarchy of control (e.g. hoists, slide sheets)."
            elif r == 7: f['value'] = "Review control measures regularly and update client care plans when physical condition changes."
        elif t == 30:
            if r == 0: f['value'] = "Support Worker / Care Assistant"
            elif r == 1: f['value'] = "Delivering direct personal care, assisting with client transfers, following WHS procedures, and reporting hazards."
            elif r == 3: f['value'] = "Residential Aged Care Facility / Community Home-based Care"
            elif r == 4: f['value'] = "Aged Care and Disability Support Sector"

        # Tables 33-53: Case study tasks
        elif t in [33, 34, 35]:
            if r == 1: f['value'] = "Client Lucy slipped from wheelchair onto bathroom floor; wet tiles and loose bathmat."
            elif r == 2: f['value'] = "Contusion and skin tear to left elbow, pain in right hip."
            elif r == 3: f['value'] = "First aid applied, ice pack to hip, sterile dressing on elbow, Registered Nurse attended, dynamic transfer conducted."
            else: f['value'] = "Immediate verbal report to supervisor Sarah Jenkins, followed by completion of Incident Report Form."
        elif t in [36, 37, 38]:
            if r == 1: f['value'] = "Worker strained lower back while manually repositioning client Lucy in bed without slide sheet."
            elif r == 2: f['value'] = "Acute lumbar muscle spasm and reduced spinal flexion."
            elif r == 3: f['value'] = "Task ceased immediately, supervisor notified, first aid applied (rest/cold pack), GP medical assessment scheduled."
            else: f['value'] = "Worker injury incident report lodged, SafeWork notification reviewed, slide sheet training scheduled for team."
        elif t in range(39, 54):
            f['value'] = "Reported hazard immediately to workplace supervisor Sarah Jenkins, isolated the area with warning signage, and logged details in the workplace hazard register."

    return fields

def populate_chcage011(fields):
    for f in fields:
        if f['section'] == 'Assessor Section':
            continue
        if f.get('type') == 'checkbox':
            if f['table_idx'] == 3 and f['row_idx'] == 3 and f['index_in_cell'] == 1:
                f['value'] = True
            elif f['table_idx'] == 54:
                if f['row_idx'] == 1 and f['col_idx'] in [0, 2]:
                    f['value'] = True
                elif f['row_idx'] == 4 and f['index_in_cell'] in [0, 3]:
                    f['value'] = True
            elif f['table_idx'] == 55:
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
            tests = {
                1: "Mini-Mental State Examination (MMSE): Evaluates orientation, word recall, attention, calculation, language, and visuospatial skills.",
                2: "Montreal Cognitive Assessment (MoCA): Assesses short-term memory, executive functioning, visuospatial abilities, language, and abstraction.",
                3: "Rowland Universal Dementia Assessment Scale (RUDAS): Culturally and linguistically fair screening tool designed for CALD populations."
            }
            if r in tests: f['value'] = tests[r]
            elif r == 4: f['value'] = "Early diagnosis enables proactive care planning, timely therapeutic intervention, access to support services, and client involvement in advanced care directives."
            elif r == 5: f['value'] = "Biomarker imaging (Amyloid and Tau PET scans) and cerebrospinal fluid (CSF) or plasma biomarker analysis."
            elif r == 6: f['value'] = "Identifies pathological protein deposits prior to extensive irreversible neurodegeneration."
            elif r == 7: f['value'] = "Cognitive stimulation therapy and regular physical exercise programs."
            elif r == 8: f['value'] = "Maintains synaptic plasticity, improves mood, preserves daily living skills, and delays functional decline."

        # Table 4: Causes of dementia
        elif t == 4:
            if r == 1: f['value'] = "Dementia is a progressive, irreversible neurodegenerative condition characterized by cognitive decline severe enough to interfere with daily life, caused by progressive brain cell damage."
            elif r == 2: f['value'] = "Vascular disease: Multiple cerebral infarctions, strokes, and atherosclerosis reducing cerebral oxygenation and damaging neural pathways."
            elif r == 3: f['value'] = "Genetic mutation: Familial mutations in APP, PSEN1, and PSEN2 genes leading to early-onset neurodegeneration."
            elif r == 4: f['value'] = "Severe traumatic brain injury (TBI) and chronic neuroinflammation accelerating tau phosphorylation."
            elif r == 5: f['value'] = "Ageing (the single greatest risk factor) causing diminished cellular repair, mitochondrial dysfunction, and blood-brain barrier degradation."

        # Table 5 & 6: Types of dementia
        elif t == 5:
            types_d = {
                1: "Alzheimer's Disease: Most common type, characterized by early episodic memory loss, word-finding difficulty, and gradual deterioration of executive functioning.",
                2: "Vascular Dementia: Stepwise cognitive decline resulting from impaired cerebral blood supply, mini-strokes, and localized ischemia.",
                3: "Frontotemporal Dementia: Early onset degeneration of frontal and temporal lobes, causing pronounced personality changes, behavioural disinhibition, and aphasia.",
                4: "Vascular dementia: Caused by reduced cerebral blood flow due to stroke, arteriosclerosis, or small vessel disease, leading to a stepwise decline in cognitive function, executive planning, and motor coordination.",
                5: "Multi-infarct dementia: A specific form of vascular dementia caused by multiple successive mini-strokes (transient ischemic attacks) damaging localized areas of brain tissue."
            }
            if r in types_d: f['value'] = types_d[r]
        elif t == 6:
            types_d2 = {
                1: "Lewy Body Dementia: Cognitive decline marked by recurrent visual hallucinations, parkinsonian motor symptoms (rigidity, tremor), and marked fluctuations in attention.",
                2: "Korsakoff Syndrome: Severe chronic memory disorder caused by thiamine (Vitamin B1) deficiency, frequently linked to prolonged alcohol abuse, causing anterograde amnesia and confabulation.",
                3: "Frontotemporal lobar degeneration: Atrophy in the frontotemporal cortices resulting in progressive language impairment (primary progressive aphasia) or social conduct deterioration.",
                4: "Huntington's disease: An inherited autosomal dominant neurodegenerative genetic disorder causing progressive chorea (involuntary movements), emotional disturbances, and cognitive decline.",
                5: "Parkinson's Disease: A neurodegenerative disease characterized by loss of dopamine-producing brain cells, producing tremor, bradykinesia, rigidity, and late-stage dementia with Lewy bodies.",
                6: "Younger onset dementia: Dementia diagnosed in individuals under the age of 65, often presenting with significant atypical behavioural or linguistic changes and profound socioeconomic impact."
            }
            if r in types_d2: f['value'] = types_d2[r]

        # Table 7 & 8: Pathological features & plaques/tangles
        elif t == 7:
            if r == 1: f['value'] = "Dementia causes progressive neuronal death, loss of synaptic connections, and overall brain atrophy, particularly in the hippocampus and cerebral cortex."
            elif r == 2: f['value'] = "Amyloid plaques are extracellular deposits composed of misfolded insoluble beta-amyloid peptide aggregates that accumulate between nerve cells."
            elif r == 3: f['value'] = "Plaques disrupt inter-neuronal chemical communication, trigger neuroinflammation, and activate microglial immune responses that damage surrounding synapses."
            elif r == 4: f['value'] = "Amyloid plaques accumulate between neurons, disrupting synaptic communication, triggering chronic localized neuroinflammation, and activating microglia that destroy surrounding neural pathways."
        elif t == 8:
            if r in [0, 1]: f['value'] = "Neurofibrillary tangles are abnormal intracellular accumulations of hyperphosphorylated tau protein inside neurons."
            elif r == 2: f['value'] = "Tau protein detaches from microtubules and tangles into insoluble filaments, causing internal transport systems to collapse and leading to cell death."
            elif r == 3: f['value'] = "Progressive cerebral cortex atrophy and ventricular enlargement."
            elif r == 4: f['value'] = "Reduces total cerebral mass and destroys cognitive networks responsible for memory, reasoning, and speech."

        # Table 9: Symptoms and indicators
        elif t == 9:
            symps = {
                1: "Memory loss: Repeatedly forgetting recently learned information, asking the same questions, and misplacing familiar items.",
                2: "Communication difficulty: Struggling to find common words, losing train of thought, and speaking in fragmented sentences.",
                3: "Disorientation: Confusion regarding the current time, day, season, and becoming lost in familiar environments.",
                4: "Indicator: Neglect of personal hygiene, unwashed clothing, and skipping meals.",
                5: "Indicator: Uncharacteristic mood swings, withdrawal from social hobbies, and sudden paranoia.",
                6: "Indicator: Difficulty completing familiar multi-step routines such as preparing a cup of tea or dressing.",
                7: "Progressive aphasia: Increasing difficulty understanding or expressing spoken and written words.",
                8: "Apraxia: Inability to execute purposeful motor movements (e.g. buttoning a shirt) despite intact physical ability.",
                9: "Agnosia: Failure to recognize familiar objects, sounds, or faces (e.g. not recognizing a comb or close family member)."
            }
            if r in symps: f['value'] = symps[r]

        # Table 10: Behaviours of concern
        elif t == 10:
            behs = {
                1: "Wandering: Walking aimlessly or attempting to leave the facility searching for past home or work.",
                2: "Agitation: Restlessness, pacing, shouting, or emotional distress often triggered by environmental overstimulation.",
                3: "Sundowning: Increased confusion, anxiety, and restlessness in the late afternoon and evening.",
                4: "Vocal disruption: Repetitive shouting, calling out for family, or groaning expressing underlying discomfort.",
                5: "Resistance to care: Pushing staff away or shouting during bathing and dressing due to fear, embarrassment, or pain.",
                6: "Physical aggression: Striking out, scratching, or pinching when feeling trapped or threatened.",
                7: "Hoarding or hiding: Stashing food, utensils, or clothing in closets and under mattresses due to insecurity.",
                8: "Disinhibition: Making inappropriate social comments or undressing publicly due to loss of frontal lobe inhibitory control."
            }
            if r in behs: f['value'] = behs[r]

        # Tables 11-25: Communication, validation, pain, environment
        elif t == 11:
            f['value'] = "Validation therapy involves accepting and acknowledging the person's subjective feelings and reality rather than attempting reality reorientation or arguing."
        elif t == 12:
            f['value'] = "Reminiscence therapy uses sensory prompts (photos, music, familiar objects) to encourage the person to talk about past positive memories, enhancing self-worth and mood."
        elif t == 13:
            f['value'] = "Speak in a calm, soothing voice; use short, simple sentences; maintain friendly eye contact; allow ample processing time; and use gentle reassuring gestures."
        elif t == 14:
            f['value'] = "Non-verbal communication includes facial expressions, warm smile, relaxed open posture, gentle touch on forearm, and nodding to show empathy."
        elif t == 15:
            f['value'] = "Unmet needs such as undetected physical pain, urinary tract infections, hunger, thirst, full bladder, feeling cold, fatigue, or boredom."
        elif t == 16:
            f['value'] = "Abbey Pain Scale: Evaluates non-verbal cues including vocalization, facial grimacing, change in body language, physiological indicators, and physical changes."
        elif t == 17:
            f['value'] = "Wong-Baker FACES Pain Rating Scale: Visual pictorial rating scale showing six cartoon faces ranging from happy/no pain (0) to crying/worst pain (10)."
        elif t == 18:
            f['value'] = "Clear pictorial and bold text signage at eye level on bathroom and bedroom doors, and high color contrast between toilet seat, walls, and flooring."
        elif t == 19:
            f['value'] = "Even, glare-free natural lighting, minimizing loud background television/radio noise, and providing quiet, comforting sensory break spaces."
        elif t == 20:
            f['value'] = "Maintain consistent daily care routines, familiar caregivers, and keep personal mementos and family photographs prominently visible."
        elif t == 21:
            f['value'] = "Dignity of risk allows the person living with dementia to engage in chosen meaningful activities (e.g. supervised gardening, folding towels) while managing risks safely."
        elif t == 22:
            f['value'] = "Support independence by offering simplified binary choices (e.g. 'Would you like the blue shirt or the green shirt?'), encouraging self-feeding with adapted cutlery."
        elif t == 23:
            f['value'] = "Physical abuse (unexplained bruising), emotional abuse (belittling/threatening), financial exploitation (unauthorized account withdrawals), and neglect (untreated sores)."
        elif t == 24:
            f['value'] = "Report immediately to the supervisor, notify the Aged Care Quality and Safety Commission under the Serious Incident Response Scheme (SIRS), and record in incident log."
        elif t == 25:
            f['value'] = "Collaborate closely with family members, actively listen to their historical knowledge of the client, provide respite service information, and respect cultural customs."
        elif t == 27:
            comm_methods = {
                1: ("Clear, concise speech using simple words, calm tone, and one idea at a time.", "Example: 'Good morning, John. Here is your warm cup of tea.'"),
                2: ("Facial expressions, eye contact, relaxed body posture, and reassuring gestures.", "Example: Sitting at eye level, smiling warmly, and nodding gently while the person speaks."),
                3: ("Demonstrating respect for the person's cultural customs, language preferences, and traditions.", "Example: Addressing an elder with their preferred honorific title and respecting eye contact customs."),
                4: ("Creating an environment where the person feels their identity is respected and free from discrimination.", "Example: Engaging an accredited bilingual carer or interpreter when discussing daily care preferences."),
                5: ("Providing gentle current environmental cues (calendars, clocks) when appropriate without causing distress.", "Example: Placing a large-print calendar and wall clock in the resident's bedroom."),
                6: ("Using empathetic verbal affirmations that convey safety, care, and comfort.", "Example: 'You are safe here with me, Arthur. I am right beside you.'")
            }
            if r in comm_methods:
                f['value'] = comm_methods[r][0] if c == 1 else comm_methods[r][1]
        elif t == 28:
            comm_methods2 = {
                1: ("Open arm posture, warm eye contact, and gentle unhurried movements.", "Example: Resting a reassuring hand gently on the resident's forearm during a stressful moment."),
                2: ("Entering the person's subjective reality rather than correcting or arguing about facts.", "Example: If the resident is worried about getting children from school, saying 'You love your children very much; tell me about them.'"),
                3: ("Acknowledging and mirroring the person's underlying emotional state.", "Example: 'I can see that you are feeling very frustrated right now. I understand.'"),
                4: ("Allowing the person to express crying, anger, or fear without shushing, judging, or dismissing them.", "Example: Staying calmly present beside a crying resident and offering a tissue with a quiet presence."),
                5: ("Engaging the person in pleasant conversations about positive past life events and achievements.", "Example: Reviewing a personalized memory box containing old family photos and a favorite gardening trowel.")
            }
            if r in comm_methods2:
                f['value'] = comm_methods2[r][0] if c == 1 else comm_methods2[r][1]
        elif t == 29:
            if r == 2:
                stressors = [
                    "Environmental stressors: External stimuli such as loud alarms, bright fluorescent glare, or crowded rooms that overwhelm sensory processing.",
                    "Internal physical stressors: Undetected pain, constipation, urinary tract infection, or fatigue producing distress.",
                    "Psychological stressors: Loss of autonomy, feeling misunderstood, grief, or fear from disorientation."
                ]
                f['value'] = stressors[idx] if idx < len(stressors) else stressors[-1]
            elif r == 3:
                examples = [
                    "Loud dining room noise overwhelms acoustic filtering, leading to agitation and refusal to eat.",
                    "Accumulated minor frustrations across a morning routine trigger an afternoon catastrophic reaction."
                ]
                f['value'] = examples[idx] if idx < len(examples) else examples[-1]
            elif r == 4:
                f['value'] = "Cumulative stressors build up tension until the person reaches a tipping point, resulting in severe agitation, shouting, combativeness, or complete emotional withdrawal."

        # Tables 30-57: Case studies and documentation
        elif t in range(30, 58):
            if "client" in p or "name" in p:
                f['value'] = "Arthur Pendelton (Resident living with moderate Alzheimer's disease)"
            elif "strategy" in p or "approach" in p:
                f['value'] = "Implement person-centred redirection, gentle music therapy, validation of feelings, and provide a quiet sensory environment."
            elif "incident" in p or "report" in p or "description" in p:
                f['value'] = "At 16:30 resident Arthur exhibited signs of sundowning, pacing the corridor anxiously and asking for his deceased wife. Worker engaged Arthur in folding towels, played 1950s big band music, and offered a warm cup of herbal tea. Resident settled well within 20 minutes."
            else:
                f['value'] = "Documented factual observations in progress notes, informed the Registered Nurse on duty, and updated the positive behaviour support strategies in Arthur's care plan."

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
            if r == 1: f['value'] = "Developmental: Building participant capacity and natural community supports to promote safety and self-advocacy."
            elif r == 2: f['value'] = "Preventive: Worker screening checks, NDIS Code of Conduct training, and proactive service quality standards."
            elif r == 3: f['value'] = "Corrective: Complaints handling, incident management, and compliance enforcement by the NDIS Commission."
            elif r == 4: f['value'] = "NDIS Practice Standards: Core module specifying requirements for person-centred support and human rights."
            elif r == 5: f['value'] = "NDIS Code of Conduct: Sets ethical and safe practice standards for all registered and unregistered NDIS providers and workers."
            elif r == 6: f['value'] = "Positive Behaviour Support Capability Framework: Guides practitioners in behaviour support and reducing restrictive practices."
            elif r == 7: f['value'] = "NDIS Quality and Safeguards Commission"
            elif r == 8: f['value'] = "https://www.ndiscommission.gov.au"
            elif r == 9: f['value'] = "Ensures high quality, safe services and investigates complaints regarding NDIS-funded supports."
            elif r == 10: f['value'] = "Requires workers to immediately report reportable incidents (death, serious injury, abuse, unauthorized restrictive practice)."
        elif t == 3:
            f['value'] = "Participants are engaged in supported decision-making, identifying potential hazards together, discussing safety alternatives, and balancing dignity of risk with duty of care."

        # Table 4 & 5: Social devaluation & Social Role Valorisation (SRV)
        elif t == 4:
            if r == 1: f['value'] = "Social devaluation occurs when a person or group is viewed by society as having low social worth, leading to negative stereotypes, segregation, and marginalisation."
            elif r == 2: f['value'] = "Low expectations, loss of autonomy, limited access to mainstream community activities, and institutionalisation."
            elif r == 3: f['value'] = "Disability support workers actively challenge devaluation by promoting social inclusion, valuing individual strengths, and supporting valued social roles."
            elif r == 4: f['value'] = "Promoting community visibility, supported employment, volunteer roles, and equal civic participation."
        elif t == 5:
            f['value'] = "Social Role Valorisation (SRV), developed by Wolf Wolfensberger, posits that people are much less likely to be devalued or abused if they occupy valued social roles (e.g. employee, student, friend, homeowner, artist) within their community."

        # Table 6-8: Strengths-based practice
        elif t == 6:
            practices = {
                1: "Identifying and building upon existing individual abilities, passions, and community connections.",
                2: "Respecting the participant as the primary decision-maker and director of their own support journey.",
                3: "Focusing on capacity building, skill acquisition, and expanding independence rather than focusing on deficits.",
                4: "Facilitating self-direction and supported decision-making, allowing participants to direct their own routines and community activities."
            }
            if r in practices: f['value'] = practices[r]
        elif t == 7:
            f['value'] = "Strengths-based practice shifts the focus away from diagnostic deficits toward individual capabilities, resiliencies, personal aspirations, and community resource mobilization."
        elif t == 8:
            prin = [
                "Focus on capacities and talents rather than deficits or medical diagnoses.",
                "The person with disability is the expert in their own life and aspirations.",
                "Collaborative partnership between support worker and participant to foster independence.",
                "Every environment contains rich informal community networks and resources to support inclusion."
            ]
            f['value'] = prin[idx] if idx < len(prin) else prin[-1]

        # Table 9 & 10: Positive behaviour support & Active support
        elif t == 9:
            pbs = {
                1: "Positive Behaviour Support (PBS) is an evidence-based framework focused on improving personal quality of life and reducing behaviours of concern by understanding the function of the behaviour and modifying environmental triggers.",
                2: "Human rights-based approach: PBS upholds participant dignity, autonomy, and actively works to eliminate restrictive practices.",
                3: "Functional Behaviour Assessment (FBA): Identifies antecedent triggers, communicative functions of behaviour, and maintaining consequences.",
                4: "Proactive strategies (environmental enrichment, routine predictability) and teaching adaptive replacement behaviours."
            }
            if r in pbs: f['value'] = pbs[r]
        elif t == 10:
            act = {
                1: "Person-Centred Active Support (PCAS) is a systematic support method that enables people with disability to be engaged in meaningful daily activities and community life, regardless of their level of disability.",
                2: "Every moment has potential: Transforming ordinary daily routines into opportunities for learning and engagement.",
                3: "Little and often: Breaking activities into small manageable components so the person can participate frequently.",
                4: "Graded assistance: Providing the right amount of help (ask, instruct, prompt, guide) so the person can succeed without taking over."
            }
            if r in act: f['value'] = act[r]

        # Tables 11-30: Task analysis, chaining, goals, AT
        elif t == 11:
            f['value'] = "Task analysis breaks a complex multi-step skill (e.g. preparing breakfast or washing laundry) into discrete, observable sequential steps to facilitate targeted teaching."
        elif t == 12:
            f['value'] = "Forward chaining teaches steps in chronological order starting from step 1; backward chaining has the worker complete initial steps and teaches the final step first so the client experiences immediate completion and success."
        elif t == 13:
            f['value'] = "Positive reinforcement involves immediately following a desired behavior with a reinforcing stimulus (verbal praise, preferred activity, tokens), increasing the likelihood of the behavior recurring."
        elif t == 14:
            f['value'] = "SMART goals are Specific, Measurable, Achievable, Relevant, and Time-bound, ensuring objective tracking of skill acquisition."
        elif t == 15:
            f['value'] = "Adaptive communication devices (speech-generating devices, AAC apps), picture exchange communication systems (PECS), adapted kitchen utensils, and electric wheelchairs."
        elif t == 16:
            f['value'] = "Regular monitoring, data collection on task independence percentage, multidisciplinary reviews, and adjusting support strategies when progress plateaus."
        elif t == 17:
            f['value'] = "Formal risk assessment balances duty of care with dignity of risk, identifying potential safety hazards and establishing supportive mitigating controls."
        elif t == 18:
            f['value'] = "Collaborate with allied health professionals (Speech Pathologist, Occupational Therapist, Physiotherapist) to ensure consistent clinical methodologies."
        elif t == 19:
            discrim = {
                1: ("Mutual reliance and interconnectedness between individuals, where a person with disability participates in reciprocal community relationships rather than one-way dependence.", "Encourages the participant to learn interpersonal and teamwork skills, enhancing self-worth and belonging through equal social contribution."),
                2: ("Unfair, prejudicial, or unequal treatment directed at a specific person with disability by another individual due to negative attitudes or bias.", "Damages self-confidence, creates emotional distress, and causes reluctance or avoidance in practicing skills in public settings."),
                3: ("Systemic policies, physical obstacles, institutional practices, or rules that disadvantage or exclude people with disability as a group.", "Directly blocks access to educational, recreational, and employment resources necessary for practicing and maintaining new functional skills.")
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
            if r == 1: f['value'] = "Article 19 - Living independently and being included in the community: Guarantees equal choice of residence and community inclusion."
            elif r == 2: f['value'] = "Article 27 - Work and employment: Recognizes the right of persons with disabilities to work on an equal basis with others in open, inclusive environments."
            elif r == 3: f['value'] = "Article 30 - Participation in cultural life, recreation, leisure and sport: Ensures equal access to cultural venues, sporting activities, and leisure pursuits."
            elif r == 4: f['value'] = "Upholds the fundamental dignity, autonomy, non-discrimination, and full societal participation of people with disability."
        elif t == 4:
            if r == 3:
                f['value'] = "Communicating personal preferences and dietary/mobility needs clearly to support workers." if c == 0 else "Enables support workers to deliver customized, person-centred support aligned with the individual's genuine choices."
            elif r == 4:
                f['value'] = "Treating service staff, fellow participants, and community members with courtesy and respect." if c == 0 else "Maintains a safe, harmonious, and welcoming environment for everyone in shared community settings."

        # Table 5 & 6: Strengths-based & Person-centred principles
        elif t == 5:
            if r == 3:
                f['value'] = "Focusing on individual capabilities and potential rather than perceived limitations or medical deficits." if c == 0 else "Builds self-efficacy, motivates the participant to attempt new community activities, and fosters positive self-identity."
            elif r == 4:
                f['value'] = "Collaborative partnership where the participant is recognized as the expert in their own life." if c == 0 else "Ensures support plans reflect the participant's authentic goals and community inclusion desires."
        elif t == 6:
            if r == 3:
                f['value'] = "Respect for personal autonomy and self-determination in all aspects of daily life." if c == 0 else "Empowers the participant to decide which community groups, hobbies, and social networks to join."
            elif r == 4:
                f['value'] = "Holistic approach considering emotional, cultural, physical, and spiritual aspirations." if c == 0 else "Ensures community participation activities resonate with the person's overall lifestyle and wellbeing."

        # Table 8-10: Human rights & Community inclusion
        elif t == 8:
            if r == 1:
                f['value'] = "Inherent dignity and individual autonomy: Respecting the person's freedom to make their own choices." if c == 0 else "Ensures community participation is directed by the participant's own interests rather than passive scheduling."
            elif r == 2:
                f['value'] = "Non-discrimination and equality of opportunity: Ensuring equal access to public services and venues." if c == 0 else "Breaks down societal stigma and guarantees equal access to recreational, educational, and civic spaces."
        elif t == 9:
            if r == 3:
                f['value'] = "Universal accessibility: Ensuring physical environments, communications, and transport are accessible to all." if c == 0 else "Enables people with physical, sensory, or cognitive impairments to enter, navigate, and participate in venues independently."
            elif r == 4:
                f['value'] = "Valued social participation: Active contribution and presence in mainstream community groups." if c == 0 else "Fosters genuine social belonging, friendship building, and combats isolation and loneliness."
        elif t == 10:
            f['value'] = "Partnering with mainstream community clubs (e.g. local sports leagues, art studios) and providing individualized active travel training." if r == 2 else "Implementing natural community mentorship programs and supported volunteer opportunities."

        # Table 11 & 12: Social & emotional wellbeing
        elif t == 11:
            if r == 2: f['value'] = "a state of complete physical, mental and social well-being and not merely the absence of disease or infirmity."
            elif r == 3: f['value'] = "Through strong social connections, reciprocal relationships, feelings of belonging, purpose, autonomy, and active participation in community life."
        elif t == 12:
            negs = {
                0: "Social isolation leads to chronic loneliness, depression, cognitive decline, and reduced self-worth.",
                1: "Stigma and discrimination generate feelings of alienation, fear of public judgment, anxiety, and low self-esteem.",
                2: "Lack of transport prevents access to social gatherings, employment, and healthcare, reinforcing seclusion.",
                3: "Unemployment or financial hardship restricts participation in fee-based social, cultural, and recreational activities.",
                4: "Inaccessible physical environments cause frustration, exhaustion, dependency, and exclusion from community venues."
            }
            f['value'] = negs[idx] if idx < len(negs) else negs[0]

        # Table 13-16: Strategies, Networks, Services
        elif t == 13:
            if r == 4:
                f['value'] = "Facilitating membership in local interest-based hobby groups (e.g. community choir, pottery class)." if c == 0 else "Encourages organic peer connections with individuals sharing mutual passions, fostering authentic friendships."
            elif r == 5:
                f['value'] = "Providing travel training to use local buses, trains, and light rail independently." if c == 0 else "Removes transport dependency, expanding access to broader community events and employment hubs."
        elif t == 14:
            if r == 2:
                f['value'] = "Local disability sports networks (e.g. Wheelchair Sports NSW)." if c == 0 else "Provides accessible competitive and social athletic opportunities, promoting fitness and peer bonding."
            elif r == 3:
                f['value'] = "Neighbourhood community centre social hubs." if c == 0 else "Offers weekly social gatherings, art workshops, computer literacy classes, and volunteering avenues."
        elif t == 15:
            if r == 2:
                f['value'] = "National Disability Insurance Scheme (NDIS) Local Area Coordination (LAC)." if c == 0 else "Connects participants to mainstream community programs, local services, and funded support."
            elif r == 3:
                f['value'] = "Community transport services." if c == 0 else "Provides accessible door-to-door transportation for individuals unable to access standard public transport."

        # Table 17-23: Active citizenship, adjustments
        elif t == 17:
            strat = ["Community education campaigns", "Legislative advocacy", "Universal design auditing", "Local council accessibility committees"]
            f['value'] = strat[idx] if idx < len(strat) else strat[-1]
        elif t == 18:
            sport_vals = [
                "Wheelchair basketball / boccia clubs", "Enhances cardiovascular fitness, motor coordination, and sportsmanship.",
                "Community walking and gentle movement groups", "Promotes physical activity in nature and casual social conversation.",
                "Local men's shed / woodwork clubs", "Fosters practical hands-on skills, mentorship, and community camaraderie.",
                "Community garden cooperatives", "Promotes outdoor leisure, sustainable gardening skills, and social inclusion.",
                "Local library book discussion clubs", "Stimulates intellectual engagement, vocabulary sharing, and peer discussion.",
                "Amateur theater and drama workshops", "Builds self-confidence, creative expression, and public presentation skills."
            ]
            f['value'] = sport_vals[idx] if idx < len(sport_vals) else sport_vals[-1]
        elif t == 19:
            f['value'] = "Active citizenship is the philosophy that individuals have rights and civic responsibilities to engage actively in democracy, public debate, and community decision-making." if r == 2 else "It empowers people with disability to exercise their voting rights, participate in local councils, express opinions, and contribute to public policy."
        elif t == 20:
            if r == 3:
                f['value'] = "Supporting attendance at local community forums and council meetings." if c == 0 else "Ensures the individual's voice and lived experience inform local urban and social planning."
            elif r == 4:
                f['value'] = "Assisting with Australian Electoral Commission voter registration and accessible voting options." if c == 0 else "Upholds the person's fundamental democratic right to vote independently and secretly."
        elif t == 21:
            if r == 3:
                f['value'] = "Connecting with independent disability advocacy services (e.g. People with Disability Australia)." if c == 0 else "Empowers the person to resolve housing, funding, or service delivery disputes effectively."
            elif r == 4:
                f['value'] = "Providing self-advocacy training workshops on asserting rights and effective communication." if c == 0 else "Builds self-confidence in speaking up during medical consultations and planning meetings."
        elif t == 22:
            if r == 3:
                f['value'] = "Providing accessible information in Easy Read, large print, or digital screen-reader formats." if c == 0 else "Ensures participants fully understand legal agreements, care options, and community resources."
            elif r == 4:
                f['value'] = "Pre-meeting preparation to list questions and goals the client wants to discuss." if c == 0 else "Maximizes meaningful participation and ensures the client's priorities are central to the meeting."
        elif t == 23:
            if r == 3:
                f['value'] = "Installing wheelchair access ramps, automatic wide doors, and height-adjustable desks." if c == 0 else "Eliminates physical barriers, enabling unrestricted physical access to community buildings."
            elif r == 4:
                f['value'] = "Providing flexible scheduling and quiet sensory rest areas in community centers." if c == 0 else "Accommodates fatigue, sensory overload, and personal care routines comfortably."

        # Tables 24-33: Assistive Technology across domains
        elif t in range(24, 34):
            at_dict = {
                24: ("Adaptive dressing sticks and button hooks", "Enables client to fasten buttons and put on clothing independently.", "Long-handled reacher grabbers", "Allows picking up items from floor without bending or risking balance loss."),
                25: ("Swivel shower stool with backrest", "Provides stable seated support during showering, preventing slip and fall injuries.", "Long-handled ergonomic sponge", "Allows washing back and lower limbs independently without strenuous stretching."),
                26: ("Slide transfer board with low-friction coating", "Facilitates smooth lateral transfers between wheelchair and bed without weight bearing.", "Mechanical mobile client hoist with mesh sling", "Allows safe, ergonomic transfers for non-weight-bearing clients, preventing worker and client injury."),
                27: ("Screen-reading software (JAWS / NVDA)", "Converts on-screen text into synthetic speech, allowing full computer and internet access.", "Handheld digital video magnifier with high contrast", "Magnifies printed text on menus, bus timetables, and documents for low-vision clients."),
                28: ("All-terrain power wheelchair with off-road tires", "Enables navigation across parklands, beaches, and nature trails for outdoor recreation.", "Adaptive bowling ramp and pusher", "Allows clients with limited upper limb strength to participate in community lawn bowls."),
                29: ("Ergonomic vertical mouse and specialized split keyboard", "Reduces repetitive strain and allows comfortable data entry in administrative employment.", "Speech-to-text dictation software (Dragon NaturallySpeaking)", "Allows rapid transcription of reports and emails without manual keyboard typing."),
                30: ("Weighted utensils with thick ribbed handles", "Stabilizes hand tremors, making self-feeding easier and preventing food spillage.", "Scoop plate with high curved rim and suction base", "Enables one-handed eating by allowing food to be pushed against the curved wall without spilling."),
                31: ("Alternating air pressure mattress overlay", "Continuously redistributes body pressure to prevent tissue ischemia and pressure ulcers.", "High-density Roho air cushion for wheelchair", "Provides immersion and envelopment to protect ischial tuberosities during long sitting periods."),
                32: ("Automated electronic pill dispenser with alarm", "Dispenses correct medication doses at programmed times, preventing missed doses.", "Smart home environmental control unit (voice-controlled lighting and thermostat)", "Enables clients with severe mobility impairments to operate home appliances independently."),
                33: ("Smartphone GPS public transit navigation app with voice alerts", "Guides participant through bus stops and transfers with real-time audio instructions.", "Portable vibrating digital watch with visual task schedule", "Provides discreet sensory reminders for appointments, medication, and shift transitions.")
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
