import sys
import json

# By Yi Luo

hashtags = {}

def analyze(tweetFile):
    global total
    tweet_file = open(tweetFile)
    for line in tweet_file:
        struct = json.loads(line)
        
        if 'entities' in struct:
            for hashtags_list in struct['entities']['hashtags']:
                    hashtag = hashtags_list['text']
                    tag = hashtag.encode('utf-8')
                    if tag in hashtags:
                        hashtags[tag] = hashtags[tag] + 1
                    else:
                        hashtags[tag] = 1
            
def main():
    analyze(sys.argv[1])
    hashdict = sorted(hashtags.iteritems(), key=lambda d:d[1], reverse = True) # to sort the whole dict is not efficient
    for pair in hashdict[:10]:
        print pair[0] + " " + str(pair[1])

if __name__ == '__main__':
    main()
