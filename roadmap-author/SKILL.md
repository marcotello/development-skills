---
name: roadmap-author
description: Transforms requirements into a backend-first implementation roadmap. It ensures all API, Schema, and Logic stories are completed before Frontend wiring begins within each Epic. This minimizes UI refactoring and ensures a stable contract between layers.
---

# Roadmap Generation Procedure (Backend-First Mandate)

Follow these steps to generate a structured implementation roadmap using the template provided in `assets/roadmap-template.md`.

## Step 1: Input Synthesis & Dependency Mapping
1.  Read `references/roadmap-guide.md` to internalize the "Backend-First" sequencing logic.
2.  Analyze the PRD and Architecture to map out the data models and API requirements.
3.  **Halt and Query:** Ask the user 3-5 questions about data persistence priorities and specific API complexity.

## Step 2: Phase Segmentation
1.  Divide the project into technical lifecycle phases (Foundation -> Core Logic -> UI Integration -> Polish).

## Step 3: Epic & Story Sequencing (The Strict Order)
1.  For every Epic, you **MUST** organize stories in this strict chronological order:
    * **Group A: Backend (The Engine):** Database Migrations -> Domain Entities/Ports -> Application Services -> Controllers/API Endpoints -> Integration Tests.
    * **Group B: Frontend (The Shell):** Feature Stores (Signals) -> Component Architecture -> UI/UX Styling -> API Wiring & Integration.
2.  **Constraint:** Group B stories must never be scheduled before Group A stories are complete within the same functional domain.

## Step 4: Atomic Units of Work (UoW)
1.  Break each story into UoWs. Ensure Backend UoWs include "Update Swagger/Documentation" as a completion step so the Frontend UoWs have a reference.

## Step 5: Template Execution
1.  Populate `assets/roadmap-template.md`. Ensure the visual separation between Backend and Frontend tasks is clear within each Epic.
