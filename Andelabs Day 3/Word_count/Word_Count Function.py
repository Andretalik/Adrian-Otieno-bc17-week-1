def words(sentence):
    if isinstance(sentence, str):
        result_dict = {}
        i = 0
        split_sentence = sentence.split()
        for i in range(i, len(split_sentence)):
            print(result_dict)
            for j in range(i+1, len(split_sentence)):
                if split_sentence[i] == split_sentence[j]:
                    print(split_sentence[i])
                    result_dict[split_sentence[i]] = 1
                    result_dict[split_sentence[i]] += 1
                #else:
                    #result_dict[split_sentence[i]] = 1


    return (result_dict)
