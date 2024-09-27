import sys
'''
    # 백준 11659번
    1. 프로그램 입력 조건 확인하기
        - 시간 제한 0.5초, 주어진 값이 100,000 이므로
        시간 복잡도는 O(N)정도의 알고리즘이 적당하다.
    2. 출력 형식 확인하기
        - 한줄씩 출력한다.
    3. 자료구조 정하기
        - 데이터를 받고 이를 더해야 하므로 리스트를 사용한다.
    4. 알고리즘 정하기
        - 구간 합을 구하는 알고리즘을 사용한다.
'''

N, M = map(int, sys.stdin.readline().split()) # N 수의 개수, M 합을 구해야하는 횟수
Lst = list(map(int, sys.stdin.readline().strip().split())) # N 개의 수
sum_Lst = [0]

# 구간 합 구하기
plus = 0
for i in range(len(Lst)):
    plus += Lst[i]
    sum_Lst.append(plus)
for i in range(M):
    s, e = map(int, sys.stdin.readline().split())
    print(sum_Lst[e] - sum_Lst[s-1])