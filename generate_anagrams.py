



def genanagrams(word,res,temp):
    if(len(res) >= 100000):
        return
    if len(word)==0:
        res.append(temp)
        return

    for i in range(len(word)):
        genanagrams(word[0:i]+word[i+1:],res,temp+word[i])





def main():    
    word = "kbeznak parmatonic"     
    res= [] 
    genanagrams(word,res,"");
    print len(set(res))
    print list(set(res))

main()
