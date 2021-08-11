"""
    1) List are mutable -  they will be method to add update and delete element from the list
    2) List is ordered data structure - support indexing slicing
    3) multiple data type
"""

subjects = [10,20,30,40,"python",'java',[100,200,300,400]]

print(subjects[0]) #0
print(subjects[-1]) #[100,200,300,400]
print(subjects[-1][0]) #100

#reversed
print(subjects[::-1])

