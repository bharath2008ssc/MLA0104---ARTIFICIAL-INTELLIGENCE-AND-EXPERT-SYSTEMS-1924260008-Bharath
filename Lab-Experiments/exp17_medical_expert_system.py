"""
Experiment 17: Medical Expert System
Scenario: A healthcare expert system assists doctors by identifying diseases from patient symptoms.
Expected Outcome: Infer diseases using rule-based reasoning.
"""

DISEASE_RULES = [
    {"disease": "Influenza (Flu)", "symptoms": {"fever", "cough", "body_ache", "fatigue"}},
    {"disease": "Common Cold", "symptoms": {"sneezing", "runny_nose", "sore_throat"}},
    {"disease": "Dengue Fever", "symptoms": {"high_fever", "severe_headache", "joint_pain", "rash"}},
    {"disease": "Migraine", "symptoms": {"severe_headache", "nausea", "light_sensitivity"}}
]

def diagnose_patient(patient_symptoms):
    patient_set = set(s.lower().strip() for s in patient_symptoms)
    matches = []

    for rule in DISEASE_RULES:
        matched = rule["symptoms"].intersection(patient_set)
        confidence = (len(matched) / len(rule["symptoms"])) * 100
        if matched:
            matches.append((confidence, rule["disease"], matched))

    matches.sort(reverse=True)
    return matches

if __name__ == "__main__":
    observed_symptoms = ["high_fever", "joint_pain", "rash", "fatigue"]
    print("Patient Symptoms:", observed_symptoms)
    print("
--- Diagnostic Inference Results ---")
    for confidence, disease, matched in diagnose_patient(observed_symptoms):
        print(f"Disease: {disease} | Match Confidence: {confidence:.1f}% | Matched Symptoms: {list(matched)}")
