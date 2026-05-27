# Epics, Stories, and Subtasks: [Project Name]

**Architect:** James (Backend-First Strategy)
**Status:** [Draft/Active]

---

## Epic: [Epic Title]
**Extensive Description:** [Comprehensive paragraph explaining the goal and technical scope.]

### [Phase A] Backend Requirements

#### Story: (Backend) [Story Title - e.g., Implement POST /users]
* **User Story:** As a [Role], I want to [Action] so that [Value].
* **Technical Description:** [Logical requirement and implementation path.]
* **Subtasks (Units of Work):**
    1. [ ] **DB Migration:** Implement Liquibase changes for [Table].
    2. [ ] **Persistence:** Update Prisma schema and generate types.
    3. [ ] **Logic & API:** Implement Service logic and Controller endpoints.
    4. [ ] **Testing:** Add unit tests for Service and Controller logic.
* **Acceptance Criteria:**
    1. [Criterion 1]
    2. [Criterion 2]

---

### [Phase B] Frontend Requirements

#### Story: (Frontend) [Story Title - e.g., User Creation Screen]
* **User Story:** As a [Role], I want to [Action] so that [Value].
* **Technical Description:** [UI/UX requirement and state management path.]
* **Subtasks (Units of Work):**
    1. [ ] **UI/UX:** Create Angular component markup using Spartan UI.
    2. [ ] **State & API:** Implement Signal Store logic and wire to backend API.
    3. [ ] **Unit Tests:** Implement Vitest components tests.
    4. [ ] **E2E Tests:** Implement Cypress end-to-end flows.
* **Acceptance Criteria:**
    1. [Criterion 1]
    2. [Criterion 2]
