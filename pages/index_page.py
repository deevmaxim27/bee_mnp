from playwright.sync_api import Page
import config


class IndexPage:
    _BUTTON_NACHAT_PERECHOD = "//div//h1[@class='AIVQ3 o2F3Q b1Q9I']"

    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    def get_text_from_nachat_perechod_button(self, page: Page) -> None:
        return page.locator(self._BUTTON_NACHAT_PERECHOD).get_attribute('text')
