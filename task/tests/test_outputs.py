import json
from pathlib import Path


def test_report_exists():
    """The agent produced a non-empty report file."""
    assert Path("/app/report.json").exists(), "no report.json found"
    assert Path("/app/report.json").stat().st_size > 0, "report.json is empty"

def test_total_requests():
    """The agent correctly counted the total number of requests."""
    report = Path("/app/report.json")

    with report.open("r", encoding="utf-8") as f:
        data = json.load(f)

    assert data["total_requests"] == 6, "incorrect total_requests count"

def test_unique_ips():
    """The agent correctly identified the total number of unique ip addresses."""
    report = Path("/app/report.json")

    with report.open("r", encoding="utf-8") as f:
        data = json.load(f)

    assert data["unique_ips"] == 3, "incorrect unique_ips count"

def test_top_path():
    """The agent correctly identified the path to the most visited page."""
    report = Path("/app/report.json")

    with report.open("r", encoding="utf-8") as f:
        data = json.load(f)

    assert data["top_path"] == "/index.html", "incorrect top_path identified"
