# === Stage 7: Связи между сущностями ===
# Project: WeatherDiary
from datetime import date


class DataIntegrityError(Exception):
    pass


class Day:
    def __init__(self, day: date, temperature: float,
                 precipitation: float, wind: float):
        self.day = day
        self.temperature = temperature
        self.precipitation = precipitation
        self.wind = wind


class Measurement:
    def __init__(self, day: Day, temperature: float,
                 precipitation: float, wind: float):
        self.day = day
        self.temperature = temperature
        self.precipitation = precipitation
        self.wind = wind


def get_measurements_for_day(day: Day, measurements: list) -> list:
    return [m for m in measurements if m.day is day]


def check_integrity(day: Day, measurements: list) -> None:
    expected = get_measurements_for_day(day, measurements)
    if len(expected) != 1:
        raise DataIntegrityError(
            f"Ожидается ровно один замер для дня {day.day}, "
            f"найдено: {len(expected)}")
    m = expected[0]
    if m.day != day.day:
        raise DataIntegrityError(
            f"Связка нарушена: замер привязан к {m.day.day}, "
            f"а не к {day.day}")
    if m.day is not day:
        raise DataIntegrityError(
            f"Связка нарушена: замер ссылается на другой объект дня")
    if m.day.temperature != day.temperature:
        raise DataIntegrityError(
            f"Связка нарушена: температура замера "
            f"{m.day.temperature} не совпадает с "
            f"днём {day.temperature}")
    if m.day.precipitation != day.precipitation:
        raise DataIntegrityError(
            f"Связка нарушена: осадки замера "
            f"{m.day.precipitation} не совпадают с "
            f"нём {day.precipitation}")
    if m.day.wind != day.wind:
        raise DataIntegrityError(
            f"Связка нарушена: ветер замера {m.day.wind} не совпадает "
            f"с днём {day.wind}")
