# DeviceBridge — Copyright (C) 2026 Luchosdevf
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations
from pydantic import BaseModel, Field

class Device(BaseModel):

    """un dispositivo Android detectado por adb"""

    serial: str
    state: str

    @property 
    def is_ready(self)-> bool:
        return self.state == "device"

class BatteryStatus(BaseModel):
    """Estado de bateria obtenido de Dumpsys"""

    serial: str
    level: int = Field(ge=0, le=100)
    scale: int = 100
    temperature_c: float
    voltage_mv: int  |  None = None
    status_code: int
    status: str
    health_code: int
    health: str
    present: bool = True 
    technology: str  | None = None
    powered: list[str] = Field(default_factory=list)

