'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# def count_th(word):
    
#     # count = 0 

#     # for i in word:
#     #     if i == "th":
#     #         count = count + 1 
#     # return count 

#     return word.count("th")

def count_th(word):
    string = 'th'
    if string not in word: 
        return 0
    if string in word: 
        word = word.replace(string, 'new', 1)
        print(word)
        return count_th(word) + 1 
 
word = "abcthxyz"
print(count_th(word))