# Liquibase Standards & Directory Blueprint

### Folder Hierarchy

```text
/database/
├── liquibase/
│   ├── changelog-master.xml          # Main entry point
│   ├── liquibase.properties.example  # DB Property Template
│   ├── changes/                      # Vertical migration files
│   └── test-data/                    # Seed data for Dev/Test
│       ├── changelog-test-data.xml   # Test data entry point
│       └── [category]/               # Subfolders (users, accounts, etc.)

```
