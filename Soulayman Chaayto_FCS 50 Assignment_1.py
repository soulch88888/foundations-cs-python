# -------------------------Exercie 1 :-----------------------------

top=input("insert top value:");
bottom=input("insert bottom value:");
val=input("insert val:");
if (top > val and bottom < val ):
    print("True");
else :
    print("False");

# ------------------------Exercice 2:----------------------------

a=int(input("insert first integer:"));
b=int(input("insert second integer:"));
c=int(input("insert third integer:"));
# max=0;
# min=0;
if (a > b and a > c ):
    # max=a;
    print("The max value is a");
    if b>c :
        # min=c;
        print("The min value is c");
    else:
        # min=b;
        print("The min value is b");
elif (b > a and b > c):
    # max=b;
    print("The max value is b");
    if a>c:
        # min=c;
        print("The min value is c");
    else:
        # min=a;
        print("The min value is a");
else :
    # max=c;
    print("The max value is c");
    if a>b :
        # min = b;
        print("The min value is b");
    else :
        # min=a;
        print("The min value is a");
# print("the max value is: ", max);
# print("\nthe min value is: ", min);


# -------------------Exercie 3----------------------------

grade=float(input("Enter your grade: "));
if grade < 0:
    print("Invalid Grade");
elif grade <=59:
    print("F");
elif grade < 69:
    print("D");
elif grade < 79:
    print("C");
elif grade < 89:
    print("B");
elif grade < 100:
    print ("A");
else :
    print("Invalid Grade");
