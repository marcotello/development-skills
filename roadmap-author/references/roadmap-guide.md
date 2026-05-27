# High-Integrity Roadmap Guide: The Backend-First Mandate

### The Philosophy: "Contract-Driven Development"
In the Finova standard, the Backend is the "Source of Truth." Building the backend entirely before the frontend prevents "UI Churn"—the wasted time spent updating components because the API structure changed mid-development.

### The Epic Internal Structure
Each Epic must be a mini-vertical slice, but the internal execution is strictly horizontal:

1.  **Persistence Layer:** Always start with the Liquibase migration and Prisma schema.
2.  **Logic Layer:** Implement the Domain Entities and Application Services.
3.  **Access Layer:** Finalize the Controller and ensure the API returns the correct HTTP codes.
4.  **State Layer:** Once the API is stable, build the NgRx Signal Store.
5.  **View Layer:** Finally, implement the Spartan UI components and wire them to the Store.

### Benefits of this Approach
* **Decoupling:** You can test 100% of the business logic via Vitest/Jest before the browser even opens.
* **Stable Signals:** The Frontend developer (or agent) knows exactly what data is coming in, making Signal `computed()` logic much easier to write.
* **Parallelization:** Once the Backend Group A is done, a different agent can work on Group B without needing to touch the backend code again.
