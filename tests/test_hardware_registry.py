"""
Unit tests for hardware registry loader.
"""

import unittest
import os
from hardware_registry.loader import load_devices, load_payloads


class HardwareRegistryTests(unittest.TestCase):
    def test_load_devices_registers_esp32(self):
        reg = load_devices("hardware_registry/devices")
        esp = reg.get("esp32-devkit")
        self.assertIsNotNone(esp)
        # Check required fields exist in the loaded metadata
        for field in [
            "device_id",
            "device_type",
            "model",
            "manufacturer",
            "power",
            "interfaces",
        ]:
            self.assertIn(field, esp)

    def test_load_payloads_finds_metadata(self):
        payloads = load_payloads("hardware_registry/payloads")
        # There should be at least one payload collection for esp32
        self.assertTrue(any(p.get("device_id") == "esp32-devkit" for p in payloads))


if __name__ == "__main__":
    unittest.main()
