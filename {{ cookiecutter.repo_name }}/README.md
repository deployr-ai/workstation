{{cookiecutter.project_name}}
==============================

Este es el repositorio de {{cookiecutter.project_name}}.


Organización del proyecto
------------

    ├── LICENSE
    ├── README.md          <- Este readme.
    ├── artifacts          <- Repositorio de artefactos, como logs, transformadores, etc.
    ├── data
    │   ├── preprocessed   <- Data intermedia con algunas transformaciones.
    │   ├── stage          <- La data lista para ser utilizada en un modelo.
    │   └── raw            <- La data de origen, inmutable.
    │
    ├── docs               <- Proyecto default de Sphinx.
    │
    ├── models             <- Modelos listos.
    │
    ├── notebooks          <- Jupyter notebooks. Dejamos una convención sugerida:
    │                         iniciales-numero-descripcion corta. Ejemplo:
    │                         `he-1.0-eda-base-clientes`.
    │
    ├── references         <- Manuales de la data, documentación, todo lo relevante para trabajar.
    │
    ├── reports            <- Reportes en HTML, PDF, LaTeX, etc.
    │   └── figures        <- Carpeta para guardar imágenes de rápido acceso.
    │
    └── src                <- Código del proyecto.
    
    
Para ejecutar:
------------

Desde esta carpeta, ingresar el comando make workstation-up.

