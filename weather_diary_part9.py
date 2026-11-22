# === Stage 9: Фильтрация записей ===
# Project: WeatherDiary
from datetime import date


def filter_days_by_temperature(days, min_temp=None, max_temp=None):
    """Возвращает список дней с температурой в заданном диапазоне.

    min_temp и max_temp — числа или None. При None соответствующая
    граница не проверяется. Сравнение включительное.
    """
    result = []
    for day in days:
        temp = day["temperature"]
        if min_temp is not None and temp < min_temp:
            continue
        if max_temp is not None and temp > max_temp:
            continue
        result.append(day)
    return result


def filter_days_by_date_range(days, start_date=None, end_date=None):
    """Возвращает список дней с датой в заданном диапазоне.

    start_date и end_date — объекты date или None. При None
    соответствующая граница не проверяется. Сравнение включительное.
    """
    result = []
    for day in days:
        day_date = day["date"]
        if start_date is not None and day_date < start_date:
            continue
        if end_date is not None and day_date > end_date:
            continue
        result.append(day)
    return result


def filter_days(days, min_temp=None, max_temp=None, start_date=None, end_date=None):
    """Комбинирует фильтрацию по температуре и по диапазону дат.

    Все заданные фильтры применяются одновременно: день попадает
    в результат только если он удовлетворяет всем из них.
    Параметры None отключают соответствующую проверку.
    """
    return [
        day
        for day in days
        if (min_temp is None or day["temperature"] >= min_temp)
        and (max_temp is None or day["temperature"] <= max_temp)
        and (start_date is None or day["date"] >= start_date)
        and (end_date is None or day["date"] <= end_date)
    ]
