import json
import random
from faker import Faker
from datetime import datetime

fake = Faker()


# Function to generate a random date within a given range
def random_date(start_date, end_date):
    random_datetime = fake.date_between_dates(date_start=start_date, date_end=end_date)
    return random_datetime.strftime("%Y-%m-%d")


def reg_no():
    fiscal_year = fake.random_element(elements=("2019", "2020", "2021", "2022", "2025"))
    registration_location = fake.random_element(elements=("KTM", "NPG", "JNP"))
    num = fake.ssn()
    return fiscal_year + "-" + registration_location + "-" + num


# Generate 1000 Patient fixtures
patients = []
for _ in range(100):
    patient = {
        "model": "bvs_patient.Patient",
        "pk": _ + 1,
        "fields": {
            "creator": 1,
            "registration_date": random_date(datetime(2020, 1, 1), datetime(2023, 1, 1)),
            "fiscal_year": fake.random_element(elements=("2019", "2020", "2021", "2022", "2025")),
            "registration_location": fake.random_element(elements=("KTM", "NPG", "JNP")),
            "registration_number": reg_no(),
            # Add other patient fields here
            "fname": fake.first_name(),
            "lname": fake.last_name(),
            "country": "Nepal",
            "provence": fake.random_element(
                elements=("Koshi", "Madhesh", "Bagmati", "Gandaki", "Lumbini", "Karnali", "Sudurpashchim")),
            "district": fake.random_element(
                elements=("Jhapa", "Siraha", "Parsa", "Tanahu", "Dang", "Banke", "Surkhet")),
            "local": fake.random_element(
                elements=("Biratnagar", "Kathmandu", "Dhangadi", "Nepalgung", "Pokhara", "Bharatpur", "Butwal")),
            "ward": random.randint(1, 37),
            "tole": fake.random_element(
                elements=("Sundarbasti", "Makhan Tole", "Dafechari Marga", "Sahid Chowk", "Gaida Chowk", "Baneshwor",
                          "Sankhamul")),
            # "foreign_address":,

            "country2": "Nepal",
            "provence2": fake.random_element(
                elements=("Koshi", "Madhesh", "Bagmati", "Gandaki", "Lumbini", "Karnali", "Sudurpashchim")),
            "district2": fake.random_element(
                elements=("Jhapa", "Siraha", "Parsa", "Tanahu", "Dang", "Banke", "Surkhet")),
            "local2": fake.random_element(
                elements=("Biratnagar", "Kathmandu", "Dhangadi", "Nepalgung", "Pokhara", "Bharatpur", "Butwal")),
            "ward2": random.randint(1, 37),
            "tole2": fake.random_element(
                elements=("Sundarbasti", "Makhan Tole", "Dafechari Marga", "Sahid Chowk", "Gaida Chowk", "Baneshwor",
                          "Sankhamul")),
            # "foreign_address2":,

            "date_of_birth": random_date(datetime(1970, 1, 1), datetime(2023, 1, 1)),
            "age_at_incident": random.randint(1, 100),
            "month_at_incident": random.randint(1, 12),
            "gender": fake.random_element(elements=("Male", "Female", "Other")),
            "citizenship_no": fake.license_plate(),
            "patient_contact": random.randint(9800000000, 9899999999),
            "optional_contact": random.randint(9800000000, 9899999999),
            "parents_contact": random.randint(9800000000, 9899999999),
            # "patient_education": "",
            # "patient_language": "",

            "patient_occupation": random.randint(1, 6),
            "suppose_occupation": random.randint(1, 6),
            "parents_occupation": random.randint(1, 6),

            "ethnic_group": random.randint(1, 5),
            "religion": random.randint(1, 5),
            "family_type": random.randint(1, 5),

            "material_status": fake.random_element(elements=("Married", "Unmarried", "Divorced")),
            "number_of_child": random.randint(1, 6),
            "number_of_siblings": random.randint(1, 6),

            # "economic_status": "",
            # "echo_other": "",
            # "family_support": "",
            # "pregnant_women": "",
            # "lactating_mother": "",
            # "with_disabilities": "",
            # "mental_illness": "",
            # "epilepsy": "",
            # "hiv_positive": "",

            "date_of_incident": random_date(datetime(1970, 1, 1), datetime(2023, 1, 1)),
            # "area_of_burn": "",
            # "percentage_of_burn": "",
            # "degree_of_burn": "",

            "burn_cause": random.randint(1, 5),
            "burn_type": random.randint(1, 5),

            # "place_of_incident": "",
            # "description_of_incident": "",
            # "person_at_hospital": "",
            # "relation_to_parent": "",
            # "person_contact": "",
            "created": datetime.now().strftime("%Y-%m-%d"),
            "updated": datetime.now().strftime("%Y-%m-%d")
        }
    }
    patients.append(patient)

with open("patients.json", "w") as patient_file:
    json.dump(patients, patient_file, indent=4)
