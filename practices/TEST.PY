#darin larose p1
def Sigma():

#this is the main function that runs the whole program.
#it shows a menu and lets users choose which calculator to use.
    
   
    print("financial calculator")
    
    
    # keep showing the menu until user wants to quit
    while True:
        print("\nwhat do you want to calculate?")
        print("1. savings time calculator (how long to save for a goal)")
        print("2. compound interest calculator (money grows with interest)")
        print("3. budget allocator (divide income into categories)")
        print("4. sale price calculator (price after discount)")
        print("5. tip calculator (how much tip to leave)")
        print("6. exit program")
        
        choice = input("\nenter your choice (1-6): ")
        
        if choice == "1":
            savings_time_calculator()
        elif choice == "2":
            compound_interest_calculator()
        elif choice == "3":
            budget_allocator()
        elif choice == "4":
            sale_price_calculator()
        elif choice == "5":
            tip_calculator()
        elif choice == "6":
            print("\nthanks for using the financial calculator!")
            print("goodbye!")
            break
        else:
            print("\nplease enter a number from 1 to 6.")

# =========================================
# function 1: savings time calculator
# =========================================
def savings_time_calculator():
    """
    this calculates how long it will take to save for a goal.
    """
    print("\n" + "=" * 50)
    print("savings time calculator")
    print("=" * 50)
    
    # get user input
    goal = float(input("how much money do you want to save? $"))
    
    print("\nhow often will you save money?")
    print("1. every week")
    print("2. every month")
    period_choice = input("enter 1 or 2: ")
    
    deposit = float(input("\nhow much will you save each time? $"))
    
    # calculate time based on weekly or monthly
    if period_choice == "1":
        # weekly savings
        weeks_needed = goal / deposit
        months_needed = weeks_needed / 4.33  # average weeks in a month
        
        # show results
        print(f"\nit will take {weeks_needed:.1f} weeks to save ${goal:.2f}")
        print(f"that's about {months_needed:.1f} months")
        
    elif period_choice == "2":
        # monthly savings
        months_needed = goal / deposit
        years_needed = months_needed / 12
        
        # show results
        print(f"\nit will take {months_needed:.1f} months to save ${goal:.2f}")
        print(f"that's about {years_needed:.1f} years")
    
    else:
        print("please enter 1 or 2 next time.")

# =========================================
# function 2: compound interest calculator
# =========================================
def compound_interest_calculator():
    """
    this calculates how money grows with compound interest.
    """
    print("\n" + "=" * 50)
    print("compound interest calculator")
    print("=" * 50)
    
    # get user input
    start_amount = float(input("starting amount of money: $"))
    rate = float(input("interest rate (percent per year): "))
    years = float(input("number of years to grow: "))
    
    # convert percent to decimal
    rate_decimal = rate / 100
    
    # this is an inner function - it does part of the main calculation
    def calculate_final_amount(start, rate, years):
        """
        inner function: this does the actual compound interest math.
        it calculates a = p(1 + r)^t
        it can use the variables from the parent function.
        """
        # a = p(1 + r)^t formula
        final = start * ((1 + rate) ** years)
        return final
    
    # use the inner function to calculate
    final_amount = calculate_final_amount(start_amount, rate_decimal, years)
    
    # show results
    print(f"\nstarting with: ${start_amount:.2f}")
    print(f"interest rate: {rate}% per year")
    print(f"time: {years} years")
    print(f"final amount: ${final_amount:.2f}")
    
    # show how much was earned in interest
    interest_earned = final_amount - start_amount
    print(f"you earned ${interest_earned:.2f} in interest!")

# ==========================================
# function 3: budget allocator
# =========================================
def budget_allocator():
    
    #this divides income into different spending categories.
    
    print("\n" + "=" * 50)
    print("budget allocator")
    print("=" * 50)
    
    # get number of categories
    num_categories = int(input("how many budget categories do you have? "))
    
    # lists to store category names and percentages
    categories = []
    percentages = []
    
    # get category names
    for i in range(num_categories):
        name = input(f"what is category {i+1} called? ")
        categories.append(name)
    
    # get monthly income
    income = float(input("\nwhat is your monthly income? $"))
    
    # get percentages for each category
    print("\nnow enter what percent of your income goes to each category.")
    total_percent = 0
    
    for i in range(num_categories):
        while True:
            percent = float(input(f"what percent for {categories[i]}? "))
            
            # check if adding this percent would go over 100%
            if total_percent + percent > 100:
                print(f"warning: that would make {total_percent + percent}% total!")
                print(f"you only have {100 - total_percent}% left to use.")
                continue
            else:
                percentages.append(percent)
                total_percent += percent
                break
    
    # show the budget
    print("\n" + "-" * 50)
    print("your budget:")
    print("-" * 50)
    
    for i in range(num_categories):
        amount = income * (percentages[i] / 100)
        print(f"{categories[i]}: {percentages[i]}% = ${amount:.2f}")
    
    print(f"\ntotal: {total_percent}% of ${income:.2f}")

# =========================================
# function 4: sale price calculator
# =========================================
def sale_price_calculator():
    
    #this calculates the price after a discount.
   
    print("\n" + "=" * 50)
    print("sale price calculator")
    print("=" * 50)
    
    # get user input
    original_price = float(input("how much does the item cost originally? $"))
    discount_percent = float(input("what percent is the discount? "))
    
    # calculate discount amount
    discount_amount = original_price * (discount_percent / 100)
    
    # calculate final price
    final_price = original_price - discount_amount
    
    # show results
    print(f"\noriginal price: ${original_price:.2f}")
    print(f"discount: {discount_percent}% (${discount_amount:.2f})")
    print(f"sale price: ${final_price:.2f}")
    
    # if there's tax (extra feature)
    add_tax = input("\ndo you want to add sales tax? (yes/no): ").lower()
    
    if add_tax == "yes" or add_tax == "y":
        tax_rate = float(input("what is the sales tax rate (percent)? "))
        tax_amount = final_price * (tax_rate / 100)
        total_with_tax = final_price + tax_amount
        
        print(f"\nsales tax ({tax_rate}%): ${tax_amount:.2f}")
        print(f"total with tax: ${total_with_tax:.2f}")

# =========================================
# function 5: tip calculator
# =========================================
def tip_calculator():
    
    #this calculates how much tip to leave.
    
    print("\n" + "=" * 50)
    print("tip calculator")
    print("=" * 50)
    
    # get user input
    bill_amount = float(input("how much is the bill? $"))
    tip_percent = float(input("what percent tip do you want to leave? "))
    
    # this is another inner function
    def calculate_tip(bill, percent):
        
        #inner function: calculates the tip amount.
        #this keeps the tip calculation separate and organized.
        
        tip = bill * (percent / 100)
        return tip
    
    # calculate using the inner function
    tip_amount = calculate_tip(bill_amount, tip_percent)
    total_bill = bill_amount + tip_amount
    
    # show results
    print(f"\nbill amount: ${bill_amount:.2f}")
    print(f"tip ({tip_percent}%): ${tip_amount:.2f}")
    print(f"total to pay: ${total_bill:.2f}")
    
    # show how to split the bill (extra feature)
    split = input("\ndo you want to split the bill? (yes/no): ").lower()
    
    if split == "yes" or split == "y":
        people = int(input("how many people? "))
        each_pays = total_bill / people
        print(f"each person pays: ${each_pays:.2f}")


Sigma()
