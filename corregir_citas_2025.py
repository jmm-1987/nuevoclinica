import sqlite3
import random
from datetime import datetime, timedelta

# Configuración de la base de datos
DATABASE = "clinica.db"

def eliminar_citas_2024():
    """Elimina todas las citas de agosto de 2024"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM citas WHERE fecha LIKE "2024-08%"')
    citas_eliminadas = cursor.rowcount
    
    conn.commit()
    conn.close()
    
    print(f"🗑️ Se han eliminado {citas_eliminadas} citas de agosto de 2024")
    return citas_eliminadas

def generar_citas_agosto_2025():
    """
    Genera citas reales para el mes de agosto de 2025
    Incluye diferentes tipos de tratamientos, horarios variados y estados diversos
    """
    
    # Datos de pacientes reales
    pacientes = [
        {"nombre": "María González López", "email": "maria.gonzalez@email.com", "telefono": "612345678"},
        {"nombre": "Carlos Rodríguez Martín", "email": "carlos.rodriguez@email.com", "telefono": "623456789"},
        {"nombre": "Ana Fernández Jiménez", "email": "ana.fernandez@email.com", "telefono": "634567890"},
        {"nombre": "Luis Pérez García", "email": "luis.perez@email.com", "telefono": "645678901"},
        {"nombre": "Carmen Sánchez Ruiz", "email": "carmen.sanchez@email.com", "telefono": "656789012"},
        {"nombre": "Javier Moreno Díaz", "email": "javier.moreno@email.com", "telefono": "667890123"},
        {"nombre": "Isabel Torres Vega", "email": "isabel.torres@email.com", "telefono": "678901234"},
        {"nombre": "Miguel Ángel Castro Luna", "email": "miguel.castro@email.com", "telefono": "689012345"},
        {"nombre": "Elena Morales Herrera", "email": "elena.morales@email.com", "telefono": "690123456"},
        {"nombre": "Roberto Silva Mendoza", "email": "roberto.silva@email.com", "telefono": "601234567"},
        {"nombre": "Patricia Vega Ortega", "email": "patricia.vega@email.com", "telefono": "612345678"},
        {"nombre": "Francisco Javier Ruiz", "email": "francisco.ruiz@email.com", "telefono": "623456789"},
        {"nombre": "Laura Mendoza Castro", "email": "laura.mendoza@email.com", "telefono": "634567890"},
        {"nombre": "Diego Herrera Silva", "email": "diego.herrera@email.com", "telefono": "645678901"},
        {"nombre": "Sofía Luna Morales", "email": "sofia.luna@email.com", "telefono": "656789012"}
    ]
    
    # Tipos de tratamientos disponibles
    tratamientos = [
        "Limpieza Dental",
        "Empaste Dental", 
        "Ortodoncia",
        "Implante Dental",
        "Blanqueamiento Dental",
        "Endodoncia",
        "Corona Dental",
        "Extracción Dental"
    ]
    
    # Horarios disponibles (solo días laborables)
    horarios = [
        "09:00", "09:30", "10:00", "10:30", "11:00", "11:30",
        "12:00", "12:30", "16:00", "16:30", "17:00", "17:30",
        "18:00", "18:30", "19:00", "19:30"
    ]
    
    # Estados posibles
    estados = ["pendiente", "confirmada", "completada", "cancelada"]
    
    # Generar fechas para agosto de 2025 (solo días laborables)
    fechas_agosto = []
    for dia in range(1, 32):  # Agosto tiene 31 días
        fecha = datetime(2025, 8, dia)
        # Solo incluir días laborables (lunes a viernes)
        if fecha.weekday() < 5:  # 0=Lunes, 4=Viernes
            fechas_agosto.append(fecha.strftime("%Y-%m-%d"))
    
    # Conectar a la base de datos
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Verificar si ya existen citas en agosto de 2025
    cursor.execute('SELECT COUNT(*) FROM citas WHERE fecha LIKE "2025-08%"')
    citas_existentes = cursor.fetchone()[0]
    
    if citas_existentes > 0:
        print(f"Ya existen {citas_existentes} citas en agosto de 2025.")
        conn.close()
        return
    
    # Generar citas
    citas_generadas = 0
    
    for fecha in fechas_agosto:
        # Generar entre 3 y 8 citas por día
        num_citas_dia = random.randint(3, 8)
        
        # Seleccionar horarios únicos para este día
        horarios_dia = random.sample(horarios, min(num_citas_dia, len(horarios)))
        
        for i in range(num_citas_dia):
            paciente = random.choice(pacientes)
            tratamiento = random.choice(tratamientos)
            hora = horarios_dia[i] if i < len(horarios_dia) else random.choice(horarios)
            estado = random.choices(estados, weights=[0.3, 0.4, 0.2, 0.1])[0]  # Más confirmadas que canceladas
            
            # Insertar cita
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
    
    # Confirmar cambios
    conn.commit()
    conn.close()
    
    print(f"✅ Se han generado {citas_generadas} citas para agosto de 2025")
    print(f"📅 Fechas con citas: {len(fechas_agosto)} días laborables")
    print(f"👥 Pacientes utilizados: {len(pacientes)}")
    print(f"🦷 Tratamientos incluidos: {len(tratamientos)} tipos")
    
    # Mostrar estadísticas por estado
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT estado, COUNT(*) 
        FROM citas 
        WHERE fecha LIKE "2025-08%" 
        GROUP BY estado
    ''')
    
    print("\n📊 Distribución por estado:")
    for estado, cantidad in cursor.fetchall():
        print(f"   • {estado.capitalize()}: {cantidad} citas")
    
    # Mostrar citas por tratamiento
    cursor.execute('''
        SELECT motivo, COUNT(*) 
        FROM citas 
        WHERE fecha LIKE "2025-08%" 
        GROUP BY motivo 
        ORDER BY COUNT(*) DESC
    ''')
    
    print("\n🦷 Citas por tratamiento:")
    for tratamiento, cantidad in cursor.fetchall():
        print(f"   • {tratamiento}: {cantidad} citas")
    
    conn.close()

def verificar_citas_2025():
    """Verifica las citas generadas para agosto de 2025"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Contar total de citas en agosto de 2025
    cursor.execute('SELECT COUNT(*) FROM citas WHERE fecha LIKE "2025-08%"')
    total = cursor.fetchone()[0]
    print(f"📊 Total de citas en agosto de 2025: {total}")
    
    # Mostrar algunas citas de ejemplo
    cursor.execute('''
        SELECT fecha, hora, nombre, motivo, estado 
        FROM citas 
        WHERE fecha LIKE "2025-08%" 
        ORDER BY fecha, hora 
        LIMIT 10
    ''')
    
    print("\n📋 Primeras 10 citas de agosto de 2025:")
    print("-" * 60)
    for fecha, hora, nombre, motivo, estado in cursor.fetchall():
        print(f"{fecha} {hora} | {nombre[:20]}... | {motivo} | {estado}")
    
    conn.close()

if __name__ == "__main__":
    print("🦷 Corrección de Citas - Agosto 2025")
    print("=" * 50)
    
    # Paso 1: Eliminar citas de 2024
    print("\n1️⃣ Eliminando citas de agosto de 2024...")
    citas_eliminadas = eliminar_citas_2024()
    
    # Paso 2: Generar citas para 2025
    print("\n2️⃣ Generando citas para agosto de 2025...")
    generar_citas_agosto_2025()
    
    # Paso 3: Verificar resultado
    print("\n3️⃣ Verificando resultado...")
    verificar_citas_2025()
    
    print("\n" + "=" * 50)
    print("✅ Proceso completado!")
    print("Ahora puedes acceder al panel de control en: http://localhost:5000/panel") 