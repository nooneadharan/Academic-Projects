#Choices
def menu():
    print("MAIN MENU\n")
    print("[1]\t PRELIM")
    print("[2]\t MIDTERM")
    print("[3]\t FINALS")
    print("[4]\t Exit\n")

def prelim():
    separator()
    print("PRELIM\n")
    print("[1]\t Display")
    print("[2]\t Input and Output")
    print("[3]\t Performing Calculations")
    print("[4]\t Decision Structure 1")
    print("[5]\t Decision Structure 2")
    print("[6]\t Try and Except")
    print("[7]\t Prelim Laboratory")
    print("[8]\t Exit")

def midterm():
    separator()
    print("MIDTERM\n")
    print("[1]\t Repetition Structure")
    print("[2]\t Looping structure 1")
    print("[3]\t Looping Structure 2")
    print("[4]\t Strings")
    print("[5]\t Function 1")
    print("[6]\t Function 2")
    print("[7]\t Funtion and Module")
    print("[8]\t Exit")

def finals():
    separator()
    print("FINALS\n")
    print("[1]\t List 1")
    print("[2]\t List 2")
    print("[3]\t 2 Dimensional List")
    print("[4]\t Tuple")
    print("[5]\t File Handling")
    print("[6]\t Dictionary")
    print("[7]\t Exit")

#Processing Choices
def prelim_choice():
    prelim_choice = int(input("\nEnter choice: "))
    if prelim_choice == 1:
        prelim_c1()

    elif prelim_choice == 2:
        prelim_c2()

    elif prelim_choice == 3:
        prelim_c3()
        
    elif prelim_choice == 4:
        prelim_c4()

    elif prelim_choice == 5:
        prelim_c5()
    
    elif prelim_choice == 6:
        prelim_c6()

    elif prelim_choice == 7:
        prelim_c7()

    elif prelim_choice == 8:
        print("\nExiting Prelims...")
    
    else: 
        print("\nInvalid Input")

def midterm_choice():
    midterm_choice = int(input("\nEnter choice: "))
    if midterm_choice == 1:
        midterm_c1()

    elif midterm_choice == 2:
        midterm_c2()

    elif midterm_choice == 3:
        midterm_c3()
        
    elif midterm_choice == 4:
        midterm_c4()

    elif midterm_choice == 5:
        midterm_c5()
    
    elif midterm_choice == 6:
        midterm_c6()

    elif midterm_choice == 7:
        midterm_c7()

    elif midterm_choice == 8:
        print("\nExiting Midterms...")

    else: 
        print("\nInvalid Input")

def finals_choice():
    finals_choice = int(input("\nEnter choice: "))
    if finals_choice == 1:
        finals_c1()

    elif finals_choice == 2:
        finals_c2()

    elif finals_choice == 3:
        finals_c3()
        
    elif finals_choice == 4:
        finals_c4()

    elif finals_choice == 5:
        finals_c5()
    
    elif finals_choice == 6:
        finals_c6()

    elif finals_choice == 7:
        print("\nExiting Midterms...")
    
    else: 
        print("\nInvalid Input")

#Prelim Programs
def prelim_c1():
    separator()
    print("Display 1a:")
    print("\"Python\" is a","\twidely used,","\tinterpreted,","\tobject-oriented, and","\thigh-level programing language","with \'dynamic semantics\', used for general-purpose programming.", sep="\n")

    
    print("\nDisplay 1b:")
    print("\"Python\" is a")
    print("\twidely used,")
    print("\tinterpreted,")
    print("\tobject-oriented, and")
    print("\thigh-level programing language")
    print("with \'dynamic semantics\', used for general-purpose programming. ")
    
    print("\nDisplay 1c:")
    a = "\"Python\" is a"
    b = "\twidely used,"
    c = "\tinterpreted,"
    d = "\tobject-oriented, and"
    e = "\thigh-level programing language"
    f = "with \'dynamic semantics\', used for general-purpose programming. "
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)

