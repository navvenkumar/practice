# calculator program
def inputs():
    args = {}
    nums = []
    num1 = input("enter a number")
    status_1 = num1.isdecimal()
    while not status_1:
        print("invalid number !!!")
        num1 = (input("enter valid number"))
        status_1 = num1.isdecimal()
    num1 = int(num1)
    nums.append(num1)
    num2 = input("enter a number")
    status_1 = num2.isdecimal()
    while not status_1:
        print("invalid number !!!")
        num2 = (input("enter valid number"))
        status_1 = num2.isdecimal()
    num2 = int(num2)
    nums.append(num2)
    print("select 1.addition 2.subtraction 3.multiplication 4.division")
    ope = input("enter a number")
    status_1 = ope.isdecimal()
    while not status_1:
        print("invalid number !!!")
        ope = (input("enter valid number"))
        status_1 = ope.isdecimal()
    opera = int(ope)
    args['nums'] = nums
    args['op'] = opera
    return args


def calculator():
    args = inputs()
    if args['op'] == 1:
        result1 = lambda args1: args1['nums'][0] + args1['nums'][1]
        result = result1(args)
    elif args['op'] == 2:
        result1 = lambda args2: args2['nums'][0] - args2['nums'][1]
        result = result1(args)
    elif args['op'] == 3:
        result1 = lambda args3: args3['nums'][0] * args3['nums'][1]
        result = result1(args)
    elif args['op'] == 4:
        result1 = lambda args4: args4['nums'][0] / args4['nums'][1]
        result = result1(args)
    else:
        result = 'invalid Opeartion'
    return True, result


status1, res = calculator()
print(res)
