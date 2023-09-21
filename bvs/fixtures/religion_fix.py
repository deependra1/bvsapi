import json
from datetime import datetime


religion_names = ["Hindu", "Buddhist", "Muslim", "Kiratist(indigenous ethnic religion)", "Christian", "Sikhs", "Jains"]

religions = []
for index, religion_name in enumerate(religion_names):
    religion = {
        "model": "bvs_religion.Religion",
        "pk": index + 1,
        "fields": {
            "religion": religion_name,
            "created": datetime.now().strftime("%Y-%m-%d"),
            "updated": datetime.now().strftime("%Y-%m-%d")
        }
    }
    religions.append(religion)

with open("religions.json", "w") as religion_file:
    json.dump(religions, religion_file, indent=4)
