str1 = 'abcd'
str2 = '1234'
str3 = 'Python sample string abcd'

# what we want is "Python sample string 1234"

string_map = str.maketrans(str1,str2)
result = str3.translate(string_map)

print('str3 =',str3)
print('result =',result)