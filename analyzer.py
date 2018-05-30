import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""

   
        self.positive=set()
        self.negative=set()
        file = open(positives, "r")
        for line in file:
            if line.startswith(":"):
                pass
            else:
                self.positive.add(line.rstrip("\n"))
        file.close()
        
        file = open(negatives, "r")
        for line in file:
            if line.startswith(":"):
                pass
            else:
                self.negative.add(line.rstrip("\n"))
        file.close()
        
        
        

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

    
        
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        
        for i in range (len(tokens)):
            tokens[i]=tokens[i].lower()
        score=0    
        for word in tokens:
            if word in self.positive:
                score=score+1
            elif word in self.negative:
                score=score-1
            else:
                score=score+0
                
        return score
