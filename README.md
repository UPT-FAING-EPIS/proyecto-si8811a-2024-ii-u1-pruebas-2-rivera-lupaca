# Pruebas a la interfaz de Login

### Reporte

Despliegue con github pages
https://upt-faing-epis.github.io/proyecto-si8811a-2024-ii-u1-pruebas-2-rivera-lupaca/#

## Preparando entorno de pruebas

Enlace a la configuracion:
https://github.com/UPT-FAING-EPIS/proyecto-si8811a-2024-ii-u1-pruebas-2-rivera-lupaca/issues/6

### Requerimientos

- Python
- Appium
- Appium Inspector
- Librerias: Selenium, pytest, allure-pytest, appium-python-client.
- Allure
- Vscode

### Comandos

Instalando las librerias:
Selenium:

```
pip install selenium
```

Para instalar Appium-python

```
pip install appium-Python-Client==2.0.0
```

Instalando allure-pytest

```
pip install allure-pytest
```

Instalando pytest

```
pip install pytest
```

## BrowserStack para pruebas automatizadas

### Clonamos la plantilla

```
git clone https://github.com/browserstack/pytest-appium-app-browserstack
cd pytest-appium-app-browserstack
```

### Creando entorno de trabajo venv

Dentro del repositorio de pruebas

```
python -m venv env
env\Scripts\activate
pip install -r requirements.txt

```

### Configuramos el browserstack.yml

```
userName: <TuUsuario>
accessKey: <TuAccessKey>
framework: pytest
app: bs://sample.app
platforms:
  - platformName: android
    deviceName: Samsung Galaxy S22 Ultra
    platformVersion: 12.0
  - platformName: android
    deviceName: Google Pixel 7 Pro
    platformVersion: 13.0
  - platformName: android
    deviceName: OnePlus 9
    platformVersion: 11.0
parallelsPerPlatform: 1
browserstackLocal: true
buildName: browserstack-build-1
projectName: BrowserStack Sample
```

### Ejecutamos la prueba

```
cd android
browserstack-sdk pytest -s bstack_sample.py
```

## Resultados

![alt text](/img/browser1.png)
![alt text](/img/browser2.png)
![alt text](/img/browser3.png)

## Imagenes

![alt text](/img/image.png)
![alt text](/img/image-2.png)
![alt text](/img/image-3.png)
![alt text](/img/image-1.png)
