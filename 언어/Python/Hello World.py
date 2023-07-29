#해당 Hello World.py 는 여러 가지 출력을 해보는 걸 기본 목적으로 잡고 있습니다.

#파이썬 오류 확인 방법
#SyntaxError(문법 오류) : 파이썬의 문법, 즉 규칙에 맞지 않아서 컴퓨터가 해석 할 수 없을때 발생한다
#NameError(이름 오류) : 사람이 컴퓨터에 미리 알려주지 않은 이름을 약속 없이 그냥 쓸때 발생한다 ex)변식자가 없는 경우
#TypeError(데이터 종류 오류) : 데이터의 종류에 알맞지 않은 규칙으로 데이터를 처리하려고 할 때 발생한다

#1.기본적인 파이썬 print() 명령어
print("Hello World") #print()로 Hello World출력하기
print("안녕하세요!\n저는 홍길동 입니다!") #\n 는 줄바꿈 기능 입니다.

#2-1.기본적인 데이터 명령어
#파이썬에 기본 데이터 종류는 숫자(정수,실수),문자,리스트 가 있습니다
#프린트 명령어중 ('') ("") '',""은 다 문자로 인식 한다
print('"홍길동은" 이번 시험이 망했습니다...') #작은따옴표로 돌러싸인 전체를 문자로 인식 한다

#print(""홍길동은" 이번 시험이 망했습니다...") 오류 예시

#2-2.문자데이터로 연산하기 + 문자끼리 연결하기
#파이썬 기능에 문자" + "문자"를 연결 기능이 있다 
print("파이썬" + "연결") #이렇게 문자끼리 연결도 가능하다

#파이썬 기능에 문자" (수식) 숫자 를 연산하는 기능이 있다 
print("파이썬" * 10) #이렇게 숫자와 문자를 연결해 "파이썬" 10번을 출력한다

#이렇게 사용더 가능하다
print("파이썬" * 5)
print("-" * 50)
print("시작" * 10)
