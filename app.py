#!/usr/bin/env python3
"""Run the weather agent from the project root."""

import runpy
import sys
from pathlib import Path


source_dir = Path(__file__).parent / "src"
sys.path.insert(0, str(source_dir))
runpy.run_path(str(source_dir / "app.py"), run_name="__main__")
