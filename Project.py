print("Welcome to the Pattern Generator and Number Analyzer!")

while(True):
    print("\nSelect an option:")
    print("1. Generate Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = int(input("Enter your Choice: "))

    match choice:
        case 1:
            row = int(input("Enter the Number of rows for the Pattern:"))
            print("Pattern:")

            for i in range (1, row+1):
                print("*" *i)

        case 2:
            start = int(input("Enter the start of the range : ")) 
            end = int(input("Enter the end of the range :"))

            sum = 0     
            for i in range(start, end+1 ):
                  if i % 2==0:
                    print(f"namber {i} is even")
                  else:
                    print(f"number {i} is Odd")     
                  sum = sum + i

            print(f"Sum of all numbers from {start} to {end} is: {sum}")
        case 3:
        
            print("Exiting the program.Goodbye!")
            break



        


