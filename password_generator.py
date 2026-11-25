import random
numbers = int(input("How many numbers do you want?"))
letters = int(input("How many letters do you want?"))
symbols = int(input("How many symbols do you want?"))

numb = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
let = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]
sym = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

password1 = []

for i in range (numbers):
    password1.append(random.choice(numb))
for i in range (letters):
     password1.append(random.choice(let))
for i in range (symbols):
     password1.append(random.choice(sym))

random.shuffle(password1)
password = "".join(password1)
print (password)