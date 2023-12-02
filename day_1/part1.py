def main():
    lines = get_lines()
    lines = remove_non_numeric_characters(lines)
    lines = add_first_and_last_digit(lines)
    sum_lines = sum_int_values_of_lines(lines)
    print(lines)
    print(sum_lines)


def get_lines():
    lines = []
    with open('input.txt') as file:
        for line in file:
            lines.append(line.strip())

    return lines


def remove_non_numeric_characters(lines):
    new_lines = []  # Create a new list to store modified lines
    for line in lines:
        new_line = ''.join(character for character in line if character.isdigit())
        new_lines.append(new_line)  # Append the modified line to the new list

    return new_lines  # Return the new list with modified lines


def add_first_and_last_digit(lines):
    new_lines = []

    for line in lines:
        new_line = line
        #if len(line) != 1:
        new_line = line[0] + line[-1]

        new_lines.append(new_line)

    return new_lines


def sum_int_values_of_lines(lines):
    sum_lines = 0
    for line in lines:
        sum_lines += int(line)

    return sum_lines


main()
