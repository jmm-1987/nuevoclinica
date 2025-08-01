import sqlite3
from datetime import datetime

def verificar_citas_lunes():
    """Verifica las citas de los lunes en agosto de 2025"""
    
    conn = sqlite3.connect('clinica.db')
    cursor = conn.cursor()
    
    # Obtener todas las citas de agosto de 2025
    cursor.execute('''
        SELECT fecha, hora, nombre, motivo, estado 
        FROM citas 
        WHERE fecha LIKE "2025-08%" 
        ORDER BY fecha, hora
    ''')
    
    citas = cursor.fetchall()
    
    print(f"📊 Total de citas en agosto 2025: {len(citas)}")
    
    # Identificar los lunes de agosto 2025
    lunes_agosto = []
    for dia in range(1, 32):
        fecha = datetime(2025, 8, dia)
        if fecha.weekday() == 0:  # 0 = lunes
            lunes_agosto.append(fecha.strftime("%Y-%m-%d"))
    
    print(f"📅 Lunes en agosto 2025: {lunes_agosto}")
    
    # Contar citas por lunes
    citas_por_lunes = {}
    for fecha in lunes_agosto:
        citas_lunes = [cita for cita in citas if cita[0] == fecha]
        citas_por_lunes[fecha] = len(citas_lunes)
        print(f"  {fecha}: {len(citas_lunes)} citas")
    
    # Mostrar algunas citas de ejemplo de lunes
    print("\n📋 Ejemplos de citas de lunes:")
    for fecha in lunes_agosto:
        citas_lunes = [cita for cita in citas if cita[0] == fecha]
        if citas_lunes:
            print(f"\n{fecha} (Lunes):")
            for cita in citas_lunes[:3]:  # Mostrar solo las primeras 3
                print(f"  {cita[1]} | {cita[2][:20]}... | {cita[3]} | {cita[4]}")
    
    # Verificar que hay citas en los lunes
    total_citas_lunes = sum(citas_por_lunes.values())
    print(f"\n✅ Total de citas en lunes: {total_citas_lunes}")
    
    if total_citas_lunes > 0:
        print("✅ Las citas de lunes están presentes en la base de datos")
        print("🔍 Ahora puedes verificar en el panel que se muestran correctamente")
    else:
        print("❌ No hay citas en lunes - esto podría ser un problema")
    
    conn.close()

if __name__ == "__main__":
    print("🧪 Verificando citas de lunes en agosto 2025...")
    verificar_citas_lunes()
    print("\n🌐 Para verificar en el panel:")
    print("   http://localhost:5001/panel")
    print("   - Cambia a vista 'Mes'")
    print("   - Navega a agosto 2025")
    print("   - Verifica que los lunes muestran las citas correctamente") 