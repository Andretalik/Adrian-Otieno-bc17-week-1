def words(sentence):
    if isinstance(sentence, str):
        split_sentence = sentence.split()
        result_dict = {}
        for word in split_sentence:
            #print(word) : this was and still could be used for debugging purposes
            if word in result_dict:
                if word.isdigit():
                    word = int(word)
                    result_dict[word] += 1
                else:
                    result_dict[word] += 1
            else:
                if word.isdigit():
                    word = int(word)
                    result_dict[word] = 1
                else:
                    result_dict[word] = 1
    return result_dict
    else:
        return "Only sentences accepted"
    
