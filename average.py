from math import sqrt
def average(lst):
    mean = 0
    for num in lst:
        mean += num
    mean /= len(lst)
    return mean

#static list
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
lstsq = [(i - average(lst))**2 for i in lst]
print(f'The Mean is {round(average(lst), 3)} and the Standard deviation is {round(sqrt(average(lstsq)), 3)}')
