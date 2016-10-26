def parse_file(crypto_file):
    text = open(crypto_file)
    all_words = " ".join([s.strip().lower() for s in text.readlines()])
    return sweep_punct(all_words)

def sweep_punct(string):
    string = str(string)
    punctuation = [",","!","?",".","'","\"","-"]
    for p in punctuation:
        string = string.replace(p,"")
    return (string)
    
def letter_matching(eng_word, crypt_word, subs_queue):
    
    for x,y in zip(crypt_word,eng_word):
        for a,b in subs_queue:
            if(a == x and b != y):
                return False
    return True
        
def recursive_word_find(EnglishDict, crypt_list, crypt_word_i, subs_queue):
    crypt_word = crypt_list[crypt_word_i]
    if(crypt_word_i == len(crypt_list)+1):
        return subs_queue
    w_len = len(crypt_word)
    len_apro_words = [w for w in EnglishDict if len(w) == w_len]   
    for i in range(len(len_apro_words)):
        if(letter_matching(len_apro_words[i],crypt_word, subs_queue)):
            for x,y in zip(crypt_word,len_apro_words[i]):
                if( (x,y) not in subs_queue):
                    subs_queue.append((x,y))
            return recursive_word_find(EnglishDict, crypt_list, crypt_word_i+1, subs_queue)
    return recursive_word_find(EnglishDict, crypt_list, 0, [])
                
if __name__ == '__main__':   
    
    inputfile = "input.txt"
    EnglishDictionary = open("EnglishWords.txt")
    outputfile = open('output.txt', 'w')
    all_words = parse_file(inputfile)
   
    EnglishDictionary = " ".join([w.strip() for w in EnglishDictionary.readlines()])
    
    crypt_list = all_words.split(" ")    
    crypt_list = sorted(crypt_list,key=len)
    print(crypt_list)
    subs_queue = []
    i = 0
    recursive_word_find(EnglishDictionary, crypt_list, i, subs_queue)
    
       
"""
find smallest words in eng lang first, check against the corresponding size 
words and keep corresponding letters in tupple queue. When we go through 
more words, only use words from eng lang that have the correct corresponding 
letters. If fails, start over
       
"""