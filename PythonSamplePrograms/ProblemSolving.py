#Problem 1 :
#Given a String S and List of Words W, identify the number of words which are a subsequence of String S
subSetString=['abcde']
words=['a','bb','ac','adc','ade','ae','ca','an','abe','aeb']
#words=['a','bb','ac','adc']
matchWords=[]
print("Simply Test Printing")
for word in words:
    print(f"Each Word in Words is {word}")
    match3 = -1
    matchIndex=0
    for i in range(len(word)):
        matchLetter=word[i]
        matchIndex=subSetString[0].find(matchLetter,match3+1)
        #print(f"Letter Matched  is {matchLetter} and  Index of Letter is {matchIndex}")
        if matchIndex==-1:
            break;
        match3=matchIndex
    if matchIndex > -1:
        print(f"Selected Word is :{word}")
        matchWords.append(word)
print(f"Number of Matched words is : {len(matchWords)} and selected words are : {matchWords}")

print("testing git hub on Functions_Repository file")



