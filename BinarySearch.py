a = [5, 12, 28, 29, 40, 41, 53, 54, 68, 69, 79, 80, 83, 89, 90, 100]
x = input('Input a number: ')
left = 0
right = len(a) - 1


while left <= right:
    middle = (left + right) // 2
  
    if a[middle] == int(x): 
        print('[{:2}] 목록에 {:3}이(가) 있습니다'.format(x, middle))
        break   
    elif a[middle] < int(x):
        left = middle + 1    
    else:
        right = middle - 1

if left > right: 
    print('{:3}이(가) 목록에 없습니다.'.format(x))
