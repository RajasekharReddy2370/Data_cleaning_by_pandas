from fuzzywuzzy import fuzz
def string_matches_with_list(string, string_list, threshold=70):
    """
    Check if a string matches with any of the strings in a list with a certain similarity threshold.
    Args:
    - string: The string to compare.
    - string_list: The list of strings to compare against.
    - threshold: The similarity threshold (default is 70).
    Returns:
    - True if the string matches with any string in the list above the threshold, False otherwise.
    """
    for item in string_list:
        similarity_score = fuzz.ratio(string.lower(), item.lower())
        print(item,similarity_score)
        if similarity_score >= threshold:
            print(item, similarity_score)
            return True
    return False

# Example usage
string = 'raj'
string_list = ["rajsekhar1", "rajasekhar2", "raja3", "another_example"]

if string_matches_with_list(string, string_list):
    print(f"'{string}' matches with at least one string in the list.")
else:
    print(f"'{string}' does not match with any string in the list.")

