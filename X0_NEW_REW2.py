print()
print('                ', 'WELKOME TO TIC-TAC-TUE GAME!!!')
print()
print('INSTRUCTIONS:')
print()
print('-','ENTER x OR 0 BEFORE EACH STEP.')
print()
print('-','ENTER NUMBERS FROM 1 T0 3 AS YOUR COORDINATES.')
print()
    
def print_field():
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()
          
a = [[0, 1, 2, 3], [1, '_', '_', '_'], [2, '_', '_', '_'], [3, '_', '_', '_']]

c = input("PLEASE ENTER 's' TO START A GAME: ")
if c == 's':
    print()
    print_field()
    print()
if c != 's':
    print('YOU HAVE ENTERED INCORRECT SYMBOL! GAME OVER!')
    exit('GAME OVER')
        
def cell_occupation(i, j):
    if a[i][j] == 'x' or a[i][j] == '0':
        print('THE CELL IS OCCUPIED! PLEASE ENTER OTHER COORDINATES.')
        print()
        print('PLEASE REAPET YOUR STEP!')
        if a[i][j] == 'x':
            add_step(sign)
        if a[i][j] == '0':
            add_step(sign)
        return True
    return False

        
def add_step(sign):
    print()
    print(f"STEP FOR '{sign}' PLAYER")
    while True:
        print()
        j = input("ENTER X COORDINATE: ")
        i = input("ENTER Y COORDINATE: ")
        print()
        try:
            j = int(j)
            i = int(i)
        except:
            print('ARE YOU SURE YOU HAVE ENTERED A NUMBER?')
            print()
            print('PLEASE REAPET YOUR STEP!')
            print()
            continue
        if i not in range(len(a)) or j not in range(len(a[i])):
            print('YOU HAVE ENTERED INCORRECT COORDINATES!')
            print()
            print('PLEASE REAPET YOUR STEP!')
            print()
            print_field()
            add_step(sign)
            break
        if not cell_occupation(i, j):
            a[i][j] = sign 
            print_field()
        break


def symbol_player_checking(sign):
    print("YOU HAVE ENTERED INCORRECT SYMBOL! PLEASE ENTER x OR O TO CONTINUE.")
    return True
    return False

def check_the_winner():
    winner_cells = (((1, 1), (2, 1), (3, 1)), ((1, 2), (2, 2), (3, 2)), ((1, 3), (2, 3), (3, 3)),
                    ((1, 1), (1, 2), (1, 3)), ((2, 1), (2, 2), (2, 3)), ((3, 1), (3, 2), (3, 3)),
                    ((1, 1), (2, 2), (3, 3)), ((3, 1), (2, 2), (1, 3)))
    for value in winner_cells:
        symbols = []
        for c in value:
            symbols.append(a[c[0]][c[1]])
        if  symbols == ["x", "x", "x"]:
            print()
            print('            ',"THE WINNER IS X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print()
            print('            ',"THE WINNER IS 0!!!")
            return True
    return False

count = 0
while True:
    count = count + 1
    print()
    sign = input("ENTER KEY x OR 0 TO PLAY: ")
    if sign == 'x' or sign == '0':
        add_step(sign)
    if sign != 'x' and sign != '0':
        symbol_player_checking(sign)
    if check_the_winner():
        print()
        print('            ','GAME OVER!')
        break
    if count == 9:
        print()
        print('            ','DRAWN!','GAME OVER!')
        break
    





      

    

