sentence = "this is a cat"


def short_word_length(sentence):


    my_list = list(sentence.split(" "))
    result = min((word for word in my_list if word), key=len)

    print("The length of the shortest word '%s' is %s!" % (result, len(result)))

short_word_length(sentence)
