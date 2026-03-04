import json
import random

cities = ["Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Chennai"]
industries = ["IT", "Manufacturing", "Retail", "Pharma", "Logistics"]

retail = []
sme = []

for i in range(200):
    retail.append({
        "id": f"R{i}",
        "name": f"Retail_User_{i}",
        "city": random.choice(cities),
        "cibil": random.randint(600, 800),
        "foir": random.randint(20, 60),
        "ltv": random.randint(50, 90),
        "dpd": [random.randint(0, 30) for _ in range(6)]
    })

    sme.append({
        "id": f"S{i}",
        "name": f"SME_Company_{i}",
        "industry": random.choice(industries),
        "cibil": random.randint(650, 800),
        "dscr": round(random.uniform(1.0, 2.0), 2),
        "ltv": random.randint(50, 85),
        "dpd": [random.randint(0, 60) for _ in range(6)]
    })

with open("retail_applicants.json", "w") as f:
    json.dump(retail, f)

with open("sme_applicants.json", "w") as f:
    json.dump(sme, f)

print("Generated 200 Retail + 200 SME applicants")
