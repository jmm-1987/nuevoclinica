import sqlite3
from datetime import datetime, date

def crear_cita_hoy():
    """Crear una cita de prueba para hoy"""
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
        
        # Crear una cita de prueba para hoy (fecha actual real)
        fecha_hoy = date.today().strftime("%Y-%m-%d")
        
        print(f"📅 Fecha actual: {fecha_hoy}")
        
        cursor.execute('''
            INSERT INTO citas (nombre, email, telefono, motivo, fecha, hora, estado)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', ("Paciente Prueba Hoy", "prueba@email.com", "612345678", "Revisión periódica", fecha_hoy, "10:00", "pendiente"))
        
        conn.commit()
        conn.close()
        
        print(f"✅ Cita de prueba creada para {fecha_hoy} a las 10:00")
        print(f"📅 Ahora puedes ir al panel y hacer clic en el día de hoy para ver la cita")
        
    except Exception as e:
        print(f"❌ Error al crear cita de prueba: {str(e)}")

if __name__ == "__main__":
    crear_cita_hoy()
