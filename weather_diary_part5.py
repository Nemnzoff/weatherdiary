# === Stage 5: Удаление и восстановление ===
# Project: WeatherDiary
from datetime import date


class Day:
    def __init__(self, date, temperature, precipitation, wind):
        self.date = date
        self.temperature = temperature
        self.precipitation = precipitation
        self.wind = wind
        self.deleted = False

    def soft_delete(self):
        self.deleted = True

    def restore(self):
        self.deleted = False

    def is_deleted(self):
        return self.deleted
