[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/vK6WBQ1t)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=15560940)
npx wdio config

# UNIVERSIDAD PRIVADA DE TACNA

## Facultad de Ingeniería

## Escuela profesional de Ingeniería de Sistemas

### Proyecto: Juegos Florales

### Pruebas de Aceptación/Interfaz

### Integrantes:

| ID  | Nombres | Apellidos      | Código     |
| --- | ------- | -------------- | ---------- |
| 1   | Jhonny  | Rivera Mendoza | 2020067144 |
| 2   | Ronal Daniel  | Lupaca Mamani  | 20200671.. |

---


### Diagrama de 

```mermaid
graph TD
    A[VS Code - Ejecución de pruebas] -->|Envía pruebas| B[BrowserStack - Appium]
    B -->|Ejecución en dispositivo Android| C[Dispositivo Android]
    C -->|Resultados de pruebas| D[BrowserStack - Gestión de resultados]
    D -->|Gestión de reportes| E[Allure Reporter]
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
