# dice roll assigment

# random not built in python
import random

# main program loop
loop = True
while loop:
    print("Option 1: Roll Dice Once")
    print("Option 2: Roll Dice 5 Times")
    print("Option 3: Roll Dice ‘n’ Times")
    print("Option 4: Roll Dice until Snake Eyes")
    print("Option 5: Exit")
    

# get slecetion from user
    selection = input("Enter selection (1-5): ")

    # action bassed on selction 
    if selection == "1":

        for n in range(1):   
            randNum1 = random.randint(1, 7)
            randNum2 = random.randint(1, 7)
            print(str(randNum1) + "," + str(randNum2) + " " + "(sum: " + str(randNum1 + randNum2) + ")" )
    
    elif selection == "2":
        for n in range(5):   
            randNum1 = random.randint(1, 7)
            randNum2 = random.randint(1, 7)
            print(str(randNum1) + "," + str(randNum2) + "2" + "(" + str(randNum1 + randNum2) + ")" )       

    elif selection == "3":
         rolls = float(input("How many rolls would you like?"))
         for n in range(int(rolls)):   
            randNum1 = random.randint(1, 7)
            randNum2 = random.randint(1, 7)
            print(str(randNum1) + "," + str(randNum2) + "2" + "(" + str(randNum1 + randNum2) + ")" )        
    elif selection == "4":
         rolls = float(input("How many rolls would you like?"))
         for n in range(int(rolls)):   
            randNum1 = random.randint(1, 7)
            randNum2 = random.randint(1, 7)
            print(str(randNum1) + "," + str(randNum2) + "2" + "(" + str(randNum1 + randNum2) + ")" )        
