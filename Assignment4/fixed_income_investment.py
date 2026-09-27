# Fixed-income investment Revenue program

# Validation Loop
while True:
    monthly_investment = monthly_investment if (monthly_investment := float(input("Enter a monthly Investment amount: "))) > 0 else -1
    if monthly_investment == -1:
        print("Error: Investment must be positive number")
        continue
    break

while True:
    yearly_interest_rate = (yearly_interest_rate / 12) / 100 if (yearly_interest_rate := float(input("Enter a yearly interest rate: "))) > 0 else -1
    if yearly_interest_rate == -1:
        print("Error: Yearly interest rate must be a positive number")
        continue
    break

while True:
    investment_years = investment_years if (investment_years := int(input("Enter how many years to invest: "))) > 0 else -1
    if investment_years == -1:
        print("Error: Investment period must be a positive number of years")
        continue
    break

# Compute Revenue
last_balance = 0

for month in range(1, (investment_years * 12 + 1)):
    # Get revenue
    revenue = (last_balance + monthly_investment) * yearly_interest_rate
    last_balance += revenue + monthly_investment
    print(f"Month {month} revenue: {last_balance} ")

print(f"After {investment_years:,d} years, you will receive a total investment revenue of {last_balance:,.2f} at a yearly rate of {yearly_interest_rate * 1200:.1f}")
