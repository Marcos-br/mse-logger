from typing import Dict, Union
from mse_logger import mse_logger


@mse_logger
def funcao04(payload: Dict[str, Union[str, int]]) -> None:
    return None


@mse_logger
def funcao05(a: int, b: int) -> int:
    return a / b


def main():
    myDict = {"texto": "a", "numero": 3}
    funcao04(myDict)
    funcao05(6, 2)
    funcao05(6, 0)
