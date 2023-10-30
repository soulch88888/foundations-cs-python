#Exercie1 :
num = int(input("enter your number: "));
numCounter = num;
NumOfDigits = 0;
while True:
    NumOfDigits += 1;
    # print(NumOfDigits);
    # print(numCounter);
    if numCounter // 10 == 0:
        break;
    else: numCounter = numCounter//10;
print("the number of digits is: ", NumOfDigits);

#-----------------------------------------------------------------------
#Exercie2 :
n = int(input("Enter a number (n): "))
for i in range(1, n + 1):
    print('*' * i);

#-----------------------------------------------------------------------
#Exercie3 :
list1 = [54,76,2,4,98,100];
flag = 0;
int1 = int(input("enter the first integer: "));
int2 = int(input("enter the second integer: "));
while int1 > int2:
    print("Please enter the small integer first.");
    int1 = int(input("enter the first integer: "));
    int2 = int(input("enter the second integer: "));
for i in range(len(list1)):
    if list1[i] > int1 and list1[i] <int2:
        print(list1[i]);
        flag = 1;
if flag == 0:
    print("there is no corresponding values in the list ");

#-----------------------------------------------------------------------
#Exercie4 :
Names = ["Maria", "Hala", "Ghady", "Ehsan", "Joe", "Zoe"];
while True:
    letter = input("enter a letter or write 'stop' to exit:").lower();
    foundNames = [];
    if letter == 'stop':
        break;
    for i in range(len(Names)):
        if letter in Names[i].lower():
            foundNames.append(Names[i]);
    print(foundNames);


