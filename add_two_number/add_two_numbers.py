def add_two_numbers(num1, num2):
    """
    This function adds two numbers together.

    Args:
        num1 (int): The first number to add.
        num2 (int): The second number to add.

    Returns:
        int: The sum of the two numbers.
    """
    if num1 is None or num2 is None:
        raise ValueError("Please enter two valid integers.")
    return num1+num2

if __name__ == "__main__":

    while True:
        try:
            nums = input("input num1, num2\n")
            n1, n2 = nums.split(',')
            n1 = int(n1)
            n2 = int(n2)
            break
        except ValueError:
            print("Please enter two valid integers separated by a comma.")

    print(add_two_numbers(n1, n2))