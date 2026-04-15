from playwright.sync_api import Page, Locator

class WidgetPage:
    def __init__(self, page: Page):
        self.page = page
        # Локаторы
        self._wrapper = page.locator(".sc-dino-typography-h")
        self._widget_body = page.locator("[class^=widgetWrapper]")
        self._header_text = page.locator("header h5")
        self._button_open = page.locator("[data-test=openWidget]")
        self._button_write_to_us = page.locator("button[class^=btn]")
        self._popular_articles = page.locator("li[class^=articles__]")

    def open_widget(self):
        # Кнопка открытия обычно глобальная
        self._button_open.click()

    def get_popular_articles(self) -> list[Locator]:
        # Ждем появления элементов и возвращаем список
        self._popular_articles.first.wait_for()
        return self._popular_articles.all()

    def click_write_to_us(self):
        self._button_write_to_us.click()

    def get_title(self) -> str:
        return self._header_text.inner_text().strip()

    @property
    def widget_body(self) -> Locator:
        return self._widget_body
