import sqlite3
from datetime import datetime, date

def test_vista_semanal():
    """Probar la carga de citas en la vista semanal"""
    try:
        conn = sqlite3.connect("clinica.db")
        cursor = conn.cursor()
        
        # Obtener todas las citas
        cursor.execute("SELECT * FROM citas ORDER BY fecha, hora")
        citas = cursor.fetchall()
        
        print(f"📊 Total de citas en la base de datos: {len(citas)}")
        
        # Mostrar las citas con su formato de fecha
        for cita in citas:
            id_cita, nombre, email, telefono, motivo, fecha, hora, estado = cita
            print(f"📅 Cita {id_cita}: {nombre} - {fecha} {hora} - {estado}")
            
            # Verificar si la fecha está en el formato correcto
            try:
                fecha_obj = datetime.strptime(fecha, "%Y-%m-%d")
                print(f"   ✅ Fecha válida: {fecha_obj.strftime('%d/%m/%Y')}")
            except ValueError:
                print(f"   ❌ Fecha inválida: {fecha}")
        
        # Simular la lógica de la vista semanal
        print("\n🔍 Simulando vista semanal:")
        
        # Obtener la fecha actual (o usar una fecha específica para pruebas)
        fecha_actual = date.today()
        print(f"📅 Fecha actual: {fecha_actual}")
        
        # Calcular el inicio de la semana (lunes)
        dia_semana = fecha_actual.weekday()  # 0=lunes, 6=domingo
        inicio_semana = fecha_actual.replace(day=fecha_actual.day - dia_semana)
        print(f"📅 Inicio de semana: {inicio_semana}")
        
        # Generar los 7 días de la semana
        dias_semana = []
        for i in range(7):
            dia = inicio_semana.replace(day=inicio_semana.day + i)
            dias_semana.append(dia)
            print(f"   📅 Día {i+1}: {dia.strftime('%A %d/%m/%Y')} ({dia.strftime('%Y-%m-%d')})")
            
            # Buscar citas para este día
            fecha_str = dia.strftime("%Y-%m-%d")
            citas_del_dia = [cita for cita in citas if cita[5] == fecha_str]
            print(f"      📋 Citas encontradas: {len(citas_del_dia)}")
            for cita in citas_del_dia:
                print(f"         - {cita[1]} ({cita[6]}) - {cita[7]}")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_vista_semanal()
