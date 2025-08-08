import sqlite3
from datetime import datetime, timedelta

def agregar_citas_prueba():
    print("➕ AGREGANDO CITAS DE PRUEBA")
    print("=" * 40)
    
    try:
        conn = sqlite3.connect("clinica.db")
        cursor = conn.cursor()
        
        # Verificar si la tabla existe
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='citas'")
        if not cursor.fetchone():
            print("❌ La tabla 'citas' no existe. Creando...")
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
            conn.commit()
            print("✅ Tabla 'citas' creada")
        
        # Obtener fecha actual
        hoy = datetime.now()
        
        # Citas de prueba para los próximos días
        citas_prueba = [
            {
                'nombre': 'María García',
                'email': 'maria.garcia@email.com',
                'telefono': '612345678',
                'motivo': 'Revisión periódica',
                'fecha': (hoy + timedelta(days=1)).strftime('%Y-%m-%d'),
                'hora': '09:00',
                'estado': 'pendiente'
            },
            {
                'nombre': 'Juan López',
                'email': 'juan.lopez@email.com',
                'telefono': '623456789',
                'motivo': 'Limpieza Dental',
                'fecha': (hoy + timedelta(days=1)).strftime('%Y-%m-%d'),
                'hora': '10:30',
                'estado': 'confirmada'
            },
            {
                'nombre': 'Ana Martínez',
                'email': 'ana.martinez@email.com',
                'telefono': '634567890',
                'motivo': 'Empaste Dental',
                'fecha': (hoy + timedelta(days=2)).strftime('%Y-%m-%d'),
                'hora': '16:00',
                'estado': 'pendiente'
            },
            {
                'nombre': 'Carlos Rodríguez',
                'email': 'carlos.rodriguez@email.com',
                'telefono': '645678901',
                'motivo': 'Ortodoncia',
                'fecha': (hoy + timedelta(days=3)).strftime('%Y-%m-%d'),
                'hora': '11:00',
                'estado': 'confirmada'
            },
            {
                'nombre': 'Laura Sánchez',
                'email': 'laura.sanchez@email.com',
                'telefono': '656789012',
                'motivo': 'Blanqueamiento',
                'fecha': (hoy + timedelta(days=4)).strftime('%Y-%m-%d'),
                'hora': '17:30',
                'estado': 'pendiente'
            }
        ]
        
        # Insertar citas de prueba
        for cita in citas_prueba:
            cursor.execute('''
                INSERT INTO citas (nombre, email, telefono, motivo, fecha, hora, estado)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (cita['nombre'], cita['email'], cita['telefono'], 
                  cita['motivo'], cita['fecha'], cita['hora'], cita['estado']))
            print(f"✅ Cita agregada: {cita['nombre']} - {cita['fecha']} {cita['hora']}")
        
        conn.commit()
        conn.close()
        
        print(f"\n🎉 Se agregaron {len(citas_prueba)} citas de prueba")
        print("💡 Ahora puedes verificar el panel para ver las citas")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    agregar_citas_prueba()

