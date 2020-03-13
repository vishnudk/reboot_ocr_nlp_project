import nltk
import heapq
from nltk.probability import FreqDist
def txt_summry(text_data):
    text_data=text_data.lower()
    tokens = nltk.word_tokenize(text_data)
    fdist = FreqDist(tokens)
    maxfreq = max(fdist.values())
    for word in fdist:
        fdist[word] = (fdist[word]/maxfreq) 
    sentence_list = nltk.sent_tokenize(text_data)
    sentence_scores = {}     
    for sent in sentence_list: 
        #considering each word in the sentence, in lowercase
        for word in nltk.word_tokenize(sent.lower()):
            """checking if the word exists in the word_frequencies dictionary.
            This check is performed since we created the sentence_list list from the wikiarticle_text object but the word frequencies were calculated 
            using the formatted_wikiarticle object(which doesn't contain any stop words, numbers, etc.)"""
            if word in fdist.keys(): 
                #considering only those sentences which have less than 30 words
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        #for first word of sentence, setting frequency to frequency of the first word
                        sentence_scores[sent] = fdist[word] 
                    else:
                        #for other words (not first word) in same sentence, increasing frequency by frequency of the word
                        sentence_scores[sent] += fdist[word]

     #gathering the 7 sentences which have the largest scores into a list 
    summary_sentences = heapq.nlargest(3, sentence_scores, key=sentence_scores.get)
    
    #making the sentences into a printable format
    summary = ''.join(summary_sentences)
    
    #generating the summary 
    print("Summarised version of the article: ")
    print()
    print(summary)
    return summary
    