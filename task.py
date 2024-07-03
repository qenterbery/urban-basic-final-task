import csv

MAX_FLOOR_MEDIUM = 16
MAX_FLOOR_LOW = 5
MIN_FLOOR_LOW = 1

filename = "housing_data.csv"


def read_file(filename: str) -> list[dict]:
    """Читает данные из CSV файла и преобразует их в список словарей.

    :param filename: Название файла, содержащего данные.
    :return: Список словарей с данными о домах.
    """
    with open(filename, encoding="utf-8") as f:
        houses_in_func = list(csv.DictReader(f))
    for dictionary in houses_in_func:
        dictionary["floor_count"] = int(dictionary["floor_count"])
        dictionary["heating_value"] = float(dictionary["heating_value"])
        dictionary["area_residential"] = float(dictionary["area_residential"])
        dictionary["population"] = int(dictionary["population"])
    return houses_in_func


houses = read_file(filename)
floor_count = 5


def classify_house(floor_count: int) -> str:
    """Классифицирует дом на основе количества этажей.

    Проверяет, является ли количество этажей целым числом и положительным значением.
    Возвращает категорию дома в зависимости от количества этажей.

    :param floor_count: Количество этажей в доме.
    :return: Категория дома в виде строки: "Малоэтажный", \
    "Среднеэтажный" или "Многоэтажный".
    """
    houses_floor_counting = "0"
    if not isinstance(floor_count, int):
        type_er = "Тип данных floor_count не соответствует требованиям"
        raise TypeError(type_er)
    if floor_count <= 0:
        val_er = "Значение floor_count не соответствует требованиям"
        raise ValueError(val_er)
    if MIN_FLOOR_LOW <= floor_count <= MAX_FLOOR_LOW:
        houses_floor_counting = "Малоэтажный"
    if MAX_FLOOR_LOW < floor_count <= MAX_FLOOR_MEDIUM:
        houses_floor_counting = "Среднеэтажный"
    if floor_count > MAX_FLOOR_MEDIUM:
        houses_floor_counting = "Многоэтажный"
    return houses_floor_counting


def get_classify_houses(houses: list[dict]) -> list[str]:
    """Классифицирует дома на основе количества этажей.

    :param houses: Список словарей с данными о домах.
    :return: Список категорий домов.
    """
    houses_floor_counting = []
    for classifying in houses:
        classifying_int = int(classifying["floor_count"])
        if not isinstance(classifying_int, int):
            type_er = (
                "Тип данных floor_count из списка houses не соответствует требованиям"
            )
            raise TypeError(type_er)
        if classifying_int <= 0:
            val_er = (
                "Значение floor_count из списка houses не соответствует требованиям"
            )
            raise ValueError(val_er)
        if MIN_FLOOR_LOW <= classifying_int <= MAX_FLOOR_LOW:
            houses_floor_counting.append("Малоэтажный")
        if MAX_FLOOR_LOW < classifying_int <= MAX_FLOOR_MEDIUM:
            houses_floor_counting.append("Среднеэтажный")
        if classifying_int > MAX_FLOOR_MEDIUM:
            houses_floor_counting.append("Многоэтажный")

    return houses_floor_counting


categories = get_classify_houses(houses)


def get_count_house_categories(categories: list[str]) -> dict[str, int]:
    """
    Подсчитывает количество домов в каждой категории.

    :param categories: Список категорий домов.
    :return: Словарь с количеством домов в каждой категории.
    """
    count_house_categories = {}
    for count_classification in categories:
        if count_classification not in count_house_categories:
            count_house_categories[count_classification] = 1
        else:
            count_house_categories[count_classification] += 1
    return count_house_categories


counted_house_categories = get_count_house_categories(categories)


def min_area_residential(houses: list[dict]) -> str:
    """Находит адрес дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца.

    :param houses: Список словарей с данными о домах.
    :return: Адрес дома с наименьшим средним количеством квадратных метров
    жилой площади на одного жильца.
    """
    average_area_list = []
    for list_perebor in houses:
        average_area_dict = {}
        house_address = list_perebor["house_address"]
        area_residential = float(list_perebor["area_residential"])
        population = int(list_perebor["population"])
        average_area = area_residential / population
        average_area_dict["house_address"] = house_address
        average_area_dict["average_area"] = average_area
        average_area_list.append(average_area_dict)

    min_area = float("inf")
    min_area_address = "0"

    for perebor_average_area_list in average_area_list:
        perebor_average_area_list_area = float(
            perebor_average_area_list["average_area"],
        )
        if perebor_average_area_list_area < min_area:
            min_area_address = perebor_average_area_list["house_address"]
            min_area = perebor_average_area_list["average_area"]

    return min_area_address


min_area_residential(houses)
