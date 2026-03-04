import requests

SARVAM_KEY = "sk_rc853rl4_5uIuUN2Brd sme_retail_loan  kpKFqZia1T10vV" # API KEy : sk_rc853rl4_5uIuUN2Brd sme_retail_loan  kpKFqZia1T10vV - 5-3-2026 : 02:17 AM | sme_retail_loan

def translate_text(text):
    try:
        r = requests.post(
            "https://api.sarvam.ai/v1/translate",
            headers={
                "Authorization": f"Bearer {SARVAM_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "input": text,
                "source_language": "en",
                "target_language": "hi"
            }
        )
        if r.status_code == 200:
            return r.json().get("translated_text", "Error")
        return "API Error"
    except:
        return "Translation Failed"
