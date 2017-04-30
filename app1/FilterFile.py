def isEnglish(s):
    try:
        s.decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True



#waysDataForTrie.txt


f = open('waysDataForTrieNew.txt', 'w')
#f.write('hi there\n')  # python will convert \n to os.linesep



with open("waysDataForTrie.txt", "r") as ins:
    array = []
    for line in ins:
    	if (isEnglish(line)):
    		f.write(line)
    		#f.write("\n")	
    		

f.close()