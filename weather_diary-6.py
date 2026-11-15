# === Stage 6: Связанная сущность ===
# Project: WeatherDiary
from datetime import date


class Measurement:
    def __init__(self, date, temperature, wind_speed):
        self.date = date
        self.temperature = temperature
        self.wind_speed = wind_speed

    def __repr__(self):
        return f"Measurement(date={self.date}, temperature={self.temperature}, wind_speed={self.wind_speed})"


class Diary:
    def __init__(self):
        self._measurements = {}

    def add_measurement(self, day_id, date, temperature, wind_speed):
        measurement = Measurement(date, temperature, wind_speed)
        self._measurements[(day_id, date)] = measurement
        return measurement

    def get_measurement(self, day_id, date):
        return self._measurements.get((day_id, date))

    def list_measurements(self, day_id):
        return [
            measurement for measurement in self._measurements.values()
            if measurement.date.year == day_id.year
            and measurement.date.month == day_id.month
            and measurement.date.day == day_id.day
        ]