def prelim_c2():
    separator()
    print("Input and Output 1:")
    character = input ("Input a character: ")
    word1 = input ("Word 1: ")
    word2 = input ("Word 2: ")
    word3 = input ("Word 3: ")
    word4 = input ("Word 4: ")
    word5 = input ("Word 5: ")
    result = word1 + character + word2 + character + word3 + character + word4 + character + word5
    print ("The result:" + result)

    print("\nInput and Output 2:")
    a =input ("Input a floating point value: ")
    print("From float to integer: ", float (a), " to ", int(float(a)))
    print("from integer to string")
    print("Binary: ", int(float (a)), " to ", bin(int(float (a))))
    print("Octal: ", int(float (a)), " to ", oct(int(float (a))))
    print("Hexadecimal: ", int(float(a))," to ", hex(int (float(a))))

def prelim_c3():
    separator()
    print("Performing Calculations: ")
    val1 = int(input ("Input value for x: "))
    val2 = int(input ("Input value for y: "))
    val3 = int(input ("Input value for z: "))

    valx = val1**3
    valy = val2**2
    valz = val3**3

    a = 3
    b = (a * valx * valy * valz)
    c = (b + val1)
    d = (val1 + val2 + val3)
    e = (c / d)

    print (round(e,2))

def prelim_c4():
    separator()
    print("Decision Structure 1:")
    #Student name
    studentname = input("Student Name: ")

    #Year level (1-5)
    yearlevel = int(input("Year Level(1-5): "))
    if yearlevel==1:
        rateperunit = 1325.00
    elif yearlevel==2:
        rateperunit = 1240.00
    elif yearlevel==3:
        rateperunit = 1195.00
    elif yearlevel==4 or 5:
        rateperunit = 1085.00
    else:
        print("Invalid input")

    #Course code (IT/it, N/n, E/e, C/c) determines the lab rate
    coursecode = input("Course Code: ")
    if coursecode=="IT" or "it":
        labrate = 4325.00
    elif coursecode=="N" or "n":
        labrate = 4500.00
    elif coursecode=="E" or "e":
        labrate = 3987.00
    elif coursecode=="C" or "c":
        labrate = 4113.00
    else:
        print("Invalid input")

    #Number of units
    numberofunits = int(input("Number of Units: "))

    #Number of labs
    numberoflabs = int(input("Number of labs: "))

    #Terms of payment determines the discount given 
    termsofpayment = int(input("Terms of Payment: "))
    if termsofpayment==1:
        discount = 2000.00
    elif termsofpayment==2:
        discount = 1000.00
    elif termsofpayment>=3:
        discount = 0.00
    else:
        print("Invalid terms of payment!")

    #Divider/line display
    print('\n==========================\n')

    #Breakdown of fees
    print("Breakdown of Fees: ")

    #Tuition fee is the product of the rate per unit and the number of units 
    tuitionfee = rateperunit * numberofunits
    print("Tuition Fee: P {:,.2f}".format(tuitionfee))

    #Laboratory fee is the product of the number of labs and lab rates
    laboratoryfee = numberoflabs * labrate
    print("Laboratory Fee: P {:,.2f}".format(laboratoryfee))

    #Miscellaneous fee is the product of the tuition fee and 6.7% or 0.067
    miscellaneuosfee = tuitionfee * 0.067
    print("Miscellaneus Fee: P {:,.2f}".format(miscellaneuosfee))

    #Total amount due is the sum of the tuition fee, laboratory fee, and miscellaneous fee
    totalamountdue = tuitionfee + laboratoryfee + miscellaneuosfee
    print("Total Amount Due: P {:,.2f}".format(totalamountdue))

    #Discount depends on the terms of payment
    print("Discount: P {:.2f}".format(discount))
    if termsofpayment==1:
        initialpayment = totalamountdue - discount
    elif termsofpayment==2:
        initialpayment = (totalamountdue - discount) / 2
    elif termsofpayment>=3:
        initialpayment = totalamountdue / 10

    #Initial payment
    print("Inital Payment: P {:,.2f}".format(initialpayment))

    #Balance after initial payment
    balanceafterinitialpayment = totalamountdue - initialpayment - discount
    print("Balance after initial payment: P {:,.2f}".format(balanceafterinitialpayment))

def prelim_c5():
    separator()
    distance = float(input('Distance Traveled(km): '))
    time = float(input('Duration of ride(minutes): '))
    addedrate = 4.50
    flagdown = 60 
    totalfare1 = (int(time / 2) * addedrate) + flagdown
    totalfare2 = (distance * addedrate) + flagdown
    if totalfare1>totalfare2:
        print("Total fare: P{:.2f}".format(totalfare1))
    elif totalfare1<totalfare2:
        print("Total fare: P{:.2f}".format(totalfare2))

