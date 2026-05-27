---
name: epics-stories-author
description: Transforms technical architectures into a three-tier backlog (Epic -> Story -> Subtask). It treats Stories as logical requirements and Subtasks as atomic Units of Work (UoW). Enforces a Backend-First mandate to ensure API stability before UI development.
---

# Epics, Stories, and Subtasks Generation Procedure

Follow these steps to generate a structured project backlog using the template provided in `assets/epics-stories-template.md`.

## Step 1: Synthesis & Hierarchy Mapping
1.  Read `references/epics-stories-guide.md` to internalize the relationship between Stories (Requirements) and Subtasks (Units of Work).
2.  Analyze the Project PRD and Architecture to identify the functional domains.
3.  **Halt and Query:** Ask 3-5 questions to clarify the "Definition of Done" for subtasks (e.g., "Do all frontend subtasks require Cypress tests?").

## Step 2: Epic Definition
1.  Divide the project into functional Epics.
2.  Provide an **Extensive Description** for each, focusing on the business value and the architectural boundaries.

## Step 3: Story & Subtask Mapping (The Execution Flow)
1.  Within each Epic, implement the **Backend-First Mandate**: All Backend Stories must be completed before Frontend Stories begin.
2.  **Define the Story:** Create the logical requirement (e.g., "Implement User Authentication").
3.  **Decompose into Subtasks (Units of Work):** For every story, generate the mandatory atomic subtasks:
    * **Backend Pattern:** 1. DB/Liquibase -> 2. Prisma Mapping -> 3. Logic/Controllers -> 4. Unit Tests.
    * **Frontend Pattern:** 1. UI Markup -> 2. Logic/State Management -> 3. Unit/E2E Tests.

## Step 4: Logic Validation
1.  Verify that every Subtask is "Atomic"—it should be a single, non-ambiguous task for a coding agent.
2.  Ensure that Backend subtasks for API endpoints include a requirement to update Swagger/OpenAPI documentation.

## Step 5: Template Execution
1.  Populate `assets/epics-stories-template.md`.
2.  Maintain the "James" Persona: technically deep, methodical, and pragmatic.
