"""
Experiment 20: Person DOB Knowledge Base
Scenario: A citizen information portal retrieves personal details using date of birth records.
Expected Outcome: Query stored facts using logical reasoning.
"""

from datetime import date

CITIZEN_RECORDS = [
    {"id": "CIT101", "name": "Arun Kumar", "dob": date(1998, 5, 14), "city": "Chennai"},
    {"id": "CIT102", "name": "Priya Nair", "dob": date(2005, 11, 22), "city": "Coimbatore"},
    {"id": "CIT103", "name": "Vikram Rao", "dob": date(1962, 3, 9), "city": "Madurai"},
    {"id": "CIT104", "name": "Meera Iyer", "dob": date(1998, 5, 14), "city": "Chennai"}
]

def calculate_age(dob, ref_date=date(2026, 11, 16)):
    return ref_date.year - dob.year - ((ref_date.month, ref_date.day) < (dob.month, dob.day))

def find_by_dob(target_dob):
    return [rec for rec in CITIZEN_RECORDS if rec["dob"] == target_dob]

def find_senior_citizens():
    return [rec for rec in CITIZEN_RECORDS if calculate_age(rec["dob"]) >= 60]

if __name__ == "__main__":
    search_date = date(1998, 5, 14)
    print(f"Citizens born on {search_date}:")
    for person in find_by_dob(search_date):
        print(f" - {person['name']} ({person['id']}), Age: {calculate_age(person['dob'])}, City: {person['city']}")

    print("
Eligible Senior Citizens (Age >= 60):")
    for senior in find_senior_citizens():
        print(f" - {senior['name']} (Age: {calculate_age(senior['dob'])})")
