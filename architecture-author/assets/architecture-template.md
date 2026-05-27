# Technical Architecture Document: [Project Name]

**Version:** 1.0
**Status:** Approved - Holistic System Design
**Stack:** [Frontend], [Backend], [Database], [ORM], [Migrations]
**Architect:** James (Holistic System Architect)

---

## 1. System Philosophy & Big Picture
[A brief description of the system's high-level architecture—e.g., Modular Monolith—and how it addresses the business mission.]

## 2. Backend Architecture (Clean / Hexagonal)
### 2.1 The Layering Strategy
[Define the 4 layers: Presentation, Application, Domain, Infrastructure.]

### 2.2 Module Structure (Cohesion-First)
[Show a visual directory map of how modules are organized.]

### 2.3 Specialized Patterns
[Detail any CQRS, Read Models, or specific Design Patterns like Strategies or Factories.]

## 3. Frontend Architecture
### 3.1 Component Architecture
[Define Smart vs. Dumb components and the UI library strategy.]

### 3.2 State Management
[Define the Store strategy (e.g., Signal Store) and reactivity rules.]

## 4. Data Integrity & Precision
### 4.1 Data Standards
[Detail numeric precision, currency handling, or specific validation rules.]

### 4.2 Persistence Logic
[Describe the ORM vs. Migration strategy.]

## 5. Infrastructure & Cross-Cutting Concerns
### 5.1 Security & Auth
[Describe Token rotation, Cookie management, and Interceptors.]

### 5.2 Observability
[Detail the structured logging and monitoring strategy.]

---

## 6. Implementation Rules for Agents (The Golden Rules)
1. [Rule 1: e.g., No Leaky Abstractions]
2. [Rule 2: e.g., Signal-Native Only]
3. [Rule 3]
4. [Rule 4]
