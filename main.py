import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Example usage: python main.py "/usr/bin/chromedriver" "https://www.365scores.com/es/news/premios-365-scores-mejor-jugador/" "//iframe[@src='https://www.riddle.com/embed/a/aXXyEyed?lazyImages=true&staticHeight=false']" "//h3[normalize-space()='Camilo MD']" "//button[normalize-space()='Elegir']" "//p[contains(text(),'¡Gracias por votar! A seguir con las siguientes ca')]" 10

def click_radio_button(driver, frame_selector, radio_button_selector, choose_selector, check_selector, checked):
    try:
        frame = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, frame_selector))
        )

        print("- Frame loaded")

        driver.switch_to.frame(frame)

        radio_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, radio_button_selector))
        )

        radio_button.click()

        print("- Option selected")

        choose_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, choose_selector))
        )

        choose_button.click()

        print("- Voting...")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, check_selector))
        )

        print(f"- CHECKED: {checked}")
        return 1

    except Exception as e:
        print(f"- ERROR: {e}")
        print("- Continue...")
        return 0

    finally:
        # Close the browser window
        driver.refresh()
        print("- Refreshing...")

def main(chrome_driver_path, url, frame_selector, radio_button_selector, choose_selector, check_selector, max_attempts):
    service = webdriver.ChromeService(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get(url)

    attempts = 0
    checked = 1

    while attempts < int(max_attempts):
        i = click_radio_button(driver, frame_selector, radio_button_selector, choose_selector, check_selector, checked)
        checked += i
        attempts += 1

    driver.quit()

if __name__ == "__main__":
    if len(sys.argv) != 8:
        print("Usage: python script.py <chrome_driver_path> <url> <frame_selector> <radio_button_selector> <choose_selector> <check_selector> <max_attempts>")
        sys.exit(1)

    chrome_driver_path, url, frame_selector, radio_button_selector, choose_selector, check_selector, max_attempts = sys.argv[1:]

    main(chrome_driver_path, url, frame_selector, radio_button_selector, choose_selector, check_selector, max_attempts)
