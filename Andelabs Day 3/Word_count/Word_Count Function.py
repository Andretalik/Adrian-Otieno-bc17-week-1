def words(sentence):
    if isinstance(sentence, str):
        split_sentence = sentence.split()
        '''for word in split_sentence:
            if word.isdigit() in split_sentence:
                word = int(word)'''
        result_dict = {i: split_sentence.count(i) for i in split_sentence}
        return result_dict

    else:
        return "Only sentences allowed"
