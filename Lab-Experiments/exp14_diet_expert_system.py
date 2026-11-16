"""
Experiment 14: Diet Recommendation Expert System
Scenario: A nutrition application recommends diet plans based on age, BMI, and health conditions.
Expected Outcome: Recommend personalized diet plans using rules.
"""

def recommend_diet(age, weight_kg, height_m, condition):
    bmi = weight_kg / (height_m ** 2)
    recommendations = [f"Calculated BMI: {bmi:.1f}"]

    # Rule base for BMI category
    if bmi < 18.5:
        recommendations.append("Category: Underweight -> High-calorie, protein-rich diet with nuts, dairy, and complex carbs.")
    elif 18.5 <= bmi < 25.0:
        recommendations.append("Category: Normal Weight -> Balanced maintenance diet with whole grains, lean protein, and vegetables.")
    else:
        recommendations.append("Category: Overweight/Obese -> Calorie-deficit, high-fiber diet with low glycemic foods.")

    # Rule base for age
    if age >= 60:
        recommendations.append("Senior Rule: Increase Calcium, Vitamin D, and easily digestible proteins.")
    elif age < 18:
        recommendations.append("Youth Rule: Ensure adequate iron, calcium, and healthy fats for growth.")

    # Rule base for medical conditions
    cond = condition.lower()
    if cond == "diabetes":
        recommendations.append("Condition Rule (Diabetes): Avoid refined sugars; prioritize low-GI foods and leafy greens.")
    elif cond == "hypertension":
        recommendations.append("Condition Rule (Hypertension): Follow DASH diet; restrict sodium intake (<1500mg/day).")
    elif cond == "none":
        recommendations.append("Condition Rule: Stay hydrated (2.5-3L water/day) and maintain regular meal timings.")

    return recommendations

if __name__ == "__main__":
    plan = recommend_diet(age=62, weight_kg=82, height_m=1.70, condition="diabetes")
    print("--- Personalized Diet Expert System Output ---")
    for item in plan:
        print("-", item)
