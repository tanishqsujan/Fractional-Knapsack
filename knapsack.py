class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
        
#main greedy function to solve problem
def fractionalknapsack(W, arr):
    
    #Sorting item on basis of ratio
    arr.sort(key = lambda x: (x.profit/x.weight), reverse= True)
    
    #Result (value in knapsack)
    Finalvalue = 0.0
    
    #Looping through all items
    for item in arr:
        
        #If adding item won't overflow, add it completely
        if item.weight <= W:
            W -= item.weight
            Finalvalue += item.profit
            
        #If we can't add current item, add fractional part of it
        else:
            Finalvalue += item.profit * W / item.weight
            break
        
    #returning the final value
    return Finalvalue

#Driver code
if __name__ == "__main__":
    W = 50
    arr = [Item(60, 20), Item(90, 30), Item(40, 10)]
    
    #Function call
    max_val = fractionalknapsack(W, arr)
    print(max_val)