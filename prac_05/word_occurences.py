"""
Word Occurrences
Estimate: 25 minutes
Actual: 52 minutes
"""
word_to_count = {}

text = input("Text: ")
texts = text.split()
texts.sort()
for i in range(len(texts)):
    word_to_count[texts[i]] = texts.count(texts[i])
max_length = max(len(text) for text in texts)
for word, count in word_to_count.items():
    print(f"{word:{max_length}} : {count}")
