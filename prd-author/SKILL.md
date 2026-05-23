---
name: prd-author
description: Generates high-integrity Product Requirements Documents (PRDs) by bridging business objectives with granular architectural constraints. It follows the Architectural-PM Method, ensuring technical anchors and scalability are defined early. Use when initializing new products or sub-modules.
---

# PRD Generation Procedure

Follow these steps to transform a product concept into a complete, technically sound PRD using the template provided in `assets/prd-template.md`.

## Step 1: Context Gathering
1.  Read `references/creation-guide.md` to internalize the 10-step Architectural-PM workflow.
2.  Analyze the user's initial input to identify the primary mission and target market.
3.  **Halt and Query:** Before drafting, ask the user 5-7 strategic questions focusing on the "Big Picture" (market gaps, AI strategy, and critical data constraints).

## Step 2: Strategic Alignment (Phases 1 & 2)
1.  Define the product persona (e.g., Companion vs. Professional Tool).
2.  Perform a gap analysis based on user-provided competitor documentation.
3.  Establish the "Technical Anchor." Identify non-negotiables such as data precision, isolation levels, or mandatory audit trails.

## Step 3: Architectural Foundation (Phase 3)
1.  Define the tech stack (Frontend, Backend, Database).
2.  Establish Data Integrity Rules (e.g., "No floating-point math for calculations").
3.  Apply the **James Persona** principles: Holistic thinking, patterns-first, and security at every layer.

## Step 4: Functional Decomposition (Phase 4)
1.  Break the requirements into cohesive feature modules.
2.  Define AI/Interface interactions (raw data vs. structured JSON for Generative UI).

## Step 5: Roadmap Planning (Phase 5)
1.  Sequence features into logical Epics (Infrastructure -> Core -> Planning -> Intelligence).
2.  Verify that all "Units of Work" are atomic and executable in a single session.

## Step 6: Template Execution
1.  Open `assets/prd-template.md`.
2.  Populate every section of the template with the data generated in the previous steps.
3.  Ensure the tone remains professional, technically deep, and pragmatic.
4.  Verify that all math or technical specifications use LaTeX-style syntax for clarity.

## Step 7: Final Review
1.  Cross-reference the generated PRD against the "Technical Anchor" defined in Step 2.
2.  Confirm that the roadmap aligns with the stated business goals.
