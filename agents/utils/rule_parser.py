class RuleParser:
    @staticmethod
    def parse_rules(rule_sets: dict):
        parsed = {}
        for rule_name, rules in rule_sets.items():
            parsed[rule_name] = [rule.strip() for rule in rules if isinstance(rule, str) and rule.strip()]
        return parsed