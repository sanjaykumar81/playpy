import re


def count_words(sentence):
    sentence = re.sub("[!@£$%^&*:,._]", " ", sentence)
    sentence = re.sub("''+", " ", sentence)
    sentence = re.sub(" '", " ", sentence)
    sentence = re.sub("' ", " ", sentence)
    sentence = re.sub("(')$", "", sentence)
    word_list = (sentence.lower()).split()
    word_set = set(word_list)
    word_count = {}
    for word in word_set:
        word_count[word] = word_list.count(word)

    return word_count
