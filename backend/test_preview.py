"""Run with `python -m unittest test_preview`; no headset or provider calls."""
import os
import tempfile
import unittest
from unittest.mock import patch

from device_manager import DeviceManager
from session_manager import SessionManager


class PreviewTest(unittest.TestCase):
    def test_preview_never_attempts_physical_headset(self):
        with patch.dict(os.environ, {"VERCEL_ENV": "preview"}), patch.object(
            DeviceManager, "_connect_muse", side_effect=AssertionError("physical device attempted")
        ), patch.object(DeviceManager, "_connect_synthetic") as synthetic:
            DeviceManager()
        synthetic.assert_called_once()

    def test_preview_state_stays_in_temporary_storage(self):
        with tempfile.TemporaryDirectory() as directory, patch.dict(
            os.environ, {"VERCEL_ENV": "preview"}
        ), patch("session_manager.tempfile.gettempdir", return_value=directory):
            manager = SessionManager()
            self.assertEqual(manager.data_dir, os.path.join(directory, "studyamp-preview"))
            manager.save_sessions()
            self.assertTrue(os.path.isfile(manager.data_file))


if __name__ == "__main__":
    unittest.main()
