### 🔍 AI Hypothesis Generator (CLI)

#### 💬 How to enter facts:

→ Format: predicate(arg1, arg2)
→ Example: has_property(sky, dark)
→ Type 'done' when you're finished.

Enter fact: help

🆘 Help - Accepted input formats:

- `has_property(entity, property)` → e.g. `has_property(animal, feathers)`
- `can(entity, ability)` → e.g. `can(animal, fly)`
- `is_a(entity, category)` → e.g. `is_a(bird, animal)`
- `boils_at(entity, temperature)` → e.g. `boils_at(substance, 100C)`
- `makes_sound(entity, sound)` → e.g. `makes_sound(sky, rumbling)`
- `use_sunlight(entity, action)` → e.g. `can(plant, use_sunlight)`
- `has_symptom(entity, symptom)` → e.g. `has_symptom(john, fever)`
- `has_part(entity, part)` → e.g. `has_part(car, wheels)`

Enter fact: has_property(animal, feathers)
Enter fact: can(animal, fly)  
Enter fact: done

📚 Initial Facts:
('has_property', 'animal', 'feathers')
('can', 'animal', 'fly')

🧠 Inferred Facts:
('hypothesis', 'animal', 'might_be_a_bird')

💡 Hypotheses:
→ might_be_a_bird

---

## 🖼 GUI (Graphical User Interface) Mode  

### Main Page (`gui.py`)  
![Main GUI](image.png)  

1. **Fact Entry Box** → Type in your facts here.  
2. **"Show Help" Button** → Displays all supported formats so you never have to memorize them.  

---

### Help Page  
![Help Page](image-1.png)  

**Formats Supported:**
- `has_property(entity, property)` → e.g. `has_property(animal, feathers)`
- `can(entity, ability)` → e.g. `can(animal, fly)`
- `is_a(entity, category)` → e.g. `is_a(bird, animal)`
- `boils_at(entity, temperature)` → e.g. `boils_at(substance, 100C)`
- `makes_sound(entity, sound)` → e.g. `makes_sound(sky, rumbling)`
- `use_sunlight(entity, action)` → e.g. `can(plant, use_sunlight)`
- `has_symptom(entity, symptom)` → e.g. `has_symptom(john, fever)`
- `has_part(entity, part)` → e.g. `has_part(car, wheels)`

---

### Example Flow in GUI:
1. Enter facts, for example:
   - `has_property(animal, arms)`
   - `can(animal, swim)`
2. Click **Generate Hypothesis** → See generated hypotheses in the result box.  
3. You can:
   - Add more facts (they’ll be added to the existing list)  
   - Or click **Clear All** to start fresh.  

---

Now you’re ready to generate smart, AI-powered hypotheses in seconds.  
We’d love for you to try it out and share your feedback.  

— *@Chirag_Varu*  
