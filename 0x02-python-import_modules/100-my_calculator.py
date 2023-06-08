#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys

    def calc():
        if len(sys.argv) != 4:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        else:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            operator = sys.argv[2]
            if operator == "+":
                print("{} {} {} = {}"
                      .format(a, operator, b, calculator_1.add(a, b)))
            elif operator == "-":
                print("{} {} {} = {}"
                      .format(a, operator, b, calculator_1.sub(a, b)))
            elif operator == "/":
                print("{} {} {} = {}"
                      .format(a, operator, b, calculator_1.div(a, b)))
            elif operator == "*":
                print("{} {} {} = {}"
                      .format(a, operator, b, calculator_1.mul(a, b)))
            else:
                print("Unknown operator. Available operators: +, -, * and /")
                sys.exit(1)
    calc()
