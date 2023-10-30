import random
from typing import Protocol, List


class TransformerInterface(Protocol):
    dimension: int

    def encode(self, s: str) -> List[float]:
        pass


class FakeTransformer:
    def __init__(self, dimension=50):
        self.dimension = dimension

    def encode(self, s) -> List[float]:
        return [random.random() for _ in range(self.dimension)]