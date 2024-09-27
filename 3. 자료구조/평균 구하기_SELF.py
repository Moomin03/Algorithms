import sys
'''
    # 백준 1546번
    1. 프로그램 입력 조건 확인하기
        - 시간 제한이 2초, 입력 받는 값이 1000보다 작거나 같으므로
        최대 시간 복잡도는 O(N**2)까지도 가능하다!
    2. 출력 형식 확인하기
        - 소숫점이 있는 상태로 출력이 되었다.
    3. 자료구조 정하기
        - 리스트 형태를 사용해서 해당 값을 입력받는다.
    4. 알고리즘 정하기
        - 최대값을 M이라고 할때, 모든 점수를 점수 / M * 100의 형태로 고친다.
        - 이후에 해당 리스트를 sum()하고 리스트의 길이로 나눈다.
'''

N = int(sys.stdin.readline().strip())
Lst = list(map(int, sys.stdin.readline().strip().split()))
M = max(Lst)
New_score = [i/M*100 for i in Lst]
print(sum(New_score)/len(New_score))