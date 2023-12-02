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

        if red_count > red_limit or green_count > green_limit or blue_count > blue_limit:
            return False

    return True


def process_game_data(file_path, red_limit, green_limit, blue_limit):
    with open(file_path, 'r') as file:
        game_data = file.readlines()

    possible_games = []
    for record in game_data:
        game_id, game_record = record.split(': ')
        game_id = int(game_id.split()[1])
        if is_game_possible(game_record, red_limit, green_limit, blue_limit):
            possible_games.append(game_id)

    return sum(possible_games), possible_games


file_path = 'input.txt'
red_limit, green_limit, blue_limit = 12, 13, 14

sum_possible_games, possible_games = process_game_data(file_path, red_limit, green_limit, blue_limit)
print(f'Possible games: {possible_games}')
print(f'Sum of possible games: {sum_possible_games}')

