import sqlite3

def verificar_citas_2025():
    conn = sqlite3.connect('clinica.db')
    cursor = conn.cursor()
    
    # Verificar citas de 2024 (deberían estar eliminadas)
    cursor.execute('SELECT COUNT(*) FROM citas WHERE fecha LIKE "2024-08%"')
    citas_2024 = cursor.fetchone()[0]
    print(f"📊 Citas de agosto 2024: {citas_2024} (deberían ser 0)")
    
    # Verificar citas de 2025
    cursor.execute('SELECT COUNT(*) FROM citas WHERE fecha LIKE "2025-08%"')
    citas_2025 = cursor.fetchone()[0]
    print(f"📊 Citas de agosto 2025: {citas_2025}")
    
    if citas_2025 > 0:
        print("\n📋 Primeras 10 citas de agosto de 2025:")
        print("-" * 60)
        cursor.execute('''
            SELECT fecha, hora, nombre, motivo, estado 
            FROM citas 
            WHERE fecha LIKE "2025-08%" 
            ORDER BY fecha, hora 
            LIMIT 10
        ''')
        
        for fecha, hora, nombre, motivo, estado in cursor.fetchall():
            print(f"{fecha} {hora} | {nombre[:20]}... | {motivo} | {estado}")
    else:
        print("\n❌ No se encontraron citas para agosto de 2025")
        print("Ejecutando generación manual...")
        
        # Generar citas manualmente
        from datetime import datetime
        import random
        
        pacientes = [
            {"nombre": "María González López", "email": "maria.gonzalez@email.com", "telefono": "612345678"},
            {"nombre": "Carlos Rodríguez Martín", "email": "carlos.rodriguez@email.com", "telefono": "623456789"},
            {"nombre": "Ana Fernández Jiménez", "email": "ana.fernandez@email.com", "telefono": "634567890"}
        ]
        
        tratamientos = ["Limpieza Dental", "Empaste Dental", "Ortodoncia"]
        horarios = ["09:00", "10:00", "11:00", "16:00", "17:00"]
        
        # Generar algunas citas de prueba
        for dia in range(1, 6):  # Solo primeros 5 días
            fecha = f"2025-08-{dia:02d}"
            for i, hora in enumerate(horarios[:3]):
                paciente = random.choice(pacientes)
                tratamiento = random.choice(tratamientos)
                estado = random.choice(["pendiente", "confirmada"])
                
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
        
        conn.commit()
        print("✅ Se han generado citas de prueba para agosto de 2025")
    
    conn.close()

if __name__ == "__main__":
    verificar_citas_2025() 