def login(username,password):
    if username == "abc":
        if password == 'abc@123':
            return 'Login success'
        return 'Incorrect password'
    return 'Username is not exist'


result = login('admin', '12345678')
print(result)

result = login('abc','12345678')
print(result)

result = login('abc', 'abc@123')
print(result)

