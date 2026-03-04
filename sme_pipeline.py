def process_sme(applicant):
    score = applicant["cibil"] + (applicant["dscr"] * 50)
    risk = "Low" if score > 800 else "Medium" if score > 700 else "High"
    return score, risk
