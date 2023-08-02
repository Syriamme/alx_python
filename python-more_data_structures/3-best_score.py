def best_score(a_dictionary):
    if not a_dictionary:
        return None

    # Get first key and value from the dictionary
    max_key, max_value = list(a_dictionary.items())[0]

    # Iterate over all items in the dictionary
    for key, value in a_dictionary.items():
        # If the current value is higher than the max value, update max_key and max_value
        if value > max_value:
            max_key = key
            max_value = value

    return max_key