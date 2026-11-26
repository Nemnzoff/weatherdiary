# === Stage 10: Сортировка записей ===
# Project: WeatherDiary
from datetime import date


def sort_key(entry):
    return (entry["date"], entry["created_at"])


def sort_entries(entries, reverse=False):
    return sorted(entries, key=sort_key, reverse=reverse)
