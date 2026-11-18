# Lab 12 - Document Analysis System
# Analyze a sentence and count different types of characters

sentence = input("Enter a sentence: ")

# Initialize counters
words = len(sentence.split())
vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

# Count each type of character
for ch in sentence:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == ' ':
        spaces += 1
    else:
        special += 1

total_letters = vowels + consonants
total_chars = len(sentence)

# Calculate vowel percentage
if total_letters > 0:
    vowel_pct = (vowels / total_letters) * 100
else:
    vowel_pct = 0.0

# Display the report
print("=============================================")
print("  DOCUMENT ANALYSIS REPORT")
print("=============================================")
print(f"Sentence: {sentence}")
print(f"Total characters: {total_chars}")
print()
print("--- Character Breakdown ---")
print(f"Words:              {words}")
print(f"Vowels:             {vowels}")
print(f"Consonants:         {consonants}")
print(f"Digits:             {digits}")
print(f"Spaces:             {spaces}")
print(f"Special characters: {special}")
print()
print("--- Summary ---")
print(f"Total letters: {total_letters}")
print(f"Vowel percentage: {vowel_pct}%")
print()
print("=============================================")
print("Analysis Complete!")
print("=============================================")
