# Exercise 1: SLA status
# Write a function sla_status(hours) that returns:
#   'Within SLA' if the ticket is open 24 hours or less
#   'Reminder'   if it is open more than 24 and up to 48 hours
#   'Escalate'   if it is open more than 48 hours
# Then loop over the list [5, 30, 52, 24, 49] and print each
# number of hours with its status.
# Expected: 5 Within SLA, 30 Reminder, 52 Escalate,
#           24 Within SLA, 49 Escalate


def sla_status(hours):
    if hours > 48:
        return 'Escalate'
    elif hours > 24:
        return 'Reminder'
    else:
        return 'Within SLA'
    
for h in [5, 30, 52, 24, 49]:
    print(h, sla_status(h))


# Exercise 2: Spare-parts quote total
# A quote has two lines:
#   5 parts at CHF 1,000 each
#   12 parts at CHF 500 each
# If the subtotal is above CHF 10,000, apply a 5% discount.
# Then add Swiss VAT of 8.1% on the discounted amount.
# Print the subtotal, discount, net amount, VAT and total,
# rounded to 2 decimals.
# Expected: 11000, 550.0, 10450.0, 846.45, 11296.45


price1 = 1000
price2 = 500
line1 = 5 * price1
line2 = 12 * price2
subtotal = line1 + line2
if subtotal > 10000:
    discount = subtotal * 0.05
else:
    discount = 0

net_amount = subtotal - discount
vat = net_amount * 0.081
total_incl_vat = net_amount + vat
print(subtotal, discount, net_amount, round(vat, 2), round(total_incl_vat, 2))



# Exercise 3: Price change check
# Write a function pct_change(old, new) that returns the price
# change in percent: (new - old) / old * 100
# Test it on three quote lines:
#   1000 -> 1050,  200 -> 204,  500 -> 480
# Print each result rounded to 1 decimal, and print 'FLAG'
# next to any increase above 3%.
# Expected: 5.0 FLAG, 2.0, -4.0


def pct_change(old, new):
    return  (new - old) / old *100

for old, new in [(1000, 1050), (200, 204), (500, 480)]:
    change = pct_change(old, new)
    if change > 3:
        print(round(change, 1), 'FLAG')
    else:
        print(round(change, 1))

# Exercise 4: Tender go/no-go
# Ask the user for:
#   - the contract value in CHF
#   - the number of days left until the deadline
#   - whether all mandatory requirements are met (y/n)
# Print 'GO' only if the value is at least CHF 150,000,
# at least 10 days are left, AND the answer is 'y'.
# Otherwise print 'NO-GO' and the reason.
# If the user types text instead of a number (e.g. 'abc'),
# print an error message instead of crashing.
# Test at least 4 cases: one GO, and one for each reason
# to say no.


while True:
    line = input('Contract value in CHF ')
    try:
        contract_value_chf = float(line)
        break
    except ValueError:
        print('Error, Type a contract value in CHF')

while True:
    line = input('The number of days left until deadline ')
    try:
        number_of_days_deadline = int(line)
        break
    except ValueError:
        print('Error, type number of days')

while True:
    requirements = input('All mandatory requirements are met (y/n) ') .strip().lower()
    if requirements == 'y' or requirements == 'n':
        break
    print('Error, type y or n')

if contract_value_chf < 150000:
    print('NO-GO: contract value is less than 150000CHF')
elif number_of_days_deadline < 10:
    print('NO_GO: deadline less than 10 days')
elif requirements == 'n':
    print('NO-G0: requirements are not met')
else: 
    print('GO')




# Exercise 5: Service budget
# A service budget is CHF 50,000.
# Month 1 costs CHF 4,000. Each following month costs 1% more
# than the month before.
# Use a while loop to count how many FULL months the budget
# covers. Check before each month that enough money is left;
# never go over the budget.
# Print in the loop the number of months, the total spent and what is left,
# rounded to 2 decimals.
# Expected: 11 months, 46267.34 spent, 3732.66 left

budget = 50000
monthly_cost = 4000
months = 0
spent = 0

while spent + monthly_cost <= budget:
    spent = spent + monthly_cost
    months = months + 1
    monthly_cost = monthly_cost * 1.01

    print(months, round(spent, 2), round (budget-spent, 2))