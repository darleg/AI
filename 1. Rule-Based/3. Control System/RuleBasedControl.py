# rule_based_control.py

class RuleBasedControl:
    def __init__(self):
        self.rules = []
        self.facts = []

    def add_rule(self, condition, action):
        """Add a rule: condition -> action"""
        self.rules.append({'condition': condition, 'action': action})

    def add_fact(self, fact):
        """Add a fact to working memory"""
        self.facts.append(fact)

    def evaluate_rules(self):
        """Match rules against facts and execute actions"""
        for rule in self.rules:
            if self.match_condition(rule['condition'], self.facts):
                self.execute_action(rule['action'])

    def match_condition(self, condition, facts):
        """Check if condition matches any fact"""
        # Example: condition is a list of required facts
        return all(fact in facts for fact in condition)

    def execute_action(self, action):
        """Execute the action (can modify facts or trigger outputs)"""
        print(f"Executing action: {action}")

# Example usage
if __name__ == "__main__":
    rbc = RuleBasedControl()

    # Define rules
    rbc.add_rule(['temperature_high'], "activate_cooling_system()")
    rbc.add_rule(['pressure_low'], "activate_pump()")
    rbc.add_rule(['temperature_high', 'pressure_low'], "activate_emergency_shutdown()")

    # Add facts (sensor readings)
    rbc.add_fact("temperature_high")
    rbc.add_fact("pressure_low")

    # Evaluate rules
    rbc.evaluate_rules()
