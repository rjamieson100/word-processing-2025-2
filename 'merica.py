# List all the words that can be spelled using only the 2-letter shortcodes for the 50 American states. (AL, AK, AZ, AR, CA, CO, CT, ...)
# Example: VANDAL (Virginia, North Dakota, Alabama).


def start():
    list_codes = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT",
                       "DE", "DC", "FL", "GA", "HI", "ID", "IL",
                       "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                       "MA", "MI", "MN", "MS", "MO", "MT", "NE",
                       "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
                       "OH", "OK", "OR", "PA", "RI", "SC", "SD",
                       "TN", "TX", "UT", "VT", "VA", "WA", "WV",
                       "WI", "WY"]
    list_words = ["TEST", "VANDAL"]
    print(list_words[1])
    for x in range (len(list_words)-1):
        print(x)

# -----------
start()