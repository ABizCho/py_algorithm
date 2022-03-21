'''
알고리즘 수행시간 측정

    프로그램을 수행하는 컴퓨터 성능 및 환경에 따라 수행시간이 다르게 나옴
    (= 대략적인 상대 비교를 위해 사용하자)
'''

import time

# 측정 시작
start_time = time.time() 


# 메인 소스코드 ( 측정 대상 )
for i in range(1000) :
    print(i)
    
# 측정 종료
end_time = time.time() #
print('time :',end_time - start_time) # 수행시간 출력
