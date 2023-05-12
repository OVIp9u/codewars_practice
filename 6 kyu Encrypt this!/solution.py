def encrypt_this(text):
    if not text:
        return ''

    text_list = text.split(' ')
    text_code = ''
    for word in text_list:
        word_code = ''
        if len(word)>0:
            word_code += str(ord(word[0]))
        if len(word)>1:
            word_code += str(word[-1])
        if 2<len(word)<=3:
            word_code += str(word[1])
        elif len(word)>3:
            word_code += str(word[2:-1]) + str(word[1])
        text_code += word_code + ' '    
    return text_code[:-1]
