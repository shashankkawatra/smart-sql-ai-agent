import os
import re
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def clean_sql(sql: str) -> str:
    sql = re.sub(r"```sql", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"```", "", sql)
    return sql.strip()

def generate_sql(prompt: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert SQL generator. "
                    "Return ONLY a valid SQL SELECT query. "
                    "Do not include explanations or markdown."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
        max_tokens=512
    )

    if not response or not response.choices:
        raise RuntimeError("Groq returned empty response")

    content = response.choices[0].message.content
    if not content:
        raise RuntimeError("Groq returned no SQL output")

    return clean_sql(content)
