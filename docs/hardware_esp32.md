````markdown name=docs/hardware_esp32.md
```markdown
# ESP32 (ESP32-WROOM-32) Hardware Descriptor

This document is generated from hardware_registry/devices/esp32.json and
provides a human-readable summary of the metadata used by UAIR.

## Overview

- Device ID: esp32-devkit
- Model: ESP32-WROOM-32
- Manufacturer: Espressif Systems

## Power

- Voltage: 3.3 V
- Max current (recommended): 500 mA

## Interfaces

- GPIO, I2C, SPI, UART, WiFi, BLE

## GPIO (common, safe pins listed)

- GPIO2
- GPIO4
- GPIO5
- GPIO13
- GPIO14
- GPIO18
- GPIO19
- GPIO21
- GPIO22
- GPIO23

## Supported sensors

- i2c_temperature
- i2c_imu
- adc_analog

## Supported actuators

- gpio_led
- gpio_relay
- pwm_motor

## Flashing (metadata only)

- Method: serial (esptool)
- Tools: esptool.py, esp-idf (idf.py), platformio
- Notes: Flash over USB-serial using a compatible adapter and follow tool instructions for boot/erase/write.

## Safety constraints

- Recommended supply voltage: 3.3 V
- Min: 3.0 V
- Max: 3.6 V
- Max device current (recommended): 500 mA
- Recommended max GPIO pin current: 12 mA

## Payloads and injectors (metadata)

See `hardware_registry/payloads/esp32_payloads.json` for predefined payload templates and injector metadata. These are human-reviewable templates; UAIR will suggest them but will not execute flashing or any hardware actions without explicit human authorization.

```
````
