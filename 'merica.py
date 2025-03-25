
def merica():
    """
    List all the words that can be spelled using only the 2-letter shortcodes for the 50 American states. (AL, AK, AZ, AR, CA, CO, CT, ...)
    Example: VANDAL (Virginia, North Dakota, Alabama).

    This definition is O(n^3) notation, as it has 3 nested loops.
    """
    list_codes = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT",
                       "DE", "FL", "GA", "HI", "ID", "IL",
                       "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                       "MA", "MI", "MN", "MS", "MO", "MT", "NE",
                       "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
                       "OH", "OK", "OR", "PA", "RI", "SC", "SD",
                       "TN", "TX", "UT", "VT", "VA", "WA", "WV",
                       "WI", "WY"] #50 long
    list_words = ["VANDAL", "PACT", "FAIL", "HIDE", "AJEGEJCIW", "AL", "", "pane"]
    #Words are capslock sensitive
    list_spelled = [] #list of words that can be spelled using the codes
    for x in range (len(list_words)): #list of words
        success = 0
        if len(list_words[x]) % 2 == 0 and len(list_words[x]) > 0: #even length, not nothing
            for y in range (len(list_words[x])-1): #length of word
                for z in range(len(list_codes)): #list of codes
                    if (list_words[x][0+y*2:2+y*2]) == list_codes[z]: #check
                        success += 2
            #all pairs in the word have been checked    
            if success == len(list_words[x]):
                list_spelled.append(list_words[x])
        #else, does nothing with it
    print(list_spelled)

# -----------
merica()