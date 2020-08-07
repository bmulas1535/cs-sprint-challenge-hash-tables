def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Create a dictionary for each array, and put it into a numbered dictionary
    dict_of_arrays = {i : dict.fromkeys(arrays[i], 1) for i in range(len(arrays))}
    # Search the next dictionary for each of the previous dictionaries' keys
    # Update the search so that only the matching keys persist
    # continue until all dictionaries have been searched
    # The remaining search keys are the only keys that exist in all arrays
    search = list(dict_of_arrays[0].keys())
    # Check the following dictionaries for these keys:
    i = 1
    found = []
    while i < len(arrays):
        # Compare the search keys to the current dict keys
        for x in search:
            res = dict_of_arrays[i].get(x)
            # If the keys exists, persist that key to the next
            # iteration
            if res is not None:
                found.append(x)
        # Assuming these keys are the only matching keys, update the search pattern
        search = found
        # reset the matching keys
        found = []
        # Move the counter down by 1
        i = i + 1
    # Once all arrays have been searched, the search variable
    # will only contain the values that exist in all arrays.
    return search

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
