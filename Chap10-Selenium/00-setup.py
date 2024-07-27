from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
chrome_options = Options()


# Set up the Chrome WebDriver using webdriver-manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Navigate to the website
driver.get("https://www.python.org")

# Find elements on the page
upcoming_events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li")

# Extract and print the information
for event in upcoming_events:
    event_name = event.find_element(By.CSS_SELECTOR, "a").text
    event_date = event.find_element(By.CSS_SELECTOR, "time").text
    print(f"{event_date}: {event_name}")

# Close the browser
driver.quit()

