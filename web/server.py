from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
rule_engine_path = os.path.join(parent_dir, 'rule_engine.py')
if not os.path.isfile(rule_engine_path):
    raise ImportError(f"Could not find 'rule_engine.py' in the parent directory ({parent_dir}). Please ensure the file exists.")

# Ensure the parent directory is in sys.path before importing
try:
    from rule_engine import apply_forward_chaining
except ModuleNotFoundError as e:
    raise ImportError(f"Failed to import 'rule_engine'. Make sure 'rule_engine.py' exists in {parent_dir} and is not empty. Original error: {e}")
from utils import parse_fact_input
from knowledge_base import rules
try:
    from nlp_utils import parse_natural_language_fact
except ImportError:
    parse_natural_language_fact = None

app = Flask(__name__)
CORS(app)

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.get_json()
    user_facts = []
    for fact in data.get('facts', []):
        try:
            parsed = parse_fact_input(fact)
            user_facts.append(parsed)
        except Exception:
            if parse_natural_language_fact:
                nlp_facts = parse_natural_language_fact(fact)
                user_facts.extend(nlp_facts)
    if not user_facts:
        return jsonify({'result': 'No valid facts provided.'})
    inferred_facts = apply_forward_chaining(user_facts, rules)
    new_facts = [f for f in inferred_facts if f not in user_facts]
    hypotheses = [f for f in inferred_facts if f[0] == "hypothesis"]
    result = ''
    if new_facts:
        result += '🧠 Inferred Facts:\n' + '\n'.join(str(f) for f in new_facts) + '\n\n'
    result += '💡 Hypotheses:\n'
    if hypotheses:
        for h in hypotheses:
            result += f"  → {h[2]}\n"
    else:
        result += 'No hypothesis generated.'
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
