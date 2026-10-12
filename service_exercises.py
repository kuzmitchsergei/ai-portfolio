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


# Exercise 3: Price change check
# Write a function pct_change(old, new) that returns the price
# change in percent: (new - old) / old * 100
# Test it on three quote lines:
#   1000 -> 1050,  200 -> 204,  500 -> 480
# Print each result rounded to 1 decimal, and print 'FLAG'
# next to any increase above 3%.
# Expected: 5.0 FLAG, 2.0, -4.0


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


# Exercise 5: Service budget
# A service budget is CHF 50,000.
# Month 1 costs CHF 4,000. Each following month costs 1% more
# than the month before.
# Use a while loop to count how many FULL months the