

def reverse_string(value):
    if type(value)==list or type(value) == str:
        return value[::-1]
    return str(value)[::-1]

print(reverse_string('Python'))
print(reverse_string([10,20,30,40]))
print(reverse_string(1234))