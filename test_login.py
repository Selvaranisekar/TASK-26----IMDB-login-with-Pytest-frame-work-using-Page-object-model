from pytestimdb.utilities.selenium_util import search_title_name, save_screenshot


def test_login(browser):
    browser.get("https://www.imdb.com/search/title/")
    search_title_name(browser)
    save_screenshot(browser)

