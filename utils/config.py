
class Config:
    BASE_URL = "file:///C:/Users/Malathy.Ranganathan/OneDrive - ZETES SA NV/AUTOMATION/pytest_fixtures/fixtures_practice.html"
    TIMEOUT = 10
    BROWSER = "CHROME"

    @staticmethod
    def get_browser():
        return Config.BROWSER

