import numpy as np
def shellSort(array, n):

    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                (array[j], array[j + 1]) = (array[j + 1], array[j])

data = np.random.randint(100, size=8)
print('Terdapat 8 bilangan acak yang masih belum terurut : ')
print(data)    
print('')
print('Pilih Metode Pengurutan :')         
print ('1. Bubble Sort')
print ('2. Shell Sort')
sort = input()



if sort == 1 :
  bubbleSort(data)
  print('Hasil pengurutan dengan metode Bubble sort : ')
  print(data)
else :
  size = len(data)
  shellSort(data, size)
  print('Hasil pengurutan dengan metode Shell sort:')
  print(data)
