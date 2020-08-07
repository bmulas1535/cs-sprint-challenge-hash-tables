def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # The length should be greater than 2
    # if length < 2:
    ## pairs = None
    ## Just setting pairs to None will have this effect.
    pairs = None
    # Create a dictionary of weight items, with the weight as the key, and the index location 
    # as the value. Runtime O(n) // optimized with dict comprehension //
    # weight_dict = {x : weights.index(x) for x in weights}
    weight_dict = {x : weights.index(x) for x in weights}
    # Iterate over each weight and check if the compliment to the limit exists.
    # Ignore the same weight in the initial search
    # for i, weight in weights:
    for i, weight in enumerate(weights):
        ## pair = weight_dict.get(limit - weight)
        pair = weight_dict.get(limit - weight)
        ## we do not want the same value if that is an option
        ## if pair is not None:
        if pair is not None:
            ### if pair == index location for weight:
            if pair == i:
                #### pass
                pass
            ### The above will ignore the same weight value on the current iteration
            ### If pair is not none otherwise, a sum value was found. Add it's index and the
            ### current weight index to the pairs variable
            ### else:
            else:
                #### pairs = (i, weights_dict[pair])
                #### pairs needs to be sorted from highest to lowest...
                pairs = tuple(sorted([i, pair], reverse=True))
                #### break
                break
    # Pairs will either contain the index values, or 
    # it will be None. Return it.
    # return pairs
    return pairs
