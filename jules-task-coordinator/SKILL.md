---
name: jules-task-coordinator
description: Orchestrates sequential software development by decomposing Linear stories into atomic units of work and delegating them to Google Jules. Enforces an API-first priority, ensuring the NestJS/Liquibase backend is complete before Angular v21 UI implementation. Acts as a technical bridge by providing architectural clarification to Jules and maintaining task-to-session state mappings. Use for Signal Sphere repositories. Don't use for parallel feature development.
---

# Jules Task Coordinator

## Procedures

**Step 1: Alignment and Dependency Check**
1. You are going to excecute 
2. Make sure the PRD, Architecture document and Stories are accesible is a folder. If you don't know the path, please ask for those documents. 
3. Read `subtasks.md` to align with the current Story. The user will give you the path to access the file. Ask for the path if the user don't give you the path.
4. Execute `python3 scripts/manage-state.py --action get-next` to identify the next atomic subtask.
5. **Strict Enforcement:** If the subtask belongs to UI (Angular), verify that all related subtasks in API (NestJS) are marked "COMPLETED" in `state/state.json`. If not, halt and notify the user of the dependency blocker.

**Step 2: Atomic Unit Dispatch**
1. Construct a "Unit of Work" prompt following the format in `state/unit-work-template.md` using the subtask's technical context and checklist.
2. **Liquibase Guard:** If the task is API-based and involves data changes, ensure "Task 0" in the checklist is the creation of the Liquibase XML changeset.
3. Execute the delegation: `/jules new "[Prompt]"`
4. Extract the Session ID from the output and run:
   `python3 scripts/manage-state.py --action update --linear-id [ID] --session-id [ID] --repo [Repo_Path]`

**Step 3: Support and Clarification Loop**
1. Poll progress via `/jules status`.
2. If Jules reports a "Blocker," "Ambiguity," or a build failure:
    a. Analyze the logs provided in the status output.
    b. Read PRD and Architecture document to find the deterministic solution.
    c. Output a clear "ARCHITECT DIRECTIVE" for the user to provide to the Jules Cloud Console to unblock the agent.
3. Repeat polling until status is "Completed".

**Step 4: Local Verification and State Closure**
1. Once "Completed," execute the local command `jules teleport [sessionID]` to apply the patch to the local environment for final verification. Please ask for the project path in case you doesn't know where is it. 
2. If the verification is successful, complete the Pull Request in Github via gh. 
3. If the verification is not successful, ask jules to fix the issues in the same session and go to Step 3.
2. Run `python3 scripts/manage-state.py --action complete --linear-id [ID]`.
4. Proceed to Step 1 for the next sequential subtask.

## Error Handling
* **Build Failure:** If NestJS or Angular builds fail, read the logs and issue a "Self-Correction" prompt to Jules before human intervention.
* **State Mismatch:** If `state.json` loses sync, re-run `jules remote list --session` to recover active IDs.
