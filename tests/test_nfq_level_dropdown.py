from playwright.sync_api import Page, expect
from constants import NFQ_LEVELS, EQF_LEVELS, AWARD_CLASSES, SECTORS, AWARDING_BODIES


def test_nfq_level_dropdown_values(page: Page) -> None:
    page.goto("https://irq.ie/search/qualifications")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Allow all cookies").click()
    dropdown = page.get_by_label("NFQ Levels")
    dropdown.wait_for(state="visible")
    dropdown.click()

    options = page.get_by_role("option").all()
    values = [opt.text_content().strip() for opt in options if opt.text_content().strip()]

    assert values == NFQ_LEVELS, f"Actual values ({len(values)}): {values}"


def test_eqf_level_dropdown_values(page: Page) -> None:
    page.goto("https://irq.ie/search/qualifications")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Allow all cookies").click()

    dropdown = page.get_by_label("EQF Levels")
    dropdown.wait_for(state="visible")
    dropdown.click()

    options = page.get_by_role("option").all()
    values = [opt.text_content().strip() for opt in options if opt.text_content().strip()]

    assert values == EQF_LEVELS, f"Actual values ({len(values)}): {values}"


def test_award_class_dropdown_values(page: Page) -> None:
    page.goto("https://irq.ie/search/qualifications")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Allow all cookies").click()

    dropdown = page.get_by_label("Award Class")
    dropdown.wait_for(state="visible")
    dropdown.click()

    options = page.get_by_role("option").all()
    values = [opt.text_content().strip() for opt in options if opt.text_content().strip()]

    assert values == AWARD_CLASSES, f"Actual values ({len(values)}): {values}"


def test_sector_dropdown_values(page: Page) -> None:
    page.goto("https://irq.ie/search/qualifications")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Allow all cookies").click()

    dropdown = page.get_by_label("Sector")
    dropdown.wait_for(state="visible")
    dropdown.click()

    options = page.get_by_role("option").all()
    values = [opt.text_content().strip() for opt in options if opt.text_content().strip()]

    assert values == SECTORS, f"Actual values ({len(values)}): {values}"


def test_awarding_body_dropdown_values(page: Page) -> None:
    page.goto("https://irq.ie/search/qualifications")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Allow all cookies").click()

    dropdown = page.get_by_label("Awarding Body")
    dropdown.wait_for(state="visible")
    dropdown.click()

    options = page.get_by_role("option").all()
    values = [opt.text_content().strip() for opt in options if opt.text_content().strip()]

    assert values == AWARDING_BODIES, f"Actual values ({len(values)}): {values}"


def test_field_of_learning_typeahead_contains_arts(page: Page) -> None:
    page.goto("https://irq.ie/search/qualifications")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Allow all cookies").click()

    field = page.get_by_label("Field of learning")
    field.press_sequentially("a")

    expect(page.get_by_role("option", name="Arts and humanities")).to_be_visible()
