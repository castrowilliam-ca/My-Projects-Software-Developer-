from red_scanner import PUERTOS_RIESGO, hacer_ping, escanear_puerto

import tkinter as tk
from tkinter import ttk, messagebox
import threading
import socket
import subprocess
import platform

PUERTOS_RIESGO = {
    21: ("FTP", "Tráfico en texto plano. Alto riesgo de intecepción de contraseñas."),
    22: ("SSH", "Acceso remoto. Riesgo de fuerza bruta si no se bloquean reintentos."),
    23: ("Telnet", "Inseguro por diseño. Todo el tráfico viaja en texto plano."),
    80: ("HTTP", "Web sin cifrado SSL. Suceptible a espionaje en redes locales."),
    443: ("HTTPS", "Tráfico web cifrado. Generalmente seguro."),
    3389: ("RDP", "Escritorio Remoto de Wundows. Blanco habitual de ataques de fuerza bruta")
}