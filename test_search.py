from selene import browser, be, have


def test_succesfull_search(browser_1920_1080):
    browser.element('//*[@id="searchbox_input"]').should(be.blank).type('qa guru').press_enter()
    assert browser.element('//*[@id="react-layout"]').should(have.text('qa.guru'))


def test_unsuccesfull_search(browser_1920_1080):
    text_for_failed_search = 'ebrrtbrberefrwfewf'
    browser.element('//*[@id="searchbox_input"]').should(be.blank).type(text_for_failed_search).press_enter()
    assert (browser.element('//*[@id="react-layout"]').
            should(have.text(f'По запросу {text_for_failed_search} результаты не найдены.')))