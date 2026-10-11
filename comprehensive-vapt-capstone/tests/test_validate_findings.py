import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_findings.py"
SAMPLE = ROOT / "findings" / "findings.json"

class ValidationTests(unittest.TestCase):
    def test_sample_data_is_valid(self):
        result = subprocess.run([sys.executable, str(SCRIPT), str(SAMPLE)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_duplicate_ids_are_rejected(self):
        data = json.loads(SAMPLE.read_text())
        data[1]["id"] = data[0]["id"]
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            json.dump(data, f)
            name = f.name
        try:
            result = subprocess.run([sys.executable, str(SCRIPT), name], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
        finally:
            Path(name).unlink(missing_ok=True)

if __name__ == "__main__":
    unittest.main()
