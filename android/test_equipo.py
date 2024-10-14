import unittest
import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import base64
import time

@allure.feature("Inicio de sesión y Navegación de Equipos")
@allure.story("Iniciar sesión con Microsoft y navegar a Equipos y Team Prueba")
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

    @allure.step("Navegar a Equipos y abrir detalles del equipo A")
    def test_open_team_details(self):
        # 1. Presionar el botón "Equipos" para ir a la vista de equipos
        try:
            equipos_button = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Equipos']"))
            )
            equipos_button.click()
            allure.attach("Botón de 'Equipos' presionado con éxito", name="Detalle del paso", attachment_type=allure.attachment_type.TEXT)
            print("Botón de 'Equipos' presionado con éxito.")
            time.sleep(5)  # Dar tiempo para que la vista de equipos cargue
        except Exception as e:
            allure.attach(f"Error: {str(e)}", name="Error al presionar el botón 'Equipos'", attachment_type=allure.attachment_type.TEXT)
            self.fail(f"Error localizando o presionando el botón 'Equipos': {e}")

        # 2. Seleccionar el equipo "Equipo A"
        try:
            equipo_a_button = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc=\"Equipo A\nDetalles del equipo A\nParticipantes: 3\"]"))
            )
            equipo_a_button.click()
            allure.attach("Equipo 'A' seleccionado con éxito", name="Detalle del paso", attachment_type=allure.attachment_type.TEXT)
            print("Equipo 'A' seleccionado con éxito.")
            time.sleep(5)  # Dar tiempo para que cargue la vista de detalles del equipo
        except Exception as e:
            allure.attach(f"Error: {str(e)}", name="Error al seleccionar el equipo 'A'", attachment_type=allure.attachment_type.TEXT)
            self.fail(f"Error seleccionando el equipo 'A': {e}")

        # 3. Verificar los participantes del equipo A
        try:
            participante_juan = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Juan Pérez\nDetalles del participante']"))
            )
            self.assertTrue(participante_juan.is_displayed(), "El participante 'Juan Pérez' no fue encontrado.")
            allure.attach("Participante 'Juan Pérez' encontrado con éxito", name="Participante", attachment_type=allure.attachment_type.TEXT)
            print("Participante 'Juan Pérez' encontrado con éxito.")
        except Exception as e:
            allure.attach(f"Error: {str(e)}", name="Error verificando los participantes del equipo A", attachment_type=allure.attachment_type.TEXT)
            self.fail(f"Error verificando los participantes del equipo A: {e}")

        # 4. Presionar el botón "Cerrar"
        try:
            close_button = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Cerrar']"))
            )
            close_button.click()
            allure.attach("Botón 'Cerrar' presionado con éxito", name="Detalle del paso", attachment_type=allure.attachment_type.TEXT)
            print("Botón 'Cerrar' presionado con éxito.")
        except Exception as e:
            allure.attach(f"Error: {str(e)}", name="Error al presionar el botón 'Cerrar'", attachment_type=allure.attachment_type.TEXT)
            self.fail(f"Error localizando o presionando el botón 'Cerrar': {e}")

    @allure.step("Navegar a Team Prueba y verificar error al cargar participantes")
    def test_open_team_prueba_with_error(self):
        # 1. Presionar el botón "Equipos" para ir a la vista de equipos (reutilizando código)
        try:
            equipos_button = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Equipos']"))
            )
            equipos_button.click()
            allure.attach("Botón de 'Equipos' presionado con éxito", name="Detalle del paso", attachment_type=allure.attachment_type.TEXT)
            print("Botón de 'Equipos' presionado con éxito.")
            time.sleep(5)  # Dar tiempo para que la vista de equipos cargue
        except Exception as e:
            allure.attach(f"Error: {str(e)}", name="Error al presionar el botón 'Equipos'", attachment_type=allure.attachment_type.TEXT)
            self.fail(f"Error localizando o presionando el botón 'Equipos': {e}")

        # 2. Seleccionar el equipo "Team Prueba"
        try:
            team_prueba_button = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Team Prueba\nDetalles Prueba\nParticipantes: 1']"))
            )
            team_prueba_button.click()
            allure.attach("Equipo 'Team Prueba' seleccionado con éxito", name="Detalle del paso", attachment_type=allure.attachment_type.TEXT)
            print("Equipo 'Team Prueba' seleccionado con éxito.")
            time.sleep(5)  # Dar tiempo para que cargue la vista de detalles del equipo
        except Exception as e:
            allure.attach(f"Error: {str(e)}", name="Error seleccionando el equipo 'Team Prueba'", attachment_type=allure.attachment_type.TEXT)
            self.fail(f"Error seleccionando el equipo 'Team Prueba': {e}")

        # 3. Verificar si hay error al cargar los participantes
        try:
            error_message = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Error: Exception: Failed to load participantes']"))
            )
            self.assertTrue(error_message.is_displayed(), "No se encontró el mensaje de error al cargar los participantes.")
            allure.attach("Error mostrado correctamente", name="Error de participantes", attachment_type=allure.attachment_type.TEXT)
            print("Error al cargar los participantes mostrado correctamente.")
        except Exception as e:
            allure.attach(f"Error: {str(e)}", name="Error verificando el mensaje de error al cargar los participantes", attachment_type=allure.attachment_type.TEXT)
            self.fail(f"Error verificando el error al cargar los participantes: {e}")

        # 4. Presionar el botón "Cerrar"
        try:
            close_button = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@content-desc='Cerrar']"))
            )
            close_button.click()
            allure.attach("Botón 'Cerrar' presionado con éxito", name="Detalle del paso", attachment_type=allure.attachment_type.TEXT)
            print("Botón 'Cerrar' presionado con éxito.")
        except Exception as e:
            allure.attach(f"Error: {str(e)}", name="Error al presionar el botón 'Cerrar'", attachment_type=allure.attachment_type.TEXT)
            self.fail(f"Error localizando o presionando el botón 'Cerrar': {e}")

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
