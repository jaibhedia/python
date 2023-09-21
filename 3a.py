sentence = input("Enter a sentence : ")
wordList = sentence.split(" ")
print("This sentence has", len(wordList), "words")
digCnt = upCnt = loCnt = 0
for ch in sentence:
 if '0' <= ch <= '9':
  digCnt += 1
 elif 'A' <= ch <= 'Z':
  upCnt += 1
 elif 'a' <= ch <= 'z':
  loCnt += 1
print("This sentence has", digCnt, "digits", upCnt, "upper case letters", loCnt, "lower case letters")