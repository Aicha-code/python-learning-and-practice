def main():
    print("Welcome to the Arithmetic Formatter!\n")
    print("You can enter up to five arithmetic problems involving addition or subtraction.")
    print("Each problem should be in the format: 'operand1 operator operand2' (e.g., '32 + 698').")
    operation= input("Enter the arithmetic problems separated by commas as in the example above: ")
    problems = [problem.strip() for problem in operation.split(",")]
    show_answers = input("Do you want to display the answers? (yes/no): ").strip().lower() == 'yes'
    arranged_problems = arithmetic_arranger(problems, show_answers)
    print(arranged_problems)

def arithmetic_arranger(problems, show_answers=False):
    try:
        if len(problems) >5:
            return "Error: Too many problems."
        divided_problems=[
            p.split(" ") for p in problems
        ]
        
        first_operands = []
        operators = []
        lines=[]
        answers=[]

        for i in range(len(divided_problems)):
            first_operand = divided_problems[i][0]
            operator = divided_problems[i][1]

            second_operand = divided_problems[i][2]     
            if not first_operand.isdigit() or not second_operand.isdigit():
                return "Error: Numbers must only contain digits."
            if len(first_operand) > 4 or len(second_operand)>4:
                return 'Error: Numbers cannot be more than four digits.'

            if operator not in ['+', '-']:
                return "Error: Operator must be '+' or '-'."
            width = max(len(first_operand), len(second_operand)) + 2
            lines.append("-" * width)
            first_operands.append(first_operand.rjust(width))
            operators.append(operator + second_operand.rjust(width - 1))
            if show_answers:
                if operator == '+':
                    result= str(int(first_operand) + int(second_operand))
                else:
                    result = str(int(first_operand) - int(second_operand))
                answers.append(result.rjust(width))
        arranged_first_line = "    ".join(first_operands)
        arranged_second_line = "    ".join(operators)
        arranged_lines = "    ".join(lines)
        problem=  arranged_first_line + "\n" + arranged_second_line + "\n" + arranged_lines
        if show_answers:
            problem = problem+ "\n" + "    ".join(answers)

        return problem
    except IndexError:
            return "Error: Invalid problem format. Try again!"

if __name__ == "__main__":
    main()

