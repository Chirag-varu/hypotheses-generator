from typing import List, Tuple, Dict, Any
from knowledge_base import rules

Fact = Tuple[str, str, str]  # e.g., ("has_property", "sky", "dark")
Substitution = Dict[str, str]


def match_fact(fact: Fact, condition: Fact) -> Substitution | None:
    """
    Try to match a fact with a condition. Returns the substitution if it matches.
    """
    if len(fact) != 3 or len(condition) != 3:
        return None

    substitution = {}
    for f, c in zip(fact, condition):
        if c.startswith("X"):  # variable
            substitution[c] = f
        elif f != c:
            return None  # mismatch
    return substitution


def substitute(condition: Fact, substitution: Substitution) -> Fact:
    """
    Apply substitution to a condition.
    """
    return tuple(substitution.get(token, token) for token in condition)


def condition_matches(facts: List[Fact], condition: Fact) -> List[Substitution]:
    """
    Find all facts that match the given condition and return list of valid substitutions.
    """
    matches = []
    for fact in facts:
        sub = match_fact(fact, condition)
        if sub is not None:
            matches.append(sub)
    return matches


def merge_substitutions(subs_list: List[Substitution]) -> Substitution | None:
    """
    Merge a list of substitutions. Return None if there's a conflict.
    """
    result = {}
    for sub in subs_list:
        for key, value in sub.items():
            if key in result and result[key] != value:
                return None  # conflict
            result[key] = value
    return result

def apply_forward_chaining(facts: List[Fact], rules: List[Dict[str, Any]]) -> List[Fact]:
    inferred_facts = []
    known_facts = set(facts)

    while True:
        new_inferred = []

        for rule in rules:
            all_substitutions = []

            for condition in rule["conditions"]:
                matches = condition_matches(list(known_facts), condition)
                if not matches:
                    break
                all_substitutions.append(matches)

            # Cartesian product of substitutions for all conditions
            from itertools import product
            for combination in product(*all_substitutions):
                merged = merge_substitutions(combination)
                if merged:
                    conclusion = substitute(rule["conclusion"], merged)
                    if conclusion not in known_facts:
                        new_inferred.append(conclusion)

        if not new_inferred:
            break

        for f in new_inferred:
            known_facts.add(f)
            inferred_facts.append(f)

    return inferred_facts