# 배열의 주어진 범위의 합을 2로 나눈 몪을 구하시오
import random

test_case = int(input())
answer = 0
A = [0] * 100001

for i in range(10001):
    A[i] = random.randrange(1, 101)

for t in range(1, test_case+1):
    start, end = map(int, input().split())
    
    for i in range(start, end+1):
        answer += A[i]
    
    print("{} | {}".format(test_case, answer/2))