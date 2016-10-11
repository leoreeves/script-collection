from decimal import Decimal

amount = Decimal(input("Amount(£): "))
VAT = Decimal(0.2) # VAT = 20%
add_total = amount + (amount * VAT)
minus_total = amount / Decimal(1.2)
calc = input("Exclude or Add VAT? [e/a] ").lower()

if calc == 'e':
    print('Net Amount (inc. VAT): £' + str(round(amount,2)))
    print('VAT (at 20%): ' + '£' + str(round(amount - minus_total, 2)))
    print('Gross Amount (exc.VAT): £' + str(round(minus_total,2)))

if calc == 'a':
    print('Net Amount (exc. VAT): £' + str(round(amount,2)))
    print('VAT (at 20%): ' + '£' + str(round(amount * VAT,2)))
    print('Gross Amount (incl.VAT): £' + str(round(add_total,2)))
