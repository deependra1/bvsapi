import json
from datetime import datetime


family_types = ["Nuclear families", "Grandparent families", "Single-parent families", "Extended families", "Childless families", "Stepfamilies"]

families = []
for index, family_type in enumerate(family_types):
    religion = {
        "model": "bvs_family.Family",
        "pk": index + 1,
        "fields": {
            "family_type": family_type,
            "created": datetime.now().strftime("%Y-%m-%d"),
            "updated": datetime.now().strftime("%Y-%m-%d")
        }
    }
    families.append(religion)

with open("families.json", "w") as families_file:
    json.dump(families, families_file, indent=4)
