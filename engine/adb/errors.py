from __future__ import annotations 


class AdbError(RuntimeError):
    """Error ejecutando Adb"""

class AdbNotFoundError(AdbError):
    """El Binario Adb no esta disponible"""