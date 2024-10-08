import sys
'''
    # 백준 11720번
    1. 프로그램 입력 조건 확인하기
        - 시간 제한이 1초이고, 입력받는 N의 개수가 100개 이하이므로
        최대 시간 복잡도는 O(N**3)까지도 가능하다!
    2. 출력 형식 확인하기
        - 하나의 값으로 출력된다!
    3. 자료구조 정하기
        - 문자열이 주어질 때, 문자열에 리스트를 씌우면 '111111' 이던 값이 [1, 1, 1, 1, 1, 1]로 변한다.
        따라서 리스트 구조를 사용해야한다.
    4. 알고리즘 정하기
        - 파이썬에 내장되어 있는 합 알고리즘인 sum()함수를 사용해야한다. (시간복잡도 O(N))
'''

N = int(sys.stdin.readline().strip())
M = list(map(int, sys.stdin.readline().strip()))
print(sum(M))