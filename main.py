from math import *
from statistics import median
from scipy import stats
def statmean(A):
    """
    Считает среднее значения выборки.Если в выборке есть бесконечность,то подсчитать нельзя
    """
    for i in A:
        if i == float('inf') or len(A) == 0:
            return 'Error'
    return(fsum(A)/len(A))
def statmedian(A):
    """
    Функция высчитывает медиану.Идет проверка на четность из-за отличия формул.Для четного случая применена функция из statistic в связи со сложностью вычислений
    """
    sorted(A)
    if len(A) % 2 != 0:
        num = (len(A) + 1) // 2
        return A[num - 1]
    return median(A)
def statQ(A):
    """
        Функция высчитывает выборочные квартили.Разбивается массив данных на три равных части с высчитом медиан
    """
    first = statmedian(A)
    B = A[len(A)//2:]
    C = A[:len(A)//2]
    second = statmedian(B)
    third = statmedian(C)
    return first, second, third
def statR(A):
    """
            Функция высчитывает размах.
    """
    return max(A) - min(A)
def statMid(A , k):
    """
        Функция высчитывает выборочный центральный к-тый момент
    """
    s = 0
    for i in A:
        s += ((i - statmean(A)) ** k)
    return s / (len(A) - 1)
def statS2(A):
    """
        Функция высчитывает  дисперсию и стандартное отклонения применяя частный случай формулы центрального момента
    """
    return f'диспресия = {statMid(A , 2)},отклонение равно {statMid(A , 2) ** 0.5} '
def StadZ(A):
    """
        Стандартизация распределения функция выдает Z параметр стандартизации (отклонение)
    """
    t = statMid(A, 2) ** 0.5
    s = 0
    for i in A:
        s += ((i - statmean(A)) ** 2)
    return s / t
def stat_SE(A):
    return (statMid(A, 2) ** 0.5) / len(A)

def True_dist(A,interval = 0.99):
    alpha = 1 - interval
    z = abs(stats.norm.ppf(alpha / 2))
    sd = statMid(A , 2) ** 0.5
    m = statmean(A)
    return (round(m - z * stat_SE(A), 2), round(m + z * stat_SE(A), 2))
def menu(A, k =2):
    """
            Основная Функция выбора.Выдает то значения какое выберете из заданных функций
    """
    print('1.Выборочное среднее', '2. Медиана', '3. Квартили распределения', '4. Размах', '5. Диспресия и стандартное отклонение', sep='\n')
    print('6 Стандартизация данных', ' 7 k-тый центральный элемент M', '8. Стандартная ошибка среднего', '9. Доверительный интервал', sep='\n')

    while True:
        x = int(input('выберите номер для подсчета'))
        if x == 1:
            print(statmean(A))
            continue
        elif x == 2:
            print(statmedian(A))
            continue
        elif x == 3:
            print(statQ(A))
            continue
        elif x == 4:
            print(statR(A))
            continue
        elif x == 5:
            print(statS2(A))
            continue
        elif x == 6:
            print(StadZ(A))
            continue
        elif x == 7:
            print(statMid(A, k))
            continue
        elif x == 8:
            print(stat_SE(A))
            continue
        elif x == 9:
             print(True_dist(A))
             continue
        elif x == 0:
            print('Выход')
            break
        else:
            print('Error ошибочный номер')
            continue
