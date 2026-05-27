---
name: architecture-author
description: Generates high-integrity Technical Architecture Documents by defining decoupled, modular monoliths following Clean Architecture principles. It converts PRD requirements into technical blueprints, ensuring the separation of core business logic from infrastructure and persistence layers. Use when moving from product discovery to technical implementation.
---

# Architecture Document Generation Procedure

Follow these steps to transform a Product Requirements Document (PRD) into a comprehensive technical blueprint using the template provided in `assets/architecture-template.md`.

## Step 1: Input Analysis & Alignment
1.  Read `references/architecture-guide.md` to internalize the James Persona's Architectural-PM workflow.
2.  Analyze the provided PRD to identify core entities, critical data integrity requirements, and user-driven technical needs.
3.  **Halt and Query:** Before drafting, ask the user 3-5 technical clarification questions focusing on persistence preferences (ORM/Migrations), state management needs, and specific security constraints.

## Step 2: Define System Boundaries (Phase 1)
1.  Establish the "Decoupled Modular Monolith" philosophy.
2.  Define strict boundaries between the "Core/Domain" and "Infrastructure/Adapters" to ensure SOLID compliance.
3.  Map the high-level module structure based on functional requirements.

## Step 3: Persistence & Data Standard (Phase 2)
1.  Define the financial or data-grade standards (e.g., Numeric precision for currency).
2.  Specify the dual-tool strategy for DDL (Migrations) vs. DML (ORM).
3.  Define atomic operation requirements to prevent state corruption.

## Step 4: Frontend & UI Strategy (Phase 3)
1.  Establish the state management pattern (e.g., Signal-based, Reactive).
2.  Define the relationship between UI logic (Brain) and Styling (HLM/CSS).
3.  Set rules for component communication (Inputs/Outputs vs. Service-driven).

## Step 5: Infrastructure & Cross-Cutting Concerns (Phase 4)
1.  Define the Observability strategy (Structured JSON logging).
2.  Establish Security transport rules (Cookie-based auth, token rotation).
3.  Map any specialized Read Models (e.g., CQRS-lite) for performance-heavy views like Dashboards.

## Step 6: Template Execution
1.  Open `assets/architecture-template.md`.
2.  Populate every section of the template with the specifications generated in previous steps.
3.  Ensure the tone remains that of a "James Persona": comprehensive, pragmatic, technically deep, and patterns-first.
4.  **Enforce Implementation Rules:** Explicitly list 4-5 "Golden Rules" for coding agents to prevent leaky abstractions.

## Step 7: Final Validation
1.  Verify that every technical decision in the document can be traced back to a PRD requirement.
2.  Confirm that the architecture supports "Progressive Complexity" as defined in the core principles.
