def spin_words(sentence):
    output = ' '.join([word[::-1] if len(word)>=5 else word for word in sentence.split()])
    print(output)
    return output