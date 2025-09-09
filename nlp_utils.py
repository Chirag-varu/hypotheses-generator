import spacy

nlp = spacy.load('en_core_web_sm')

def parse_natural_language_fact(sentence: str):
    """
    Parse sentences like 'X has property feather and can fly', 'X is a bird', 'X has wings', etc. into structured facts.
    Returns a list of (predicate, arg1, arg2) tuples.
    """
    doc = nlp(sentence)
    facts = []
    subj = None
    subj_token = None
    # Try to get subject (first noun or pronoun)
    for token in doc:
        if token.dep_ in ('nsubj', 'nsubjpass'):
            subj = token.text
            subj_token = token
            break
    if not subj:
        # fallback: first noun
        for token in doc:
            if token.pos_ == 'NOUN' or token.pos_ == 'PROPN' or token.pos_ == 'PRON':
                subj = token.text
                subj_token = token
                break
    if not subj:
        return []

    # Use the original text for the subject (preserve casing)
    subj_original = subj_token.text if subj_token else subj

    # Lowercase sentence for easier matching
    s = sentence.lower()


    # Helper to lemmatize a word using spaCy
    def lemma(word):
        return nlp(word)[0].lemma_ if word else word




    # is_a: 'X is a Y' or 'X is Y'
    if ' is a ' in s:
        parts = s.split(' is a ')
        if len(parts) == 2:
            y = lemma(parts[1].split()[0])
            facts.append(('is_a', subj_original, y))
    elif ' is ' in s:
        parts = s.split(' is ')
        if len(parts) == 2:
            y = lemma(parts[1].split()[0])
            facts.append(('is_a', subj_original, y))

    # has_property: 'X has property Y' or 'X has Y'
    if 'has property' in s:
        idx = s.index('has property') + len('has property')
        rest = s[idx:].strip().split(' and ')[0].split(' or ')[0]
        y = lemma(rest.split()[0]) if rest else ''
        if y:
            facts.append(('has_property', subj_original, y))
    elif ' has ' in s:
        idx = s.index(' has ') + len(' has ')
        rest = s[idx:].strip().split(' and ')[0].split(' or ')[0]
        y = lemma(rest.split()[0]) if rest else ''
        if y:
            facts.append(('has_property', subj_original, y))

    # can: 'X can Y', 'X can use sunlight', 'X can fly'
    if ' can ' in s:
        idx = s.index(' can ') + len(' can ')
        rest = s[idx:].strip().split(' and ')[0].split(' or ')[0]
        y = lemma(rest.split()[0]) if rest else ''
        if 'use sunlight' in rest:
            facts.append(('can', subj_original, 'use_sunlight'))
        elif y:
            facts.append(('can', subj_original, y))

    # makes_sound: 'X makes sound Y', 'X sounds like Y'
    if 'makes sound' in s:
        idx = s.index('makes sound') + len('makes sound')
        y = lemma(s[idx:].strip().split()[0]) if s[idx:].strip().split() else ''
        if y:
            facts.append(('makes_sound', subj_original, y))
    elif 'sounds like' in s:
        idx = s.index('sounds like') + len('sounds like')
        y = lemma(s[idx:].strip().split()[0]) if s[idx:].strip().split() else ''
        if y:
            facts.append(('makes_sound', subj_original, y))

    # boils_at: 'X boils at Y'
    if 'boils at' in s:
        idx = s.index('boils at') + len('boils at')
        y = lemma(s[idx:].strip().split()[0]) if s[idx:].strip().split() else ''
        if y:
            facts.append(('boils_at', subj_original, y))

    # has_symptom: 'X has symptom Y'
    if 'has symptom' in s:
        idx = s.index('has symptom') + len('has symptom')
        y = lemma(s[idx:].strip().split()[0]) if s[idx:].strip().split() else ''
        if y:
            facts.append(('has_symptom', subj_original, y))

    # has_part: 'X has part Y'
    if 'has part' in s:
        idx = s.index('has part') + len('has part')
        y = lemma(s[idx:].strip().split()[0]) if s[idx:].strip().split() else ''
        if y:
            facts.append(('has_part', subj_original, y))

    # Multiple facts in one sentence: handle 'and' and 'or'
    # e.g. 'X has wings and can fly'
    if ' and ' in s or ' or ' in s:
        # Split on 'and' or 'or', parse each part
        import re
        parts = re.split(r' and | or ', s)
        for part in parts:
            if part.strip() == '':
                continue
            if part == s:
                continue  # already parsed
            facts.extend(parse_natural_language_fact(subj + ' ' + part.strip()))

    return facts