def prelim_c6():
    separator()
    try:
        a =input ("Input a floating point value: ")
        print("From float to integer: ", float (a), " to ", int(float(a)))
        print("from integer to string")
        print("Binary: ", int(float (a)), " to ", bin(int(float (a))))
        print("Octal: ", int(float (a)), " to ", oct(int(float (a))))
        print("Hexadecimal: ", int(float(a))," to ", hex(int (float(a))))

    except KeyboardInterrupt:
        print("\nThe action does not apply to the program")

    except ValueError:
        print("Invalid input")

    finally: 
        print("Thank you for participating!")

def prelim_c7():
    separator()
    print("MJ LAWN-MOWING SERVICE\n")
    print("==========================\n")
    width = int(input("Enter Width: "))
    length = int(input("Enter Length: "))

    totalSqFt = width * length

    if totalSqFt <= 4000:
        numOfWeek = "2 weeks"
        totalLawn = 50000 * 2
    elif totalSqFt < 6000:
        numOfWeek = "5 weeks"
        totalLawn = 75000* 5
    elif totalSqFt > 6000:
        numOfWeek = "6 weeks"
        totalLawn = 100000 * 6
    else:
        print("Invalid")

    print("Total Sq. Ft: {:,.2f}".format(totalSqFt))
    print("Number of Week/s Lawn: " + numOfWeek)
    print("Total Lawn: {:,.2f}".format(totalLawn))

    print("\nChoose Payment Plan")
    print("[1] Cash")
    print("[2] Twice")
    print("[3] 12 Months\n")

    payPlan = input("Enter Your Payment Plan: ")

    if payPlan == '1':
        serviceCharge = totalLawn * 0
        totalAmtLwn = serviceCharge + totalLawn
        totalPayPrDue = totalAmtLwn 
    elif payPlan == '2':
        serviceCharge = totalLawn * .05
        totalAmtLwn = serviceCharge + totalLawn
        totalPayPrDue = totalAmtLwn / 2
    elif payPlan == '3':
        serviceCharge = totalLawn * .10
        totalAmtLwn = serviceCharge + totalLawn
        totalPayPrDue = totalAmtLwn / 12
    else:
        print("Invalid")

    print("Service Charge: {:,.2f}".format(serviceCharge))
    print("Total Amount Lawn: {:,.2f}".format(totalAmtLwn))
    print("Total Pay Per Due: {:,.2f}".format(totalPayPrDue))
    print("Thank you for choosing MJ!")

#Midterm Programs
def midterm_c1():
    separator()
    print("Repetition Structure:")
    #Initial Investment
    initialInv = int(input("Enter Initial Investment: Php "))
    if initialInv > 0:
        #Annual Investment
        annualInv = int(input("Enter Annual Investment: Php "))
        if annualInv > 0:
            #Annual Interest Rate
            annualInteRate = float(input("Enter Annual Interest Rate (%): "))
            #Converting the Annual Interest Rate from percentage to decimal form
            percent = annualInteRate * 0.01
            if annualInteRate > 0:
                #Years of Investment/ Number of Years
                yrsOfInv = int(input("Enter Number of Years: "))
                print("Year\tAnnual Interest \tSavings")
                year = 0 
                while year < yrsOfInv:
                    year = year + 1
                    annualInt = initialInv * percent
                    initialInv = initialInv + annualInt + annualInv
                    print(year, "\tPhp {:,.2f}".format(annualInt), "\t\tPhp {:,.2f}".format(initialInv))
                print("At the end of", yrsOfInv, "years your savings is Php {:,.2f}".format(initialInv))
            else: 
                print("Invalid Input\nPlease try again") 
        else: 
            print("Invalid Input\nPlease try again")   
    else: 
        print("Invalid Input\nPlease try again")   

def midterm_c2():
    separator()
    print("Looping structure 1:")
    numVal = int(input("Enter the number values needed: "))
    listname = []
    even = []
    odd = []
    for i in range (1, numVal + 1):
        num = int(input("Enter number: "))
        listname.append(numVal)
        if num % 2 == 0:
            even.append(num)
        else: 
            odd.append(num)
    summation = sum(even)
    count = len(odd)
    print("Sum of even numbers: ", summation)
    print("Number of odd numbers: ", count)

