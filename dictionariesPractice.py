ask = input("phone number: ")
word_form = ''
word = {
    "1": "one",
    "2": "two",
    "3": 'three',
    "4": 'four',
    "5": 'five',
    "6": 'six',
    "7": 'seven',
    "8": 'eight',
    "9": 'nine',
    '0': 'zero'
}

for x in ask:
   word_form += word.get(x, "!") + " "
print(word_form)