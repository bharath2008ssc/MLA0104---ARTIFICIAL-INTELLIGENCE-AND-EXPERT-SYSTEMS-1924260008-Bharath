"""
Experiment 27: Vowel Identification using Rule-Based Logic
Scenario: A text-processing application identifies vowels in a given sentence for language analysis.
Expected Outcome: Classify characters based on predefined rules.
"""

VOWEL_RULES = {'a', 'e', 'i', 'o', 'u'}

def is_vowel_rule(char):
    return char.lower() in VOWEL_RULES

def analyze_sentence(sentence):
    vowels_found = []
    consonants_found = []

    for ch in sentence:
        if ch.isalpha():
            if is_vowel_rule(ch):
                vowels_found.append(ch)
            else:
                consonants_found.append(ch)

    return vowels_found, consonants_found

if __name__ == "__main__":
    sample_text = "Artificial Intelligence and Expert Systems"
    vowels, consonants = analyze_sentence(sample_text)

    print(f"Input Sentence: '{sample_text}'")
    print(f"Identified Vowels ({len(vowels)}): {vowels}")
    print(f"Identified Consonants ({len(consonants)}): {consonants}")
