def main():
    lines = get_lines()
    print(len(lines))
    print(lines)
    lines = convert_words_to_numbers(lines)
    print(lines)
    lines = remove_non_numeric_characters(lines)
    lines = add_first_and_last_digit(lines)
    sum_lines = sum_int_values_of_lines(lines)
    print(lines)
    print(sum_lines)
    print(len(lines))


def convert_words_to_numbers(lines):
    new_lines = []
    for line in lines:
        newline = "                                                                               "
        new_line_list = list(newline)
        position = line.find('one')
        if position != -1:
            new_line_list[position] = '1'

        position = line.find('two')
        if position != -1:
            new_line_list[position] = '2'

        position = line.find('three')
        if position != -1:
            new_line_list[position] = '3'

        position = line.find('four')
        if position != -1:
            new_line_list[position] = '4'

        position = line.find('five')
        if position != -1:
            new_line_list[position] = '5'

        position = line.find('six')
        if position != -1:
            new_line_list[position] = '6'

        position = line.find('seven')
        if position != -1:
            new_line_list[position] = '7'

        position = line.find('eight')
        if position != -1:
            new_line_list[position] = '8'

        position = line.find('nine')
        if position != -1:
            new_line_list[position] = '9'

        position = line.find('1')
        if position != -1:
            new_line_list[position] = '1'

        position = line.find('2')
        if position != -1:
            new_line_list[position] = '2'

        position = line.find('3')
        if position != -1:
            new_line_list[position] = '3'

        position = line.find('4')
        if position != -1:
            new_line_list[position] = '4'

        position = line.find('5')
        if position != -1:
            new_line_list[position] = '5'

        position = line.find('6')
        if position != -1:
            new_line_list[position] = '6'

        position = line.find('7')
        if position != -1:
            new_line_list[position] = '7'

        position = line.find('8')
        if position != -1:
            new_line_list[position] = '8'

        position = line.find('9')
        if position != -1:
            new_line_list[position] = '9'

        newline = ''.join(new_line_list)
        newline = newline.strip()
        newline = newline.replace(' ', '')

        new_lines.append(newline)

    return new_lines


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
