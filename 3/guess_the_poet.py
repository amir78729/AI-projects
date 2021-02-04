from nltk import ngrams, FreqDist


def create_dictionary_bigram(lst):
    dictionary = {}
    for item in lst:
        if item[1] > 2:
            text = '' + item[0][0] + ' ' + item[0][1]
            dictionary[text] = item[1]
    return dictionary


def create_dictionary_unigram(lst):
    number_of_words = 0
    dictionary = {}
    for item in lst:
        if item[1] > 2:
            text = '' + item[0][0]
            dictionary[text] = item[1]
            number_of_words += item[1]
    word_count.append(number_of_words)
    return dictionary


# P(Ci) = count(Ci) / M
def p_unigram(ci, poet_index):
    try:
        return dictionary_unigram[poet_index][ci] / word_count[poet_index]
    except KeyError:
        return 0


# P(Ci|Ci-1) = count(Ci-1 Ci) / count(Ci-1)
def p_bigram(ci, ci_1, poet_index):
    try:
        string = '' + ci_1 + ' ' + ci
        return dictionary_bigram[poet_index][string] / dictionary_unigram[poet_index][ci_1]
    except KeyError:
        return 0


def back_off(λ1, λ2, λ3, ε, ci, ci_1, poet_index):
    return λ3 * p_bigram(ci, ci_1, poet_index) + λ2 * p_unigram(ci, poet_index) + λ1 * ε


if __name__ == '__main__':
    λ1 = '?'
    λ2 = '?'
    λ3 = '?'
    ε = '?'
    poets = ['ferdowsi', 'hafez', 'molavi']
    dictionary_unigram, dictionary_bigram, number_of_unigrams, number_of_bigrams, word_count = [], [], [], [], []
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
        dictionary_unigram[index] = create_dictionary_unigram(dictionary_unigram[index])
        print('\t>>> UNIGRAM: {} ELEMENTS'.format(number_of_unigrams[index]))
        dictionary_bigram.append(all_counts[2].most_common(number_of_bigrams[index]))
        dictionary_bigram[index] = create_dictionary_bigram(dictionary_bigram[index])
        print('\t>>> BIGRAM: {} ELEMENTS'.format(number_of_bigrams[index]))
        print('\t>>> NUMBER OF WORDS: {}'.format(word_count[index]))
        index += 1
        print()
    print(' - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n')

    print(p_unigram('اسب', 0))
    ci_1 = 'عشق'
    ci = 'را'
    s = 'عشق را'
    s = s.split(' ')
    print(s)
    ci_1 = s[0]
    ci = s[1]
    print(ci_1)
    print(ci)
    print(p_bigram(ci, ci_1, 2))


