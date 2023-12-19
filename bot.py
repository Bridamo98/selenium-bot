from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.365scores.com/es/news/premios-365-scores-mejor-jugador/'
# Specify the path to the ChromeDriver executable
chrome_driver_path = '/usr/bin/chromedriver'
# Create a new instance of the Chrome driver
service = webdriver.ChromeService(executable_path = chrome_driver_path)
driver = webdriver.Chrome(service=service)
# Open the URL in the Chrome browser
driver.get(url)
frame_selector = "//iframe[@src='https://www.riddle.com/embed/a/aXXyEyed?lazyImages=true&staticHeight=false']"
radio_button_selector = "//h3[normalize-space()='Camilo MD']"
check_selector = "//p[contains(text(),'¡Gracias por votar! A seguir con las siguientes ca')]"



def click_radio_button():

    try:

        frame = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, frame_selector))
        )

        print(frame)

        driver.switch_to.frame(frame)


        radio_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, radio_button_selector))
        )

        print(radio_button)

        radio_button.click()
        radio_button.click()

        print(f"Clicked on radio button with selector: {radio_button_selector}")

        choose_selector = "//button[normalize-space()='Elegir']"

        choose_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, choose_selector))
        )

        print(choose_button)

        choose_button.click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, check_selector))
        )


    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the browser window
        driver.refresh()

# Example usage
i = 1
while i < 101:
    click_radio_button()

