# === Stage 1: Каркас модуля ===
# Project: WeatherDiary
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Day:
    date: date
    temperature: float
    precipitation: float
    wind: float


def make_demo_days() -> list[Day]:
    demo = [
        Day(date(2024, 1, 1), 2.0, 0.0, 3.5),
        Day(date(2024, 1, 2), -1.0, 5.0, 6.1),
        Day(date(2024, 1, 3), -4.0, 12.0, 8.7),
        Day(date(2024, 1, 4), 0.0, 0.0, 2.2),
        Day(date(2024, 1, 5), 4.0, 0.0, 1.8),
    ]
    return demo


def main() -> None:
    days = make_demo_days()
    print("WeatherDiary v0.1")
    print("Демо-дневник за январь 2024")
    print("-" * 30)
    for day in days:
        print(f"{day.date}  t={day.temperature:+.1f}  "
              f"осадки={day.precipitation:.1f}  "
              f"ветер={day.wind:.1f}")
    print("-" * 30)
    print(f"Всего записей: {len(days)}")
    print("Завершено. Этап 1 из 69.")


if __name__ == "__main__":
    main()
