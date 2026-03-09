def word_frequency(text):
    words = text.lower().split()

    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    top5 = sorted_words[:5]

    total_words = len(words)
    top5_sum = sum(count for word, count in top5)

    proportion = (top5_sum / total_words) * 100

    print("Top 5 words:", top5)
    print("Total number of words:", total_words)
    print("Proportion of 5 most common words:", proportion, "%")


text = input("Enter text: ")
word_frequency(text)
