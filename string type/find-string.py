subjects = "HTML,CSS,PYTHON,JAVA,DJango"

print('PYTHON' in subjects)
print(subjects.index('PYTHON'))
#print(subjects.index('python')) #error

print(subjects.find('PYTHON'))
print(subjects.find('HTML'))
print(subjects.rfind('HTML'))