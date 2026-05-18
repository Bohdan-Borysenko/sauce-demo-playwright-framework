import os
from datetime import datetime

def take_screenshot(page, test_name: str):
    """Takes a screenshot when the test fails"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    page.screenshot(path=f"{screenshot_dir}/{test_name}_{timestamp}.png")