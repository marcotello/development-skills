# High-Integrity Architecture Guide: The Architectural-PM Method

### Phase 1: Holistic System Philosophy
* **Modular Monolith:** Design for a single codebase that behaves like microservices internally. Use strict folder structures to enforce boundaries.
* **Clean/Hexagonal Architecture:** The "Core" (Domain/Application) must never know about the "Infrastructure" (Database/API Framework).

### Phase 2: Data Integrity & The Persistence Anchor
* **The Precision Standard:** Define non-negotiables for numeric data (e.g., `NUMERIC(19, 2)`) to avoid floating-point math issues.
* **Atomic Rollbacks:** Mandate the use of database transactions for any state change involving multiple entities.
* **Separation of Concerns:** Use Mappers to translate between Database Types and Domain Entities.

### Phase 3: Frontend Performance & DX
* **Signal-Native Reactivity:** Use modern reactive primitives (Signals) to minimize change detection cycles.
* **Headless UI Strategy:** Separate the functional logic (Brain) from the visual styling (CSS/Tailwind) to improve maintenance and customization.

### Phase 4: Observability & Security
* **Structured Logging:** All logs must be machine-readable (JSON) and include contextual metadata (UserId, RequestId).
* **Defense in Depth:** Security must exist at the API gateway, the service layer, and the component level.
* **Read-Only Models:** For complex views (like Dashboards), bypass standard service orchestration and use optimized "Query Repositories."
