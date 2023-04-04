RED = "red"
BLUE = "blue"
YELLOW = "yellow"
color1 = str(input("Enter the first primary colour in lower case letters:"))
color2 = str(input("Enter the second primary colour in lower case letters:"))
if color1!=RED and color1!=BLUE and color1!=YELLOW:
    print("Error: Invalid Color1") 
elif color2!=RED and color2!=BLUE and color2!=YELLOW:
    print("Error: Invalid Color2")
elif color1==color2:
    print("Error: The two colors you entered are same.")
else:
    if color1 == RED and color2 == BLUE or color1==BLUE and color2 == RED :
        print("PURPLE")
    elif color1 == BLUE and color2 == YELLOW or color1 == YELLOW and color2 == BLUE: 
        print("GREEN") 
    elif color1 == RED and color2 == YELLOW or color1 == YELLOW and color2 == RED:
        print("ORANGE")