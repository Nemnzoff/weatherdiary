# === Stage 4: Редактирование записей ===
# Project: WeatherDiary
ALLOWED_FIELDS = ("temperature", "precipitation", "wind")


def _coerce(value):
    if isinstance(value, str):
        return float(value)
    return value


def edit_day(day_id, changes):
    if day_id not in DAY_RECORDS:
        raise KeyError(day_id)

    new_record = dict(DAY_RECORDS[day_id])
    for field, value in changes.items():
        if field not in ALLOWED_FIELDS:
            raise ValueError(field)
        if field == "date":
            raise ValueError("date")
        new_record[field] = _coerce(value)

    DAY_RECORDS[day_id] = new_record
    return new_record


DAY_RECORDS = {}


def add_day(record):
    DAY_RECORDS[record["date"]] = record


def get_day(day_id):
    return DAY_RECORDS.get(day_id)


def list_days():
    return list(DAY_RECORDS.values())


if __name__ == "__main__":
    add_day({"date": "2024-06-01", "temperature": 21.5, "precipitation": 0.0, "wind": 3.2})
    add_day({"date": "2024-06-02", "temperature": 23.1, "precipitation": 5.0, "wind": 4.8})

    edited = edit_day("2024-06-01", {"temperature": 20.0})
    print(edited)

    try:
        edit_day("2024-06-01", {"date": "2024-06-03"})
    except ValueError as exc:
        print("blocked:", exc)

    try:
        edit_day("2024-06-01", {"humidity": 50})
    except ValueError as exc:
        print("blocked:", exc)

    try:
        edit_day("9999-12-31", {"temperature": 10})
    except KeyError as exc:
        print("missing:", exc)
