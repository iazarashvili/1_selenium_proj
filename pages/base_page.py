

class BasePage:
    def __init__(self, browser):
        self.browser = browser


    def element(self, args):
        return self.browser.find_element(*args)

    def type(self, text, selector):
        self.element(selector).send_keys(text)