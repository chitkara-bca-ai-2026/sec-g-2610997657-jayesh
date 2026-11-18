# Lab 10 - Text Processing Tool
# Perform various string operations on user input

print("==========================================")
print("        TEXT PROCESSING TOOL")
print("==========================================")

sentence = input("Enter a sentence: ")

print()
print("--- Processing Results ---")

# Indexing - get character at specific position
pos = int(input("Enter position for indexing: "))
print(f"Character at position {pos}  : '{sentence[pos]}'")

# Slicing - extract a portion of the string
start = int(input("Enter start index for slicing : "))
end = int(input("Enter end index for slicing   : "))
print(f"Sliced string [{start}:{end}]      : '{sentence[start:end]}'")

# Case conversion
print(f"Uppercase                : {sentence.upper()}")
print(f"Lowercase                : {sentence.lower()}")

# Replace a word
old_word = input("Enter word to replace    : ")
new_word = input("Enter replacement word   : ")
print(f"After replace            : {sentence.replace(old_word, new_word)}")

# Length of the sentence
print(f"Length of sentence       : {len(sentence)}")

print()
print("==========================================")
print("Analysis Complete!")
print("==========================================")
