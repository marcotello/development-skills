---
name: high-detail-backlog-author
description: Generates high-integrity backlogs consisting of Extensive Epics and Super Ultra Detailed Stories. It prioritizes exhaustive technical and functional descriptions over granular subtasking, ensuring the Story acts as a complete requirement contract. Enforces a Backend-First sequencing mandate.
---

# High-Detail Backlog Generation Procedure

Follow these steps to generate a project backlog using the "James Persona" standards and the template provided in `assets/epics-stories-template.md`.

## Step 1: Input Synthesis & Technical Deep Dive
1.  Read `references/high-detail-guide.md` to internalize the "Super Ultra Detailed" narrative standard.
2.  Analyze the Project PRD and Architecture Document to identify functional domains.
3.  **Halt and Query:** Ask 5-7 strategic questions to uncover "the detail of the detail." Focus on business logic edge cases, specific data validation rules, and exact state transitions.

## Step 2: Extensive Epic Definition
1.  Break the project into functional Epics.
2.  Draft an **Extensive Description** for each: A comprehensive paragraph explaining the business "North Star," technical boundaries, and how it fits into the holistic system.

## Step 3: Drafting Super Ultra Detailed Stories
1.  Apply the **Backend-First Mandate**: Within each Epic, sequence all Backend Stories before Frontend Stories.
2.  For each Story, write a **Super Ultra Detailed Description**. This must include:
    * **The Logic:** Detailed explanation of the internal processing, algorithms, or state changes.
    * **The Contract:** Specifics on DTOs, API endpoints (for backend), or Store signals (for frontend).
    * **The Constraints:** Validation rules, error handling paths, and performance requirements.
3.  Draft **Acceptance Criteria**: Numbered, testable conditions that leave zero room for ambiguity.

## Step 4: Quality Control
1.  Review each story. If a developer could ask "How do I handle [X] edge case?", the description is not detailed enough.
2.  Ensure all technical notation uses LaTeX-style syntax for mathematical or scientific clarity.

## Step 5: Template Execution
1.  Populate `assets/epics-stories-template.md` following the user's specific structure.
2.  Ensure the tone is pragmatic, professional, and technically authoritative.
