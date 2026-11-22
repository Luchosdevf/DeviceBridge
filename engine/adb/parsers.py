from __future__ import annotations 
from models import Device



def parse_devices_output(output: str) -> list[Device]:
    """convierte la salida de adb devices es una lista de Device"""
    devices: list[Device] = []

    for raw in output.splitlines():
        line = raw.strip()
        if not line or line.lower().startswith("list of devices"):
            continue
        if line.startswith("*"):
            continue

        parts = line.split()
        if len(parts) < 2:
            continue

        devices.append(Device(serial=parts[0], state=parts[1]))

    return devices