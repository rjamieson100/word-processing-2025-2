# List all the words for which the reversed word is also a word, but not a palindrome.
# Example: STRESSED

def find_reversible():
    
    word_set = set(words)
    result = []
    
    for word in words: