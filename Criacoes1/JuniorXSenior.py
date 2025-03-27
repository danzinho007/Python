def merge_words(words):
    output = None
    if len(words) == 0:
        output = ""
    else :
        output = words[0]
        if 1 == len(words):
            return output
        else :
            for word in words[1:]:
                output += " " + word
    return output

words_list = ["Hello", "world", "from", "Python"]
result = merge_words(words_list)
print(result)  # Output: "Hello world from Python"
