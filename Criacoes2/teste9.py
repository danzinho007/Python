import random

NUM_OF_TICKET = 20
LENGTH_OF_TICKET = 10

char_lst = []

def get_lst(lst, c1, c2):
    for i in range(ord(c1), ord(c2) + 1):
        lst.append(chr(i))

get_lst(char_lst, '0', '9')
get_lst(char_lst, 'a', 'z')
get_lst(char_lst, 'A', 'Z')

def gen_ticket():
    return "".join(random.choices(char_lst, k=LENGTH_OF_TICKET))

result = set()
while len(result) < NUM_OF_TICKET:
    result.add(gen_ticket())

print(result)
