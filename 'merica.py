# List all the words that can be spelled using only the 2-letter shortcodes for the 50 American states. (AL, AK, AZ, AR, CA, CO, CT, ...)
# Example: VANDAL (Virginia, North Dakota, Alabama).


def merica():
    list_codes = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT",
                       "DE", "DC", "FL", "GA", "HI", "ID", "IL",
                       "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                       "MA", "MI", "MN", "MS", "MO", "MT", "NE",
                       "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
                       "OH", "OK", "OR", "PA", "RI", "SC", "SD",
                       "TN", "TX", "UT", "VT", "VA", "WA", "WV",
                       "WI", "WY"] #51 long
    list_words = ["VANDAL", "PACT", "FAIL"]
    list_spelled = []
    for x in range (len(list_words)): #list of words
        success = 0
        
        if len(list_words[x]) % 2 == 0: #even length
            
            for y in range (len(list_words[x])-1): #length of word
                
                for z in range(len(list_codes)): #list of codes
                    
                    if (list_words[x][0+y*2:2+y*2]) == list_codes[z]: #check
                        success += 2
                
        if success == len(list_words[x]):
            list_spelled.append(list_words[x])

    print(list_spelled)

# -----------
merica()