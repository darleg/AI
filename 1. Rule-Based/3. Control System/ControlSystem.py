"""
Rule-Based Control System Example
----------------------------------
This program demonstrates a simple forward-chaining rule-based control system.
It evaluates sensor inputs against predefined rules and triggers control actions.
"""

from typing import Callable, Dict, Any, List


class Rule:
    """Represents a control rule with a condition and an action."""
    def __init__(self, name: str, condition: Callable[[Dict[str, Any]], bool], action: Callable[[Dict[str, Any]], None]):
        self.name = name
        self.condition = condition
        self.action = action

    def evaluate(self, facts: Dict[str, Any]) -> bool:
        """Check if the rule's condition is satisfied."""
        try:
            return self.condition(facts)
        except Exception as e:
            print(f"[ERROR] Rule '{self.name}' condition failed: {e}")
            return False

    def execute(self, facts: Dict[str, Any]) -> None:
        """Execute the rule's action."""
        try:
            self.action(facts)
        except Exception as e:
            print(f"[ERROR] Rule '{self.name}' action failed: {e}")


class RuleEngine:
    """Manages and executes rules based on facts."""
    def __init__(self):
        self.rules: List[Rule] = []

    def add_rule(self, rule: Rule) -> None:
        self.rules.append(rule)

    def run(self, facts: Dict[str, Any]) -> None:
        """Forward-chaining: check all rules and execute those whose conditions are met."""
        for rule in self.rules:
            if rule.evaluate(facts):
                print(f"[INFO] Rule triggered: {rule.name}")
                rule.execute(facts)


# Example control actions
def turn_on_fan(facts: Dict[str, Any]) -> None:
    print("Action: Fan turned ON to cool down temperature.")
    facts["fan_status"] = "ON"

def turn_off_fan(facts: Dict[str, Any]) -> None:
    print("Action: Fan turned OFF.")
    facts["fan_status"] = "OFF"

def sound_alarm(facts: Dict[str, Any]) -> None:
    print("Action: Alarm sounded due to high temperature!")
    facts["alarm_status"] = "ON"


# Example usage
if __name__ == "__main__":
    # Initial facts (sensor readings)
    facts = {
        "temperature": 35,  # Celsius
        "fan_status": "OFF",
        "alarm_status": "OFF"
    }

    # Create rule engine
    engine = RuleEngine()

    # Add rules
    engine.add_rule(Rule(
        name="Turn on fan if temperature > 30°C",
        condition=lambda f: f["temperature"] > 30 and f["fan_status"] == "OFF",
        action=turn_on_fan
    ))

    engine.add_rule(Rule(
        name="Sound alarm if temperature > 40°C",
        condition=lambda f: f["temperature"] > 40,
        action=sound_alarm
    ))

    engine.add_rule(Rule(
        name="Turn off fan if temperature < 25°C",
        condition=lambda f: f["temperature"] < 25 and f["fan_status"] == "ON",
        action=turn_off_fan
    ))

    # Run the engine
    print("[INFO] Initial facts:", facts)
    engine.run(facts)
    print("[INFO] Updated facts:", facts)
