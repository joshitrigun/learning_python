class InvalidFormulaException(Exception):
    pass


def evaluate(formula):
    f = formula.split()
    if len(f) > 3:
        raise InvalidFormulaException('Formula should not have spaces ex: 10 + 4: ')
    if f[1] == '+' or '/' or '-' or '*':
        op1 = int(f[0])
        op2 = int(f[2])
        if f[1] == '+':
            res = op1 + op2
        elif f[1] == '-':
            res = op2 - op1
        elif f[1] == '*':
            res = op2 * op1
        else:
            res = op1 / op2
        return res
    else:
        return InvalidFormulaException('Formula should be in this form ex: 10 + 5')



try:
    formula = input('Enter the formula ex: 10 + 4 ')
    print(evaluate(formula))
except InvalidFormulaException as e:
    print(e)