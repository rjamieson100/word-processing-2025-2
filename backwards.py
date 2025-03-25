import requests

# Function to download the dictionary from GitHub
def load_dictionary_from_github(url):
    try:
        response = requests.get(url)  # Try to get the file from GitHub
        response.raise_for_status()  # Check if the request was successful (200 OK)
        return set(response.text.strip().splitlines())  # Convert the file content to a set of words
    except requests.exceptions.RequestException as e:  # Catch any request-related errors
        print(f"Error downloading the dictionary: {e}")
        return set()  # Return an empty set if there's an error

# URL of your dictionary file on GitHub (Raw file URL)
dictionary_url = "https://raw.githubusercontent.com/rjamieson100/word-processing-2025-2/refs/heads/Backwards/dictionary.txt"

# Load dictionary from GitHub
dictionary = load_dictionary_from_github(dictionary_url)

# Example input words to check
input_words = ["stressed", "diaper", "drawer", "gateman", "racecar", "reward", "repaid"]

# Function to find reversible non-palindromes (same as before)
def find_reversible_non_palindromes(word_list, dictionary):
    seen = set()
    result = []

    for word in word_list:
        reversed_word = word[::-1].lower()

        if reversed_word in dictionary and word.lower() != reversed_word and word.lower() not in seen:
            result.append(word)
            seen.add(word.lower())
            seen.add(reversed_word)

    return result if result else ["No reversible words found"]

# Run the function
reversible_words = find_reversible_non_palindromes(input_words, dictionary)
print(reversible_words)