'''

Abraham Cheng
cs 458
homework 1, correct coin change dynamic programming solution

'''


def dynamicchange(money, coins, result):    #include results table to make lookup faster
    for count in range(money + 1):
        minimum = count                     #count gets a value in amount of change to be calculated
        for i in[j for j in coins if j <= minimum]:     #j looks through coins as long as coins <= money
            if result[count - i] + 1 < minimum:
                minimum = result[count - i] + 1
        result[count] = minimum
    return result[money]

print("input your amount of change:")
money = int(input())                        #cast to int type, default is nonetype
if money == 0:                              #check input for 0
    print("Error, change is 0")
    exit(0)
print("input your coin denominations separated by a space:")
coins = [int(x) for x in input().split()]   #translate user input separated by space into list
print(dynamicchange(money, coins, [0]*(money + 1)),"coins")     #initialize results list + 1 to account for indexing