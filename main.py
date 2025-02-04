#Take input of a string
str1 = input("please Enter a sentence: ")
total = 1 #initialise

fori in range (len(str1)): # type: ignore
#loop will run to calculate the length using string operation
if(str1[i] == ' ' ):
    #condition 1
        total = total + 1

print("Total Number of Words in this String = ", total)

