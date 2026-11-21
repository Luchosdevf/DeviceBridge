# DeviceBridge

<p align="center">
  <strong>A desktop toolkit for Android devices.</strong>
  <br>
  Diagnose, inspect and manage your Android device from one place.
  <br><br>
  <img src="https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/C%23-.NET%2010-512BD4?style=for-the-badge&logo=dotnet">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/License-Apache%202.0-blue?style=for-the-badge">
</p>

---

## What is DeviceBridge?

DeviceBridge is a desktop application I'm building to make Android device diagnostics and management easier.

It combines a C# desktop interface with Python scripts and ADB to run automatic checks, collect device information and perform useful operations without having to deal with multiple tools separately.

The idea is simple: connect your phone, run some checks and get everything organized in one place.

## Features

*Planned and under development.*

- **Device Detection** — Detect connected Android devices.
- **Device Information** — View Android versions, build properties and hardware details.
- **Battery Checks** — Check battery level, temperature and available health information.
- **Storage Analysis** — Check storage usage and available space.
- **RAM Monitoring** — View memory usage and statistics.
- **Package Inspector** — Browse installed applications and package details.
- **Automatic Checks** — Run Python scripts to analyze different parts of the device.
- **Diagnostic Reports** — Generate reports with collected information.
- **Device History** — Keep previous diagnostic results.

## How it works

DeviceBridge uses different technologies for different tasks:

| Technology | Purpose |
|---|---|
| C# / .NET 10 | Main application |
| Avalonia UI | Desktop interface |
| Python | Diagnostic scripts and automation |
| ADB | Communication with Android |
| SQLite | Local data and history |
| JSON | Communication between C# and Python |

### Architecture

```text
        DeviceBridge
              |
        C# Desktop App
              |
        Python Engine
              |
       Diagnostic Scripts
              |
            ADB
              |
        Android Device
```

## Project Structure

```text
DeviceBridge/
├── src/
│   ├── DeviceBridge.App/
│   └── DeviceBridge.Core/
│
├── engine/
│   ├── checks/
│   ├── adb/
│   ├── reports/
│   ├── main.py
│   └── requirements.txt
│
├── tests/
│   ├── csharp/
│   └── python/
│
├── config/
├── docs/
├── .gitignore
└── README.md
```

## Requirements

- .NET 10 SDK
- Python 3
- Android Platform Tools (ADB)
- Git
- SQLite

## Development

DeviceBridge is still a work in progress. Its main focus is building a reliable connection between the desktop application, Python scripts and Android devices.

The project is being developed with modularity in mind, so new diagnostic checks and features can be added without having to rewrite the entire application.

### Getting started

```bash
# C# app
dotnet build
dotnet run --project src/DeviceBridge.App

# Python engine
python3 -m venv .venv
. .venv/bin/activate
pip install -r engine/requirements.txt
python engine/main.py

# Tests
dotnet test
pytest tests/python
```

## License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <strong>DeviceBridge</strong>
  <br>
  <sub>One place for your Android diagnostics.</sub>
</p>
