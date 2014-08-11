import sys
import json

# By Yi Luo

scores = {}  # initialize an empty dictionary
results = []

def readsentfile(dictFile):
    sent_file = open(dictFile)
    for line in sent_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    

def analyze(tweetFile):
    tweet_file = open(tweetFile)
    for line in tweet_file:
        struct = json.loads(line)
        s = 0
        if 'text' in struct:
            origtext = struct['text']
            text = origtext.encode('utf-8')
            parts = text.split(" ")
            
            for part in parts:
                if part in scores:
                    s += scores[part]
        results.append(s)
        
def main():
    readsentfile(sys.argv[1])
    analyze(sys.argv[2])
    
    for each in results:
        print each

if __name__ == '__main__':
    main()
