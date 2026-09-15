# CareConnect Assessment Automation — Agents & Developer Guidelines

## 1. Project Overview

This repository contains the assessment materials, automated answer generation pipeline, and document injection system for **Certificate III in Individual Support (Ageing and Disability)** under the Australian Vocational Education and Training (VET) framework, configured for **New South Wales (NSW)** jurisdiction.

The project covers **15 units of competency** across **16 Assessment Workbooks**:

| Folder / Prefix | Unit Code | Unit Title |
| :--- | :--- | :--- |
| `1. CHCCCS031 - ...` | **CHCCCS031 (Part A & B)** | Provide individualised support |
| `2. CHCCCS038 - ...` | **CHCCCS038** | Facilitate the empowerment of people receiving support |
| `3. CHCCCS040 - ...` | **CHCCCS040** | Support independence and wellbeing |
| `4. CHCCCS041 - ...` | **CHCCCS041** | Recognise healthy body systems |
| `5. CHCCOM005 - ...` | **CHCCOM005** | Communicate and work in health or community services |
| `6. CHCDIV001 - ...` | **CHCDIV001** | Work with diverse people |
| `7. CHCLEG001 - ...` | **CHCLEG001** | Work legally and ethically |
| `8. HLTINF006 - ...` | **HLTINF006** | Apply basic principles and practices of infection prevention and control |
| `9. HLTWHS002 - ...` | **HLTWHS002** | Follow safe work practices for direct client care |
| `10. CHCAGE011 - ...` | **CHCAGE011** | Provide support to people living with dementia |
| `11. CHCAGE013 - ...` | **CHCAGE013** | Work effectively in aged care |
| `12. CHCDIS011 - ...` | **CHCDIS011** | Contribute to ongoing skills development using a strengths-based approach |
| `13. CHCDIS012 - ...` | **CHCDIS012** | Support community participation and social inclusion |
| `14. CHCDIS020 - ...` | **CHCDIS020** | Work effectively in disability support |
| `15. CHCPAL003 - ...` | **CHCPAL003** | Deliver care services using a palliative approach |

---

## 2. Core Architecture & Pipeline

The pipeline follows a reproducible, three-stage workflow:

```
[Assessor Guides (AGB)] + [Original Workbooks (AWB)]
                     │
                     ▼
        extract_and_generate.py
                     │
                     ▼
          answers_<UNIT>.yaml (16 files)
                     │
   ┌─────────────────┴─────────────────┐
   ▼                                   ▼
populate_group*.py           clean_all_novice_answers.py
(Generates benchmarks)       (Cleans rubric preambles & novice tone)
   └─────────────────┬─────────────────┘
                     │
                     ▼
             apply_answers.py
           + clean_answer_formatting.py
                     │
                     ▼
      <Unit Folder>/*-AWB-Filled.docx (16 files)
```

### Key Scripts

1. **`extract_and_generate.py`**:
   - Inspects docx structures, extracts `<w:ffData>` (text fields) and `<w:sdt>` (checkboxes).
   - Maps table coordinates `(table_idx, row_idx, col_idx, index_in_cell)` and assigns unique field IDs.
2. **`populate_group2_benchmarks.py` & `populate_group3_benchmarks.py`**:
   - Populates Groups 2 & 3 answers directly into intermediate YAML files using novice trainee voice.
3. **`clean_all_novice_answers.py`**:
   - Cleans remaining units (Group 1, CHCDIS020, CHCPAL003).
   - Strips Assessor Guide preamble patterns (`"The candidate must..."`, `"Model answers are provided below..."`, `"For a satisfactory performance..."`).
   - Disaggregates multi-slot cells (`index_in_cell: 0, 1, 2`) into distinct items.
4. **`clean_answer_formatting.py`**:
   - Hides default grey shading on candidate form fields by unlinking form field runs into clean `<w:t>` runs and setting `<w:doNotShadeFormData/>`.
   - Hides borders (`val="nil"`) on open-ended question answer boxes (single-column answer tables/cells) while preserving grid borders on multi-column analysis tables.
5. **`apply_answers.py`**:
   - Master XML injection engine.
   - Reads `answers_<UNIT>.yaml` and injects candidate values into `*-AWB-Filled.docx`.
   - Leaves all **Assessor Sections** untouched (empty).

---

## 3. Candidate Persona & Response Tone Rules

- **Persona**: Alex Chen, Certificate III Trainee.
- **Tone**:
  - Direct, practical, professional frontline support worker voice.
  - Practical workplace actions: asking for client consent, observing physical and behavioral changes, consulting the individualised care plan, reporting to the supervisor/RN, adhering to NSW WHS guidelines.
  - **No Senior/Legalistic Jargon**: Do not write like an RTO compliance director, senior clinical nurse, or lawyer unless specifically required by the prompt.
  - **No Assessor Rubric Phrases**: Never include phrases such as *"The candidate will..."*, *"Satisfactory performance requires..."*, or *"Model answers below..."*. Answers must read as the student's direct response.
- **Assessor Fields**:
  - `is_assessor_section: true` or sections titled "Assessor Section" / "Record of Assessment" **must remain completely blank** (value: `""` or `null`).
  - Never check "Satisfactory (S)" or "Not Yet Satisfactory (NYS)" checkboxes—these are exclusively for RTO assessors.

---

## 4. Document Styling & Formatting Standards

- **Output Destination**:
  - Original source files (`*-AWB-F-*.docx`) must **NEVER** be overwritten.
  - Filled outputs must always be saved as `*-AWB-Filled.docx` inside their respective numbered unit folder.
- **Visual Appearance**:
  - Form field grey background shading must be hidden.
  - Open-ended question response boxes must have borders hidden (`val="nil"`) so answers look like naturally typed text following the prompt.
  - Multi-column structured tables (e.g. matrices, schedules, comparison charts) must keep visible borders.

---

## 5. Upcoming Tasks & Roadmap (from `todo.md`)

- **Document Metadata Scheduling**:
  - Configure document metadata (`lastModifiedBy`, creation/revision dates) chronologically from top to bottom (e.g., `2024-03-01`, `2024-04-01`, etc.).
  - Set `lastModifiedBy` to `Chinsu Park` (or previous authors as specified in task schedule).
- **ESL / Novice Learner Adjustments**:
  - For units **14 (CHCDIS020)** and **15 (CHCPAL003)**, fine-tune answers to reflect an authentic novice Korean learner tone (natural, slightly simpler syntax, sincere frontline focus, 100% technically correct).
