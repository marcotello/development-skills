### 3. Changeset Template 

```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog
    xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
    http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.4.xsd">

    <changeSet id="[ID]" author="[AUTHOR]">
        <comment>Description of what this change achieves</comment>
        <sql>
            -- Write SQL here with existence checks
            -- Example: CREATE TABLE IF NOT EXISTS table_name (...);
        </sql>
        <rollback>
            <sql>
                -- Write rollback SQL here
                -- Example: DROP TABLE IF EXISTS table_name;
            </sql>
        </rollback>
    </changeSet>
</databaseChangeLog>
```

