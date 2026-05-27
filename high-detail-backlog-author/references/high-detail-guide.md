# The James Standard: Super Ultra Detailed Stories

### What is a "Super Ultra Detailed" Description?
In this method, the Story is the contract. It should be so descriptive that subtasks are merely a mechanical byproduct of the requirement. 

**A Detailed Story includes:**
1.  **Functional Context:** Why are we doing this, and what is the exact user journey?
2.  **Data Specifications:** What specific fields are being touched? What are the types, lengths, and constraints?
3.  **Logical Flow:** A step-by-step prose description of the algorithm or process (e.g., "The service must first check cache [A], then verify permission [B], and finally initiate an atomic transaction [C]").
4.  **Edge Case Handling:** Explicit instructions on what happens when things go wrong (e.g., 404 vs 401 handling).
5.  **State Management (Frontend):** Exact details on which signals are updated and what triggers the side effects.

### The Backend-First Vertical Slice
We maintain a strict separation of concerns within the Epic:
* **Group A (Backend):** We build the "Engine" first. These stories define the API surface area and the "Truth" of the data.
* **Group B (Frontend):** We build the "Shell." These stories consume the stable API contract defined in Group A.

### Acceptance Criteria (AC) Standard
ACs must be binary (Pass/Fail). For a Backend story, an AC might be: *"The POST /users endpoint must return a 409 Conflict if the email already exists in the identity schema."*
