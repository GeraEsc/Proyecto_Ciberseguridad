import subprocess
import pandas as pd
import os
from datetime import datetime

def run_incident_collector():
    print(f"[{datetime.now()}] Iniciando recolección de datos de red...")
    
    try:
        # Ejecuta comando de sistema para ver conexiones activas
        raw_data = subprocess.check_output("netstat -ano", shell=True).decode('latin-1')
        
        # Simulación de parseo y guardado en CSV para análisis posterior
        # En un escenario real, aquí filtrarías IPs sospechosas
        log_entry = {
            "timestamp": [datetime.now()],
            "source_tool": ["Cortex XDR Simulation"],
            "event_type": ["Network Connection Audit"],
            "status": ["Manual Review Required"]
        }
        
        df = pd.DataFrame(log_entry)
        file_path = 'data/security_logs.csv'
        
        # Guardar sin borrar lo anterior
        df.to_csv(file_path, mode='a', index=False, header=not os.path.exists(file_path))
        print(f"Éxito: Datos almacenados en {file_path}")
        
    except Exception as e:
        print(f"Error al recolectar datos: {e}")

if __name__ == "__main__":
    run_incident_collector()