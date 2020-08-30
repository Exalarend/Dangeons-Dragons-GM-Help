import random


def dice(number=1, side=6):
    """"Первое число - это количество кубиков, а второе - количество его сторон.
    Создает список выпавших кубиков"""
    import random
    start = 0
    sum_dice = []
    while start < number:
        start += 1
        cube = random.randrange(1, side + 1)
        sum_dice += [cube]
    return sum_dice


def characteristic(sum_dice):
    """Принимает параметр и создает пары типа (Парамаетр,Модификатор)"""
    modifier = None
    if sum_dice >= 10:
        modifier = str(int((sum_dice - 10) / 2))
    if sum_dice > 11:
        modifier = '+' + modifier
    else:
        sum_dice -= 1
        modifier = str(int((sum_dice - 10) / 2))
        sum_dice += 1
    return sum_dice, modifier


def proficiency_bonus(lvl):
    """ Получает на вход уровень игрока и возвращает значение его 'Бонуса мастерства'."""
    bonus = 0
    if lvl <= 4:
        bonus = 2
    elif lvl <= 8:
        bonus = 3
    elif lvl <= 12:
        bonus = 4
    elif lvl <= 16:
        bonus = 5
    elif lvl < 20:
        bonus = 6
    else:
        bonus = 'Вы указали что-то не правильно!'
    return bonus


def hit(hit_klass, constitution_modifier, lvl=1, anoser_modifier=0):
    total_hit = sum(hit_klass) + constitution_modifier * lvl + anoser_modifier
    return total_hit


def random_parameter():
    """Функция создает 6 рандомных параметров и их модификаторов"""
    intermediary = None
    parameter = [None, None, None, None, None, None]
    x = 0
    while x < 6:
        intermediary = dice(4, 6)
        intermediary.remove(min(intermediary))
        parameter[x] = sum(intermediary)
        x += 1
    parameter.sort(reverse=True)
    return parameter


def all_characteristic(priority_characteristics, random_characteristics, class_characteristics):
    """Функция принимает последовательность характеристик класса, которые распределены по приоритетам,
    присваивает им рандомные параметры, прибавляет классовые бонусы к характеристике
    а остальные характеристики и параметры распределяет рандомно"""
    all_characteristics = ["Сила",
                           "Телосложение",
                           "Ловкость",
                           "Интеллект",
                           "Харизма",
                           "Мудрость"
                           ]
    characteristics = {}
    for intermediary in priority_characteristics:
        characteristics[intermediary] = max(random_characteristics)
        if intermediary in class_characteristics:
            characteristics[intermediary] += class_characteristics[intermediary]
        random_characteristics.remove(max(random_characteristics))
        all_characteristics.remove(intermediary)
    random.shuffle(all_characteristics)
    for intermediary in all_characteristics:
        characteristics[intermediary] = max(random_characteristics)
        random_characteristics.remove(max(random_characteristics))
    return characteristics
