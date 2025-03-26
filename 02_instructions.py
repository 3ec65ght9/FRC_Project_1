def make_statement(decoration, text):
    """Create headings (3 lines), subheadings (2 lines) and emphasised
    text / mini-headings (1 line). Only use emoji for single line statements"""

    print(f"{decoration * 1} {text} {decoration * 1}")


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


    def instructions():
        make_statement("Instructions!", "ℹ️")
