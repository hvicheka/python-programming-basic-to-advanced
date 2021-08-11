def linear_search(arr,key):
    for value in arr:
        if value == key:
            return True
    return False



numbers = [10,20,30,40,50]
key = 40
result = linear_search(numbers,key)
print(result)