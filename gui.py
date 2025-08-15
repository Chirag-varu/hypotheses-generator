import tkinter as tk
from tkinter import scrolledtext, messagebox
from rule_engine import apply_forward_chaining
from utils import parse_fact_input
from knowledge_base import rules

class HypothesisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Hypothesis Generator")
        self.user_facts = []

        # Input label
        tk.Label(root, text="Enter Fact (predicate(arg1, arg2)):", font=("Arial", 12)).pack(pady=5)

        # Input field
        self.fact_entry = tk.Entry(root, width=50, font=("Arial", 12))
        self.fact_entry.pack(pady=5)

        # Buttons frame
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Add Fact", command=self.add_fact).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Show Help", command=self.show_help).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Generate Hypotheses", command=self.generate_hypotheses).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Clear All", command=self.clear_all).grid(row=0, column=3, padx=5)

        # Facts display
        tk.Label(root, text="📚 Entered Facts:", font=("Arial", 12, "bold")).pack()
        self.facts_display = scrolledtext.ScrolledText(root, width=60, height=8, font=("Arial", 10))
        self.facts_display.pack(pady=5)

        # Output display
        tk.Label(root, text="💡 Results:", font=("Arial", 12, "bold")).pack()
        self.output_display = scrolledtext.ScrolledText(root, width=60, height=10, font=("Arial", 10))
        self.output_display.pack(pady=5)

    def add_fact(self):
        fact_text = self.fact_entry.get().strip()
        if not fact_text:
            messagebox.showwarning("Input Error", "Please enter a fact.")
            return
        try:
            parsed = parse_fact_input(fact_text)
            self.user_facts.append(parsed)
            self.facts_display.insert(tk.END, f"{parsed}\n")
            self.fact_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Invalid Format", f"{e}\nUse format: predicate(arg1, arg2)")

    def show_help(self):
        help_text = """
🆘 Accepted input formats:
• has_property(entity, property)      e.g. has_property(animal, feathers)
• can(entity, ability)                e.g. can(animal, fly)
• is_a(entity, category)              e.g. is_a(bird, animal)
• boils_at(entity, temperature)       e.g. boils_at(substance, 100C)
• makes_sound(entity, sound)          e.g. makes_sound(sky, rumbling)
• can(entity, use_sunlight)           e.g. can(plant, use_sunlight)
• has_symptom(entity, symptom)        e.g. has_symptom(john, fever)
• has_part(entity, part)              e.g. has_part(car, wheels)
        """
        messagebox.showinfo("Help", help_text)

    def generate_hypotheses(self):
        if not self.user_facts:
            messagebox.showwarning("No Facts", "Please enter at least one fact.")
            return

        inferred_facts = apply_forward_chaining(self.user_facts, rules)
        new_facts = [f for f in inferred_facts if f not in self.user_facts]
        hypotheses = [f for f in inferred_facts if f[0] == "hypothesis"]

        self.output_display.delete(1.0, tk.END)

        if new_facts:
            self.output_display.insert(tk.END, "🧠 Inferred Facts:\n")
            for fact in new_facts:
                self.output_display.insert(tk.END, f"  {fact}\n")
        else:
            self.output_display.insert(tk.END, "No new facts inferred.\n")

        self.output_display.insert(tk.END, "\n💡 Hypotheses:\n")
        if hypotheses:
            for h in hypotheses:
                self.output_display.insert(tk.END, f"  → {h[2]}\n")
        else:
            self.output_display.insert(tk.END, "No hypothesis generated.\n")

    def clear_all(self):
        self.user_facts.clear()
        self.facts_display.delete(1.0, tk.END)
        self.output_display.delete(1.0, tk.END)
        self.fact_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = HypothesisGUI(root)
    root.mainloop()
