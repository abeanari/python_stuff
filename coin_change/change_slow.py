'''

Abraham Cheng
cs 458
homework 1, correct coin change recursive solution

'''
def Recursivechange(money, coins):
    minimum = money
    if money in coins:
        #print("1 %d coin" %money)
        return 1
    else:
        for i in [j for j in coins if j <= money]:      #nested loop one to check coins<=money and an iterative loop for coins found
            numCoin = 1 + Recursivechange(money-i, coins)
            if numCoin < minimum:
                minimum = numCoin
    return minimum



print("input your amount of change:")
money = int(input())                        #cast to int type, default is nonetype
if money == (0):                            #check input for 0
    print("Error, change is 0")
    exit(0)
print("input your coin denominations separated by a space:")
coins = [int(x) for x in input().split()]   #translate user input separated by space into list
print(Recursivechange(money, coins),"coins")
