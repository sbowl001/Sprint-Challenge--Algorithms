'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # count = 0 

    # for i in word:
    #     if i == "th":
    #         count = count + 1 
    # return count 

    return word.count("th")
 
word = "abcthxyz"
print(count_th(word))