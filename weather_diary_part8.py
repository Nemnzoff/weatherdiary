# === Stage 8: Генерация идентификаторов ===
# Project: WeatherDiary
import uuid
from datetime import datetime


def make_project_id(prefix="weatherdiary"):
    """Сгенерировать уникальный идентификатор с префиксом проекта.

    Формат: {prefix}_{short-uuid}
    При наложении на существующий идентификатор добавляется счётчик,
    чтобы гарантировать уникальность в пределах сессии генерации.
    """
    while True:
        raw = uuid.uuid4().hex[:8]
        candidate = f"{prefix}_{raw}"
        if candidate not in _active_ids:
            _active_ids.add(candidate)
            return candidate


_active_ids = set()


def register_id(value):
    """Зарегистрировать идентификатор и защитить его от повторного создания.

    Позволяет другим модулям (дневник, замеры) использовать сгенерированный
    идентификатор и одновременно помечать его как занятого, чтобы
    make_project_id не возвращал дубликат в той же сессии.
    """
    _active_ids.add(value)
    return value


def clear_active_ids():
    """Очистить реестр активных идентификаторов (например, при перезапуске)."""
    _active_ids.clear()
