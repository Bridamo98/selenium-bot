from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

windows_chrome_driver_path = 'C:\\Users\\briam\\Downloads\\chromedriver-win64\\chromedriver.exe'
linux_chrome_driver_path = '/usr/bin/chromedriver'
url = 'https://www.365scores.com/es/news/premios-365-scores-mejor-jugador/'
chrome_driver_path = windows_chrome_driver_path # change this
service = webdriver.ChromeService(executable_path = chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url)
frame_selector = "//iframe[@src='https://www.riddle.com/embed/a/aXXyEyed?lazyImages=true&staticHeight=false']"
radio_button_selector = "//h3[normalize-space()='Camilo MD']"
check_selector = "//p[contains(text(),'¡Gracias por votar! A seguir con las siguientes ca')]"
choose_selector = "//button[normalize-space()='Elegir']"
checked = 1
def click_radio_button():

    try:

        frame = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, frame_selector))
        )

        print("- Frame loaded")

        driver.switch_to.frame(frame)

        # sleep(1)

        radio_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, radio_button_selector))
        )

        # sleep(1)

        radio_button.click()

        print("- Option selected")

        choose_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, choose_selector))
        )

        # sleep(1)

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

attempts = 0
while attempts < 1000:
    i = click_radio_button()
    checked+=i
    attempts+=1

driver.quit()