def midterm_c3():
    separator()
    print("Looping structure 2:")
    proceed = 1
    while proceed == 1:

        number1 = int(input("Enter 1st number: "))
        number2 = int(input("Enter 2nd number: "))
        proceed = 0    
        if number1 and number2 >=0:
            print("*******************************************\nMain Menu")
            print("[1]\t Output all odd numbers between the first and second number")
            print("[2]\t Output sum of all even numbers between the first and second number")
            print("[3]\t Output all the numbers and their square between the first and second number")
            print("[4]\t Exit")
            print("*******************************************")
            proceed = 1
            while (proceed == 1):
                choice = int(input("Enter choice: "))
                num1 = number1
                num2 = number2
                if choice == 1:
                    proceed = 1
                    print("Menu 1")
                    print("Odd numbers between", num1, "and", num2)
                    if num1 + 1 > num2:
                        num1 = num1 - 1
                        while num1 > num2:
                            print(num1)
                            num1 = num1 - 2
                    elif num1 < num2: 
                        num1 = num1 + 1
                        while num1 < num2:
                            print(num1)
                            num1 = num1 + 2
                    answer = input('Do you want to try Looping Structure 2 again? Answer [y/n]: ')
                    if answer == 'y' or answer == 'Y':
                        proceed = 1
                    elif answer == 'n' or answer == 'N':
                        proceed = 0
                        print('End of Program')

                elif choice == 2:
                    proceed = 1
                    print("Menu 2")
                    add = 0
                    num = num1
                    for i in range(num1, num2 + 1):
                        if num1 % 2 == 0:
                            add = add + num1
                        num1 = num1 + 1
                    print("Sum of all even numbers between", num, "and", num2, "is", add)
                    answer = input('Do you want to try Looping Structure 2 again? Answer [y/n]: ')
                    if answer == 'y' or answer == 'Y':
                        proceed = 1
                    elif answer == 'n' or answer == 'N':
                        proceed = 0
                        print('End of Program')

                elif choice == 3:
                    proceed = 1
                    print("Menu 3")
                    print("Number\tSquare Number")
                    if num1 > num2:
                        x1 = num1
                        while num1 > num2 - 1:
                            print(x1, "\t", num1 * num1)
                            num1 = num1 - 1
                            x1 = x1 - 1
                    elif num1 < num2:
                        x1 = num1
                        while num1 < num2 + 1:
                            print(x1, "\t", num1 * num1)
                            num1 = num1 + 1
                            x1 = x1 + 1
                    answer = input('Do you want to try Looping Structure 2 again? Answer [y/n]: ')
                    if answer == 'y' or answer == 'Y':
                        proceed = 1
                    elif answer == 'n' or answer == 'N':
                        proceed = 0
                        print('End of Program')
                elif choice == 4:
                    print("End of program")
                    proceed = 0

def midterm_c4():
    separator()
    print("Strings:")
    go = 0
    print("Creating a Password")
    print("*"*50)
    print("The password must be at least seven characters long")
    print("It must contain at least one uppercase letter")
    print("It must contain at least one lowercase letter")
    print("It must contain at least one numeric digit")
    print("It must contain at least one special character")
    print("No spaces")
    print("*"*50)

    while  go == 0:

        passw = input("Enter your password: ")
        spechar = ['!', '-', '+', '@', '#', '$', '%', '^', '&', '*', '(', ')', '.', '/', '?',]

        def valid_password():
            if go == 1:
                print("Password is valid.")
            elif go == 0:
                print("Password is not valid. Try again.")

        #The password must be at least seven characters’ long
        if len(passw) >= 7:       
            go = 0

            if len(passw) <= 15:
                go = 0

                #It must contain at least one uppercase letter
                if any(char.isupper() for char in passw):
                    go = 0   

                    #It must contain at least one lowercase letter
                    if any(char.islower() for char in passw):
                        go = 0
        
                        #It must contain at least one numeric digit
                        if any(char.isdigit() for char in passw):
                            go = 0
        
                            #It must contain at least one special character
                            if any(char in spechar for char in passw):
                                go = 0

                                #No spaces
                                if any(char.isspace() for char in passw):
                                    go = 0
                                    valid_password()

                                else: 
                                    go = 1
                                    valid_password()
                            else:
                                valid_password()
                        else:
                            valid_password()
                    else:
                        valid_password()
                else:
                    valid_password()
            else:
                valid_password()
        else:
            valid_password()

