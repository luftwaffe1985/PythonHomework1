str = input("Enter a formula: ")
str = str.split(" ")    
for i in range (len(str)):
    if str[i] == '*':
        result1 = int(str[i-1]) * int(str[i+1]) 
    elif str[i] == '/':
        result1 = int(str[i-1]) / int(str[i+1])
# print (int(result1))
for i in range (len(str)):
        if str[i] == '+':
            result = result1 + int(str[i-1]) 
        elif str[i] == '-':
            result = int(str[i-1]) - result1 
print (int(result))
