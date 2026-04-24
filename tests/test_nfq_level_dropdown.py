from playwright.sync_api import Page


def test_nfq_level_dropdown_values(page: Page) -> None:
    page.goto("https://irq.ie/search/qualifications")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Allow all cookies").click()
    dropdown = page.get_by_label("NFQ Levels")
    dropdown.wait_for(state="visible")
    dropdown.click()

    options = page.get_by_role("option").all()
    values = [opt.text_content().strip() for opt in options if opt.text_content().strip()]

    assert len(values) == 10, f"Expected 10 NFQ levels, got {len(values)}: {values}"
    assert values == [str(i) for i in range(1, 11)], f"Unexpected values: {values}"
