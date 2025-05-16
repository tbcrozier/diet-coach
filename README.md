# diet-coach

🥗 Diet Coach – AI-Powered Meal Logger
Diet Coach is a Python-based tool that uses a local LLM (via Ollama) to estimate the nutritional content of freeform meal descriptions and logs them to Google BigQuery for long-term tracking and analysis.

✅ Features
🧠 Uses a local LLM (LLaMA 2 via Ollama) — no API keys required

🍽️ Accepts freeform meal descriptions like:
"3 scrambled eggs with toast and a banana"

🔍 Estimates calories, protein, carbs, and fat

📦 Saves meal data to BigQuery, including:

User ID

Timestamp

Original meal text

Parsed nutrition data

Raw LLM response (for traceability)

📈 Enables analytics over time (e.g., daily nutrient totals)

📊 BigQuery Schema
Field	Type	Description
timestamp	DATETIME	When the meal was logged
user_id	STRING	User identifier
meal_description	STRING	Text of what was eaten
calories	FLOAT	Estimated calories
protein_g	FLOAT	Estimated protein (grams)
carbs_g	FLOAT	Estimated carbs (grams)
fat_g	FLOAT	Estimated fat (grams)
raw_response	STRING	Full LLM response text