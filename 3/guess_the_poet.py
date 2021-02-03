import nltk, re, pprint, string
from nltk import ngrams, FreqDist


def create_dictionary(lst):
    dictionary = {}
    for i in lst:
        if i[1] > 2:
            text = '' + i[0][0] + ' ' + i[0][1]
            dictionary[text] = i[1]
    return dictionary


def p_unigram(ci):
    pass


def p_bigram(ci, ci_1):
    pass


def back_off(λ_1, λ_2, λ_3, ε, ci, ci_1):
    return λ_3 * p_bigram(ci, ci_1) + λ_2 * p_unigram(ci) + λ_1 * ε


if __name__ == '__main__':
    poets = ['ferdowsi', 'hafez', 'molavi']
    dictionary_unigram = []
    dictionary_bigram = []
    number_of_unigrams = []
    number_of_bigrams = []
    index = 0
    for poet in poets:
        print('>>> CREATING LANGUAGE MODELS FOR \"{}\"...'.format(poet.upper()))
        file_name = "train_set/{}_train.txt".format(poet)
        file = open(file_name, encoding="utf8")
        content = file.read()
        content_list = content.replace('\n', ' ')
        content_list = content_list.replace('\u200c', '')
        content_list = content_list.replace(' ، ', ' ')
        content_list = content_list.split(" ")

        all_counts = dict()
        for size in 1, 2:
            all_counts[size] = FreqDist(ngrams(content_list, size))
        number_of_unigrams.append(all_counts[1].B())
        number_of_bigrams.append(all_counts[2].B())
        dictionary_unigram.append(all_counts[1].most_common(number_of_unigrams[index]))
        print('\t>>> UNIGRAM HAS BEEN CREATED FOR \"{}\" WITH {} ELEMENTS'.format(poet.upper(), number_of_unigrams[index]))
        dictionary_bigram.append(all_counts[2].most_common(number_of_bigrams[index]))
        print('\t>>> BIGRAM HAS BEEN CREATED FOR \"{}\" WITH {} ELEMENTS'.format(poet.upper(), number_of_bigrams[index]))
        index += 1
        print()
    dictionary_unigram[0].reverse()
    print(dictionary_unigram[0])
    for i in dictionary_bigram[0]:
        if i[1] > 2:
            print('{}:{}/{}'.format(i[1], i[0][0], i[0][1]))

    dictionary_bigram[0] = create_dictionary(dictionary_bigram[0])
    print(dictionary_bigram[0])

    s = 'که از'
    s = s.split(' ')
    print(s)
    new_s = '' + s[0] + '/' + s[1]
    print(new_s)
