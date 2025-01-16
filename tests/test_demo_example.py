def test_google_title(browser):
    browser.get("https://google.com")
    assert browser.title == "Google", "Тайтл страницы не такой как мы хотели"


def test_facebook_title(browser):
    browser.get("https://facebook.com")
    assert "Facebook" in browser.title, "Тайтл страницы не такой как мы хотели"
