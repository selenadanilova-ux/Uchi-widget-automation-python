import pytest
from playwright.sync_api import expect, Page
from pages.widget_page import WidgetPage

@pytest.fixture(autouse=True)
def setup(page: Page):
    # Настройка перед каждым тестом
    page.goto("https://uchi.ru")
    
    # Закрытие кук, если они есть
    cookie_button = page.locator("._UCHI_COOKIE__button")
    if cookie_button.is_visible():
        cookie_button.click()
    
    yield

def test_widget_opens(page: Page):
    widget_page = WidgetPage(page)
    widget_page.open_widget()
    
    # Проверка видимости
    expect(widget_page.widget_body).to_be_visible()

def test_has_correct_title(page: Page):
    widget_page = WidgetPage(page)
    widget_page.open_widget()

    articles = widget_page.get_popular_articles()
    # Кликаем по первой статье (индексация в Python с 0)
    articles[0].click()

    widget_page.click_write_to_us()

    assert widget_page.get_title() == "Связь с поддержкой"

# ВАШ НОВЫЙ АВТОТЕСТ: Проверка поиска в виджете
def test_search_field_exists(page: Page):
    widget_page = WidgetPage(page)
    widget_page.open_widget()
    
    # Находим поле поиска (пример селектора)
    search_input = page.locator("input[placeholder*='поиск' i]")
    expect(search_input).to_be_visible()
