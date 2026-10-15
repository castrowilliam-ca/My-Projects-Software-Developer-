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

def hacer_ping(ip_o_dominio):
    parametro = "-n" if platform.system().lower() == "windows" else "-c"
    comando = ["ping", parametro, "1", ip_o_dominio]

    resultado = subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return resultado.returncode == 0

def escanear_puerto(ip, puerto):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.8)
    resultado = sock.connect_ex((ip, puerto))
    sock.close()
    return resultado == 0