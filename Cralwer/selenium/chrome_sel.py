from selenium import webdriver

prefs = {
    "profile.managed_default_content_settings.images":2
}
chrome_options  = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(options=chrome_options)
browser.get("https://naver.com")
input()