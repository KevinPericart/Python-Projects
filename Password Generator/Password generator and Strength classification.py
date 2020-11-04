import random, string

def password(length, num = False, strength = 'weak'):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    letter = lower + upper
    dig = string.digits
    punct = string.punctuation
    pwd = ''
    if strength == 'weak':
        if num:
            length -= 2
            for i in range(2):
                pwd += random.choice(dig)
        for i in range(length) :
            pwd += random.choice(lower)

    elif strength == 'strong' :
        if num :
            length -= 2
            for i in range(2) :
                pwd += random.choice(dig)
        for i in range(length) :
            pwd += random.choice(letter)

    elif strength == 'very' :
        ran = random.randint(2, 4)
        if num :
            length -= ran
            for i in range(ran) :
                pwd += random.choice(dig)
        length -= ran
        for i in range(ran) :
            pwd += random.choice(punct)
        for i in range(length) :
            pwd += random.choice(letter)

    pwd = list(pwd)
    random.shuffle(pwd)
    return ''.join(pwd)

print(password(2, num = True, strength = 'weak'))
print(password(10, num = True, strength = 'strong'))
print(password(15, num = True, strength = 'very'))
