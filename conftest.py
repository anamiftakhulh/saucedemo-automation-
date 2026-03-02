import pytest
from utils.driver_factory import get_driver
from utils.logger import get_logger
from utils.screenshot import take_screenshot


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs["driver"]
        take_screenshot(driver, item.name)
