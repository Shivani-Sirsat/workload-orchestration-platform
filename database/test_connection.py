import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from database.connection import (
    get_connection
)

conn = get_connection()

print(
    "Connected to PostgreSQL"
)

conn.close()