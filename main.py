# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from pickle import FALSE


def  find_anagram(word, anagram):
    # [assignment] Add your code here
    sort_strn1 = sorted(word)
    sort_strn2 = sorted(anagram)
    if sort_strn1 == sort_strn2:
        return True
    else:
        return False 
print(find_anagram("rome","more"))
