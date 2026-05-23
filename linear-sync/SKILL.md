---
name: linear-sync
description: Manage project hierarchy in Linear by adding or updating Epics, Stories, and Subtasks. Use when syncing decomposed backlog items to Linear to maintain the 3-level visual hierarchy (Epic -> Story -> Subtask).
---

# Linear Sync

This skill enables the systematic management of the **Signal Sphere** project hierarchy within Linear. It ensures that every architectural decision and granular unit of work is visually traceable and ready for implementation.

## Hierarchy Levels

1.  **Epics (Level 1):** High-level initiatives representing major system phases.
    - **Format:** `Epic [X.X]: [Name]`
2.  **Stories (Level 2):** Feature-specific requirements linked to an Epic.
    - **Format:** `[Epic X.X] ST-[X.X.X]: [Name]`
    - **Parent:** Must be linked to an Epic ID using `parentId`.
3.  **Subtasks (Level 3):** Atomic Units of Work linked to a Story.
    - **Format:** `[ST-X.X.X] [Index]. [Name]`
    - **Parent:** Must be linked to a Story ID using `parentId`.

## Guidelines

### 1. Create vs. Update
- **Create:** If an entity does not have a Linear ID in the local `LINEAR_MAPPING.md`, use `mcp_linear_save_issue` without an `id`.
- **Update:** If an ID exists, always pass the `id` parameter to `mcp_linear_save_issue` to modify the existing issue.

### 2. Parent-Child Integrity
- Before creating Stories, ensure the parent Epic ID is known.
- Before creating Subtasks, ensure the parent Story ID is known.
- Always pass the `parentId` to establish the hierarchy in Linear's sub-issue view.

### 3. Detailed Descriptions
Include all relevant context in the Linear issue description:
- **For Stories:** Include "Story Description" and "Acceptance Criteria".
- **For Subtasks:** Include "Technical Context" and "Implementation Checklist".

### 4. Local Traceability
After every sync operation (create or update), update the local `LINEAR_MAPPING.md` file in the relevant Epic directory to ensure the documentation stays in sync with Linear.

## Usage Patterns

### Add Epic with Stories
1. Create the Epic issue.
2. Capture the returned ID.
3. Iteratively create each Story as a sub-issue of that ID.

### Add Subtasks to Existing Story
1. Look up the Story ID from `LINEAR_MAPPING.md`.
2. Iteratively create Subtasks using that ID as the `parentId`.

### Update Existing Entity
1. Pass the existing Linear ID.
2. Update the `description` or `title` based on the latest architectural decomposition.
