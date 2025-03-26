
def make_statement(decoration, text, lines=1):
    """Create headings (3 lines), subheadings (2 lines) and emphasised
    text / mini-headings (1 line). Only use emoji for single line statements"""

    middle = f"{decoration * 3} {text} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)

    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)


make_statement("Fundraising for charity", 'decoration "=", lines: 3')
print()
make_statement("Start fundraising", 'decoration"*", lines: 2')
print()
make_statement("Emoji in action", 'decoration "💵", lines: 1')
