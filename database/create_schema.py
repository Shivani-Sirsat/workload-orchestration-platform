from database.connection import (
    get_connection
)


conn = get_connection()

cursor = conn.cursor()

with open(
    "database/schema.sql",
    "r"
) as file:

    cursor.execute(
        file.read()
    )

conn.commit()

cursor.close()

conn.close()

print(
    "Schema created successfully"
)