# DeviceBridge — Copyright (C) 2026 Luchosdevf
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations 


class AdbError(RuntimeError):
    """Error ejecutando Adb"""

class AdbNotFoundError(AdbError):
    """El Binario Adb no esta disponible"""