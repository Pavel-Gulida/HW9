
def popular_words (text, words):
    text = text.lower()
    text = text.split()
    d1 = dict.fromkeys(words, 0)
    for word in words:
        for text_word in text:
            if word == text_word:
                d1[word] += 1
    return d1


assert popular_words("When I was One I had just begun When I was Two I was nearly new", ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
