# P(n, r) = n! / (n-r)

"""
abc n = 3
=>
abc
acb
bac
bca
cab
cba

abcd (n = 4)
abcd
=>
a bcd
a bdc
a cbd
a cdb
a dbc
a dcb

b acd
b adc
b cad
b cda
b dac
b dca

"""

def permute(text, index):
    if index >= len(text):
        print("".join(text))
        return
    permute(text, index + 1)
    for i in range(index + 1, len(text)):
        text[index], text[i] = text[i], text[index]
        permute(text, index + 1)
        text[index], text[i] = text[i], text[index]

text = list(input())
permute(text, 0)

