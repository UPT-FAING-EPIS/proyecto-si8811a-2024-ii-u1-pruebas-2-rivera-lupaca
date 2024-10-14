import unittest
import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import base64
import time

@allure.feature("Inicio de sesión y Navegación a Eventos")
@allure.story("Iniciar sesión con Microsoft y navegar a varios eventos")
class LoginAndEventTest(unittest.TestCase):

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
        try:
            login_button = self.driver.find_element(By.XPATH, "//android.widget.Button[@content-desc='Iniciar sesión con Microsoft']")
            login_button.click()
            allure.attach("Botón presionado con éxito", name="Detalle del paso", attachment_type=allure.attachment_type.TEXT)
            print("Botón de inicio de sesión presionado con éxito.")
        except Exception as e:
            allure.attach(f"Error: {str(e)}", name="Error al presionar el botón", attachment_type=allure.attachment_type.TEXT)
            self.fail(f"Error localizando o presionando el botón de inicio de sesión: {e}")

        # Ingresar correo electrónico
        try:
            email_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@class='android.widget.EditText' and @index='0']"))
            )
            email_field.click()
            email_field.clear()
            email_field.send_keys('jhorivera@upt.pe')
            allure.attach("Correo electrónico ingresado", name="Correo electrónico", attachment_type=allure.attachment_type.TEXT)
            print("Correo electrónico ingresado con éxito.")
        except Exception as e:
            allure.attach(f"Error: {str(e)}", name="Error al ingresar el correo", attachment_type=allure.attachment_type.TEXT)
            self.fail(f"Error localizando o ingresando el correo electrónico: {e}")

        # Presionar el botón "Next"
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

        # Ingresar contraseña
        try:
            password_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@class='android.widget.EditText' and @index='0']"))
            )
            password_field.click()
            password_field.clear()
            password_field.send_keys('34b.j5a8')  # Reemplaza con la contraseña correspondiente
            allure.attach("Contraseña ingresada", name="Contraseña", attachment_type=allure.attachment_type.TEXT)
            print("Contraseña ingresada con éxito.")
        except Exception as e:
            allure.attach(f"Error: {str(e)}", name="Error al ingresar la contraseña", attachment_type=allure.attachment_type.TEXT)
            self.fail(f"Error localizando o ingresando la contraseña: {e}")

        # Presionar el botón "Sign in"
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

        # Verificar que se completó el inicio de sesión
        try:
            dashboard_element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Bienvenido, Jhonny RIVERA MENDOZA!']"))
            )
            allure.attach("Inicio de sesión completado con éxito", name="Estado de inicio de sesión", attachment_type=allure.attachment_type.TEXT)
            print("Inicio de sesión completado con éxito.")
        except Exception as e:
            allure.attach(f"Error: {str(e)}", name="Error durante la verificación del inicio de sesión", attachment_type=allure.attachment_type.TEXT)
            self.fail(f"Error verificando la carga del dashboard: {e}")

    @allure.step("Navegar a la sección de Eventos")
    def test_navigate_to_events(self):
        # Navegar a la sección de "Eventos"
        try:
            eventos_button = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Eventos']"))
            )
            eventos_button.click()
            allure.attach("Botón de 'Eventos' presionado con éxito", name="Detalle del paso", attachment_type=allure.attachment_type.TEXT)
            print("Botón de 'Eventos' presionado con éxito.")
            time.sleep(5)  # Espera para permitir la carga de la vista de eventos
        except Exception as e:
            allure.attach(f"Error: {str(e)}", name="Error al presionar el botón 'Eventos'", attachment_type=allure.attachment_type.TEXT)
            self.fail(f"Error localizando o presionando el botón 'Eventos': {e}")

        # Definir eventos y hacer clic en cada uno
        events = [
            ("Cuento", "//android.view.View[@content-desc='Cuento\n24/09/2024 - 24/09/2024\nFAING\nResultado: Aún por verse']"),
            ("Ortografia", "//android.view.View[@content-desc='Ortografia\n24/09/2024 - 24/09/2024\nFAEDCOH\nResultado: Aún por verse']"),
            ("Concurso de Tik Tok", "//android.view.View[@content-desc='Concurso de Tik Tok \"Viviendo y Comiendo Sano\"\n24/09/2024 - 24/09/2024\nResultado: Aún por verse']"),
            ("Miss y Mister Talento", "//android.view.View[@content-desc='Miss y Mister Talento\n24/09/2024 - 24/09/2024\nFAING\nResultado: Aún por verse']")
        ]

        for event_name, event_xpath in events:
            try:
                # Verifica si la lista de eventos ha vuelto a cargar antes de intentar hacer clic
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Eventos']"))
                )

                event_element = WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, event_xpath))
                )
                event_element.click()
                allure.attach(f"Evento '{event_name}' presionado con éxito", name="Detalle del paso", attachment_type=allure.attachment_type.TEXT)
                print(f"Evento '{event_name}' presionado con éxito.")
                time.sleep(2)
                self.driver.back()  # Volver a la lista de eventos

                # Espera hasta que la lista de eventos vuelva a cargarse después de regresar
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Eventos']"))
                )
            except Exception as e:
                allure.attach(f"Error: {str(e)}", name=f"Error al presionar el evento '{event_name}'", attachment_type=allure.attachment_type.TEXT)
                self.fail(f"Error localizando o presionando el evento '{event_name}': {e}")

    @classmethod
    def tearDownClass(cls):
        # Detener la grabación de pantalla después de la pausa
        video = cls.driver.stop_recording_screen()

        # Guardar el video como archivo .mp4
        with open("test_login.mp4", "wb") as video_file:
            video_file.write(base64.b64decode(video))

        # Finaliza la sesión
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
