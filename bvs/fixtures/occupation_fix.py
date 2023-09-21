import json
from datetime import datetime


occupation_names = ["Farmer", "Teacher", "Construction worker", "Hotelier", "Government jobs", "Tour guide", "Retailer", "Healthcare Workers", "Businesses", "House wife"]

occupations = []
for index, occupation_name in enumerate(occupation_names):
    religion = {
        "model": "bvs_occupation.Occupation",
        "pk": index + 1,
        "fields": {
            "occupation_name": occupation_name,
            "created": datetime.now().strftime("%Y-%m-%d"),
            "updated": datetime.now().strftime("%Y-%m-%d")
        }
    }
    occupations.append(religion)

with open("occupations.json", "w") as occupations_file:
    json.dump(occupations, occupations_file, indent=4)
