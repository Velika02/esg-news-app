# processor.gpt_extractor.py
# ✅ Use GPT to extract ESG risk information (topic, domain, risk_level)

import openai
import os
import json

# Set OpenAI API Key (ensure you load this from a secure environment variable)
openai.api_key = os.getenv("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")

def extract_esg_signal_from_text(text, model="gpt-4"):
    """
    Use a GPT model to extract structured ESG risk information from a news paragraph.
    Returns fields: topic, esg_domain, risk_level, summary
    """
    prompt = f"""
You are an ESG analyst. From the following news excerpt, extract if there are any ESG-related issues.
Return in JSON format:
[
  {{"topic": ..., "esg_domain": ..., "risk_level": ..., "summary": ...}}
]
Text:
{text}
"""
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        content = response["choices"][0]["message"]["content"]
        return json.loads(content)
    except Exception as e:
        print("❌ GPT extraction failed:", e)
        return []

# ✅ Example run
if __name__ == "__main__":
    sample_text = "Regeneron has been flagged by environmental groups for overuse of chemical solvents in its manufacturing plants."
    results = extract_esg_signal_from_text(sample_text)
    print(json.dumps(results, indent=2))

