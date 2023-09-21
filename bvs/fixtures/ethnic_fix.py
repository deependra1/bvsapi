import json
from datetime import datetime

ethnic_type_names = ["Brahman/Chhetri/Thakuri/Sanyasi(Dasnami) Hill", "Aadibasi/Janajati Hill", "Dalit Hill", "Backward Region", "Madhesi"]

ethnic_groups = []
for index, ethnic_type_name in enumerate(ethnic_type_names):
    ethnic_group = {
        "model": "bvs_ethnic.Ethnic",
        "pk": index + 1,
        "fields": {
            "ethnic_group": ethnic_type_name,
            "created": datetime.now().strftime("%Y-%m-%d"),
            "updated": datetime.now().strftime("%Y-%m-%d")
        }
    }
    ethnic_groups.append(ethnic_group)

with open("ethnic.json", "w") as ethnic_file:
    json.dump(ethnic_groups, ethnic_file, indent=4)
