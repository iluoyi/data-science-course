import sys
import json

# By Yi Luo

termCount = {}
total = 0

def analyze(tweetFile):
    global total
    tweet_file = open(tweetFile)
    for line in tweet_file:
        struct = json.loads(line)

        if 'text' in struct:
            origtext = struct['text']
            text = origtext.encode('utf-8')
            #text.replace("\n\r\f", " ")

            parts = text.split(" ")
            
            for part in parts:
                part = part.strip(' \t\n\r')
                if part in termCount:
                    termCount[part] += 1
                else:
                    termCount[part] = 1
                total += 1
    
def calculate(): 
    global total
    terms = list(termCount)
    for term in terms:
        print term + " " + str(termCount[term] / float(total))
    
       
def main():
    analyze(sys.argv[1])
    calculate()

if __name__ == '__main__':
    main()
