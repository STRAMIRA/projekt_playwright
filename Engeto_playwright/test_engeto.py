import re
from playwright.sync_api import Page


def test_engeto_title(page: Page):
    """Ověří, že stránka má správný title"""
    page.goto("https://engeto.cz/")
    assert "engeto" in page.title().lower()


def test_engeto_header_visible(page: Page):
    """Ověří, že hlavní nadpis je viditelný"""
    page.goto("https://engeto.cz/")
    header = page.locator("h1")
    expect = header.is_visible()
    assert expect is True


def test_engeto_contact_button(page: Page):
    """Ověří, že existuje tlačítko Kontakt"""
    page.goto("https://engeto.cz/")
    contact_button = page.get_by_role("link", name=re.compile("kontakt", re.IGNORECASE))
    assert contact_button.first.is_visible()
