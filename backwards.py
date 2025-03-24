# List all the words for which the reversed word is also a word, but not a palindrome.
# Example: STRESSED
"""
Finds words in the predefined list where the word backwards is a new word but not a palindrome.

Returns:
    List: a list of words that meet the criteria.
"""
def find_reversible():
    
    word_set = set(words) # Converts the word list to a set and not a list because lists have a BigO of O(n) while sets have a Big O of O(1) meaning sets are faster to lookup.
    result = [] # List to store valid words and have an order
    
    for word in words:
        reversed_words = word[::-1] # Reverses the word
        if reversed_words in word_set and word != reversed_words:
            result.append(word)
    
    return result

words = ["stressed", "desserts", "level", "hello", "world", "drawer", "reward", "racecar"]

reversible_words = find_reversible()
print(reversible_words)