import os
import json
import pytest

REPORT_PATH = "/app/report.json"

@pytest.fixture
def report_data():
    assert os.path.exists(REPORT_PATH), f"Expected report file missing at {REPORT_PATH}"
    with open(REPORT_PATH, "r") as f:
        return json.load(f)

def test_criterion_1_file_validity():
    """Verification of Success Criterion 1: The report file exists and is valid JSON."""
    assert os.path.exists(REPORT_PATH)
    with open(REPORT_PATH, "r") as f:
        data = json.load(f)
    assert isinstance(data, dict)
    assert "total_requests" in data
    assert "unique_ips" in data
    assert "top_path" in data

def test_criterion_2_total_requests(report_data):
    """Verification of Success Criterion 2: The total_requests value matches exact log count."""
    assert report_data["total_requests"] == 6

def test_criterion_3_unique_ips(report_data):
    """Verification of Success Criterion 3: The unique_ips value tracks unique IP records."""
    assert report_data["unique_ips"] == 3

def test_criterion_4_top_path(report_data):
    """Verification of Success Criterion 4: The top_path matches the most frequent endpoint."""
    assert report_data["top_path"] == "/index.html"