def midterm_c5():
    separator()
    print("Function 1:")
    def display_line():
        print("\n" + "*"*50 + "\n")

    def choice1():
        display_line()
        print("MJ LAWN-MOWING SERVICE")
        display_line()
        width = int(input("Enter Width: "))
        length = int(input("Enter Length: "))

        totalSqFt = width * length

        if totalSqFt <= 4000:
            numOfWeek = "2 weeks"
            totalLawn = 50000 * 2
        elif totalSqFt < 6000:
            numOfWeek = "5 weeks"
            totalLawn = 75000* 5
        elif totalSqFt > 6000:
            numOfWeek = "6 weeks"
            totalLawn = 100000 * 6
        else:
            print("Invalid")

        print("Total Sq. Ft: {:,.2f}".format(totalSqFt))
        print("Number of Week/s Lawn: " + numOfWeek)
        print("Total Lawn: {:,.2f}".format(totalLawn))

        print("\nChoose Payment Plan")
        print("[1] Cash")
        print("[2] Twice")
        print("[3] 12 Months\n")

        payPlan = input("Enter Your Payment Plan: ")

        if payPlan == '1':
            serviceCharge = totalLawn * 0
            totalAmtLwn = serviceCharge + totalLawn
            totalPayPrDue = totalAmtLwn 
        elif payPlan == '2':
            serviceCharge = totalLawn * .05
            totalAmtLwn = serviceCharge + totalLawn
            totalPayPrDue = totalAmtLwn / 2
        elif payPlan == '3':
            serviceCharge = totalLawn * .10
            totalAmtLwn = serviceCharge + totalLawn
            totalPayPrDue = totalAmtLwn / 12
        else:
            print("Invalid")

        print("Service Charge: {:,.2f}".format(serviceCharge))
        print("Total Amount Lawn: {:,.2f}".format(totalAmtLwn))
        print("Total Pay Per Due: {:,.2f}".format(totalPayPrDue))
        print("Thank you for choosing MJ!")

    def choice2():
        display_line()
        print("INVESTMENT CALCULATOR")
        display_line()
        initialInv = int(input("Enter Initial Investment: Php "))
        if initialInv > 0:
            annualInv = int(input("Enter Annual Investment: Php "))
            if annualInv > 0:
                annualInteRate = float(input("Enter Annual Interest Rate (%): "))
                percent = annualInteRate * 0.01
                if annualInteRate > 0:
                    yrsOfInv = int(input("Enter Number of Years: "))
                    annualInt = initialInv * percent
                    year = 0
                    print("Year\tAnnual Interest \tSavings")
                    while year < yrsOfInv:
                        year = year + 1
                        annualInt = initialInv * percent
                        initialInv = initialInv + annualInt + annualInv
                        print(year,"\tPhp {:,.2f}".format(annualInt), "\t\tPhp {:,.2f}".format(initialInv))       
                    print("At the end of", yrsOfInv, "years your savings is Php {:,.2f}".format(initialInv))
                else:
                    print("Invalid Input\nPlease try again") 
            else:
                print("Invalid Input\nPlease try again")
        else:
            print("Invalid Input\nPlease try again")

    def choice3():
        display_line()
        print("TAXI FARE CALCULATOR")
        display_line()
        distance = float(input("Distance Traveled(km): "))
        time = float(input("Duration of ride(minutes): "))
        addedrate = 4.50
        flagdown = 60 
        totalfare1 = (int(time / 2) * addedrate) + flagdown
        totalfare2 = (distance * addedrate) + flagdown
        if totalfare1>totalfare2:
            print("Total fare: P{:.2f}".format(totalfare1))
        elif totalfare1<totalfare2:
            print("Total fare: P{:.2f}".format(totalfare2))

    def choice4():
        print("\nEnd of Program\n")

    proceed = 1
    while proceed == 1:
        try:
            print("Choose a function\n")
            print("\tMain Menu")
            print("\t[1] MJ LAWN-MOWING SERVICE")
            print("\t[2] INVESTMENT CALCULATOR")
            print("\t[3] TAXI FARE CALCULATOR")
            print("\t[4] EXIT\n")

            choice = int(input("Enter choice: "))

            if choice == 1:
                proceed = 1
                choice1()
                display_line()
                answer = input("Do you want to try Function 1 again? Answer [y/n]: ")
                if answer == 'y' or answer == 'Y':
                    proceed = 1
                    display_line()
                elif answer == 'n' or answer == 'N':
                    choice4()
                    break

            elif choice == 2:
                proceed = 1
                choice2()
                display_line()
                answer = input("Do you want to try Function 1 again? Answer [y/n]: ")
                if answer == 'y' or answer == 'Y':
                    proceed = 1
                    display_line()
                elif answer == 'n' or answer == 'N':
                    choice4()
                    break

            elif choice == 3:
                proceed = 1
                choice3()
                display_line()
                answer = input("Do you want to try Function 1 again? Answer [y/n]: ")
                if answer == 'y' or answer == 'Y':
                    proceed = 1
                    display_line()
                elif answer == 'n' or answer == 'N':
                    choice4()
                    break
                    

            elif choice == 4:
                choice4()
                break

            else:
                print("Invalid Input")
                display_line()
                answer = input("Do you want to try Function 1 again? Answer [y/n]: ")
                if answer == 'y' or answer == 'Y':
                    proceed = 1
                    display_line()
                elif answer == 'n' or answer == 'N':
                    choice4()
                    break

        except ValueError:
            print("\nInvalid input")
            display_line()
            answer = input("Do you want to try Function 1 again? Answer [y/n]: ")
            if answer == 'y' or answer == 'Y':
                proceed = 1
                display_line()
            elif answer == 'n' or answer == 'N':
                choice4()
                break

