from math import sqrt
str = input('Enter a list of numbers: ')
strlst = str.split()
try:
    lst = list(map(int, strlst))
    for num in lst:
        if num > 100 or num < 0:
            raise ValueError
except ValueError:
    print('Some incorrect values were entered')
    quit()
mean = sum(lst)/len(lst)
std = sqrt(sum([(i - mean)**2 for i in lst])/len(lst))
print(f'The Mean is {round(mean, 3)} and the Standard deviation is {round(std, 3)}')
