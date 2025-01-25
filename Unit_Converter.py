try:
    print("1 - Length \n2 - Temperature \n3 - Weight \n4 - Time")
    choise = int(input("Enter your Choise : "))
    print()

#Code for Length
    if choise == 1:
        
        
        length = float(input("Enter your Length in Meter : "))
        print("1 - Kilometer \n2 - Feet \n3 - Centimeter \n4 - Millimeter \n5 -Yard")
    # taking choise as an input
        print()
        
        length_choise = int(input("Enter Your Choise :"))
        if length_choise == 1:
            print(f"{length / 1000} Kilometer")
        elif length_choise == 2:
             print(f"{length * 3.28084} Feet")
        elif length_choise == 3:
            print(f"{length * 100} Centimeter")
        elif length_choise == 4:
             print(f"{length * 1000} Millimeter")
        elif length_choise == 5:
            print(f"{length * 1.09361} Yard")
        else:
            print("INVALID CHOISE")
    
    #Code for Temperature
    
    elif choise == 2:
        temperature = float(input("Enter your Temperature in Celsius : "))
        print("1 - Celsius \n2 - Fahrenheit \n3 - Kelvin")
    # taking choise as an input
        print()
        temperature_choise = int(input("Enter Your Choise :"))
        if temperature_choise == 1:
            print(f"{temperature} Celsius")
        elif temperature_choise == 2:
            print(f"{temperature * 9/5 + 32} Fahrenheit")
        elif temperature_choise == 3:
            print(f"{temperature + 273.15} Kelvin")
        else:
            print("INVALID CHOISE")
           
    
    #Code for Weight
    
    elif choise == 3:
        weight = float(input("Enter Your Weight in Kilogram"))
        print("1 - Kilogram \n2 - Grams \n3 - Pounds \n4 - Tons")
    #taking choises as an input
        print()
        weight_choise = int(input("Enter Your Choise :"))
        if weight_choise == 1:
            print(f"{weight} Kilogram")
        elif weight_choise == 2:
            print(f"{weight * 1000} Grams")
        elif weight_choise == 3:
            print (f"{weight * 2.205} Pounds")
        elif weight_choise == 4:
            print(f"{weight * 0.00110231} Tons")
        else:
            print("INVALID CHOISE")
        
    #Code for Time
    
    elif choise == 4:
        time = float(input("Enter Your Time in Hour"))
        print("1 - Hours \n2 - Minutes \n3 - Seconds \n4 - Days \n5 - Months \n6 - Years")
    #taking choise as an input
        print()
        time_choise = int(input("Enter Your Choise : "))
        if time_choise == 1:
            print (f"{time} Hours")
        elif time_choise == 2:
            print (f"{time * 60} Minutes")
        elif time_choise == 3:
            print (f"{time * 3600} Seconds")
        else:
            print("INVALID CHOISE")

except:
    print("PLEASE TRY AGAIN")
        