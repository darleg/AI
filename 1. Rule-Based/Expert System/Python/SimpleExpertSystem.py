# Simple Expert System for diagnosing flu or cold
# Author: Senior Programming Expert

# Knowledge base: rules and facts
knowledge_base = [
    {"if": {"fever", "cough", "body_ache"}, "then": "flu"},
    {"if": {"cough", "sneezing", "runny_nose"}, "then": "cold"},
    {"if": {"fever", "cough"}, "then": "possible flu"},
    {"if": {"sneezing", "runny_nose"}, "then": "possible cold"}
]

def forward_chaining(facts):
    """
    Forward chaining inference engine.
    facts: set of known facts (symptoms)
    returns: set of inferred conclusions
    """
    inferred = set()
    applied_rules = True

    while applied_rules:
        applied_rules = False
        for rule in knowledge_base:
            # Check if all conditions are met
            if rule["if"].issubset(facts) and rule["then"] not in inferred:
                inferred.add(rule["then"])
                facts.add(rule["then"])
                applied_rules = True
    return inferred

def main():
    print("=== Simple Medical Expert System ===")
    print("Enter symptoms separated by commas (e.g., fever,cough,body_ache)")
    user_input = input("Symptoms: ").strip().lower()

    # Input validation
    if not user_input:
        print("No symptoms entered. Exiting.")
        return

    # Convert input to a set of facts
    facts = {sym.strip().replace(" ", "_") for sym in user_input.split(",") if sym.strip()}

    # Run inference
    conclusions = forward_chaining(facts)

    # Output results
    if conclusions:
        print("\nPossible diagnosis based on symptoms:")
        for c in conclusions:
            print(f"- {c}")
    else:
        print("\nNo diagnosis could be made with the given symptoms.")

if __name__ == "__main__":
    main()
