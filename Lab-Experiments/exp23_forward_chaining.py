"""
Experiment 23: Forward Chaining
Scenario: A technical support system diagnoses computer faults by applying known rules to user inputs.
Expected Outcome: Derive conclusions from available facts.
"""

def forward_chaining(rules, initial_facts):
    facts = set(initial_facts)
    inference_steps = []
    added = True

    while added:
        added = False
        for conditions, conclusion in rules:
            if conditions.issubset(facts) and conclusion not in facts:
                facts.add(conclusion)
                inference_steps.append(f"Rule Fired: IF {list(conditions)} THEN '{conclusion}'")
                added = True

    return facts, inference_steps

if __name__ == "__main__":
    tech_support_rules = [
        ({"no_power_led", "power_cable_plugged"}, "faulty_power_supply"),
        ({"power_led_on", "no_display"}, "display_output_issue"),
        ({"display_output_issue", "beep_codes"}, "ram_seating_fault"),
        ({"ram_seating_fault"}, "recommend_reseat_ram_modules")
    ]

    user_reported_facts = ["power_led_on", "no_display", "beep_codes"]
    final_facts, trace = forward_chaining(tech_support_rules, user_reported_facts)

    print("Initial Symptoms:", user_reported_facts)
    print("
--- Forward Chaining Inference Trace ---")
    for step in trace:
        print(step)
    print("
Final Derived Facts:", final_facts)
