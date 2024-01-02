from typing import Dict, Union
from mse_logger import mse_logger
from continua import main


@mse_logger
def funcao01(texto: str, numero: int) -> str:
    return texto * numero


@mse_logger
def funcao02(texto: str, numero: int) -> Dict[str, Union[str, int]]:
    return {"texto": texto, "numero": numero}


@mse_logger
def funcao03(payload: Dict[str, Union[str, int]]) -> Dict[str, Union[str, int]]:
    return payload


@mse_logger
def funcao05(a: int, b: int) -> int:
    return a / b


if __name__ == "__main__":
    funcao01("a", 3)
    funcao02("a", 3)
    myDict = {"texto": "a", "numero": 3}
    funcao03(myDict)
    main()
