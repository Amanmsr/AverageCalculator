from math import sqrt
def average(lst):
    mean = 0
    for num in lst:
        mean += num
    mean /= len(lst)
    return mean

#static list
lst = [6, 5, 5, 6, 7, 6]
lstsq = [(i - average(lst))**2 for i in lst]
print(f'The mean is {average(lst)} and the standard deviation is {sqrt(average(lstsq))}')
