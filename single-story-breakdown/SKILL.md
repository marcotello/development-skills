---
name: single-story-breakdown
description: Generates a single, standalone, super ultra detailed user story for ongoing development. Enforces strict functional boundaries and provides exhaustive technical descriptions, data contracts, and binary acceptance criteria. Use when adding isolated features, resolving technical debt, or addressing independent requirements outside of a main epic roadmap. Don't use for full project planning, epic generation, or subtask checklists.
---

# Single Story Generation Procedure

Follow these steps to generate a high-integrity, standalone user story using the template provided in `assets/story-template.md`.

## Step 1: Context & Boundary Acquisition
1. Read `references/detail-guide.md` to internalize the narrative standard for isolated requirements.
2. Analyze the user's request to determine the functional domain (Backend or Frontend).
3. Analyze the Project PRD and Architecture Document to have more context about how does this new requirement fits in the big picture. 
4. Analyze the Roadmap and the Backlog to have more context about the previos requirements and how the new requiremnt will improve the system. 
5. **Halt and Query:** Ask 3-5 targeted questions focusing on the specific data contracts, integration points, and edge cases necessary to fulfill the isolated feature.

## Step 2: Architecture & Logic Mapping
1. Identify the specific architectural layer this story impacts (e.g., Prisma schema, NestJS controller, Angular component, Signal Store).
2. Map the exact data transformations, validation rules, and error handling paths required.
3. If the story bridges multiple domains, split it mentally into strict Backend and Frontend boundaries to enforce the separation of concerns.

## Step 3: Drafting the Super Ultra Detailed Description
1. Write the **Story Super ultra detailed Description**.
2. Include the functional context (why this standalone feature is needed).
3. Detail the internal logic, algorithms, and state transitions comprehensively.
4. Specify the exact API contracts, DTO properties, or UI reactivity rules.

## Step 4: Acceptance Criteria Formulation
1. Draft numbered, binary (Pass/Fail) Acceptance Criteria.
2. Ensure every edge case mapped in Step 2 has a corresponding testable criterion.

## Step 5: Template Execution
1. Open `assets/story-template.md`.
2. Populate the template with the drafted description and criteria.
3. Apply the appropriate label `(Backend)` or `(Frontend)` to the story title.

## Error Handling
* If the user attempts to combine database logic and UI markup in a single requirement, halt and instruct the user to define the backend contract first.
