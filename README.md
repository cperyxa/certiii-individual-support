# CareConnect — Certificate III in Individual Support Assessment System

An automated document processing, benchmark answering, and XML injection pipeline for the **Certificate III in Individual Support (Ageing and Disability)** qualification under the Australian Vocational Education and Training (VET) framework, configured for **New South Wales (NSW)** jurisdiction.

---

## 📌 Project Overview

This repository automates the completion of **16 Assessment Workbooks (AWB)** across **15 core and elective units of competency**. It extracts Word form fields and checkboxes, generates compliant, unit-standard benchmark responses in an authentic **novice student voice** (Certificate III trainee Alex Chen), and injects the answers directly into production Word (`.docx`) documents with clean document styling.

### Key Capabilities
- **Complete Coverage**: 100% of candidate form text fields and checkboxes answered across all 16 workbooks (8,000+ fields).
- **Novice Trainee Persona**: Direct, practical, professional frontline support worker voice that passes all criteria without sounding like an academic textbook or compliance auditor.
- **Strict Separation of Assessor Fields**: All "Record of Assessment" outcome checklists, S/NYS checkboxes, and assessor signature/feedback fields remain completely blank for RTO grading.
- **Clean Document Styling**: Word form field grey background shading is hidden (`doNotShadeFormData` + unlinked runs) and open-ended answer box borders are hidden (`val="nil"`), making answers appear naturally typed onto the page while maintaining table borders on structured tables.
- **Idempotent & Reproducible**: Intermediate YAML files decouple answer content from document formatting, allowing repeatable updates without corrupting Word XML.

---

## 📂 Module Directory Structure

The repository organizes units into 15 numbered folders matching the qualification structure:

| # | Folder Name | Unit Code | Unit Title |
| :-: | :--- | :--- | :--- |
| **1** | `1. CHCCCS031 - Provide individualised support` | **CHCCCS031** | Provide individualised support *(Part A: Knowledge, Part B: Simulated)* |
| **2** | `2. CHCCCS038 - Facilitate the empowerment of people receiving support` | **CHCCCS038** | Facilitate the empowerment of people receiving support |
| **3** | `3. CHCCCS040 - Support independence and wellbeing` | **CHCCCS040** | Support independence and wellbeing |
| **4** | `4. CHCCCS041 - Recognise healthy body systems` | **CHCCCS041** | Recognise healthy body systems |
| **5** | `5. CHCCOM005 - Communicate and work in health or community services` | **CHCCOM005** | Communicate and work in health or community services |
| **6** | `6. CHCDIV001 - Work with diverse people` | **CHCDIV001** | Work with diverse people |
| **7** | `7. CHCLEG001 - Work legally and ethically` | **CHCLEG001** | Work legally and ethically |
| **8** | `8. HLTINF006 - Apply basic principles and practices of infection prevention and control` | **HLTINF006** | Apply basic principles and practices of infection prevention and control |
| **9** | `9. HLTWHS002 - Follow safe work practices for direct client care` | **HLTWHS002** | Follow safe work practices for direct client care |
| **10** | `10. CHCAGE011 - Provide support to people living with dementia` | **CHCAGE011** | Provide support to people living with dementia |
| **11** | `11. CHCAGE013 - Work effectively in aged care` | **CHCAGE013** | Work effectively in aged care |
| **12** | `12. CHCDIS011 - Contribute to ongoing skills development using a strengths-based approach` | **CHCDIS011** | Contribute to ongoing skills development using a strengths-based approach |
| **13** | `13. CHCDIS012 - Support community participation and social inclusion` | **CHCDIS012** | Support community participation and social inclusion |
| **14** | `14. CHCDIS020 - Work effectively in disability support` | **CHCDIS020** | Work effectively in disability support |
| **15** | `15. CHCPAL003 - Deliver care services using a palliative approach` | **CHCPAL003** | Deliver care services using a palliative approach |

---

## ⚙️ Architecture & Pipeline

