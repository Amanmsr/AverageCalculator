from math import sqrt
def average(lst):
    mean = 0
    for num in lst:
        mean += num
    mean /= len(lst)
    return mean

#static list
str = input('Enter a list of numbers: ')
lst = list(map(int, str.split(' ')))
lstsq = [(i - average(lst))**2 for i in lst]
print(f'The Mean is {average(lst)} and the Standard deviation is {sqrt(average(lstsq))}')
