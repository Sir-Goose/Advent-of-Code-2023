def is_game_possible(game_record, red_limit, green_limit, blue_limit):
    combinations = game_record.split('; ')

    for combo in combinations:
        red_count, green_count, blue_count = 0, 0, 0
        for color_count in combo.split(', '):
            count, color = color_count.split()
            count = int(count)
            if color == 'red':
                red_count += count
            elif color == 'green':
                green_count += count
            elif color == 'blue':
                blue_count += count
    print(red_count, green_count, blue_count)
    return red_count, green_count, blue_count


def process_game_data(file_path, red_limit, green_limit, blue_limit):
    with open(file_path, 'r') as file:
        game_data = file.readlines()

    powers = []

    for record in game_data:
        game_id, game_record = record.split(': ')
        game_id = int(game_id.split()[1])

        red_limit, green_limit, blue_limit = is_game_possible(game_record, red_limit, green_limit, blue_limit)
        powers.append(red_limit * green_limit * blue_limit)


    return powers


file_path = 'input.txt'
red_limit, green_limit, blue_limit = 12, 13, 14

powers = process_game_data(file_path, red_limit, green_limit, blue_limit)
print(sum(powers))


