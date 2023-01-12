import random
print("                                              Welcome to the number guessing game!")
print()                                
print()
wr=0
a=random.randint(0,100)
print("A no. between 1 and 100 is being generated.....")
for i in range(100):
    print("Try no. :",i+1)
    u=int(input("Make a guess : "))
    if u == a:
        print("You have guessed the no. correctly!")
        break
    while u!=a:
        if u>a:
            print("The guessed no. is greater than the actual no. ")
            print()
            wr+=1
        if u<a:
            print("The guessed no. is less than the actual no. ")
            print()
            wr+=1
        break
print()
# print("                                              No. of tries taken :",wr+1)
print("                                              Your score is :",99-wr)

