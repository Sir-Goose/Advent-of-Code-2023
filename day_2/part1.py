class Game:
    def __init__(self, line):
        # Initialize the color lists
        self.red_list = []
        self.green_list = []
        self.blue_list = []

        # Remove the initial part (e.g., "Game 1:") and then split the line
        parts = line.split(':')[1].strip().split(';')
        for part in parts:
            color_values = part.split(',')
            for color_value in color_values:
                color_value = color_value.strip()
                if color_value:
                    # Split and check if the result has exactly two elements
                    split_values = color_value.split()
                    if len(split_values) == 2:
                        value, color = split_values
                        value = int(value)
                        if 'red' in color:
                            self.add_red(value)
                        elif 'green' in color:
                            self.add_green(value)
                        elif 'blue' in color:
                            self.add_blue(value)
                    else:
                        print(f"Invalid format in color-value pair: '{color_value}'")
                        self.add_blue(value)

    red_list = []
    green_list = []
    blue_list = []

    def add_green(self, value):
        self.green_list.append(value)

    def add_red(self, value):
        self.red_list.append(value)

    def add_blue(self, value):
        self.blue_list.append(value)

    def get_biggest_red(self):
        return max(self.red_list)

    def get_biggest_green(self):
        return max(self.green_list)

    def get_biggest_blue(self):
        return max(self.blue_list)


def main():
    games = []
    with open('input.txt', 'r') as file:
        for line in file:
            game = Game(line)
            print(game.get_biggest_red())
            print(game.get_biggest_green())
            print(game.get_biggest_blue())
            games.append(game)

    valid_games_IDs = []
    i = 1
    while i < len(games):
        if games[i].get_biggest_red() <= 12:
            if games[i].get_biggest_green() <= 13:
                if games[i].get_biggest_blue() <= 14:


                    valid_games_IDs.append(i)
        i += 1
    print(valid_games_IDs)

    sum_of_valid_games = sum(valid_games_IDs)
    print(sum_of_valid_games)




if __name__ == '__main__':
    main()
