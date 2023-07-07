# карта
mapa = [1,2,3,
        4,5,6,
        7,8,9]
# комбинации для выйгрыша
vin_comb = [[0, 1, 2],[3, 4, 5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def print_mapa():
        print(mapa[0], end= " ")
        print(mapa[1], end= " ")
        print(mapa[2])
        print(mapa[3], end=" ")
        print(mapa[4], end=" ")
        print(mapa[5])
        print(mapa[6], end= " ")
        print(mapa[7], end= " ")
        print(mapa[8])

# шаг на карте
def step_mapa(step, symbol):
        mapa[step-1] = symbol

# функция сверки победителя
def get_win():
        win = ''

        for i in vin_comb:
                if mapa[i[0]] == "X" and mapa[i[1]] == "X" and mapa[i[2]] == "X":
                        win = "X"
                if mapa[i[0]] == "O" and mapa[i[1]] == "O" and mapa[i[2]] == "O":
                        win = "O"


        return win


# Программа
game_over = False
game = True
count = 0    # счетчик для ничьей
while game_over == False:
        print_mapa()
        count += 1
        if count > 9:
                print("Ничья!")
                break
        elif game == True:
                step = int(input('Ходит первый игрок'))
                symbol = 'X'
        else:
                step = int(input('Ходит второй игрок'))
                symbol = 'O'
        step_mapa(step, symbol)
        win = get_win()
        if win != "":
                game_over = True
                print(f"Победитель: {win}")
        else:
                game_over = False
        game = not game