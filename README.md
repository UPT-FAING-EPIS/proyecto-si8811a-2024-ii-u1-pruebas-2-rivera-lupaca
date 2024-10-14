[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/vK6WBQ1t)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=15560940)

# UNIVERSIDAD PRIVADA DE TACNA

## Facultad de Ingeniería

## Escuela profesional de Ingeniería de Sistemas

### Proyecto: Juegos Florales

### Pruebas de Aceptación/Interfaz

### Integrantes:

| ID  | Nombres      | Apellidos      | Código     |
| --- | ------------ | -------------- | ---------- |
| 1   | Jhonny       | Rivera Mendoza | 2020067144 |
| 2   | Ronal Daniel | Lupaca Mamani  | 20200671.. |

---

### Diagrama de ejecucion de pruebas local

```mermaid
graph TD
    A[VS Code - Ejecución de pruebas] -->|Código en Python| B[Pytest - Selenium]
    B -->|Conexión a Appium Server| C[Appium Server]
    C -->|Ejecución de pruebas en dispositivo| D[Dispositivo Android]
    B -->|Obtención de elementos| E[Appium Inspector]
    D -->|Resultados de pruebas| F[Allure Reporter]
    D -->|Grabación de video| G[Video de la prueba]
    F -->|Generación de reporte| H[Allure Serve]
    G --> I[Video disponible localmente]

    %% Estilos personalizados
    classDef background fill:#333,stroke:#FFF,stroke-width:2px,color:#FFF;
    classDef steps fill:#444,stroke:#FFF,stroke-width:2px,color:#FFF;

    %% Aplicación de estilos
    class A,B,C,D,E,F,G,H,I background;



```

### Diagrama de ejecucion de pruebas usando BrowserStack

```mermaid
graph TD
    A[VS Code - Ejecución de pruebas] -->|Envía pruebas| B[BrowserStack - Appium]
    B -->|Ejecución en dispositivo Android| C[Dispositivo Android]
    C -->|Resultados de pruebas| D[BrowserStack - Gestión de resultados]
    D -->|Gestión de reportes| E[BrowserStack Reporter]
    D -->|Videos de pruebas| F[BrowserStack - Videos]
    E --> G[Visualización de reportes]
    F --> H[Videos disponibles en BrowserStack]

    style A fill:#333,stroke:#FFF,stroke-width:2px,color:#FFF;
    style B fill:#333,stroke:#FFF,stroke-width:2px,color:#FFF;
    style C fill:#444,stroke:#FFF,stroke-width:2px,color:#FFF;
    style D fill:#444,stroke:#FFF,stroke-width:2px,color:#FFF;
    style E fill:#555,stroke:#FFF,stroke-width:2px,color:#FFF;
    style F fill:#555,stroke:#FFF,stroke-width:2px,color:#FFF;
    style G fill:#666,stroke:#FFF,stroke-width:2px,color:#FFF;
    style H fill:#666,stroke:#FFF,stroke-width:2px,color:#FFF;


```

### Diagrama del pipeline

```mermaid
graph TD
    A[Python SDK Test workflow] --> B[Push or Workflow Dispatch]
    B --> C[Job: comment-run]
    C --> D[Runs on Ubuntu Latest]
    D --> E[Step: Checkout Code]
    E --> F[Step: Setup Python]
    F --> G[Step: Install Dependencies]
    G --> H[Step: Run Tests in Parallel on Android]

    %% Estilos personalizados
    classDef background fill:#000,stroke:#FFF,stroke-width:2px,color:#FFF;
    classDef steps fill:#444,stroke:#FFF,stroke-width:2px,color:#FFF;

    %% Aplicación de estilos
    class A,B,C,D,E,F,G,H background;

```

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
