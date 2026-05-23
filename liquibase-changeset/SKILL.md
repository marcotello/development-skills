---
name: liquibase-changeset
description: Manages version-controlled database migrations using Liquibase. Enforces strict 3-digit naming, SQL-based changesets, and a specific folder hierarchy (/database/liquibase/). Use this when creating or modifying schema elements (tables, procedures, indexes).
---

# Liquibase Migration Procedure

Follow these steps to generate and organize database migrations according to the project's strict architectural standards.

## Step 1: Identity & Metadata Setup
1.  **Check for Author:** Scan `/database/liquibase/liquibase.properties` for the `author` property.
2.  **Halt and Query:** If the `author` is not defined (e.g., `author=` is empty), ask the user: *"Please provide the author name for the migrations (e.g., marcotello) so I can save it to your properties file."*
3.  **Persist Author:** Once provided, write `author=[name]` directly into `/database/liquibase/liquibase.properties`.
4.  Generate Timestamp: Generate a unique 14-digit timestamp using the format `YYYYMMDDHHMMSS` (e.g., `20260523134500`). If generating multiple migrations at once, increment the seconds to ensure uniqueness and preserve order.

## Step 2: Repository Hierarchy Verification
Ensure the following structure exists before proceeding:
- `/database/liquibase/` - The root for Liquibase logic.
- `/database/liquibase/changes/` - Folder for all vertical migration files.
- `/database/liquibase/test-data/` - Folder for seed data.
- `/database/liquibase/changelog-master.xml` - The main entry point for schema changes.

## Step 3: Drafting the Changeset
1.  File Naming: Create a new XML file in `/database/liquibase/changes/` using: `[TIMESTAMP]-[meaningful-name].xml` (e.g., `20260523134500-create-accounts-table.xml`).
2.  ID & Author: Set `id` to the `YYYYMMDDHHMMSS` timestamp (e.g., `id="20260523134500"`) and `author` to the name persisted in properties.
3.  **Mandatory SQL:** Use `<sql>` tags. Do not use XML abstractions for DDL.
4.  **Rollback:** Add a `<rollback>` block with the specific SQL to undo the change.

## Step 4: Master Integration
1.  Open `/database/liquibase/changelog-master.xml`.
2.  Add an `<include file="changes/[filename].xml"/>` entry.
3.  For test data, place files in `/test-data/` following the same YYYYMMDDHHMMSS timestamp prefix naming convention, and register them under the appropriate changelog.

---

# Liquibase Standards Guide 

### 1. The Timestamp Prefix Rule
Files must start with a 14-digit timestamp in `YYYYMMDDHHMMSS` format (e.g., `20260523134500`). This ensures that files are globally unique, sort chronologically, and prevent merge conflicts in collaborative environments. This applies to all changeset files, including structural migrations (under `/changes/`) and seed/test data files (under `/test-data/`).

### 2. SQL-First Philosophy
We do not use Liquibase XML "helpers" (e.g., `<createTable>`). We write raw, optimized PostgreSQL SQL. This provides absolute control over performance-critical features like constraints and index types.

### 3. Defensive DDL and DML (Idempotency)
Every migration must be "re-runnable" without error.
- **Mandatory DDL:** Always check if the table, stored procedure, function, or index exists before creating, altering, or dropping it.
  - **Example:** `CREATE TABLE IF NOT EXISTS table_name (...)`, `ALTER TABLE IF EXISTS table_name ...`, `DROP TABLE IF EXISTS table_name`.
- **Mandatory DML:** Always check if the table exists before running `INSERT`, `UPDATE`, or `DELETE` operations to prevent errors if the table is missing.

### 4. Single-Table Changeset Isolation (ACID)
Every changeset must target only one single table. Do not combine operations (CREATE, ALTER, DROP, INSERT, UPDATE, DELETE) targeting different tables inside the same changeset. This ensures maximum transactional atomicity (ACID), prevents locking conflicts across distinct entities, and guarantees clean, granular rollback capabilities.

### 5. Mandatory Rollbacks
A migration without a rollback is a "breaking change." You must always provide the inverse operation in a `<rollback>` tag to ensure the database can be reverted to a previous state safely.

### 6. Financial Grade Precision
Never use `FLOAT` or `REAL` for monetary values. All currency-related columns must use `NUMERIC(19, 2)` to prevent floating-point rounding errors.

### 7. Relational Integrity
When defining foreign keys, explicitly define the behavior: `ON DELETE CASCADE` for parent-child ownership or `SET NULL` for loose references.

### 8. References
 - For detailed folder structure, see [references/file-structure.md](references/file-structure.md).
 - For changeset template, see [references/changeset-template.md](references/changeset-template.md).
