import subprocess
import json
import re

def estimate_nutrition_with_ollama(meal_description):
    prompt = f"""
    Estimate the total calories, protein (g), carbs (g), and fat (g) in this meal:

    "{meal_description}"

    Return ONLY a valid JSON object, no explanation, no markdown, just:
    {{
        "calories": 500,
        "protein_g": 25,
        "carbs_g": 40,
        "fat_g": 20
    }}
    """

    result = subprocess.run(
        ["ollama", "run", "llama2"],
        input=prompt.encode(),
        capture_output=True
    )

    raw_output = result.stdout.decode().strip()

    # Clean up markdown/code block formatting if present
    cleaned_output = re.sub(r"```(json)?", "", raw_output).strip()

    try:
        parsed = json.loads(cleaned_output)
        return parsed, raw_output
    except json.JSONDecodeError:
        print("❌ Could not parse LLM response — saving raw anyway.")
        return None, raw_output
