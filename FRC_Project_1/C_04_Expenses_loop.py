def not_blank(question):
    """Check that a user response is not blanks"""
    while True:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry, this can't be blank")


def num_check(question, num_type="float"):
    """Check that response is afloat / integer more than zero"""

    if num_type != "float":
        error = "Please enter an integer more than 0."
    else:
        error = "Please enter an integer more than 0."

    while True:
        try:

            if num_type == "float":
                response = float(input(question))
            else:
                response = int(input(question))

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def get_expenses(exp_type):
    """Gets variable / fixed expenses and outputs
    panda (as a string) and a subtotal of the expenses"""

    # list for panda
    all_items = []

    # Expenses dictionary

    # loop to get expenses
    while True:
        item_name = not_blank("Item Name: ")

        # check users enter at least one variable expense
        if (exp_type == "variable" and item_name == "xxx") and len(all_items) == 0:
            print("Oops - you have not entered anything. "
                  "You need at least one item.")
            continue

        elif item_name == "xxx":
            break

        all_items.append(item_name)

    # return all items for now so we can check loop.
    return all_items


# Main routine starts here

# get product information (name and amount being made)
product_name = not_blank("Product Name: ")
quantity_made = num_check("Quantity being made: ", "integer")
print(f"You are making {quantity_made} {product_name}")
print()

# Get variable costs using expenses function
print("Getting Variable Cost...")
variable_expenses = get_expenses("variable")
num_variable = len(variable_expenses)
print(f"You entered {num_variable} items")
print()

# Get fixed costs using expenses function
print("Getting Fixed Costs...")
fixed_expenses = get_expenses("fixed")
num_fixed = len(fixed_expenses)
print(f"You entered {num_fixed} items")
