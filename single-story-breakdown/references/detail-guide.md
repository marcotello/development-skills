# The Standalone Story Standard

### The Challenge of Isolation
As the Lead Technical Architect & Agent Coordinator, your mission is to breakdown high-level User Stories into atomic, sequential "Units of Work" for a developer agent (Claude Code, Gemini, Jules).

### The "Super Ultra Detailed" Anatomy
An isolated story must leave zero room for hallucination by the executing agent.

1. **Context & Objective:** Clearly state the isolated value of this requirement.
2. **Data & State Definition:** Explicitly name the fields, types, and persistence targets.
3. **Execution Logic:** Provide a prose-based algorithm detailing how the service or component processes the data. 
4. **Boundary Definition:** If it is a Frontend story, explicitly state the API endpoint it consumes. If Backend, define the exact JSON payload expected.
5. **Failure Modes:** Detail how the system responds to invalid inputs, network failures, or authorization rejections.

### Binary Acceptance Criteria
Criteria must be testable via automated means (e.g., Unit, Integration, or E2E tests).
* **Poor:** "The form should handle errors."
* **Super Ultra Detailed:** "Submitting the form with a duplicate email returns a 409 Conflict and triggers the `email_exists` error state in the Signal Store."
