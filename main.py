from rule_engine import apply_forward_chaining
from utils import parse_fact_input
from knowledge_base import rules

def main():
    print("🔍 AI Hypothesis Generator (CLI)")
    print("\n💬 How to enter facts:")
    print("  → Format: predicate(arg1, arg2)")
    print("  → Example: has_property(sky, dark)")
    print("  → Type 'help' to see all supported formats.")
    print("  → Type 'done' when you're finished.\n")

    user_facts = []

    while True:
        user_input = input("Enter fact: ").strip()

        if user_input.lower() == "done":
            break

        if user_input.lower() == "help":
            print("\n🆘 Help - Accepted input formats:")
            print("   • has_property(entity, property)      → e.g. has_property(animal, feathers)")
            print("   • can(entity, ability)                → e.g. can(animal, fly)")
            print("   • is_a(entity, category)              → e.g. is_a(bird, animal)")
            print("   • boils_at(entity, temperature)       → e.g. boils_at(substance, 100C)")
            print("   • makes_sound(entity, sound)          → e.g. makes_sound(sky, rumbling)")
            print("   • use_sunlight(entity, action)        → e.g. can(plant, use_sunlight)")
            print("   • has_symptom(entity, symptom)        → e.g. has_symptom(john, fever)")
            print("   • has_part(entity, part)              → e.g. has_part(car, wheels)")
            print("   • Type 'done' to finish entering facts")
            print("   • Type 'help' to view this message again\n")
            continue

        if "(" not in user_input or ")" not in user_input:
            # Try to parse as natural language
            try:
                from nlp_utils import parse_natural_language_fact
                nlp_facts = parse_natural_language_fact(user_input)
                if nlp_facts:
                    print(f"✅ Parsed as: {nlp_facts}")
                    user_facts.extend(nlp_facts)
                    continue
                else:
                    print("❌ Could not parse the sentence as a fact.")
            except Exception as e:
                print(f"❌ NLP parsing error: {e}")
            print("   ✅ Please use the format: predicate(arg1, arg2)")
            print("   Example: has_property(sky, dark)\n")
            continue

        if user_input == "":
            print("⚠️  Empty input. Please enter a valid fact or type 'done'.\n")
            continue

        try:
            parsed = parse_fact_input(user_input)
            user_facts.append(parsed)
        except Exception as e:
            print(f"❌ Invalid format: {e}")
            print("   ✅ Use format: predicate(arg1, arg2) — e.g., has_property(sky, dark)\n")

    if not user_facts:
        print("\n❗ No facts were entered. Exiting.")
        return

    print("\n📚 Initial Facts:")
    for fact in user_facts:
        print(f"  {fact}")

    inferred_facts = apply_forward_chaining(user_facts, rules)

    print("\n🧠 Inferred Facts:")
    new_facts = [f for f in inferred_facts if f not in user_facts]
    if not new_facts:
        print("  No new facts inferred.")
    else:
        for fact in new_facts:
            print(f"  {fact}")

    print("\n💡 Hypotheses:")
    hypotheses = [fact for fact in inferred_facts if fact[0] == "hypothesis"]
    if hypotheses:
        for h in hypotheses:
            print(f"  → {h[2]}")
    else:
        print("  No hypothesis generated.")

if __name__ == "__main__":
    main()
