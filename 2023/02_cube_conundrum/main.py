import re
import math

QUESTION_1_BALLS = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def part_1():
    games = import_data('2023/02_cube_conundrum/input.txt')

    sum_of_games = 0

    for game in games:
        possible = True
        game_nr = int(re.search(r'\d+', game).group())

        reveals = game.split(':')[1].split(';')

        for reveal in reveals:
            balls = reveal.split(',')
            for ball in balls:
                ball = ball.strip()

                nr_of_balls = int(re.search(r'\d+', ball).group())
                color = ball.replace(str(nr_of_balls), '').strip()

                if nr_of_balls > QUESTION_1_BALLS.get(color):
                    possible = False

        if possible:
            sum_of_games += int(game_nr)

    return sum_of_games

def part_2():
    games = import_data('2023/02_cube_conundrum/input.txt')

    all_power_of_min_balls = []

    for game in games:
        min_number_of_balls = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }

        reveals = game.split(':')[1].split(';')

        for reveal in reveals:
            balls = reveal.split(',')
            for ball in balls:
                ball = ball.strip()

                nr_of_balls = int(re.search(r'\d+', ball).group())
                color = ball.replace(str(nr_of_balls), '').strip()

                if nr_of_balls > min_number_of_balls.get(color):
                    min_number_of_balls[color] = nr_of_balls

        power_of_min_balls = math.prod(min_number_of_balls.values())
        all_power_of_min_balls.append(power_of_min_balls)


    return sum(all_power_of_min_balls)

def import_data(path):
    with open(path) as f:
        games = f.read().splitlines()


    return games

if __name__ == "__main__":
    answer = part_1()
    print(f'Answer 1: {answer}')

    answer = part_2()
    print(f'Answer 2: {answer}')