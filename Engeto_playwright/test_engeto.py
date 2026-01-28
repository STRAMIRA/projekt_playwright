import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://engeto.cz/"


@pytest.fixture
def engeto_page(page: Page) -> Page:
    """Otevře hlavní stránku Engeto před každým testem"""
    page.goto(BASE_URL)
    return page


def test_engeto_title(engeto_page: Page):
    """Ověří, že stránka má správný title"""
    expect(engeto_page).to_have_title(
        "Kurzy programování a dalších IT technologií | ENGETO"
    )


def test_main_heading_visible(engeto_page: Page):
    """Ověří, že stránka má právě jeden hlavní nadpis (h1), který je viditelný"""
    heading = engeto_page.get_by_role("heading", level=1)

    expect(heading).to_have_count(1)
    expect(heading).to_be_visible()
    expect(heading).not_to_have_text("")


def test_contact_link_present(engeto_page: Page):
    """Ověří, že odkaz Kontakt je přítomný a viditelný"""
    contact_link = engeto_page.get_by_role(
        "link", name=r"kontakt", exact=False
    )

    expect(contact_link).to_have_count(1)
    expect(contact_link).to_be_visible()
