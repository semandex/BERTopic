from importlib.metadata import version

from bertopic._bertopic import BERTopic

__version__ = version("semandex-bertopic")

__all__ = [
    "BERTopic",
]
