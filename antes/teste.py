from typing import Dict, Union
from continua import main


def funcao01(texto: str, numero: int) -> str:
    return texto * numero


def funcao02(texto: str, numero: int) -> Dict[str, Union[str, int]]:
    return {"texto": texto, "numero": numero}


def funcao03(payload: Dict[str, Union[str, int]]) -> Dict[str, Union[str, int]]:
    return payload


def funcao05(a: int, b: int) -> int:
    return a / b


if __name__ == "__main__":
    funcao01("a", 3)
    funcao02("a", 3)
    myDict = {"texto": "a", "numero": 3}
    funcao03(myDict)
    main()
