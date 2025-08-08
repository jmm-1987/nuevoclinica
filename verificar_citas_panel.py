import sqlite3
from datetime import datetime

def verificar_citas():
    """Verificar las citas en la base de datos"""
    try:
        conn = sqlite3.connect("clinica.db")
        cursor = conn.cursor()
        
        # Verificar si la tabla existe
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='citas'")
        if not cursor.fetchone():
            print("❌ La tabla 'citas' no existe")
            return
        
        # Obtener todas las citas
        cursor.execute("SELECT * FROM citas ORDER BY fecha, hora")
        citas = cursor.fetchall()
        
        print(f"📊 Total de citas en la base de datos: {len(citas)}")
        
        if len(citas) == 0:
            print("⚠️ No hay citas en la base de datos")
            print("💡 Para probar el panel, puedes crear citas usando el chatbot o el panel")
            return
        
        print("\n📋 Citas existentes:")
        for cita in citas:
            print(f"ID: {cita[0]}")
            print(f"  Nombre: {cita[1]}")
            print(f"  Email: {cita[2]}")
            print(f"  Teléfono: {cita[3]}")
            print(f"  Motivo: {cita[4]}")
            print(f"  Fecha: {cita[5]}")
            print(f"  Hora: {cita[6]}")
            print(f"  Estado: {cita[7]}")
            print("---")
        
        # Verificar citas por fecha
        cursor.execute("SELECT fecha, COUNT(*) FROM citas GROUP BY fecha ORDER BY fecha")
        citas_por_fecha = cursor.fetchall()
        
        print("\n📅 Citas por fecha:")
        for fecha, count in citas_por_fecha:
            print(f"  {fecha}: {count} cita(s)")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Error al verificar citas: {str(e)}")

def crear_cita_prueba():
    """Crear una cita de prueba para verificar el panel"""
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
        fecha_hoy = datetime.now().strftime("%Y-%m-%d")
        
        cursor.execute('''
            INSERT INTO citas (nombre, email, telefono, motivo, fecha, hora, estado)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', ("Paciente Prueba", "prueba@email.com", "612345678", "Revisión periódica", fecha_hoy, "10:00", "pendiente"))
        
        conn.commit()
        conn.close()
        
        print(f"✅ Cita de prueba creada para {fecha_hoy} a las 10:00")
        
    except Exception as e:
        print(f"❌ Error al crear cita de prueba: {str(e)}")

if __name__ == "__main__":
    print("🔍 Verificando citas en la base de datos...")
    verificar_citas()
    
    print("\n" + "="*50)
    print("¿Quieres crear una cita de prueba? (s/n): ", end="")
    respuesta = input().lower()
    
    if respuesta == 's':
        crear_cita_prueba()
        print("\n🔍 Verificando citas después de crear la de prueba...")
        verificar_citas()


