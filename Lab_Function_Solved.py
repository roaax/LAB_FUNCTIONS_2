# LAB_FUNCTIONS_2


## Create a function that takes two parameters of type int . The function should do the following:


def negative( x : int , y : int ) -> str :

    while x > 0 and y > 0:
        print("     Uh! Don't Worry and Follow the instruction")
        print("         First! Enter Two Negative Numbers!")                
        x : int = int(input("   First Number : "  ))
        y : int = int(input("   Second Number : "  ))
        continue
    else: 
        while x > y:
                return "         First Parameter Should be Smaller than Second Parameter!      "
        else:
            negative_loop : str  = ""
            for i in range( x , y+1) : 
                negative_loop = negative_loop + str(i) + "\n"   
    return negative_loop








# print("   Hi! U have to Follow the instruction to win  ")
print("      First! Enter Two Negative Numbers!  ")
x : int = int(input("   First Number : "))
y : int = int(input("   Second Number : "))
negative_loop = negative( x , y)
print(negative_loop)

