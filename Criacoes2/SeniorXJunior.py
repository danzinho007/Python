from typing import Sequence

def merge_words(words: Sequence[str]) -> str:
    if len(words) == 0:
        return ""
    output = words[0]
    if len(words) == 1:
        return output
    for word in words[1:]:
        output += " " + word
    return output

words_list = ["Hello", "world", "from", "Python"]
result = merge_words(words_list)
print(result)  # Output: "Hello world from Python"
