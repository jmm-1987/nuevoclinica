import sqlite3
import random
from datetime import datetime

DATABASE = "clinica.db"

def agregar_citas_sabado():
    """Agrega citas de sábado para agosto 2025"""
    
    # Datos de pacientes para sábados
    pacientes_sabado = [
        "María González", "Carlos López", "Ana Martínez", "Luis Rodríguez",
        "Carmen Sánchez", "Javier Pérez", "Isabel Torres", "Miguel Ruiz",
        "Elena Jiménez", "Roberto Moreno", "Sofia Castro", "Diego Silva"
    ]
    
    # Tratamientos para sábados (más urgentes)
    tratamientos_sabado = [
        "Limpieza dental", "Empaste", "Revisión", "Blanqueamiento",
        "Extracción", "Endodoncia", "Ortodoncia"
    ]
    
    # Horarios de sábado (mañana)
    horarios_sabado = ["09:00", "09:30", "10:00", "10:30", "11:00", "11:30"]
    
    # Estados
    estados = ["pendiente", "confirmada"]
    
    # Sábados de agosto 2025
    sabados_agosto = [
        "2025-08-02", "2025-08-09", "2025-08-16", 
        "2025-08-23", "2025-08-30"
    ]
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    citas_agregadas = 0
    
    for fecha in sabados_agosto:
        # 2-3 citas por sábado
        num_citas = random.randint(2, 3)
        
        for i in range(num_citas):
            paciente = random.choice(pacientes_sabado)
            tratamiento = random.choice(tratamientos_sabado)
            hora = random.choice(horarios_sabado)
            estado = random.choice(estados)
            
            # Generar datos de contacto
            email = f"{paciente.lower().replace(' ', '.')}@email.com"
            telefono = f"6{random.randint(10000000, 99999999)}"
            
            cursor.execute('''
                INSERT INTO citas (nombre, email, telefono, motivo, fecha, hora, estado)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (paciente, email, telefono, tratamiento, fecha, hora, estado))
            
            citas_agregadas += 1
    
    conn.commit()
    conn.close()
    
    print(f"✅ Se agregaron {citas_agregadas} citas de sábado")
    print("📅 Sábados con citas:")
    for fecha in sabados_agosto:
        print(f"  - {fecha}")

if __name__ == "__main__":
    print("🦷 Agregando citas de sábado para agosto 2025...")
    agregar_citas_sabado()
    print("\n🌐 Verifica en el panel: http://localhost:5001/panel") 