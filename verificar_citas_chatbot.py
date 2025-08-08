import sqlite3
from datetime import datetime, date

def verificar_citas_chatbot():
    """Verificar las citas creadas desde el chatbot"""
    try:
        conn = sqlite3.connect("clinica.db")
        cursor = conn.cursor()
        
        print("🔍 Verificando citas en la base de datos...")
        
        # Obtener todas las citas
        cursor.execute('SELECT * FROM citas ORDER BY fecha DESC, hora ASC')
        citas = cursor.fetchall()
        
        print(f"📋 Total de citas encontradas: {len(citas)}")
        
        if len(citas) == 0:
            print("❌ No hay citas en la base de datos")
            return
        
        print("\n📅 Citas ordenadas por fecha (más recientes primero):")
        print("-" * 80)
        
        for cita in citas:
            id_cita, nombre, email, telefono, motivo, fecha, hora, estado = cita
            
            # Formatear fecha para mostrar
            try:
                fecha_obj = datetime.strptime(fecha, '%Y-%m-%d')
                fecha_formateada = fecha_obj.strftime('%d/%m/%Y')
            except:
                fecha_formateada = fecha
            
            print(f"ID: {id_cita}")
            print(f"👤 Paciente: {nombre}")
            print(f"📧 Email: {email}")
            print(f"📞 Teléfono: {telefono}")
            print(f"📝 Motivo: {motivo}")
            print(f"📅 Fecha: {fecha_formateada} ({fecha})")
            print(f"🕐 Hora: {hora}")
            print(f"✅ Estado: {estado}")
            print("-" * 80)
        
        # Verificar citas de hoy
        hoy = date.today().strftime('%Y-%m-%d')
        cursor.execute('SELECT COUNT(*) FROM citas WHERE fecha = ?', (hoy,))
        citas_hoy = cursor.fetchone()[0]
        
        print(f"\n📅 Citas para hoy ({hoy}): {citas_hoy}")
        
        if citas_hoy > 0:
            cursor.execute('SELECT * FROM citas WHERE fecha = ? ORDER BY hora', (hoy,))
            citas_hoy_detalle = cursor.fetchall()
            
            print("Citas de hoy:")
            for cita in citas_hoy_detalle:
                id_cita, nombre, email, telefono, motivo, fecha, hora, estado = cita
                print(f"  - {hora}: {nombre} ({estado})")
        
        # Verificar citas de esta semana
        from datetime import timedelta
        inicio_semana = (date.today() - timedelta(days=date.today().weekday())).strftime('%Y-%m-%d')
        fin_semana = (date.today() + timedelta(days=6-date.today().weekday())).strftime('%Y-%m-%d')
        
        cursor.execute('SELECT COUNT(*) FROM citas WHERE fecha BETWEEN ? AND ?', (inicio_semana, fin_semana))
        citas_semana = cursor.fetchone()[0]
        
        print(f"\n📅 Citas de esta semana ({inicio_semana} a {fin_semana}): {citas_semana}")
        
        if citas_semana > 0:
            cursor.execute('SELECT * FROM citas WHERE fecha BETWEEN ? AND ? ORDER BY fecha, hora', (inicio_semana, fin_semana))
            citas_semana_detalle = cursor.fetchall()
            
            print("Citas de esta semana:")
            for cita in citas_semana_detalle:
                id_cita, nombre, email, telefono, motivo, fecha, hora, estado = cita
                fecha_obj = datetime.strptime(fecha, '%Y-%m-%d')
                fecha_formateada = fecha_obj.strftime('%d/%m')
                print(f"  - {fecha_formateada} {hora}: {nombre} ({estado})")
        
        conn.close()
        
        print(f"\n💡 Para probar el panel:")
        print(f"   http://localhost:5000/panel")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def crear_cita_prueba_chatbot():
    """Crear una cita de prueba como lo haría el chatbot"""
    try:
        conn = sqlite3.connect("clinica.db")
        cursor = conn.cursor()
        
        # Datos de prueba
        nombre = "Paciente Prueba Chatbot"
        email = "prueba@chatbot.com"
        telefono = "600123456"
        motivo = "Revisión periódica"
        fecha = date.today().strftime('%Y-%m-%d')
        hora = "10:00"
        
        print(f"📝 Creando cita de prueba desde chatbot...")
        print(f"   👤 Paciente: {nombre}")
        print(f"   📅 Fecha: {fecha}")
        print(f"   🕐 Hora: {hora}")
        
        # Verificar si ya existe una cita en esa hora
        cursor.execute('SELECT COUNT(*) FROM citas WHERE fecha = ? AND hora = ?', (fecha, hora))
        existe = cursor.fetchone()[0]
        
        if existe > 0:
            print(f"⚠️ Ya existe una cita en {fecha} a las {hora}")
            # Cambiar hora
            hora = "11:00"
            print(f"🔄 Cambiando hora a: {hora}")
        
        # Insertar cita
        cursor.execute('''
            INSERT INTO citas (nombre, email, telefono, motivo, fecha, hora, estado)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (nombre, email, telefono, motivo, fecha, hora, 'pendiente'))
        
        conn.commit()
        conn.close()
        
        print(f"✅ Cita creada exitosamente")
        print(f"📅 Ahora puedes ir al panel y hacer clic en el día de hoy para ver la cita")
        
    except Exception as e:
        print(f"❌ Error al crear cita: {e}")

if __name__ == "__main__":
    print("🧪 Verificando citas del chatbot...")
    verificar_citas_chatbot()
    
    print("\n" + "="*50)
    print("¿Quieres crear una cita de prueba desde el chatbot? (s/n): ", end="")
    respuesta = input().lower()
    
    if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
        crear_cita_prueba_chatbot()
        print("\n" + "="*50)
        verificar_citas_chatbot()
