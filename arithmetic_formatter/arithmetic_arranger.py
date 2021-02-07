import re


class ArrayTooLarge(Exception):
    pass


class InvalidOperator(Exception):
    pass


class TermTooLong(Exception):
    pass


class TermIsNan(Exception):
    pass


def buildString(output, input, add_newline=False):
    spacing = " " * 4
    if output:
        output += spacing + input
    else:
        output += "\n" + input if add_newline else input
    return output


def arithmetic_arranger(arr, results=False):

    try:
        if (len(arr) > 5):
            raise ArrayTooLarge()

        first_operands_str = ""
        second_operands_str = ""
        separator_str = ""
        solution_str = ""

        VALID_OPERATORS = ["+", "-"]
        VALID_TERM = re.compile(r'^\d+$')

        # iterate over every item in the list
        for equation in arr:
            # split the item over spaces and dstructure it
            first_term, operator, second_term = equation.split(" ")

            if operator not in VALID_OPERATORS:
                raise InvalidOperator()
            if (len(first_term) > 4 or len(second_term) > 4):
                raise TermTooLong()
            if (not VALID_TERM.match(first_term) or not VALID_TERM.match(second_term)):
                raise TermIsNan()

        #   solve the equations
            if (operator == "+"):
                solution = str(int(first_term) + int(second_term))
            else:
                solution = str(int(first_term) - int(second_term))

        #   check which term is the longest
        #   store the length of the longest term + 2
            total_length = max(len(first_term), len(second_term)) + 2

        #   format the terms correctly
            first_term = first_term.rjust(total_length)
            second_term = operator + second_term.rjust(total_length - 1)
            separator = "-" * total_length
            solution = solution.rjust(total_length)

        #   build the final output strings
            first_operands_str = buildString(first_operands_str, first_term)
            second_operands_str = buildString(
                second_operands_str, second_term, True)
            separator_str = buildString(separator_str, separator, True)
            solution_str = buildString(solution_str, solution, True)

        return f"{first_operands_str}{second_operands_str}{separator_str}{solution_str if results else ''}"

    except ArrayTooLarge:
        return 'Error: Too many problems.'
    except InvalidOperator:
        return "Error: Operator must be '+' or '-'."
    except TermTooLong:
        return "Error: Numbers cannot be more than four digits."
    except TermIsNan:
        return "Error: Numbers must only contain digits."


print(
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43",
                         "123 + 49", "1 - 3001"], True)

)
