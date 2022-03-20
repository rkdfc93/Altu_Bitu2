import sys  #sys 모듈 불러오기

input = sys.stdin.readline  #입력 설정

"""
 "분배법칙"을 활용!
 ex. ([]([])): 2 x (3 + 2 x 3) == 2 x 3 + 2 x 2 x 3
 =>                               (   [ ]     (   [   ]   )   )
 =>                   임시변수값:  2   6 2     4  12   4   2   1
 =>                        정답:        +6           +12        = 18

 따라서, 우선 여는 괄호가 나오면 괄호의 값을 곱해줌
 닫는 괄호는, 이전 문자가 여는 괄호일 경우 지금까지 곱한 값을 더해줌 (값이 중복으로 더해지는 것을 방지하기 위해 이전 문자가 여는 괄호인지 꼭 체크!)
            한 괄호에 대한 연산이 끝났으므로 (곱하기 연산) 다시 괄호 값을 나눠줘서 연산 진행
"""


def calc(text): #문자열을 입력받아 괄호의 값을 반환하는 함수
    bracket = dict()  # 괄호 쌍 저장
    bracket[')'] = '('  #() 쌍 저장
    bracket[']'] = '['  #[] 쌍 저장
    value = dict()  # 괄호 값 저장
    value['('] = 2  #() 값 = 2 저장
    value['['] = 3  #[] 값 = 3 저장

    stack = []  #스택 생성
    answer = 0  #반환할 값 초기화
    weight = 1  # 누적값 -> 밖을 감싸고 있는 괄호들의 곱
    prev = None  # 직전 괄호

    for i in text:  #문자열의 한 문자마다
        if i == '(' or i == '[':    #여는 괄호인 경우
            # 여는 괄호 시 곱하기
            weight *= value[i]  #누적값에 현재 괄호의 괄호값을 곱한다
            stack.append(i)     #스택에 현재 괄호를 넣는다
        else:   #여는 괄호가 아닌 경우
            if len(stack) == 0 or stack[-1] != bracket[i]:  # 올바르지 않은 괄호
                return 0    #올바르지 않으면 0을 반환하여 종료한다
            if prev == bracket[i]:  # (), [] 형태가 있다면, 현재까지 누적된 값을 더해줌
                answer += weight    #올바른 괄호 형태이므로 총 괄호값에 현재까지 누적된 값을 더한다

            # 괄호가 닫혔으므로, 누적값 나누기
            weight //= value[bracket[i]]    #누적값을 나누어서 현재까지의 계산을 마무리한다
            stack.pop() #스택에서 열린 괄호를 제거한다
        prev = i    #직전괄호가 현재 괄호로 변한다

    # 올바른 괄호라면
    if len(stack) == 0: #스택에 남은 것이 없어 올바른 괄호열이라면
        return answer   #전체 괄호값을 반환하여 종료한다

    return 0    #올바르지 않으면 0을 반환하여 종료한다


# 입력
s = input().rstrip()    #문자열은 \n을 제거하여 저장한다
# 연산 + 출력
print(calc(s))  #함수를 호출하고 결과값을 출력한다