SCHEMA_DESCRIPTION = """
Tables:

users:
- id (integer)
- name (varchar)
- email (varchar)
- created_at (timestamp)

orders:
- id (integer)
- user_id (integer)
- amount (numeric)
- status (varchar)
- created_at (timestamp)
"""
