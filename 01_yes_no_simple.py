def yes_no(question):
    """Check that users enter yes / y or no / n to a question"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n) . \n")


# Main routine goes here

# Loop for testing purposes...
while True:
    want_instructions = yes_no("Do you want to read the instructions? ")
    print(f"You choose {want_instructions}\n")
