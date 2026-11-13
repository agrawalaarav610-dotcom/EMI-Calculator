#Project Number-70 | Bank Loan Calculator 
#Calculates monthly EMI,Total Payable Amount Total Interest and checks loan eligibility (EMI must be <= 40% of monthly income.
#Concepts used: Functions, Arithmetic operators, Conditions (if / elif / else)


ELIGIBILITY_PERCENT = 40          # EMI can be at most 40% of monthly income


#EMI Calculation [ EMI = P x r x (1+r)^n / ((1+r)^n - 1) where r = annual_rate/12/100 ]
def calculate_emi(principal, annual_rate, months):
    if annual_rate == 0: # Zero interest case
        emi = principal / months
    else:
        r = annual_rate / 12 / 100                     # monthly interest rate
        power = (1 + r) ** months                      # (1 + r)^n  -> exponent operator
        emi = principal * r * power / (power - 1)
    return round(emi, 2)                               # EMI rounded to 2 decimals first



#Total Payable Amount
def calculate_total_payable(emi, months):
    return round(emi * months, 2)

#Total Interest
def calculate_total_interest(total_payable, principal):
    """Total Interest = Total Payable - Principal"""
    return round(total_payable - principal, 2)

#Eligibilty Check
def calculate_max_emi(monthly_income):
    """Maximum EMI allowed = 40% of monthly income"""
    return round(monthly_income * ELIGIBILITY_PERCENT / 100, 2)


def is_eligible(emi, monthly_income):
    """Eligible only if EMI <= 40% of monthly income"""
    if emi <= calculate_max_emi(monthly_income):
        return True
    else:
        return False

#Input Validation - Returns error if something is wrong
def validate_input(principal, annual_rate, months, monthly_income):
    if principal <= 0:
        return "Invalid loan amount. Enter a positive amount."
    elif annual_rate < 0 or annual_rate > 30:
        return "Invalid interest rate. Enter a rate between 0 and 30."
    elif months < 1 or months > 360:
        return "Invalid tenure. Enter months between 1 and 360."
    elif monthly_income <= 0:
        return "Invalid monthly income. Enter a positive amount."
    else:
        return ""

#Show result in the exact format of the test cases
def display_result(emi, total_payable, total_interest, monthly_income):
    if is_eligible(emi, monthly_income):
        print(f"EMI: Rs. {emi:.2f} | Total Payable: Rs. {total_payable:.2f} "
              f"| Total Interest: Rs. {total_interest:.2f} | Eligible: Yes")
    else:
        max_emi = calculate_max_emi(monthly_income)
        print(f"EMI: Rs. {emi:.2f}")
        print(f"Maximum allowed EMI ({ELIGIBILITY_PERCENT}% of income): Rs. {max_emi:.2f}")
        print("Loan not eligible: EMI exceeds the allowed limit.")

#Main function: takes input, calls the other functions
def main():
    print("WELCOME TO AARAV'S BANK LOAN CALCULATOR")
    principal = float(input("Principal: "))
    annual_rate = float(input("Annual rate: "))
    months = int(input("Tenure (months): "))
    monthly_income = float(input("Monthly income: "))

    error = validate_input(principal, annual_rate, months, monthly_income)
    if error != "":
        print(error)
    else:
        emi = calculate_emi(principal, annual_rate, months)
        total_payable = calculate_total_payable(emi, months)
        total_interest = calculate_total_interest(total_payable, principal)
        display_result(emi, total_payable, total_interest, monthly_income)


main()