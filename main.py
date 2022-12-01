import hashlib
from itertools import permutations

def find_hash(original_hash):
    word_file = open("words.txt","r")
    word_file = list(word_file)

    anagram = "who outlay theives"
    words = anagram.count(' ')
    words += 1

    char_list = list(set(anagram))

    if ' ' in char_list:
        char_list.remove(' ')

    final_words = []

    #Student Activity
    for i in word_file:
        flag = False
        tempWord = i.replace("\n", "")
        tempChar = list(set(tempWord))
        for i in tempChar:
            if i not in char_list:
                flag = True
                break
        if flag == False:
            final_words.append(tempWord)

    print(len(final_words))

    for elem in permutations(final_words, words):
        hash_elem = " ".join(elem)
        
        #Student Activity
        if len(hash_elem) != len(anagram):
            continue
        
        m = hashlib.md5()
        m.update(hash_elem.encode('utf-8'))
        word_hash = m.hexdigest()

        if word_hash == original_hash:
            return hash_elem

hash = '13b382e1a2f8e22535b4730d78bc8591'
answer = find_hash(hash)
print(f"Collision!  The word corresponding to the given hash is '{answer}'")
