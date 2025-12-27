"""
Loader utility for hardware registry JSON descriptors.

This module provides functions to load JSON descriptor files from the
hardware_registry/devices and hardware_registry/payloads directories and
register them with the HardwareRegistry class defined in hardware_registry/registry.py.

Important safety notes:
- This module performs no hardware access.
- It only loads metadata and registers it in-memory.
- Files are validated for presence of required top-level fields.
"""

from typing import Dict, Any, List
import json
import os

from hardware_registry.registry import HardwareRegistry


REQUIRED_DEVICE_FIELDS = [
    "device_id",
    "device_type",
    "model",
    "manufacturer",
    "power",
    "interfaces",
    "gpio_pins",
    "supported_sensors",
    "supported_actuators",
    "flashing",
    "safety_constraints",
    "buy_links",
]


def _load_json_file(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_devices(directory: str = "hardware_registry/devices") -> HardwareRegistry:
    """
    Load all JSON device descriptors from `directory` and register them.

    Returns a populated HardwareRegistry instance.
    """
    registry = HardwareRegistry()
    if not os.path.isdir(directory):
        return registry

    for fname in sorted(os.listdir(directory)):
        if not fname.lower().endswith(".json"):
            continue
        path = os.path.join(directory, fname)
        try:
            meta = _load_json_file(path)
        except Exception:
            # Skip files that cannot be parsed
            continue

        # Basic validation
        if not all(k in meta for k in REQUIRED_DEVICE_FIELDS):
            # Skip invalid descriptors
            continue

        registry.register(meta["device_id"], meta)

    return registry


def load_payloads(directory: str = "hardware_registry/payloads") -> List[Dict[str, Any]]:
    """
    Load payload metadata JSON files from the given directory and return a list of payload collections.

    This returns a list of parsed JSON objects; it does not perform any registration or hardware operations.
    """
    payloads = []
    if not os.path.isdir(directory):
        return payloads

    for fname in sorted(os.listdir(directory)):
        if not fname.lower().endswith(".json"):
            continue
        path = os.path.join(directory, fname)
        try:
            meta = _load_json_file(path)
        except Exception:
            continue
        payloads.append(meta)

    return payloads
