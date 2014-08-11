import sys
import json

# By Yi Luo

scores = {}  # initialize an empty dictionary
results = []

sentScore = {}
sentCount = {}

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
            
            newTerms = []
            for part in parts:
                if part in scores:
                    s += scores[part]
                else: # new term
                    newTerms.append(part)
        
        for term in newTerms:
            if term in sentCount:
                sentCount[term] = sentCount[term] + 1
            else:
                sentCount[term] = 1
            if term in sentScore:
                sentScore[term] = sentScore[term] + s
            else:
                sentScore[term] = s
                
        results.append(s)
    
def calculate(): 
    terms = list(sentCount)
    for term in terms:
        print term + " " + str(sentScore[term] / float(sentCount[term]))
    
       
def main():
    readsentfile(sys.argv[1])
    analyze(sys.argv[2])
    
    calculate()

if __name__ == '__main__':
    main()