def midterm_c6():
    separator()
    print("Function 2:")
    def calc_average(a, b, c, d, e):
        add = a + b + c + d + e
        ave = add / 5
        return ave

    def determine_grade(x):
        if x >= 90 and x <= 100:
            return "A"
        elif x >= 80 and x <= 89:
            return "B"
        elif x >= 70 and x <= 79:
            return "C"
        elif x >= 60 and x <= 69:
            return "D"
        elif x < 60:  
            return "F" 

    #Main
    proceed = 1
    while proceed == 1:
        try:
            gr1 = int(input("Enter 1st test score: "))
            if gr1 > 0 and gr1 <= 100:
                gr2 = int(input("Enter 2nd test score: "))
                if gr2 > 0 and gr2 <= 100:
                    gr3 = int(input("Enter 3rd test score: "))
                    if gr3 > 0 and gr3 <= 100:
                        gr4 = int(input("Enter 4th test score: "))
                        if gr4 > 0 and gr4 <= 100:
                            gr5 = int(input("Enter 5th test score: "))
                            if gr5 > 0 and gr5 <= 100:
                                gr_ave = float(calc_average(gr1, gr2, gr3, gr4, gr5))
                                print("Grade Average: {:.2f}".format(gr_ave))
                                print("Equivalent Letter Grade: ", determine_grade(gr_ave))
                                break
                            else: 
                                print("Score is invalid")
                        else: 
                            print("Score is invalid")
                    else: 
                        print("Score is invalid")
                else: 
                    print("Score is invalid")
            else: 
                print("Score is invalid")
        except ValueError:
            print("invalid input")

def midterm_c7():
    separator()
    print("Function and Module:")
    import moduleManiago
    def intro():
        print("\n" + "*"*50 + "\n")
        print("Peso Conversion Menu")
        print("[1]\tPhilPeso to US Dollar")
        print("[2]\tPhilPeso to AUS Dollar")
        print("[3]\tPhilPeso to Singapore Dollar")
        print("[4]\tUS Dollar to PhilPeso")
        print("[5]\tAUS Dollar to PhilPeso")
        print("[6]\tSingapore Dollar to PhilPeso")
        print("[7]\tExit")
        print("\n" + "*"*50 + "\n")

    #Main
    proceed = 1
    while proceed == 1:  
        intro()   
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            proceed = 1
            val = float(input("Enter value: "))
            moduleManiago.choice1(val)
        elif choice == 2:
            proceed = 1
            val = float(input("Enter value: "))
            moduleManiago.choice2(val)
        elif choice == 3:
            proceed = 1
            val = float(input("Enter value: "))
            moduleManiago.choice3(val)    
        elif choice == 4:
            proceed = 1
            val = float(input("Enter value: "))
            moduleManiago.choice4(val)
        elif choice == 5:
            proceed = 1
            val = float(input("Enter value: "))
            moduleManiago.choice5(val)
        elif choice == 6:
            proceed = 1
            val = float(input("Enter value: "))
            moduleManiago.choice6(val)
        elif choice == 7:
            print("\nEnd of Program")
            proceed = 0

