# List all words for which the odd/even letters make another word. The "odd letters" are the 1st, 3rd, 5th, ect, and the 'even letters' are the 2nd, 4th, 6th, ...
# Only words of 5+ letters (for odd) and 6+ letters (for even) should be considered, i.e. the resulting word must be 3+ letters.
# Examples: DERBY (which makes DRY), UNBUNDLED (which makes NUDE)
# Predefined set of valid words (you can expand this list as needed)
valid_word_set = {"dry", "nude", "star", "example", "hello", "bun", "lid", "red", "pen", "cat"}

def find_valid_words(word_list):
    # Create an empty list to store the valid words
    valid_words = []

    # Loop through each word in the provided word list
    for word in word_list:
        
        # Check if the word has at least 5 letters (for odd-numbered letters)
        if len(word) >= 5:
            
            # Extract the odd-numbered letters from the word (1st, 3rd, 5th, ...)
            odd_letters = word[::2]
            
            # Extract the even-numbered letters from the word (2nd, 4th, 6th, ...)
            even_letters = word[1::2]
            
            # Check if either the odd or even letters form a valid word
            if len(odd_letters) >= 3 and odd_letters.lower() in valid_word_set:
                valid_words.append(word)
            elif len(even_letters) >= 3 and even_letters.lower() in valid_word_set:
                valid_words.append(word)

    # After processing all words, return the list of valid words
    return valid_words

# Test the function with a sample list of random words
word_list = ["DERBY", "UNBUNDLED", "HELLO", "EXAMPLE", "STAR", "COMPUTER"]
valid_words = find_valid_words(word_list)

# Output the list of valid words that meet the criteria
print("Valid words:", valid_words)