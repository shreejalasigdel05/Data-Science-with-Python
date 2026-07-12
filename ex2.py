# def voting(a):
#     try:
#         if a<18:
#         # print("you cannot vote")
#             raise ValueError("Invalid age value")
#         else:
#             print("valid age for voting")
#     except Exception as e:
#         print(e)

# age=int(input("Enter the age: "))
# voting(age)

#custon exception
class BalanceException(Exception):
    pass

def check_bal():
    earn=10000
    exp=3000
    bal=earn-exp
    if bal<2000:
        raise BalanceException('not sufficint amount left')
    else:
        print("sufficient amount",bal)

try:
    check_bal()
except BalanceException as b:
    print (b)