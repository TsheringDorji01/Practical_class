def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Test the function
content = read_file('sample.txt')
print(content[:100])  # Print the first 100 characters

def count_lines(content):
    return len(content.split('\n'))

# Test the function
num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")

from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

# Test the function
common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")

def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# Test the function
avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")

def count_words(content):
    return len(content.split())

def unique_words(content):
    words = set(content.lower().split())
    return len(words)

def longest_word(content):
    words = content.split()
    longest = max(words, key=len)
    return longest, len(longest)

def case_insensitive_search(content, word):
    words = content.lower().split()
    return words.count(word.lower())

def percentage_words_longer_than_average(content):
    words = content.split()
    avg_length = average_word_length(content)
    longer_words = [word for word in words if len(word) > avg_length]
    return len(longer_words) / len(words) * 100

def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")
    print(f"Number of unique words: {unique_words(content)}")
    print(f"Longest word: '{longest_word(content)[0]}' (length: {longest_word(content)[1]} characters)")
    print(f"Count of 'the': {case_insensitive_search(content, 'the')}")
    print(f"Percentage of words longer than average: {percentage_words_longer_than_average(content):.2f}%")

# Run the analysis
analyze_text('sample.txt')

count