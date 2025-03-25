# A custom set of valid words to check the word list for
valid_words = {"stressed", "diaper", "repaid", "desserts", "drawer", "reward", "deliver", "reviled", "gateman", "nametag", "dog", "god", "tag", "gat", "live", "evil", "devil", "lived", "now", "won", "parts", "strap", "flow", "wolf", "rat", "tar", "snug", "guns", "lager", "regal", "pat", "tap", "mood", "doom", "diodes", "seodi", "rip", "pir", "pit", "tip", "taps", "spat", "stun", "nuts"}

# Function to find reversible words that are not palindromes, ensuring only one of each pair is included
def find_reversible_non_palindromes():
    """
    Finds words in the predefined list where the reversed version forms a valid word but is not a palindrome.
    Ensures only one word from each reversible pair is included.
    
    Returns:
        list: A list of words that meet the criteria.
    """
    seen = set()  # Makes a set to store words already counted
    # Uses a set rather than list because a set is faster than lists in gathering info as sets have a Big O of O(1) while lists have a Big O of O(n).
    result = []  # List to store valid words
    # Uses a list here so it retains an order.
    
    for word in words:
        reversed_word = word[::-1]  # Reverses the word
        
        # Ensure reversed word is valid, is not a palindrome, and has not already been counted
        if reversed_word in valid_words and word != reversed_word and reversed_word not in seen:
            result.append(word)  # Add to the result list
            seen.add(word)  # Mark this word as counted
            seen.add(reversed_word)  # Also mark the reversed word as counted to avoid duplicates
    
    return result if result else ["No reversible words found"]  # Ensures non-empty output

# List of words to search through
words = ["stressed", "diaper", "deliver", "hello", "world", "drawer", "gateman", "racecar"]

# Call the function and store the results
reversible_words = find_reversible_non_palindromes()
print(reversible_words)  # Output: Words that have a valid reversed counterpart
