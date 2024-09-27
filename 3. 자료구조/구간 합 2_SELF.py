import sys
'''
    # 백준 1546번
    1. 프로그램 입력 조건 확인하기
        - 시간 제한 1초, 약 2000만번 계산 가능하다! 
        표의 크기는 최대 1024라서 O(N**2)까지는 상관이 없지만, 주어지는 줄의 개수가
        10만개 이하이므로 해당 합을 구간마다 구할 수 없어서 구간 합 알고리즘을 사용해야한다.
    2. 출력 형식 확인하기
        - 구간이 주어졌을 때, 바로 값을 반환한다.
    3. 자료구조 정하기
        - 리스트의 첫 값을 0으로 받는 다는 것이 가장 중요핟.
    4. 알고리즘 정하기
        - 구간 합 알고리즘을 사용했다.
'''

N, M = map(int, sys.stdin.readline().split())
A = [[0]*(N+1)]
sum_data = [[0]*(N+1) for _ in range(N+1)]
for _ in range(N):
    row = [0]+[int(x) for x in sys.stdin.readline().split()]
    A.append(row)
for i in range(1, N+1):
    for j in range(1, N+1):
        sum_data[i][j] = sum_data[i][j-1]+sum_data[i-1][j]+A[i][j]-sum_data[i-1][j-1]
for _ in range(M):
    a, b, c, d = map(int, sys.stdin.readline().split())
    print(sum_data[c][d]-sum_data[c][b-1]-sum_data[a-1][d]+sum_data[a-1][b-1])