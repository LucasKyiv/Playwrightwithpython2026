from playwright.sync_api import expect

def test_google_search(page):
    page.goto('https://www.google.com/ncr')
    print(page.url)
    page.locator("//div[text()='Accept all']").click()
    page.locator("text=Gmail").click()
    print(page.url)
    # navigating back
    page.go_back()
    print(page.url)
    # navigating forward
    page.go_forward()
    print(page.url)
    page.go_back()
    expected_final_page_url = 'https://www.google.com/'
    expect(page).to_have_url(expected_final_page_url)