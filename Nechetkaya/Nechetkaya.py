def print_mtx(mtx):
    for i in range(len(mtx)):
        s = ''
        for j in range(len(mtx)):
            s+=(str(mtx[i][j])+' ')
        print(s)


def consistency_check(mtx,sum_col,v):
    sluch_sogl = {3: 0.58, 4: 0.9, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
    lamda = 0
    for i in range(len(v)):
        lamda += sum_col[i] * v[i]
    print("Лямбда = ",lamda)
    index_sogl = abs((lamda - len(sum_col)) / (len(sum_col) - 1))
    ocenka_sogl = round(index_sogl / sluch_sogl[len(sum_col)],4)
    print("ИС = ",index_sogl, "\nСлС = ",sluch_sogl[len(sum_col)],"\nОценка согласованности = ",ocenka_sogl)
    if (ocenka_sogl < 0.2):
        print("Все нормуль, ОС = ", ocenka_sogl)
    else:
        print("Чет коряво получилось, ну тогда каждый сам за себя. Считай без меня =)")


#Проверка матрицы на согласованность
def weight_alt(mtx):
    #Список для подсчета суммы по столбцам матрицы
    sum_column = mtx[0].copy()
    #Список для подсчета произведения для каждой строки
    mul_str = [i[0] for i in mtx]
    for i in range(1,len(mtx)):
        for j in range(len(mtx)):
            sum_column[j] += mtx[i][j]
            mul_str[j] *= mtx[j][i]
    for i in range(len(sum_column)):
        sum_column[i] = round(sum_column[i],3)
        #mul_str[i] = round(mul_str[i],3)
    print("(Не) красиво заполненная матрица (вдруг тебе такая нужна) : ")
    print_mtx(mtx)
    print("Сумма элементов по строкам :")
    print(sum_column)
    print("Произведение элементов по столбцам :")
    print(mul_str)
    #Считаем цены альтернатив
    c = [0] * len(mul_str)
    #Сумма цен альтернатив
    sum_c = 0
    for i in range(len(mul_str)):
        c[i] = round(pow(mul_str[i],1 / len(mtx)),2)
        sum_c += c[i]
    print("Цены альтернатив :")
    print(c)
    print("Сумма цен альтернатив :")
    print(sum_c)
    #Веса альтернатив
    v = [0] * len(c)
    for i in range(len(v)):
        v[i] = round(c[i] / sum_c, 3)
    print("Веса альтернатив : ")
    print(v)
    consistency_check(mtx,sum_column,v)


#Заполнение матрицы попарных сравнений (Метод Саати)
def fill_mtx(mtx):
    mtx2 = [["0"] * len(mtx) for i in range(len(mtx))] #Просто для красоты =)
    num_str = int(input('Какую строку заполним первой ? '))  # Выбираем строчку, которую первую заполним
    print("Введите значение для этой строки : ")
    # Заполняем строку по правилу
    # 1 - i-я и j-я алтернативы равноценны
    # 3 - i-я альтернатива немного предпочтительней j-й
    # 5 - i-я альтернатива предпочтительней j-й
    # 7 - i-я альтернатива значительно предпочтительней чем j-й
    # 9 - i-я альтернатива явно предпочтительней j-й
    for j in range(len(mtx)):
        print("Введите число(целое) для ",j," столбца : ")
        mtx[num_str][j] = float(input())
        mtx2[num_str][j] = "   " + str(int(mtx[num_str][j])) + "   "
        if num_str != j:#Заполняем аналогичный столбец обратными значениями
            mtx[j][num_str] = round(1 / mtx[num_str][j], 2)
            mtx2[j][num_str] = '1 / ' + str(mtx[num_str][j])
    #Заполняем таблицу по формуле mtx[i][j] = mtx[k][j] / mtx[k][i], где k - уже заполненная строка
    for i in range(len(mtx)):
        if (i  != num_str):
            for j in range(i,len(mtx)):
                if( j  != num_str):
                    mtx[i][j] = round(mtx[num_str][j]/mtx[num_str][i],2)
                    mtx2[i][j] = str(mtx[num_str][j])+ ' / ' + str(mtx[num_str][i])
                    mtx[j][i] = round(1 / mtx[i][j], 2)
                    mtx2[j][i] = '1 / ' + str(mtx[i][j])
    print("Красивая заполненая матрица(Разве не сказка?) : ")
    print_mtx(mtx2)
    weight_alt(mtx)



def create_mtx():
    size = int(input("Размер матрицы : ")) #Вводим размер матрицы
    mtx = [[0] * size for i in range(size)] #Создаем матрицу и заполняем 0
    fill_mtx(mtx)


if __name__ == '__main__':
    create_mtx()

