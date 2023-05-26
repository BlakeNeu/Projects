# Stock percentage gains / losses
import sys, re
# BEGIN - getPercentage
def getPercentage(arg1, arg2, arg3):
    x = float(arg1)
    y = float(arg2)
    pos = ''
    amount = ''
    shares = int(arg3)

    if float(x) < float(y):
        # percent = round((x - y) * 100, 2)
        percent = round(((y - x) / (x)) * 100, 2)
        ans = round(((y - x)) * shares , 2)
        pos = '+'
    else:
        percent = round(((x - y) / (y)) * 100, 2)
        ans = round(((x - y)) * shares , 2)
        pos = '-'

    # profit = round(((y - x) * float(shares) ), 2)
    calc = round(float(arg1) * float(arg3), 2)
    # percent = round((100 - x / y) * 100, 2)

    print('---------------------------------')
    print('total cost: $' + str(f"{calc:.2f}"))
    print('---------------------------------')
    print('percent: ' + pos + str(f"{percent:.2f}") + '%')
    print('profit: '+ pos +'$' + str(f"{ans:.2f}"))
    print('---------------------------------')
# END - getPercentage
# BEGIN - paramCheck
def paramCheck(value):
    if re.search('^\d*\.?\d*$', value) != None:
        return float(value)
    else:
        return 'error: check param value'
# END - variableCheck
# - BEGIN - costSharesAndPrice
def costSharesAndPrice(arg2, arg3):
    try:
        float(arg2)
        float(arg3)
        calc = round(float(arg2) * float(arg3), 2)
        print('total cost: $' + str(f"{calc:.2f}"))
        print('---------------------------------')
    except ValueError:
        print('---------------------------------')
        print('error: price or shares are not a number')

# - END - costSharesAndPrice
# program
opt = list(sys.argv)

if len(opt) == 4 and opt[1] in ("-a", "-ia"):
    print('---------------------------------')
    print('error: missing param')
    print('---------------------------------')
    sys.exit()

if opt[1] in ("-h", "--help"):
    print(' ---------------------------------------------------------------- ')
    print('| help menu                                                      |')
    print('|----------------------------------------------------------------|')
    print('| -a    | amount   |        [ price start, price end, shares ]   |')
    print('| -ia   | amount   | input: price start, price end, shares       |')
    print('| -ic   | cost     | input: price, shares                        |')
    print(' ---------------------------------------------------------------- ')
elif opt[1] == '-a':
    ans = getPercentage(opt[2], opt[3], opt[4])
elif opt[1] == '-ia':
    print('---------------------------------')
    input1 = input('price start: $')
    input2 = input('price end: $')
    input3 = input('shares: ')
    # ans_ = costSharesAndPrice(input1, input3)
    ans = getPercentage(input1, input2, input3)

elif opt[1] == '-ic':
    print('---------------------------------')
    input1 = input('price: $')
    input2 = input('shares: ')
    ans = costSharesAndPrice(input1, input2)
    print('---------------------------------')
elif not ("-h", "-help", "-a", "-ia", "ic"):
    print('---------------------------------')
    print(' no options found                ')
    print('---------------------------------')

sys.exit()
