# === Stage 3: Хранилище в памяти ===
# Project: WeatherDiary
memory_store.py

from datetime import date


class Day:
    def __init__(self, day_id, date, temperature, precipitation, wind):
        self.day_id = day_id
        self.date = date
        self.temperature = temperature
        self.precipitation = precipitation
        self.wind = wind

    def to_dict(self):
        return {
            "day_id": self.day_id,
            "date": self.date.isoformat(),
            "temperature": self.temperature,
            "precipitation": self.precipitation,
            "wind": self.wind,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            day_id=data["day_id"],
            date=date.fromisoformat(data["date"]),
            temperature=data["temperature"],
            precipitation=data["precipitation"],
            wind=data["wind"],
        )


class WeatherMemoryStore:
    def __init__(self):
        self._days = {}

    def add_day(self, day: Day) -> Day:
        self._days[day.day_id] = day
        return day

    def get_day(self, day_id) -> Day:
        return self._days.get(day_id)

    def list_days(self) -> list:
        return list(self._days.values())
