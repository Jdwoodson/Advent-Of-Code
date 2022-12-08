"""
Results:

Points:
1 - Rock        - A
2 - Paper       - B
3 - Scissors    - C

6 - Win     - Z
3 - Draw    - Y
0 - Loss    - X
"""

scores = []

with open('day2/strategy_input.txt', 'r', encoding="utf8") as file:
    data = file.read()

# print(data)

def parse_strategy(strategy):
    games_list_split = strategy.split('\n')
    games_list = [games.split(' ') for games in games_list_split]
    return games_list

def rock_paper_scissors(moves):
    '''
    Please forgive me for lord I have commited some if/else spaghetti
    '''
    my_score = 0
    opponent_move = moves[0]
    result = moves[1]

    choices = {
        'A':'Rock',
        'B':'Paper',
        'C':'Scissors',
        'X':'Lose',
        'Y':'Draw',
        'Z':'Win'
    }

    shape_score = {
        'Rock':1,
        'Paper':2,
        'Scissors':3
    }

    round_score = {
        'Lose':0,
        'Draw':3,
        'Win':6
    }

    opponent_move = choices[opponent_move]
    result = choices[result]

    # print(f'''Opponent:{opponent_move}\nI will need to: {result}''')

    if result == 'Draw':
        my_move = opponent_move
        my_score += shape_score[my_move] + round_score[result]

    elif result == 'Win' and opponent_move == 'Scissors':
        my_move = 'Rock'
        my_score += shape_score[my_move] + round_score[result]

    elif result == 'Win' and opponent_move == 'Rock':
        my_move = 'Paper'
        my_score += shape_score[my_move] + round_score[result]

    elif result == 'Win' and opponent_move == 'Paper':
        my_move = 'Scissors'
        my_score += shape_score[my_move] + round_score[result]
        
    elif result == 'Lose':
        if opponent_move == 'Paper':
            my_move = 'Rock'
        elif opponent_move == 'Rock':
            my_move = 'Scissors'
        elif opponent_move == 'Scissors':
            my_move = 'Paper'
        my_score += shape_score[my_move] + round_score[result]

    # print(f'My score would be {my_score}')
    return my_score

for game in parse_strategy(data):
    scores.append(rock_paper_scissors(game))

total = sum(scores)

print(total)
    