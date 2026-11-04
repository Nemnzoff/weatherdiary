# === Stage 2: Проверка полей ===
# Project: WeatherDiary
from datetime import date


class DayValidationError(ValueError):
    pass


def parse_date(value):
    text = value.strip()
    if not text:
        raise DayValidationError("Дата не может быть пустой.")
    if len(text) != 10:
        raise DayValidationError("Дата должна быть в формате ГГГГ-ММ-ДД (10 символов).")
    parts = text.split("-")
    try:
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
    except ValueError:
        raise DayValidationError("Дата должна быть в формате ГГГГ-ММ-ДД.")
    try:
        return date(year, month, day)
    except ValueError:
        raise DayValidationError("Неверная дата: такого дня не существует.")


def parse_temperature(value):
    text = value.strip()
    if not text:
        raise DayValidationError("Температура не может быть пустой.")
    if text.lower() in ("n/a", "нет", "нет данных", "неизвестно", "нет данных"):
        return None
    try:
        return float(text)
    except ValueError:
        raise DayValidationError("Температура должна быть числом, например 15.5.")


def parse_precipitation(value):
    text = value.strip()
    if not text:
        raise DayValidationError("Осадки не могут быть пустыми.")
    if text.lower() in ("n/a", "нет", "нет данных", "неизвестно", "без осадков"):
        return None
    try:
        return float(text)
    except ValueError:
        raise DayValidationError("Осадки должны быть числом, например 2.4 миллиметра.")


def parse_wind(value):
    text = value.strip()
    if not text:
        raise DayValidationError("Ветер не может быть пустым.")
    if text.lower() in ("n/a", "нет", "нет данных", "неизвестно", "штиль", "штиль"):
        return None
    try:
        return float(text)
    except ValueError:
        raise DayValidationError("Ветер должен быть числом, например 3.2 метра в секунду.")


def normalize_day(raw):
    raw = raw or {}
    result = {}
    for field in ("date", "temperature", "precipitation", "wind"):
        if field not in raw:
            raise DayValidationError(f"Отсутствует обязательное поле: {field}.")
        result[field] = {
            "date": parse_date(raw[field]),
            "temperature": parse_temperature(raw[field]),
            "precipitation": parse_precipitation(raw[field]),
            "wind": parse_wind(raw[field]),
        }
    return result
