import sqlite3
import random
from datetime import datetime, timedelta
import calendar

# Configuración de la base de datos
DATABASE = "clinica.db"

def generar_citas_agosto():
    """
    Genera citas reales para el mes de agosto de 2024
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
    
    # Generar fechas para agosto de 2024 (solo días laborables)
    fechas_agosto = []
    for dia in range(1, 32):  # Agosto tiene 31 días
        fecha = datetime(2024, 8, dia)
        # Solo incluir días laborables (lunes a viernes)
        if fecha.weekday() < 5:  # 0=Lunes, 4=Viernes
            fechas_agosto.append(fecha.strftime("%Y-%m-%d"))
    
    # Conectar a la base de datos
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Verificar si ya existen citas en agosto
    cursor.execute('SELECT COUNT(*) FROM citas WHERE fecha LIKE "2024-08%"')
    citas_existentes = cursor.fetchone()[0]
    
    if citas_existentes > 0:
        print(f"Ya existen {citas_existentes} citas en agosto. ¿Deseas continuar? (s/n): ", end="")
        respuesta = input().lower()
        if respuesta != 's':
            print("Operación cancelada.")
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
    
    print(f"✅ Se han generado {citas_generadas} citas para agosto de 2024")
    print(f"📅 Fechas con citas: {len(fechas_agosto)} días laborables")
    print(f"👥 Pacientes utilizados: {len(pacientes)}")
    print(f"🦷 Tratamientos incluidos: {len(tratamientos)} tipos")
    
    # Mostrar estadísticas por estado
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT estado, COUNT(*) 
        FROM citas 
        WHERE fecha LIKE "2024-08%" 
        GROUP BY estado
    ''')
    
    print("\n📊 Distribución por estado:")
    for estado, cantidad in cursor.fetchall():
        print(f"   • {estado.capitalize()}: {cantidad} citas")
    
    # Mostrar citas por tratamiento
    cursor.execute('''
        SELECT motivo, COUNT(*) 
        FROM citas 
        WHERE fecha LIKE "2024-08%" 
        GROUP BY motivo 
        ORDER BY COUNT(*) DESC
    ''')
    
    print("\n🦷 Citas por tratamiento:")
    for tratamiento, cantidad in cursor.fetchall():
        print(f"   • {tratamiento}: {cantidad} citas")
    
    conn.close()

def mostrar_citas_agosto():
    """
    Muestra las citas generadas para agosto
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT fecha, hora, nombre, motivo, estado 
        FROM citas 
        WHERE fecha LIKE "2024-08%" 
        ORDER BY fecha, hora
    ''')
    
    citas = cursor.fetchall()
    
    if not citas:
        print("No hay citas en agosto.")
        conn.close()
        return
    
    print(f"\n📋 Citas de agosto ({len(citas)} total):")
    print("-" * 80)
    
    fecha_actual = None
    for fecha, hora, nombre, motivo, estado in citas:
        if fecha != fecha_actual:
            fecha_actual = fecha
            fecha_obj = datetime.strptime(fecha, "%Y-%m-%d")
            dia_semana = fecha_obj.strftime("%A")
            print(f"\n📅 {fecha} ({dia_semana})")
            print("-" * 40)
        
        # Emoji según estado
        estado_emoji = {
            "pendiente": "⏳",
            "confirmada": "✅", 
            "completada": "🎉",
            "cancelada": "❌"
        }.get(estado, "❓")
        
        print(f"   {hora} | {estado_emoji} {nombre} | {motivo} | {estado}")
    
    conn.close()

if __name__ == "__main__":
    print("🦷 Generador de Citas para Agosto 2024")
    print("=" * 50)
    
    # Ejecutar directamente la generación de citas
    print("\nGenerando citas para agosto...")
    generar_citas_agosto()
    
    print("\n" + "=" * 50)
    print("✅ Proceso completado!")
    print("Ahora puedes acceder al panel de control en: http://localhost:5000/panel") 