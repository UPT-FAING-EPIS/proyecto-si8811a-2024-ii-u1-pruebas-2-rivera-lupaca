import unittest
import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import base64
import time

@allure.feature("Inicio de sesión y Navegación a Coordinadores Docentes")
@allure.story("Iniciar sesión con Microsoft, Navegar a Coordinadores Docentes y seleccionar elementos")
class LoginAndCoordinadoresTest(unittest.TestCase):

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

        # 2. Ingresar correo electrónico
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

        # 6. Verificar que se completó el inicio de sesión
        try:
            dashboard_element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Bienvenido, Jhonny RIVERA MENDOZA!']"))
            )
            allure.attach("Inicio de sesión completado con éxito", name="Estado de inicio de sesión", attachment_type=allure.attachment_type.TEXT)
            print("Inicio de sesión completado con éxito.")
        except Exception as e:
            allure.attach(f"Error: {str(e)}", name="Error durante la verificación del inicio de sesión", attachment_type=allure.attachment_type.TEXT)
            self.fail(f"Error verificando la carga del dashboard: {e}")

        # 7. Navegar a la sección de "Coordinadores Docentes"
        try:
            coord_button = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Coordinadores Docentes']"))
            )
            coord_button.click()
            allure.attach("Botón 'Coordinadores Docentes' presionado con éxito", name="Detalle del paso", attachment_type=allure.attachment_type.TEXT)
            print("Botón 'Coordinadores Docentes' presionado con éxito.")
            time.sleep(5)  # Espera para permitir la carga de la vista de coordinadores
        except Exception as e:
            allure.attach(f"Error: {str(e)}", name="Error al presionar el botón 'Coordinadores Docentes'", attachment_type=allure.attachment_type.TEXT)
            self.fail(f"Error localizando o presionando el botón 'Coordinadores Docentes': {e}")

        # Definir elementos y hacer clic en cada uno
        coordinadores = [
            ("Baile Moderno", "//android.view.View[@content-desc='BAILE MODERNO']"),
            ("Baileton", "//android.view.View[@content-desc='BAILETON']"),
            ("Barra", "//android.view.View[@content-desc='BARRA']"),
            ("Canto Internacional", "//android.view.View[@content-desc='CANTO INTERNACIONAL']"),
            ("Canto Nacional", "//android.view.View[@content-desc='CANTO NACIONAL']"),
            ("Creacion Poetica", "//android.view.View[@content-desc='CREACION POETICA']"),
            ("Danzas Nacionales", "//android.view.View[@content-desc='DANZAS NACIONALES']"),
        ]

        for coord_name, coord_xpath in coordinadores:
            try:
                # Verifica si la lista de coordinadores ha cargado antes de intentar hacer clic
                coord_element = WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, coord_xpath))
                )
                coord_element.click()
                allure.attach(f"Elemento '{coord_name}' presionado con éxito", name="Detalle del paso", attachment_type=allure.attachment_type.TEXT)
                print(f"Elemento '{coord_name}' presionado con éxito.")
                time.sleep(2)
                self.driver.back()  # Volver a la lista de coordinadores

                # Espera hasta que la lista de coordinadores vuelva a cargarse después de regresar
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, "//android.view.View[@content-desc='Coordinadores Docentes']"))
                )
            except Exception as e:
                allure.attach(f"Error: {str(e)}", name=f"Error al presionar el elemento '{coord_name}'", attachment_type=allure.attachment_type.TEXT)
                self.fail(f"Error localizando o presionando el elemento '{coord_name}': {e}")

    @classmethod
    def tearDownClass(cls):
        # Detener la grabación de pantalla después de la pausa
        video = cls.driver.stop_recording_screen()

        # Guardar el video como archivo .mp4
        with open("test_coordinadores.mp4", "wb") as video_file:
            video_file.write(base64.b64decode(video))

        # Finaliza la sesión
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
