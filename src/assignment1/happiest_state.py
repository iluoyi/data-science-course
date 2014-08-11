import sys
import json

# By Yi Luo

# From: http://code.activestate.com/recipes/577305-python-dictionary-of-us-states-and-territories/
statesAbb2Full = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

statesFull2Abb = dict( (statesAbb2Full[k], k) for k in statesAbb2Full)
happyState = {}


scores = {}  # initialize an empty dictionary
def readsentfile(dictFile):
    sent_file = open(dictFile)
    for line in sent_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.


def getState(line):
    text = line.encode('utf-8')
    words = text.split(" ")
    for word in words:
            word = word.strip(' \t\n\r')
            if word in statesAbb2Full:
                return word
            elif word in statesFull2Abb:
                return statesFull2Abb[word]
    return None

def getScore(line):
    s = 0
    text = line.encode('utf-8')
    words = text.split(" ")
    for word in words:
            word = word.strip(' \t\n\r')
            if word in scores:
                s += scores[word]     
    return s
    
def analyzeTweet(tweet):     
    state = None      
    s = 0         
    if 'place' in tweet:
            place = tweet['place']
            if place is not None:
                full_name = place["full_name"]
                state = getState(full_name)
    
    if 'text' in tweet:
            origtext = tweet['text']
            if state is None:
                state = getState(origtext)
            s = getScore(origtext)
   
    if state is not None:
        if state not in happyState:
            happyState[state] = s
        else:
            happyState[state] = happyState[state] + s

def parse(tweetFile):
    tweet_file = open(tweetFile)
    for line in tweet_file:
        struct = json.loads(line)
        analyzeTweet(struct)
       
def main():
    readsentfile(sys.argv[1])
    parse(sys.argv[2])
    
    maximum = -sys.maxint - 1
    happest = None
    for state in happyState.keys():
        if happyState[state] > maximum:
            maximum = happyState[state]
            happest = state

    #print happyState
    print happest
    
if __name__ == '__main__':
    main()
