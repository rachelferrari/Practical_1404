"""
Word Occurrences
Estimate: 25 minutes
Actual:
"""
word_to_count = {}

text = input("Text: ")
texts = text.split()
for i in range(len(texts)):
    word_to_count[texts[i]] = texts.count(texts[i])
for word, count in word_to_count.items():
    print(f"{word} : {count}")
