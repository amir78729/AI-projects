import nltk, re, pprint, string
from nltk import ngrams, FreqDist


def p_1_gram(ci):
    pass


def p_2_gram(ci, ci_1):
    pass


def back_off(λ_1, λ_2, λ_3, ε, ci, ci_1):
    return λ_3 * p_2_gram(ci, ci_1) + λ_2 * p_1_gram(ci) + λ_1 * ε


if __name__ == '__main__':
    poets = ['molavi', 'hafez', 'molavi']
    dictionary_unigram = []
    dictionary_bigram = []
    number_of_unigrams = []
    number_of_bigrams = []

    for poet in poets:

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
        # print(number_of_bigrams)
        dictionary_unigram.append(all_counts[1].most_common(all_counts[1].B()))

        dictionary_bigram.append(all_counts[2].most_common(all_counts[2].B()))

    print(number_of_unigrams)
    print(number_of_bigrams)
