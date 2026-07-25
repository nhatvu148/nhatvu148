"""Fail if requirements.txt and uv.lock disagree on any pinned version.

The repo installs dependencies two different ways: `uv run main.py` resolves
from uv.lock, while the pip paths read requirements.txt. Dependabot bumps them
independently, so the two can drift and leave one path running an older
version than the other reports.
"""

import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PIN = re.compile(r"^([A-Za-z0-9._-]+)==([^\s;#]+)")


def requirement_pins() -> dict[str, str]:
    pins = {}
    for raw in (ROOT / "requirements.txt").read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith(("#", "-")):
            continue
        if match := PIN.match(line):
            name, version = match.groups()
            pins[name.lower().replace("_", "-")] = version
    return pins


def locked_versions() -> dict[str, str]:
    lock = tomllib.loads((ROOT / "uv.lock").read_text())
    return {
        pkg["name"].lower().replace("_", "-"): pkg["version"]
        for pkg in lock.get("package", [])
        if "version" in pkg
    }


def main() -> int:
    pins = requirement_pins()
    locked = locked_versions()

    missing = sorted(set(pins) - set(locked))
    mismatched = sorted(
        (name, pins[name], locked[name])
        for name in set(pins) & set(locked)
        if pins[name] != locked[name]
    )

    for name, want, got in mismatched:
        print(f"::error::{name}: requirements.txt pins {want}, uv.lock has {got}")
    for name in missing:
        print(f"::error::{name} is pinned in requirements.txt but absent from uv.lock")

    if mismatched or missing:
        print(
            f"\n{len(mismatched) + len(missing)} manifest disagreement(s). "
            "Run `uv lock --upgrade-package <name>` so both agree."
        )
        return 1

    print(f"{len(pins)} pinned package(s) agree with uv.lock")
    return 0


if __name__ == "__main__":
    sys.exit(main())
