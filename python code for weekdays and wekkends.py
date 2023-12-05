a = str(input("Enter the day: "))
if(a=="saturday" or a=="sunday"):
    print("Weekend")
elif(a=="monday" or a=="tuesday" or a=="wednesday" or a=="thursday" or a=="friday"):
    print("Weekday")
else:print("Enter a valid input.")