import random
def generate_password(length = 8):
    charactor = ['@','#','$','&']
    upper = chr(random.randint(65, 90))
    lower = chr(random.randint(97,112))
    special_charactor = random.choice(charactor)
    digit = random.randint(10000,99999)
    password =  upper + lower + special_charactor + str(digit)
    sample = random.sample(password,length)
    password = ('').join(sample)

    return password
    

password = generate_password(8)
print(password)
