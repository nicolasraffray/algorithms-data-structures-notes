import math


def binary_search(array, item):
  low = 0
  high = len(array)-1
  
  while low <= high: 
    mid = math.trunc((low + high )/2)
    guess = array[mid]
    if guess == item:
      return int(mid)
    elif guess < item:
      low = mid + 1 
    else:
      high = mid - 1 

  return None
    




