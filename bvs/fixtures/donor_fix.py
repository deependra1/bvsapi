import json
from datetime import datetime


donor_names = [
    "The Kadoorie Charitable Foundation",
    "Helping Hand",
    "Impact Marathon Foundation",
    "Nepal Britain Society",
    "Cheep Burry",
    "Stepfamilies",
    "Carrol Service",
    "British Embassy",
    "BullDOG Trust",
    "Krijn(Stichting Nepal)",
    "Jackie Sherwood",
    "Sue Elizabeth Lawrence",
    "Shannan Miller",
    "Chance For Nepal(Emergency Fund)",
    "Kathrin Hagan",
    "ActionAid Nepal",
    "Betty Woodsend",
    "WENDY MARSTON",
    "Tanner Trust"

]

donors = []
for index, donor_name in enumerate(donor_names):
    religion = {
        "model": "bvs_donor.Donor",
        "pk": index + 1,
        "fields": {
            "donor_name": donor_name,
            "created": datetime.now().strftime("%Y-%m-%d"),
            "updated": datetime.now().strftime("%Y-%m-%d")
        }
    }
    donors.append(religion)

with open("donors.json", "w") as donors_file:
    json.dump(donors, donors_file, indent=4)
