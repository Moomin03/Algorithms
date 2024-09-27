import sys
'''
    # 백준 10986번
    1. 프로그램 입력 조건 확인하기
        - 시간 제한 1초, 주어질 N의 값이 1,000,0000개 이므로
        O(N) 시간 복잡도를 사용해야겠다.
    2. 출력 형식 확인하기
        - 갯수를 출력한다. (하나의 값)
    3. 자료구조 정하기
        - 구간합을 사용해야 하므로 리스트를 사용한다.
    4. 알고리즘 정하기
        - 구간 합을 구하는 알고리즘을 사용한다.
'''
N, M = map(int, sys.stdin.readline().split())
goo_sum = []
N_list = [int(i) for i in sys.stdin.readline().split()]
prefix_sum = [0]*N
prefix_sum[0] = N_list[0]
answer = 0
C = [0]*M
for i in range(1, N):
    prefix_sum[i] = prefix_sum[i-1]+N_list[i]

for i in range(N):
    remainder = prefix_sum[i]%M
    if remainder==0:
        answer+=1
    C[remainder] += 1
for i in range(M):
    if C[i]>1:
        answer += (C[i]*(C[i]-1)//2)

print(answer)