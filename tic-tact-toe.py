from graphics import *

win = GraphWin('tic-tac-toe', 500, 500)


def draw_x_axis():
    for i in range(100, 400, 100):
        line = Line(Point(i, 100), Point(i, 500))
        line.draw(win)


def draw_y_axis():
    for i in range(200, 500, 100):
        line = Line(Point(0, i), Point(400, i))
        line.draw(win)


def draw_numbers():
    x = 90
    y = 190
    cnt = 0
    for i in range(1,10):
        label = Text(Point(x, y), str(i))
        label.draw(win)
        cnt += 1
        x += 100
        if cnt == 3:
            y += 100
            x = 90
            cnt = 0


def create_board():
    draw_x_axis()
    draw_y_axis()
    draw_numbers()
    print "called"


def draw_input(x):
    label = Text(Point(20, 20), x)
    label.draw(win)


def is_valid_move(valid_move_list, t):
    if valid_move_list.get(t, 1) > 0:
       return 0

    return t


def is_winner(player_moves):
    player_moves.sort()

    # horizontal check
    for i in range(1, 8, 3):
        flag = True
        for j in range(0, 3):
            move = i+j
            # print move
            if move not in player_moves:
                flag = False
                break
        # print "-------"

        if flag:
            return True

    # vertical check
    for i in range(1, 4):
        flag = True
        for j in range(0, 7, 3):
            move = i+j
            # print move
            if move not in player_moves:
                flag = False
                break
        # print "---------------"
        if flag:
            return True
            break

    # diagonal check
    d1 = [1,5,9]
    flag = True
    for d in d1:
        if d not in player_moves:
            flag = False
            break
    if flag:
        return True

    d2 = [3,5,7]
    flag = True
    for d in d2:
        if d not in player_moves:
            flag = False
            break
    if flag:
        return True

    return False


def check_game_status(valid_move_list, moves_cnt):
    player_move = {1:[], 2:[]}
    game_status = {}
    for key in valid_move_list.keys():
        pos = key
        player = valid_move_list[key]
        if player:
            x = player_move[player]
            x.append(int(pos))
            player_move[player] = x

    print player_move[1]
    print player_move[2]
    # print "calling for player 1"
    winner_status1 = is_winner(player_move[1])
    # print "calling for player 2"
    winner_status2 = is_winner(player_move[2])

    if winner_status1:
        game_status['status'] = 'winner player 1'
    if winner_status2:
        game_status['status'] = 'winner player 2'

    if moves_cnt == 9:
        game_status['status'] = 'draw!!'

    return game_status


def get_xy(t):
    x = 50 + ((int(t) + 2)%3)*100
    y = 150 + ((int(t) - 1)/3)*100
    return x, y


if __name__ == '__main__':
    player = 1
    valid_move_list={str(x):0 for x in range(1,10)}
    moves_cnt = 0
    print valid_move_list
    player_info = dict()
    player_info[1] = {'icon': 'X', 'icon_col': 'blue'}
    player_info[2] = {'icon': 'O', 'icon_col': 'red'}


    while True:
        create_board()
        t = raw_input('your move player ' + str(player_info[player]['icon']) + ' - ')
        flag = is_valid_move(valid_move_list, t)
        if flag == 0:
            print "not a valid move"
        else:
            valid_move_list[flag] = player
            moves_cnt += 1
            x, y = get_xy(t)
            label = Text(Point(x,y), player_info[player]['icon'])
            label.setSize(30)
            label.setTextColor(player_info[player]['icon_col'])
            label.draw(win)

            if player == 1:
                player = 2
            else:
                player = 1

        print valid_move_list

        game_status = check_game_status(valid_move_list, moves_cnt)
        if game_status.get('status', None):
            print game_status['status']
            break

    win.close()
