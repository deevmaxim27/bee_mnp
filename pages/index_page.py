from playwright.sync_api import Page
import config


class IndexPage:
    _BUTTON_NACHAT_PERECHOD = "/html/body/div[1]/div[2]/main/div/div[1]/div[2]/div/div/div[2]/div[2]/form/div/div[2]/button"

    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    def get_text_from_nachat_perechod_button(self, page: Page) -> None:
        return page.locator(self, _BUTTON_NACHAT_PERECHOD).get_attribute('class')
