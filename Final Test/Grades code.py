grades = ['62','68','93','75','89','85']

print(grades [3])

def lettergrade (grades):

    if grades >=90:
        print('A')
    elif grades >=80 and grades <90:
        print('B')
    elif grades >=70 and grades <80:
        print('C')
    elif grades >=60 and grades <70:
        print('D')
    else:
        print('F')


print(lettergrade(grades))