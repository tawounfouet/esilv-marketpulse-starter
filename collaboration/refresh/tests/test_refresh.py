#!/usr/bin/env python3
"""Tests smoke : contrat pédagogique des scripts de refresh.

Aucun clone, push, merge ni modification du dépôt d'équipe.
Les dépôts utilisés pour tester Git sont créés dans un répertoire temporaire.
"""
from __future__ import annotations

import ast
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[3]
SCRIPTS = ROOT / "collaboration" / "refresh" / "scripts"


class RefreshSmokeTests(unittest.TestCase):
    def run_script(self, filename: str, *args: str, env: dict | None = None) -> str:
        path = SCRIPTS / filename
        cmd = [sys.executable, str(path), *args] if path.suffix == ".py" else ["bash", str(path), *args]
        proc = subprocess.run(
            cmd, cwd=ROOT, capture_output=True, text=True, env=env, check=False
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + "\n" + proc.stderr)
        return proc.stdout

    def test_syntax_bash_and_python(self) -> None:
        for path in SCRIPTS.iterdir():
            if path.suffix == ".sh":
                proc = subprocess.run(["bash", "-n", str(path)], capture_output=True, text=True)
                self.assertEqual(proc.returncode, 0, f"{path.name}: {proc.stderr}")
            elif path.suffix == ".py":
                ast.parse(path.read_text(encoding="utf-8"), filename=str(path))

    def test_sample_data_real(self) -> None:
        output = self.run_script("02_python_csv_json.py")
        self.assertIn("AAPL - Apple Inc.", output)
        self.assertIn("SP500 - S&P 500", output)
        self.assertGreaterEqual(output.count("Observations : 21"), 2)
        self.assertIn("Premier close : 250.00", output)
        self.assertIn("Dernier close : 266.20", output)

    def test_git_labs_are_isolated(self) -> None:
        if shutil.which("git") is None:
            self.skipTest("Git indisponible")
        with tempfile.TemporaryDirectory(prefix="marketpulse-tests-") as tmp:
            env = dict(os.environ, TMPDIR=tmp)
            local = self.run_script("03_git_local_demo.sh", env=env)
            branches = self.run_script("04_git_branches_demo.sh", env=env)
            self.assertIn("STAGING AREA", local)
            self.assertIn("Merge pédagogique", branches)
            labs = list(Path(tmp).glob("marketpulse-td0*-*"))
            self.assertEqual(len(labs), 2)
            for lab in labs:
                self.assertTrue((lab / ".git").is_dir())
            self.assertTrue((ROOT / "src" / "main.py").is_file())

    def test_review_script_is_advisory_only(self) -> None:
        if shutil.which("git") is None:
            self.skipTest("Git indisponible")
        output = self.run_script(
            "06_review_preflight.py", "--issue", "12",
            "--developer", "alice", "--reviewer", "bob"
        )
        self.assertIn("NON validées sur GitHub", output)
        self.assertIn("Aucune PR, approbation, merge ou commit", output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
