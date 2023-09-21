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
patients = []
for _ in range(1000):
    patient = {
        "model": "patient.patient",
        "pk": _ + 1,
        "fields": {
            "creator": random.randint(1, 1000),  # Assuming you have User objects with IDs 1 to 1000
            "registration_date": random_date(datetime(2020, 1, 1), datetime(2023, 1, 1)),
            "fiscal_year": fake.random_element(elements=("FY20", "FY21", "FY22")),
            # Convert date_of_birth to a string representation
            "date_of_birth": random_date(datetime(1970, 1, 1), datetime(2005, 1, 1)),
            # Add other patient fields here
        }
    }
    patients.append(patient)

# Generate 1000 Treatment fixtures
treatments = []
for _ in range(1000):
    treatment = {
        "model": "patient.treatment",
        "pk": _ + 1,
        "fields": {
            "patient": random.randint(1, 1000),  # Assuming you have Patient objects with IDs 1 to 1000
            "mode_of_transport": fake.random_element(elements=("Car", "Bus", "Walk")),
            "distance": random.randint(1, 50),
            "duration_of_stay": random.randint(1, 10),
            # Add other treatment fields here
        }
    }
    treatments.append(treatment)

# Generate 1000 Funding fixtures
fundings = []
for _ in range(1000):
    funding = {
        "model": "patient.funding",
        "pk": _ + 1,
        "fields": {
            "patient": random.randint(1, 1000),  # Assuming you have Patient objects with IDs 1 to 1000
            "donor": random.randint(1, 1000),  # Assuming you have Donor objects with IDs 1 to 1000
            "service_title": fake.random_element(elements=("Service A", "Service B", "Service C")),
            "funding_amount": round(random.uniform(100, 10000), 2),
            # Add other funding fields here
        }
    }
    fundings.append(funding)

# Generate 1000 Physiotherapy fixtures
physiotherapies = []
for _ in range(1000):
    physiotherapy = {
        "model": "patient.physiotherapy",
        "pk": _ + 1,
        "fields": {
            "patient": random.randint(1, 1000),  # Assuming you have Patient objects with IDs 1 to 1000
            "initial_status": fake.paragraph(),
            "applied_methods": fake.paragraph(),
            # Add other physiotherapy fields here
        }
    }
    physiotherapies.append(physiotherapy)

# Generate 1000 Psychosocial fixtures
psychosocials = []
for _ in range(1000):
    psychosocial = {
        "model": "patient.psychosocial",
        "pk": _ + 1,
        "fields": {
            "patient": random.randint(1, 1000),  # Assuming you have Patient objects with IDs 1 to 1000
            "client_history": fake.paragraph(),
            "client_complain": fake.paragraph(),
            # Add other psychosocial fields here
        }
    }
    psychosocials.append(psychosocial)

# Save the fixtures to JSON files
with open("patients.json", "w") as patient_file:
    json.dump(patients, patient_file, indent=4)

with open("treatments.json", "w") as treatment_file:
    json.dump(treatments, treatment_file, indent=4)

with open("fundings.json", "w") as funding_file:
    json.dump(fundings, funding_file, indent=4)

with open("physiotherapies.json", "w") as physiotherapy_file:
    json.dump(physiotherapies, physiotherapy_file, indent=4)

with open("psychosocials.json", "w") as psychosocial_file:
    json.dump(psychosocials, psychosocial_file, indent=4)
