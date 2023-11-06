items = [["tomato", 1], ["potato", 2], ["chocolate", 3], ["soap", 0.5]]
allItems = []
couponValue = 100
def addItem(allItems):
    print("the available items and their prices: ", items);
    itemChoice = input("choose an item from the list: ");
    qty = int(input("enter the quantity: "))
    for item in allItems:
        if itemChoice == item[0]:
            item[1] += qty
            return allItems
    return allItems.append([itemChoice,qty])

def checkTotal(allItems):
    totalSum = 0
    for item in allItems:
        currentItem, currentItemQty = item[0], item[1]
        for i in items:
            if currentItem == i[0]:
                totalSum += currentItemQty*i[1]
    print("the total is: ", totalSum)
    return totalSum
def addCoupon(allItems):
    global couponValue
    sale = int(input("enter the coupon value: "))
    totalSum = checkTotal(allItems)*(sale/100)
    couponValue = sale
    print("the total with the discount is: ", totalSum)
def checkout(allItems,couponValue):
    print("the items purchased are: ",allItems)
    print("the total without the coupons applied is: ", checkTotal(allItems))
    print("the total of coupons applied is : ",couponValue,"% ")
    print("the total with coupons applied is :", checkTotal(allItems) * couponValue/100)


def newOrder():
    choice = -99
    while choice != 4:
        print("Enter")
        print("1. to add an item")
        print("2. to check total")
        print("3. to add a coupon")
        print("4. to checkout")

        choice = int(input())

        if choice == 1:
            addItem(allItems)
        elif choice == 2:
            checkTotal(allItems)
        elif choice == 3:
            addCoupon(allItems)
        elif choice == 4:
            checkout(allItems,couponValue)
        else:
            print("ivalid input")

def mainMenu():
    choice = -99
    while choice != 2:
        print("Enter")
        print("1. to start a new order")
        print("2. to close the program")

        choice = int(input())

        if choice == 1:
            print("starting a new order...")
            newOrder()
        elif choice == 2:
            print("bye bye")
        else:
            print("ivalid input")


mainMenu()