import itertools as it

def FieldAbility(i,j,N): #проверка вхождения индексов i,j в размер шахматной доски
    if (i in range(N)) and (j in range(N)):
        return True
    else:
        return False

def BoardPrinter(Board): #вывод на печать матрицы шахматной доски
    for i in range(len(Board)):
        print(Board[i])
    print()
    return

def QueenPrinter(Board): #вывод на печать расстановки ферзей на доске. на входе - матрица шахматной доски
    N = len(Board)
    TempBoard = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if (Board[i][j] == -1):
                TempBoard[i][j] = 1 #во всех местах, где -1, стоит ферзь, то есть соответствующая клетка становится равной 1
        print(TempBoard[i])
    print()
    return

def PutQueenOnBoard(i,j,Board): #функция установки ферзя на доску. ко всем полям матрицы Board, которые под его ударом, прибавляется 1
    N = len(Board)
    if not FieldAbility(i,j,N):
        return "IndexError" #если индексы установки ферзя поданы некорректно, возвращаем строку с ошибкой
    if Board[i][j] != 0:
        return False #если клетка для установки ферзя под ударом, вернуть False
    for k in range(N):#прибавляем 1 ко всем полям по вертикали и горизонтали от i,j
        Board[k][j] += 1
        Board[i][k] += 1
    for k in range(1,N):#прибавляем 1 ко всем полям по диагонали от i,j
        if FieldAbility(i + k, j + k, N):
            Board[i+k][j+k] +=1
        if FieldAbility(i + k, j - k, N):
            Board[i+k][j-k] +=1
        if FieldAbility(i - k, j + k, N):
            Board[i-k][j+k] +=1
        if FieldAbility(i - k, j - k, N):
            Board[i-k][j-k] +=1
    Board[i][j] = -1 #саму клетку установки ферзя делаем равной -1
    return

def PermGenerator(N): #генерируем все перестановки чисел от 0 до N-1
    Set = [i for i in range(N)]
    return list(it.permutations(Set))

def QueenPermutationChecker(QueenPermutation): #проверка поданной перстановки ферзей на удовлетворение условиям задачи
    N = len(QueenPermutation)
    ChessBoard = [[0 for i in range(N)] for j in range(N)] #создаем пустую доску
    for i in range(N): #проходим по всем значениям перестановки ферзей
        if PutQueenOnBoard(i,QueenPermutation[i],ChessBoard) == False: #если следующий ферзь в перестановке не может быть установлен, возвращаем False
            return False
    return True #если установка всех ферзей прошла успешно, возвращаем True

N = 8 #задаем размер квадратной доски. Внимание, при N>9 время решения задачи сильно растет
QueenPlacingSet = PermGenerator(N) #генерируем все перестановки ферзей
NumberOfPermutations = len(QueenPlacingSet) #получаем количество перестановок ферзей
i = 0 #создаем счетчик успешных решений
for Q in QueenPlacingSet: #перебираем все перестановки ферзей и проверяем на корректность
    if QueenPermutationChecker(Q):
        i+=1
print(f"Generated {NumberOfPermutations} available permutations. Number of solutions is {i}")