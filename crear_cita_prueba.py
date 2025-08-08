import sqlite3
from datetime import datetime, date

def crear_cita_prueba():
    """Crear una cita de prueba para la fecha actual"""
    try:
        conn = sqlite3.connect("clinica.db")
        cursor = conn.cursor()
        
        # Crear tabla si no existe
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS citas (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                email TEXT,
                telefono TEXT,
                motivo TEXT,
                fecha TEXT,
                hora TEXT,
                estado TEXT DEFAULT 'pendiente'
            )
        ''')
        
        # Crear una cita de prueba para hoy
        fecha_hoy = date.today().strftime("%Y-%m-%d")
        
        print(f"📅 Creando cita de prueba para: {fecha_hoy}")
        
        cursor.execute('''
            INSERT INTO citas (nombre, email, telefono, motivo, fecha, hora, estado)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            "Paciente Prueba Vista Semanal",
            "prueba@email.com",
            "123456789",
            "Limpieza dental",
            fecha_hoy,
            "15:00",
            "pendiente"
        ))
        
        conn.commit()
        print("✅ Cita de prueba creada exitosamente")
        
        # Verificar que se creó correctamente
        cursor.execute("SELECT * FROM citas WHERE fecha = ?", (fecha_hoy,))
        citas_hoy = cursor.fetchall()
        print(f"📋 Citas para hoy ({fecha_hoy}): {len(citas_hoy)}")
        
        for cita in citas_hoy:
            print(f"   - {cita[1]} ({cita[6]}) - {cita[7]}")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    crear_cita_prueba()
