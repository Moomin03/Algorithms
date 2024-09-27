# 백준 2750번

import sys
# 입력 받는 횟수
N = int(sys.stdin.readline())

# 반복된 값을 저장하는 리스트
Lst = []

# N만큼 반복하여 해당 리스트에 저장
for _ in range(N):
    Got = int(sys.stdin.readline())
    Lst.append(Got)

# 해당 리스트를 정렬
Lst.sort()
# Lst = sorted(Lst)

# 해당 리스트 출력
for i in Lst:
    print(i)