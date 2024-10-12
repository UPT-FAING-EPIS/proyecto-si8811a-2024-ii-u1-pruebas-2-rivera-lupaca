import unittest
import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import time

@allure.feature("Inicio de sesión y Navegación en Ubicaciones")
@allure.story("Iniciar sesión con Microsoft y abrir ubicaciones en Google Maps")
class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Cargar las capacidades desde el archivo browserstack.yml
        with open("browserstack.yml", 'r') as stream:
            config = yaml.safe_load(stream)

        # Inicializa el driver con las Desired Capabilities
        cls.driver = webdriver.Remote("http://hub-cloud.browserstack.com/wd/hub", config)
        cls.driver.implicitly_wait(10)  # Tiempo de espera implícito

        # Inicia la grabación de pantalla
        cls.driver.start_recording_screen()

    @allure.step("Iniciar sesión con Microsoft")
    def test_login_with_microsoft(self):
        # 1. Presionar el botón "Iniciar sesión con Microsoft"
        try:
            login_button = self.driver.find_element(By.XPATH, "//android.widget.Button[@content-desc='Iniciar sesión con Microsoft']")
            login_button.click()
            allure.attach("Botón presionado con éxito", name="Detalle del paso", attachment_type=allure.attachment_type.TEXT)
            print("Botón de inicio de sesión presionado con éxito.")
        except Exception as e:
            allure.attach(f"Error: {str(e)}", name="Error al presionar el botón", attachment_type=allure.attachment_type.TEXT)
            self.fail(f"Error localizando o presionando el botón de inicio de sesión: {e}")

        # 2. Esperar a que el campo de correo esté presente y tenga foco
        try:
            email_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@class='android.widget.EditText' and @index='0']"))
            )
            email_field.click()  # Asegúrate de que el campo esté enfocado
            email_field.clear()  # Limpia el campo antes de enviar el texto
            email_field.send_keys('ronlupaca@upt.pe')  # Reemplaza con tu correo de prueba
            allure.attach("Correo electrónico ingresado con éxito", name="Correo electrónico", attachment_type=allure.attachment_type.TEXT)
            print("Correo electrónico ingresado con éxito.")
        except Exception as e:
            allure.attach(f"Error: {str(e)}", name="Error al ingresar el correo", attachment_type=allure.attachment_type.TEXT)
            self.fail(f"Error localizando o ingresando el correo electrónico: {e}")

        # 3. Presionar el botón "Next"
        try:
            next_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@text='Next']"))
            )
            next_button.click()
            allure.attach("Botón 'Next' presionado con éxito", name="Detalle del paso", attachment_type=allure.attachment_type.TEXT)
            print("Botón 'Next' presionado con éxito.")
        except Exception as e:
            allure.attach(f"Error: {str(e)}", name="Error al presionar 'Next'", attachment_type=allure.attachment_type.TEXT)
            self.fail(f"Error localizando o presionando el botón 'Next': {e}")

        # 4. Ingresar contraseña
        try:
            password_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@index='0']"))
            )
            password_field.click()
            password_field.send_keys('rD25091997_@')  # Reemplaza con tu contraseña
            allure.attach("Contraseña ingresada con éxito", name="Contraseña", attachment_type=allure.attachment_type.TEXT)
            print("Contraseña ingresada con éxito.")
        except Exception as e:
            allure.attach(f"Error: {str(e)}", name="Error al ingresar la contraseña", attachment_type=allure.attachment_type.TEXT)
            self.fail(f"Error localizando o ingresando la contraseña: {e}")

        # 5. Presionar el botón "Sign in"
        try:
            sign_in_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@text='Sign in']"))
            )
            sign_in_button.click()
            allure.attach("Botón 'Sign in' presionado con éxito", name="Detalle del paso", attachment_type=allure.attachment_type.TEXT)
            print("Botón 'Sign in' presionado con éxito.")
        except Exception as e:
            allure.attach(f"Error: {str(e)}", name="Error al presionar 'Sign in'", attachment_type=allure.attachment_type.TEXT)
            self.fail(f"Error localizando o presionando el botón 'Sign in': {e}")

        # 6. Esperar a que se complete el proceso de inicio de sesión
        time.sleep(5)

    @allure.step("Abrir ubicación en Google Maps")
    def test_open_location_in_google_maps(self):
        # 1. Presionar el botón "Ubicaciones" para ir a la vista de ubicaciones
        try:
            ubicaciones_button = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Ubicaciones']"))
            )
            ubicaciones_button.click()
            allure.attach("Botón de 'Ubicaciones' presionado con éxito", name="Detalle del paso", attachment_type=allure.attachment_type.TEXT)
            print("Botón de 'Ubicaciones' presionado con éxito.")
            time.sleep(5)  # Dar tiempo para que la vista de ubicaciones cargue
        except Exception as e:
            allure.attach(f"Error: {str(e)}", name="Error al presionar el botón 'Ubicaciones'", attachment_type=allure.attachment_type.TEXT)
            self.fail(f"Error localizando o presionando el botón 'Ubicaciones': {e}")

        # 2. Seleccionar la ubicación "Gimnasio UPT"
        try:
            gimnasio_upt_button = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc=\"Gimnasio UPT\nDirección ID: 005\nCapacidad: 800\nDescripción: Gimnasio para eventos deportivos y entrenamientos.\nToca para ver en Google Maps\"]"))
            )
            gimnasio_upt_button.click()
            allure.attach("Ubicación 'Gimnasio UPT' seleccionada con éxito", name="Detalle del paso", attachment_type=allure.attachment_type.TEXT)
            print("Ubicación 'Gimnasio UPT' seleccionada con éxito.")
            time.sleep(5)  # Dar tiempo para que cargue Google Maps
        except Exception as e:
            allure.attach(f"Error: {str(e)}", name="Error al seleccionar la ubicación 'Gimnasio UPT'", attachment_type=allure.attachment_type.TEXT)
            self.fail(f"Error seleccionando la ubicación 'Gimnasio UPT': {e}")

        # 3. Verificar que Google Maps se abrió correctamente
        try:
            google_maps_view = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Google Maps']"))
            )
            self.assertTrue(google_maps_view.is_displayed(), "Google Maps no se abrió correctamente.")
            allure.attach("Google Maps abierto correctamente", name="Detalle del paso", attachment_type=allure.attachment_type.TEXT)
            print("Google Maps abierto correctamente.")
        except Exception as e:
            self.driver.save_screenshot("google_maps_error.png")
            allure.attach.file("google_maps_error.png", name="Error de Google Maps", attachment_type=allure.attachment_type.PNG)
            self.fail(f"Error verificando la apertura de Google Maps: {e}")

    @classmethod
    def tearDownClass(cls):
        # Detener la grabación de pantalla después de la pausa
        video = cls.driver.stop_recording_screen()

        # Guardar el video como archivo .mp4
        with open("test_google_maps.mp4", "wb") as video_file:
            video_file.write(base64.b64decode(video))

        # Finaliza la sesión
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