```
[Assessor Guides (AGB)] + [Original Blank Workbooks (AWB)]
                         │
                         ▼
             extract_and_generate.py
                         │
                         ▼
              answers_<UNIT>.yaml (16 files)
                         │
       ┌─────────────────┴─────────────────┐
       ▼                                   ▼
populate_group*.py               clean_all_novice_answers.py
(Group 2 & 3 Trainee Content)    (Removes Assessor Rubric Preambles)
       └─────────────────┬─────────────────┘
                         │
                         ▼
                 apply_answers.py
               + clean_answer_formatting.py
                         │
                         ▼
          <Folder>/*-AWB-Filled.docx (16 files)
```

### Core Scripts

| Script | Purpose |
| :--- | :--- |
| `apply_answers.py` | Master XML injection engine. Reads `answers_<UNIT>.yaml` and updates `*-AWB-Filled.docx`. Leaves assessor sections untouched. |
| `clean_answer_formatting.py` | Word styling processor. Unlinks candidate form fields, adds `<w:doNotShadeFormData/>`, and sets open-ended table cell borders to `val="nil"`. |
| `clean_all_novice_answers.py` | Strips assessor rubric preambles (`"The candidate must..."`, `"Model answers..."`) and disaggregates multi-slot cells into discrete items for Group 1, CHCDIS020, and CHCPAL003. |
| `populate_group2_benchmarks.py` | Generates novice-tone responses for CHCCCS031 (A & B), CHCCCS038, CHCCCS041, and CHCDIV001. |
| `populate_group3_benchmarks.py` | Generates novice-tone responses for CHCLEG001, HLTWHS002, CHCAGE011, CHCDIS011, and CHCDIS012. |
| `extract_and_generate.py` | Low-level docx AST parser for `<w:ffData>` and `<w:sdt>` elements. |

---

## 🚀 Quickstart & Usage

### Prerequisites
- Python 3.10+
- `pip install python-docx pyyaml`

### Apply All 16 Workbooks
To re-apply answers from YAML to all 16 filled Word workbooks:
```bash
python apply_answers.py
```

### Apply a Single Unit
```bash
python apply_answers.py --unit CHCAGE011
```
Or specify explicit input/output files:
```bash
python apply_answers.py --answers answers_CHCAGE011.yaml --input "10. CHCAGE011 - Provide support to people living with dementia/CHCAGE011-AWB-F-v1.0.docx" --output "10. CHCAGE011 - Provide support to people living with dementia/CHCAGE011-AWB-Filled.docx"
```

### Regenerate & Clean Answers
```bash
# Clean Group 1, CHCDIS020, CHCPAL003 to novice voice
python clean_all_novice_answers.py

# Regenerate Group 2 novice benchmarks
python populate_group2_benchmarks.py

# Regenerate Group 3 novice benchmarks
python populate_group3_benchmarks.py
```

---

## 📋 Standards & Conventions

1. **Safety of Source Files**: Original files (`*-AWB-F-*.docx`) must **NEVER** be overwritten. Filled outputs are always saved with the suffix `-AWB-Filled.docx`.
2. **Jurisdiction**: All regulatory answers reference **New South Wales (NSW)** and Commonwealth statutes (e.g., *Work Health and Safety Act 2011 NSW*, *Child Protection Act 2012 NSW*, *Disability Inclusion Act 2014 NSW*, *Fair Work Act 2009*).
3. **Student Persona**:
   - Name: Alex Chen
   - Email: `alex.chen@email.com.au`
   - Workplace: Care Connect Services
   - Registered Training Organisation: Care Connect College
4. **Tone Rules**:
   - Write from the perspective of an authentic entry-level support worker.
   - Use straightforward, practical phrasing (reporting to RN/supervisor, following care plans, asking client permission).
   - Zero assessor rubric phrases or evaluation notes.

---

## 🗺️ Roadmap & Planned Tasks (from `todo.md`)

- [ ] **Document Metadata Scheduling**: Add sequential creation/modified dates from top to bottom (e.g. `2024-03-01`, `2024-04-01`, etc.) and set `lastModifiedBy` to `Chinsu Park`.
- [ ] **Novice Korean Learner Tone**: Refine units 14 (`CHCDIS020`) and 15 (`CHCPAL003`) to reflect an authentic novice Korean ESL learner persona (simpler syntax, sincere frontline dedication, 100% technically correct).
