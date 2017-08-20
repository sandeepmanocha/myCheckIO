import re

def checkio(words_set):

    words = list(words_set)
    words.sort(key=len)

    #print(words)

    for suffix_idx in range( len(words)-1):
        suffix = words[suffix_idx]

        #print(suffix_idx)
        for word_idx in range(suffix_idx+1, len(words)):
            word = words[word_idx]
            #print('word_idx:',word_idx)
            if suffix != word:
                #print('suffix:',suffix,' word:', word)
                if word.endswith(suffix):
                    return True

    return False


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio({"hello", "lo", "he"}))

    print(checkio({"helicopter", "li", "he"}))



    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
