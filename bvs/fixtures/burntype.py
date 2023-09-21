import json
import random
from faker import Faker
from datetime import datetime

fake = Faker()


def random_date(start_date, end_date):
    random_datetime = fake.date_between_dates(date_start=start_date, date_end=end_date)
    return random_datetime.strftime("%Y-%m-%d")


burn_types = []
for _ in range(9):
    burn_type = {
        "model": "bvs_burntype.BurnType",
        "pk": _ + 1,
        "fields": {
            "burn_type": fake.random_element(
                elements=("Accident", "Attempted Suicide", "Domestic Violence", "Acid Attack", "Other")),
            "created": datetime.now().strftime("%Y-%m-%d"),
            "updated": datetime.now().strftime("%Y-%m-%d")

        }
    }
    burn_types.append(burn_type)

    with open("burn_types.json", "w") as burn_types_file:
        json.dump(burn_types, burn_types_file, indent=4)
