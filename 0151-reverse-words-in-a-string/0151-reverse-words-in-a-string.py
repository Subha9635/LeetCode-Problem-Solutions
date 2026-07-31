class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""
        for char in s: #Traverses the string
            if char != " ":
                word += char
            elif len(word)!=0:  #Identifies if a word is selected and pushes it to the trversed words list
                words.append(word)
                word = ""
        if len(word) != 0:
            words.append(word)


        result = ""
        for i in range(len(words)-1,-1,-1): #Traverses the list in reverse order and concatenates the words in to a single string
            result += words[i]
            if i != 0:
                result += " "
        return result