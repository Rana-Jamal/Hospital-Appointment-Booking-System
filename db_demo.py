from __future__ import annotations

from database import engine
from sqlalchemy import text

def run_sql(query: str):
    with engine.begin() as conn:
        result = conn.execute(text(query))
        return result.fetchall() if result.returns_rows else result.rowcount

query = """
INSERT INTO appointments (patient_name, reason, start_time, canceled, created_at)
VALUES ('JOHN DOE', 'Checkup', '2026-01-24 14:30:00', 0, datetime('now'));
"""

print(run_sql(query))
print(run_sql("SELECT * FROM appointments;"))