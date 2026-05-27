# Implementation Roadmap: [Project Name]

**Architect:** James (Backend-First Strategy)
**Status:** [Draft/Active]

---

## 1. Phase 1: The Foundation (Infrastructure)
[Infrastructure tasks: CI/CD, Base Modules, Global Stores]

## 2. Phase 2 & 3: Functional Epics
### Epic [X]: [Functional Name, e.g., Accounts Management]
* **Objective:** Establish the full lifecycle of [X] starting with the API engine.

#### Part 1: Backend Implementation (The Engine)
- [ ] [UoW] Database Migration: Create schema for [X].
- [ ] [UoW] Domain & Repository: Implement ports and Prisma adapters.
- [ ] [UoW] Service Logic: Implement core business rules.
- [ ] [UoW] API Endpoints: Finalize Controllers and Swagger.

#### Part 2: Frontend Implementation (The Shell)
- [ ] [UoW] Feature Store: Create Signal Store for [X].
- [ ] [UoW] UI Components: Build Spartan UI component shells.
- [ ] [UoW] Integration: Wire components to the API and handle loading/error states.

---

## 3. Dependency Check
* **Rule:** No "Part 2" task may begin until all "Part 1" tasks in the same Epic are marked as Complete.
