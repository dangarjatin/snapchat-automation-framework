import pytest
import allure

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Set the directory for Allure reports
    config.option.allure_report_dir = 'sanpchat_login/tests/reports/allure-results'