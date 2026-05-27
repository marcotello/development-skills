# High-Integrity Backlog Guide: The Architectural-PM Method

### The High-Integrity Hierarchy
1.  **Epic:** A high-level functional domain (e.g., "Budgeting Engine").
2.  **Story (The Requirement):** A logical functional goal (e.g., "Add User Endpoint"). It defines the business value and acceptance criteria.
3.  **Subtask (The Unit of Work):** An atomic technical task (e.g., "Create Liquibase migration for users table"). This is what the coding agent actually executes.

### The Backend-First Vertical Slice
We do not jump between UI and API. We build the "Engine" first:
* **Backend Stories:** Establish the "Contract of Truth."
* **Frontend Stories:** Consume the contract. 

### Subtask (UoW) Standards
A Subtask is only valid if it is **Atomic**. A coding agent should be able to read a Subtask and know exactly which files to create or modify without needing to look at other subtasks for context.

#### Standard Backend Subtask Set:
* **DB Work:** Liquibase XML/SQL changes.
* **Data Mapping:** Prisma schema updates and client generation.
* **Core Development:** Implementation of Services, DTOs, and Controllers.
* **Verification:** Unit tests covering the new business logic.

#### Standard Frontend Subtask Set:
* **Visuals:** Angular component markup and styling (Spartan UI).
* **Logic:** Signal Store implementation and API service wiring.
* **Verification:** Unit tests (Vitest) and E2E tests (Cypress).
