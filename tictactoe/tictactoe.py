position = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

ending_num = 0

def game_matrix():
    print('--------')
    print(f'|{position[0][0]}{position[0][1]}{position[0][2]}|')
    print(f'|{position[1][0]}{position[1][1]}{position[1][2]}|')
    print(f'|{position[2][0]}{position[2][1]}{position[2][2]}|')
    print('--------')


def winner_analiser():

    coord_of_winner = ((position[0][0], position[0][1], position[0][2]),
                       (position[1][0], position[1][1], position[1][2]),
                       (position[2][0], position[2][1], position[2][2]),
                       (position[0][0], position[1][0], position[2][0]),
                       (position[0][1], position[1][1], position[2][1]),
                       (position[0][2], position[1][2], position[2][2]),
                       (position[0][0], position[1][1], position[2][2]),
                       (position[0][2], position[1][1], position[2][0]))

    for b in coord_of_winner:
        if b[0] == b[1] == b[2] != ' ':
            return print(f'{b[0]} is winner!')
        else:
            pass


def tictactoe():
    game_matrix()
    moves_counter = 0
    while ending_num != 1:
        user_input = input('enter coordinates')
        answer_list = []

        if user_input[0] not in ['1', '2', '3'] or user_input[1] not in ['1', '2', '3']:
            print('You should enter two numbers from 1 to 3!')
        else:
            for i in user_input:
                answer_list.append(int(i) - 1)
            if position[answer_list[0]][answer_list[1]] != " ":
                print('this position is already occupied!')
            else:

                if moves_counter % 2 == 1:
                    position[answer_list[0]][answer_list[1]] = 'x'
                elif moves_counter % 2 == 0:
                    position[answer_list[0]][answer_list[1]] = '0'
                moves_counter += 1
                game_matrix()
                winner_analiser()


tictactoe()






