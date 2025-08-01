import sqlite3
import random
from datetime import datetime

DATABASE = "clinica.db"

def generar_citas_2025():
    print("🦷 Generando citas para agosto de 2025...")
    
    # Datos de pacientes
    pacientes = [
        {"nombre": "María González López", "email": "maria.gonzalez@email.com", "telefono": "612345678"},
        {"nombre": "Carlos Rodríguez Martín", "email": "carlos.rodriguez@email.com", "telefono": "623456789"},
        {"nombre": "Ana Fernández Jiménez", "email": "ana.fernandez@email.com", "telefono": "634567890"},
        {"nombre": "Luis Pérez García", "email": "luis.perez@email.com", "telefono": "645678901"},
        {"nombre": "Carmen Sánchez Ruiz", "email": "carmen.sanchez@email.com", "telefono": "656789012"}
    ]
    
    tratamientos = ["Limpieza Dental", "Empaste Dental", "Ortodoncia", "Implante Dental", "Blanqueamiento Dental"]
    horarios = ["09:00", "10:00", "11:00", "16:00", "17:00", "18:00"]
    estados = ["pendiente", "confirmada", "completada"]
    
    # Generar fechas de agosto 2025 (solo días laborables)
    fechas = []
    for dia in range(1, 32):
        fecha = datetime(2025, 8, dia)
        if fecha.weekday() < 5:  # Lunes a viernes
            fechas.append(fecha.strftime("%Y-%m-%d"))
    
    print(f"📅 Generando citas para {len(fechas)} días laborables...")
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    citas_generadas = 0
    
    for fecha in fechas:
        # 3-6 citas por día
        num_citas = random.randint(3, 6)
        
        for _ in range(num_citas):
            paciente = random.choice(pacientes)
            tratamiento = random.choice(tratamientos)
            hora = random.choice(horarios)
            estado = random.choice(estados)
            
            cursor.execute('''
                INSERT INTO citas (nombre, email, telefono, motivo, fecha, hora, estado)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                paciente["nombre"],
                paciente["email"],
                paciente["telefono"],
                tratamiento,
                fecha,
                hora,
                estado
            ))
            
            citas_generadas += 1
    
    conn.commit()
    conn.close()
    
    print(f"✅ Se han generado {citas_generadas} citas para agosto de 2025")
    
    # Verificar
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM citas WHERE fecha LIKE "2025-08%"')
    total = cursor.fetchone()[0]
    print(f"📊 Total verificado: {total} citas")
    
    # Mostrar algunas
    cursor.execute('''
        SELECT fecha, hora, nombre, motivo, estado 
        FROM citas 
        WHERE fecha LIKE "2025-08%" 
        ORDER BY fecha, hora 
        LIMIT 5
    ''')
    
    print("\n📋 Primeras 5 citas:")
    for fecha, hora, nombre, motivo, estado in cursor.fetchall():
        print(f"  {fecha} {hora} | {nombre[:15]}... | {motivo}")
    
    conn.close()

if __name__ == "__main__":
    generar_citas_2025() 