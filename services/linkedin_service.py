from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from config import LINKEDIN_EMAIL, LINKEDIN_PASSWORD


class LinkedInService:
    def __init__(self, logger):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.maximize_window()
        self.logger = logger

    def login(self):
        """Log in to LinkedIn."""
        try:
            self.driver.get("https://www.linkedin.com/login")
            time.sleep(2)

            self.driver.find_element(By.ID, "username").send_keys(LINKEDIN_EMAIL)
            self.driver.find_element(By.ID, "password").send_keys(LINKEDIN_PASSWORD)
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

            time.sleep(3)

            if "feed" in self.driver.current_url:
                self.logger.info("Login successful.")
            else:
                self.logger.error("Login failed. Check your credentials.")
                self.driver.quit()
                exit()
        except Exception as e:
            self.logger.error(f"Error during login: {e}")
            self.driver.quit()
            exit()

    def check_url(self, url):
        """Check a URL for its status."""
        try:
            self.driver.get(url)
            time.sleep(2)

            if "Something went wrong" in self.driver.page_source:
                return "Unchecked"
            elif "Offer unavailable" in self.driver.page_source:
                return "Skipped"
            else:
                return "Valid"
        except Exception as e:
            self.logger.error(f"Error checking URL {url}: {e}")
            return "Error"

    def close(self):
        """Close the browser."""
        self.driver.quit()
