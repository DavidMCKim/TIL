# 그림과 같이 예금액과 이자율을 입력 받아서
# 예금액, 이자율, 예금이자, 잔액 출력

credit = eval(input("예금액 입력 : "))
interest_rate = eval(input("이자율 입력(%) : "))
deposit_interest = (credit*interest_rate)/100

print("----------------------")
print("예금액 : ", credit, "원")
print("dlwkdbf : ", interest_rate, "%")
print("예금이자 : ", int(deposit_interest), "원")
print("잔액 : ", int(credit+deposit_interest), "원")
print("----------------------")

print("예금액 : ", format(credit,","), "원")
print("dlwkdbf : ", interest_rate, "%")
print("예금이자 : ", format(int(deposit_interest),","), "원")
print("잔액 : ", format(int(credit+deposit_interest),","), "원")




