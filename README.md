# Registro Robusto de Ventas

## Objetivo

El objetivo de este proyecto es desarrollar un programa en Python que permita registrar una venta solicitando el precio unitario de un producto y la cantidad vendida.

El programa calcula el total de la venta y maneja de manera controlada las entradas inválidas mediante excepciones.

## Tecnologías utilizadas

* Python
* Colorama

## Crear el entorno virtual

Desde la carpeta del proyecto:

```bash
python -m venv .venv
```

## Activar el entorno virtual

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

En Windows CMD:

```cmd
.venv\Scripts\activate
```

## Instalar las dependencias

Con el entorno virtual activado:

```bash
pip install -r requirements.txt
```

## Ejecutar el programa

```bash
python registrar_venta.py
```

## Situaciones inválidas contempladas

El programa controla las siguientes situaciones:

* Precio que no puede convertirse a `float`.
* Cantidad que no puede convertirse a `int`.
* Precio negativo.
* Cantidad igual a cero.
* Cantidad negativa.

También contempla una venta válida.

## Manejo de excepciones

El programa utiliza:

* `try` para ejecutar las operaciones que pueden producir errores.
* `except ValueError` para capturar errores de conversión y validación.
* `else` para mostrar la venta registrada cuando no ocurrió ningún error.
* `finally` para informar que la operación finalizó.

## Biblioteca utilizada

Se instaló `colorama`, una biblioteca que permite trabajar con colores en la terminal.

## Estructura del proyecto

```text
registro_robusto_ventas/
│
├── registrar_venta.py
├── requirements.txt
├── README.md
└── .gitignore
```

La carpeta `.venv` se utiliza localmente y no se sube al repositorio de GitHub.
