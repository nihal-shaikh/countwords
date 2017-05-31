def countWord(filepath, word):
    content = open(filepath, "r")
    text1 = content.read()
    content.close()
    words = text1.split()
    count = 0

    for i in words:
        if (i.lower() == word.lower()):
            count += 1
    print("the word %s occurs %d times" %(word, count))






filepath = "C:\\Users\\Nihal\\Desktop\\testfile.txt"
word = "Lorem"
countWord(filepath,word)