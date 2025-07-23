sentence=input("Enter a sentence or a story : ").lower()
words = sentence.split()
word_counts= {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1