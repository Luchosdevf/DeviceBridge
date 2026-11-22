from __future__ import annotations

import shutil 
import subprocess

from adb.errors import AdbError, AdbNotFoundError
from adb.parsers import parse_devices_output
from models import Device

class AdbClient:
    """cliente minimo para ejecutar comandos adb"""

    def __init__(self, adb_path: str  | None = None, timeout: float = 15.0) -> None:
        self.adb_path = adb_path or shutil.which("adb") or "adb"
        self.timeout = timeout

    def run(self, *args: str, serial: str  | None = None) -> str:
        """ejecuta 'adb args' y devuelve la salida estandard"""
        cmd = [self.adb_path]
        if serial:
            cmd += ["-s", serial]
        cmd += list(args)

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=self.timeout,
                check=False,
            )
        except FileNotFoundError as exc:
            raise AdbNotFoundError(
                f"no se encontro binario el 'ADB' ({self.adb_path})" 
            ) from exc
        except subprocess.TimeoutExpired as exc:
            raise AdbError(f"ADB agoto el tiempo de espera: {' '.join(cmd)}") from exc
        
        if result.returncode != 0:
            detail = (result.stderr or result.stdout).strip()
            raise AdbError(f"ADB fallo {result.returncode} {detail}")
        
        return result.stdout

    def devices(self) -> list[Device]:
        """Lista los dispositivos conectados (`adb devices`)."""
        return parse_devices_output(self.run("devices"))

    def shell(self, serial: str, *args: str) -> str:
        """Ejecuta `adb -s <serial> shell <args>`."""
        return self.run("shell", *args, serial=serial)

    def version(self) -> str:
        """Devuelve la primera l�nea de `adb version`."""
        return self.run("version").splitlines()[0].strip()
