'''
Define a function to count the frequency of words in a given list of words. 
Example:

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
count_word_frequency(words) 
Output:
{'apple': 3, 'orange': 2, 'banana': 1}
'''
def count_word_frequency(words1): # Time complexity: O(n) & Space complexity: O(n)
    frequency = {}
    for word in words1:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

# Using built-in function get() to count the frequency of words in a given list of words
def count_word_frequency_2(words2): # Time complexity: O(n) & Space complexity: O(n)
    frequency = {}
    for word in words2:
        frequency[word] = frequency.get(word, 0) + 1 # get() method returns the value of the item with the specified key. If the key does not exist, it returns the default value 0.
    return frequency

words1 = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
words2 = ['tiger', 'lion', 'elephant', 'tiger', 'lion', 'tiger', 'lion', 'elephant', 'giraffe', 'tiger', 'lion']
print(count_word_frequency(words1))
print(count_word_frequency_2(words2))