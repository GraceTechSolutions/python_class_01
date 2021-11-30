# 6. Create a python programme to accept a numeric digit from keyboard and display in words.


wordlist = {
    '0': '',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'forty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety',
    '100': 'hundred',
    '1000': 'thousand',
}


num = '9239'
word = ''


if len(num) == 4:
    n1 = num[0] # 1
    n1_s = wordlist['1000']
    word = f'{word} {wordlist[n1]} {n1_s}'
    num = num[1:]


if len(num) == 3:
    n1 = num[0] # 2
    n1_s = wordlist['100']
    word = f'{word} {wordlist[n1]} {n1_s}'
    num = num[1:]

if int(num) <=20:
    word = f'{word} {wordlist[num]}'
else:
    n1 = num[0] # 30
    n2 = num[1] # 6
    n1 = n1+'0'
    word = f'{word} {wordlist[n1]} {wordlist[n2]}'

print(word)