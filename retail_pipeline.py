def process_retail(applicant):
    score = applicant["cibil"] - applicant["foir"]
    risk = "Low" if score > 650 else "Medium" if score > 550 else "High"
    return score, risk
