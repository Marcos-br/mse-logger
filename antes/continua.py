from typing import Dict, Union


def funcao04(payload: Dict[str, Union[str, int]]) -> None:
    return None


def funcao05(a: int, b: int) -> int:
    return a / b


def main():
    myDict = {"texto": "a", "numero": 3}
    funcao04(myDict)
    funcao05(6, 2)
    funcao05(6, 0)
