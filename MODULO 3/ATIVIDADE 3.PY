Def bubble_sort(arr):
  n = len(arr)

  for i in range(n):
    for j in range(0,n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]

  return arr

lista = [6,7,82,28,8,28,3,46,4,9,49,64,6,3,1,9,7,78,79,8,9,75,7,8,59,7,6,8,5,75]

print(bubble_sort(lista))