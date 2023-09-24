import json
import random
from faker import Faker
from datetime import datetime

fake = Faker()


# Function to generate a random date within a given range
def random_date(start_date, end_date):
    random_datetime = fake.date_between_dates(date_start=start_date, date_end=end_date)
    return random_datetime.strftime("%Y-%m-%d")


# Generate 1000 Patient fixtures
treatments = []
for _ in range(500):
    treatment = {
        "model": "bvs_treatment.Treatment",
        "pk": _ + 1,
        "fields": {
            "patient": random.randint(1, 100),
            "mode_of_transport": fake.random_element(elements=("Car", "Bus", "Walk", "Plane")),
            "distance": random.randint(1, 50),
            "duration_of_stay": random.randint(1, 10),
            "hospital": fake.company(),
            "hospitalized_date": random_date(datetime(2020, 1, 1), datetime(2023, 1, 1)),
            "doctor_name": fake.name(),
            "dischared_date": random_date(datetime(2020, 1, 1), datetime(2023, 1, 1)),
            "no_of_surgery": random.randint(1, 10),
            "no_of_skin_graft": random.randint(1, 10),
            "no_of_debridement": random.randint(1, 10),
            "no_of_amputation": random.randint(1, 10),
            "no_of_dressing": random.randint(1, 10),
            "no_of_nutritional": random.randint(1, 10),
            "medical_support": random.randint(1, 10),
            "created": datetime.now().strftime("%Y-%m-%d"),
            "updated": datetime.now().strftime("%Y-%m-%d")
        }
    }
    treatments.append(treatment)

# Generate 1000 Funding fixtures
fundings = []
for _ in range(500):
    funding = {
        "model": "bvs_funding.Funding",
        "pk": _ + 1,
        "fields": {
            "patient": random.randint(1, 100),
            "donor": random.randint(1, 19),
            "service_title": fake.random_element(elements=(
                "Skin graft", "Surgery", "Debridement", "Amputation", "Dressing", "Nutritional", "Medical support")),
            "funding_amount": round(random.uniform(100, 100000), 2),
            "created": datetime.now().strftime("%Y-%m-%d"),
            "updated": datetime.now().strftime("%Y-%m-%d")

        }
    }
    fundings.append(funding)

# Generate 1000 Funding fixtures
reintegrations = []
for _ in range(500):
    reintegration = {
        "model": "bvs_reintegration.Reintegration",
        "pk": _ + 1,
        "fields": {
            "patient": random.randint(1, 100),
            "question": random.randint(1, 15),
            "answer": fake.sentence(),
            "created": datetime.now().strftime("%Y-%m-%d"),
            "updated": datetime.now().strftime("%Y-%m-%d")

        }
    }
    reintegrations.append(reintegration)

# Generate 1000 Physiotherapy fixtures
physiotherapies = []
for _ in range(500):
    physiotherapy = {
        "model": "bvs_physiotherapy.Physiotherapy",
        "pk": _ + 1,
        "fields": {
            "patient": random.randint(1, 100),
            "initial_status": fake.paragraph(),
            "applied_methods": fake.paragraph(),
            "dischared_status": fake.paragraph(),
            "observation": fake.paragraph(),
            "current_status": fake.paragraph(),
            "mode_of_followup": fake.paragraph(),
            "followed_by": fake.name(),
            "created": datetime.now().strftime("%Y-%m-%d"),
            "updated": datetime.now().strftime("%Y-%m-%d")
        }
    }
    physiotherapies.append(physiotherapy)

# Generate 1000 Psychosocial fixtures
psychosocials = []
for _ in range(500):
    psychosocial = {
        "model": "bvs_pshychosocial.Psychosocial",
        "pk": _ + 1,
        "fields": {
            "patient": random.randint(1, 100),
            "client_history": fake.paragraph(),
            "client_complain": fake.paragraph(),
            "intervention": fake.paragraph(),
            "changes_after_intervention": fake.paragraph(),
            "detailed_followup_report": fake.paragraph(),
            "followup_summary": fake.paragraph(),
            "mode_of_followup": fake.paragraph(),
            "followed_by": fake.name(),
            "created": datetime.now().strftime("%Y-%m-%d"),
            "updated": datetime.now().strftime("%Y-%m-%d")
        }
    }
    psychosocials.append(psychosocial)



with open("treatments.json", "w") as treatment_file:
    json.dump(treatments, treatment_file, indent=4)

with open("fundings.json", "w") as funding_file:
    json.dump(fundings, funding_file, indent=4)

with open("physiotherapies.json", "w") as physiotherapy_file:
    json.dump(physiotherapies, physiotherapy_file, indent=4)

with open("psychosocials.json", "w") as psychosocial_file:
    json.dump(psychosocials, psychosocial_file, indent=4)

with open("reintegrations.json", "w") as reintegration_file:
    json.dump(reintegrations, reintegration_file, indent=4)
