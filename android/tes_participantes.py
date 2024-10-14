import unittest
import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import time

@allure.feature("Inicio de sesión y Búsqueda de Participantes")
@allure.story("Iniciar sesión con Microsoft y buscar participantes")
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

    @allure.step("Buscar participante llamado Erick")
    def test_search_participant(self):
        try:
            # 1. Presionar el botón "Participantes"
            participantes_button = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Participantes']"))
            )
            participantes_button.click()
            allure.attach("Botón 'Participantes' presionado con éxito", name="Detalle del paso", attachment_type=allure.attachment_type.TEXT)
            print("Botón 'Participantes' presionado con éxito.")
            time.sleep(5)  # Esperar a que la vista de participantes cargue

            # 2. Buscar un participante llamado "Erick"
            search_field = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.EditText"))
            )
            search_field.click()
            search_field.send_keys("Erick")
            allure.attach("Búsqueda iniciada para 'Erick'", name="Búsqueda", attachment_type=allure.attachment_type.TEXT)
            print("Búsqueda de 'Erick' iniciada.")
            time.sleep(2)  # Dar tiempo para que se filtre la búsqueda

            # 3. Verificar que el participante "Erick Mamani" aparece en los resultados
            participante_erick = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//android.view.View[contains(@content-desc, 'Erick Mamani')]"))
            )
            if participante_erick.is_displayed():
                allure.attach("Participante 'Erick Mamani' encontrado con éxito", name="Participante", attachment_type=allure.attachment_type.TEXT)
                print("Participante 'Erick Mamani' encontrado con éxito.")
            else:
                self.fail("El participante 'Erick Mamani' no fue encontrado.")
        
        except Exception as e:
            allure.attach(f"Error: {str(e)}", name="Error en la búsqueda", attachment_type=allure.attachment_type.TEXT)
            self.fail(f"Error verificando los participantes en la búsqueda: {e}")

    @classmethod
    def tearDownClass(cls):
        # Detener la grabación de pantalla después de la pausa
        video = cls.driver.stop_recording_screen()

        # Guardar el video como archivo .mp4
        with open("test_search_participant.mp4", "wb") as video_file:
            video_file.write(base64.b64decode(video))

        # Finaliza la sesión
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
