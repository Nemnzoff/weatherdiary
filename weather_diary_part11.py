# === Stage 11: Поиск по нескольким словам ===
# Project: WeatherDiary
from typing import List, Set, Dict, Optional


class QueryParser:
    """Разбирает строку поиска с исключениями по префиксу '-'.

    Строка: "день дождь -ночь" → искать совпадения по всем словам,
    кроме "ночь". Точное совпадение проверяется на полях сущности.
    """

    def __init__(self, text: str = ""):
        self.raw = text
        self.positive: List[str] = []
        self.negative: Set[str] = set()

    def parse(self) -> "QueryParser":
        for token in self.raw.lower().split():
            if token.startswith("-"):
                self.negative.add(token[1:].strip())
            else:
                self.positive.append(token)
        return self

    def has_terms(self) -> bool:
        return bool(self.positive) or bool(self.negative)

    def matches(self, entity: dict) -> bool:
        """Проверка сущности: все положительные, ни одно исключённое."""
        if self.negative:
            for field in entity.values():
                if field and field.lower() in self.negative:
                    return False
        if self.positive:
            haystack: List[str] = []
            for value in entity.values():
                if isinstance(value, list):
                    haystack.extend(str(v) for v in value)
                else:
                    haystack.append(str(value))
            haystack = [h for h in haystack if h]
            for term in self.positive:
                if not any(term in h for h in haystack):
                    return False
        return True


def build_index(records: List[dict]) -> Dict[str, List[str]]:
    """Индексирует каждое поле для быстрой проверки по словам."""
    index: Dict[str, List[str]] = {}
    for record in records:
        for key, value in record.items():
            if isinstance(value, list):
                for item in value:
                    index.setdefault(str(item).lower(), []).append(key)
            else:
                index.setdefault(str(value).lower(), []).append(key)
    return index


def filter_records(records: List[dict], query: str) -> List[dict]:
    """Функциональный фильтр записей по строке поиска."""
    parser = QueryParser(query).parse()
    if not parser.has_terms():
        return list(records)
    return [r for r in records if parser.matches(r)]


if __name__ == "__main__":
    sample = [
        {"date": "2024-05-01", "temperature": "15°C", "precipitation": ["дождь"], "wind": "5 м/с"},
        {"date": "2024-05-02", "temperature": "22°C", "precipitation": [], "wind": "12 м/с"},
        {"date": "2024-05-03", "temperature": "18°C", "precipitation": ["снег"], "wind": "3 м/с"},
    ]

    print("Все:")
    for r in filter_records(sample, ""):
        print(" ", r["date"], r["temperature"])

    print("Дождь:")
    for r in filter_records(sample, "дождь"):
        print(" ", r["date"], r["temperature"])

    print("Дождь, но не снег:")
    for r in filter_records(sample, "дождь -снег"):
        print(" ", r["date"], r["temperature"])

    print("Температура 20:")
    for r in filter_records(sample, "20"):
        print(" ", r["date"], r["temperature"])

    print("Пустой запрос:")
    for r in filter_records(sample, "   "):
        print(" ", r["date"], r["temperature"])
