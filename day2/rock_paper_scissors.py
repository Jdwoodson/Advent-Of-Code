"""
Module for finding score for strategy provided

Points:
1 - Rock        - A, X
2 - Paper       - B, Y
3 - Scissors    - C, Z

6 - Win
3 - Draw
0 - Loss


"""

scores = []

with open('day2/strategy_input.txt', 'r', encoding="utf8") as file:
    data = file.read()

# print(data)

def parse_strategy(strategy):
    games_list_split = strategy.split('\n')
    games_list = [games.split(' ') for games in games_list_split]
    return games_list

def rock_paper_scissors(game):
    my_score = 0
    opponent_move = game[0]
    my_move = game[1]

    rock = ['A', 'X']
    paper = ['B', 'Y']
    scissors = ['C', 'Z']

    if opponent_move in rock:
        opponent_move = 'Rock'
    if opponent_move in paper:
        opponent_move = 'Paper'
    if opponent_move in scissors:
        opponent_move = 'Scissors'
    if my_move in rock:
        my_move = 'Rock'
        my_score += 1
    if my_move in paper:
        my_move = 'Paper'
        my_score += 2
    if my_move in scissors:
        my_move = 'Scissors'
        my_score += 3
    
    print(f'{opponent_move} vs {my_move}')
        
    if my_move == opponent_move:
        print('DRAW')
        my_score += 3
    elif my_move == 'Rock' and opponent_move == 'Scissors':
        print('WIN')
        my_score += 6
    elif my_move == 'Paper' and opponent_move == 'Rock':
        print('WIN')
        my_score += 6
    elif my_move == 'Scissors' and opponent_move == 'Paper':
        print('WIN')
        my_score += 6
    else:
        print('LOSE')

    print(f'My score would be {my_score}')
    return my_score
    
for game in parse_strategy(data):
    scores.append(rock_paper_scissors(game))
    
total = sum(scores)

print(total)
    