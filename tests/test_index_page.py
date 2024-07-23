import pytest
import pages
#import time


class TestFooter:

    def test_user_should_be_able_to_open_popup_select_subscription_plan(self, page):
        pages.index_page.open_index_page(page)
#        time.sleep(10)
        actual_result = pages.index_page.get_text_from_nachat_perechod_button(page)
        assert actual_result == 'Переход в билайн со своим номером', 'Название кнопки не корректно'



