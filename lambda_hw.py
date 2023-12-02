def Tic_tac_toe(field):
        for i in field:
                i = set(i)
                if len(i) == 1:
                        return f'{i.pop()} win'
        return 'draw'

field = [input().split() for _ in range(3)]
left_diagonal = [field[i][i] for i in range(3)]
right_diagonal = [field[2- i][i] for i in range(3)]
field.append(left_diagonal)
field.append(right_diagonal)
print(Tic_tac_toe(field))