#Finals Programs
def finals_c1():
    separator()
    print("List 1:")
    list1 = []
    List2 = []
    for x in range(7):
        num = x + 1
        hours = float(input("Enter hours worked for employee "+ str(num) + ": "))
        list1.append(hours)
        grosspay = hours * 675.75 
        List2.append(grosspay)
    print ("list of Hours Worked: ", list1)
    print("*"*50)
    for x in range(7):
        num2 = x + 1
        print ("Gross Pay for employee", str(num2),": Php", List2[x])

def finals_c2():
    separator()
    print("List 2:")
    def try_again(a):
        x = 1
        while x == 1:
            answer = input("Do you want to enter another score? Answer [y/n]: ")
            if answer == 'y' or answer == 'Y':
                return 1
                
            elif answer == 'n' or answer == 'N':
                print (a)
                return 0
    def add(b):
        summation = sum(b)
        return float(summation)

    def sum_minus_min(c):
        minimum = min(c)
        summation2 = sum(c) - minimum
        return float(summation2)

    def ave(d):
        minus_min = sum_minus_min(d)
        average = minus_min / (len(d)-1)
        return float(average)
        
    cntr = 1
    listscore = []
    while cntr == 1:
        score = int(input("Enter student score: "))
        listscore.append(float(score))
        cntr = try_again(listscore)

    print("Sum of all the scores: ", add(listscore))
    print("Sum of all the scores minus the min value: ", sum_minus_min(listscore))
    print("Average of all the scores minus the min value: {:.2f}".format(ave(listscore)))

def finals_c3():
    separator()
    print("2 Dimensional List")
    #List for years
    years = []
    #List for all quarters per year
    all_qtr_list = []
    #List for all sum of all quarters per year
    annual_sales_list = []

    isyc = int(input("Input starting year covered: "))
    ieyc = int(input("Input ending year covered: "))
    for x in range (isyc,ieyc+1,1):
        years.append(x)
        print("Sales for", x)
        q1 = int(input(" Quarter  1 Sales: "))
        q2 = int(input(" Quarter  2 Sales: "))
        q3 = int(input(" Quarter  3 Sales: "))
        q4 = int(input(" Quarter  4 Sales: "))
        qtr = (q1, q2, q3, q4)
        add_ttl_sls = sum(qtr)
        all_qtr_list.append(qtr)
        annual_sales_list.append(add_ttl_sls)
        print ("Total sales for ", x, ": P {:,.2f}\n".format(add_ttl_sls))

    highest_annual_sales = max(annual_sales_list)
    position = annual_sales_list.index(highest_annual_sales)
    year_w_high_sales = all_qtr_list[position]
    max_qtr = max(year_w_high_sales)
    min_qtr = min(year_w_high_sales)

    print("Total Sales: P {:,.2f}\n".format(sum(annual_sales_list)))
    print("Year with Highest Annual Sales : ", years[position], "\n")
    print ("Quarter with Highest Sales: Quarter", year_w_high_sales.index(max_qtr)+1, "\n")
    print ("Quarter with Lowest Sales: Quarter", year_w_high_sales.index(min_qtr)+1, "\n")

def finals_c4():
    separator()
    print("Tuple")
    tuple = ("l", "h", "a", "me", "s", "i", "w", "r", "l", "j")
    str = " ".join(tuple)
    print (str)

    def slicing(a):
        print("Slicing in tuples:")
        start_value = int(input("   Enter starting value: "))
        end_value = int(input("   Enter ending value: "))
        elements = " ".join(a[start_value:end_value])
        print ("   Elements:", elements)

    def length(b):
        print("Display the length of a tuple")
        print("   Length:", len(b))

    def display_element(c):
        print("Display element")
        num = int(input("   Enter negative number: "))
        print ("   Element:", c[num])

    def count_tuple(d):
        print("Count in tuple")
        element = input("   Enter an element: ")
        print("   Count:", d.count(element))

    def display_index(e):
        print("Display Index")
        element = input("   Enter element: ")
        print("   Index is:", e.index(element))

    def find_element(f):
        print("Element in tuple")
        value = input("   Input value: ")
        if value in f:
            print("   Output: True")
        else:
            print("   Output: False")

    def maximum(g):
        print("Maximum")
        print("   Output:", max(g))

    def minimum(h):
        print("Minimum")
        print("   Output:", min(h))

    #Main
    slicing(tuple)
    length(tuple)
    display_element(tuple)
    count_tuple(tuple)
    display_index(tuple)
    find_element(tuple)
    maximum(tuple)
    minimum(tuple)

