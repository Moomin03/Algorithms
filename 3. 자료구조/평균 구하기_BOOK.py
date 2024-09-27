'''
    나의 풀이와 다른점은, 나는 입력 받은 값을 하나, 하나 변환했다면
    책에서는 공통적인 부분을 하나로 묶어서 계산했다.
    (A / M * 100 + b / M * 100 + c / M * 100) / 3 = (A + B + C) * 100 / 3
'''
n = input()
mylist = list(map(int, input().split()))
mymax = max(mylist)
sum = sum(mylist)
print(sum*100/mymax/int(n))
