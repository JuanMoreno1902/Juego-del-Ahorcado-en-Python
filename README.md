# 🕹 Juego del Ahorcado en Python (Consola)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Mode](https://img.shields.io/badge/Mode-CLI-lightgrey)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

Implementación del clásico juego del **Ahorcado** desarrollada en Python, ejecutada completamente en consola (CLI).

---

## 📌 Descripción del Proyecto

Este proyecto consiste en una versión funcional del juego del ahorcado donde el usuario debe adivinar una palabra secreta letra por letra antes de quedarse sin vidas.

El programa:

- Selecciona aleatoriamente una palabra desde una lista interna
- Muestra la palabra oculta utilizando guiones bajos `_`
- Permite ingresar una letra por turno
- Valida entradas incorrectas
- Controla letras repetidas
- Lleva un conteo de vidas
- Finaliza cuando el jugador gana o pierde

El juego se ejecuta completamente en consola, sin interfaz gráfica.

---

## 🧠 Lógica Implementada

El sistema utiliza:

- Funciones
- Listas para almacenar letras correctas e incorrectas
- Bucle `while` para controlar el flujo del juego
- Validación de entradas del usuario
- Condicionales para determinar el estado del juego
- Módulo `random` para selección aleatoria de palabras

---

## ⚙️ Tecnologías Utilizadas

- **Lenguaje:** Python 3
- **Entorno:** Consola (CLI)
- **Librería estándar:** `random`

---

## ▶ Cómo Ejecutarlo

1️⃣ Clona el repositorio:

```bash
git clone https://github.com/JuanMoreno1902/juego-del-ahorcado-en-python.git