def finals_c5():
    separator()
    print("File Handling")
    def menu():
        print("Menu\n")
        print("[A]\t Append data on the file")
        print("[R]\t Read data on the file")
        print("[W]\t Write data on the file")
        print("[E]\t Exit")

    def line():
        print("\n" + "*"*50 + "\n")

    def write_file():
        enter_name = str(input("Enter name in file: "))
        file = open (r'D:\docx\COLLEGE\1stYR_2ndSEM\6COMPRO2L\20696332', 'w')
        file.write(enter_name + "\n")
        file.close()

    def read_file():
        print("The file contains the following: ")
        file = open (r'D:\docx\COLLEGE\1stYR_2ndSEM\6COMPRO2L\20696332', 'r')
        f1 = ""
        f2 = file.readline()
        while f2 != "":
            print(f2)
            f1 += f2
            f2 = file.readline()
        file.close()

    def append_file():
        add_name = str(input("Enter additional name in file: "))
        file = open (r'D:\docx\COLLEGE\1stYR_2ndSEM\6COMPRO2L\20696332', 'a')
        file.write(add_name + "\n")
        file.close()

    def try_again():
        x = 1
        while x == 1:
            answer = str(input("Do you want to try again? Answer [y/n]: "))
            if answer == 'y' or answer == 'Y':
                line()
                return 1
                
            elif answer == 'n' or answer == 'N':
                exit()
                return 0

    def exit():
        print("\nEnd of Program\n")

    proceed = 1
    while proceed == 1:
        try:
            menu()
            choice = input("Enter choice: ")

            if choice == 'A' or 'a':
                append_file()
                line()
                proceed = try_again() 

            elif choice == 'R' or 'r':
                read_file()
                line()
                proceed = try_again()
                
            elif choice == 'W' or 'w':
                write_file()
                line()
                proceed = try_again() 
                
            elif choice == 'E' or 'e':
                exit()
                break

            else:
                print("Invalid Input")
                line()
                proceed = try_again()

        except ValueError:
            print("\nInvalid input")
            line()
            proceed = try_again()

def finals_c6():
    separator()
    print("Dictionary")

    dc1 = {"Tplex", "Slex", "Cavitex", "Mcx", "Star Tollway"}
    dc2 = {"Pangasinan", "Subic", "Bacoor, Cavite", "Muntinlupa", "Laguna"}

    lol =[]
    lol2 = []

    for x in dc1:
        lol.append(x)

    for x in dc2: 
        lol2.append(x)

    num = 0
    for x in range(5):
        print("The", lol[num], "runs through", lol2[num])
        num += 1
        
    print("\nThe following Expressway are included in this data set: ")
    for x in dc1:
        print("-", x)
    print("\nThe following Provinces are included in this data set: ")
    for x in dc2:
        print("-", x)
        
def separator():
    print("\n" + "*"*50 + "\n")

def exit():
    print("\nEnd of Program\n")

def try_again():
    x = 1
    while x == 1:
        answer = str(input("Go back to Main Menu? Answer [y/n]: "))
        if answer == 'y' or answer == 'Y':
            separator()
            return 1
            
        elif answer == 'n' or answer == 'N':
            exit()
            return 0

proceed = 1
while proceed == 1:
    try:
        menu()
        choice = int(input("Enter choice: "))

        if choice == 1:
            proceed = 1
            prelim()
            prelim_choice()
            separator()
            proceed = try_again() 

        elif choice == 2:
            proceed = 1
            midterm()
            midterm_choice()
            separator()
            proceed = try_again()
            
        elif choice == 3:
            proceed = 1
            finals()
            finals_choice()
            separator()
            proceed = try_again() 
            
        elif choice == 4:
            print("\nExiting Main Menu...")
            exit()
            break

        else:
            print("\nInvalid Input")
            separator()
            proceed = try_again()

    except ValueError:
        print("\nInvalid input")
        separator()
        proceed = try_again()
