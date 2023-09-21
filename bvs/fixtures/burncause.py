import json
import random
from faker import Faker
from datetime import datetime

fake = Faker()


def random_date(start_date, end_date):
    random_datetime = fake.date_between_dates(date_start=start_date, date_end=end_date)
    return random_datetime.strftime("%Y-%m-%d")


burn_causes = []
for _ in range(5):
    burn_cause = {
        "model": "bvs_burncause.BurnCause",
        "pk": _ + 1,
        "fields": {
            "burn_cause": fake.random_element(
                elements=("Accident", "Attempted Suicide", "Domestic Violence", "Acid Attack", "Other")),
            "created": datetime.now().strftime("%Y-%m-%d"),
            "updated": datetime.now().strftime("%Y-%m-%d")

        }
    }
    burn_causes.append(burn_cause)

    with open("burn_causes.json", "w") as burn_causes_file:
        json.dump(burn_causes, burn_causes_file, indent=4)
