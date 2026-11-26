# DeviceBridge — Copyright (C) 2026 Luchosdevf
# SPDX-License-Identifier: GPL-3.0-or-later

"""DeviceBridge engine — punto de entrada.

Orquesta las comprobaciones (checks), el acceso a ADB y la generación
de informes sobre los dispositivos conectados.
"""

from rich.console import Console

console = Console()


def main() -> None:
    console.print("[bold green]DeviceBridge engine[/bold green] listo.")


if __name__ == "__main__":
    main()
