import sqlite3
from datetime import datetime

def verificar_todas_citas():
    """Verifica todas las citas de agosto 2025"""
    conn = sqlite3.connect('clinica.db')
    cursor = conn.cursor()
    
    # Obtener todas las citas de agosto 2025
    cursor.execute('''
        SELECT fecha, hora, nombre, motivo, estado 
        FROM citas 
        WHERE fecha LIKE "2025-08%" 
        ORDER BY fecha, hora
    ''')
    citas = cursor.fetchall()
    
    print(f"📊 Total de citas en agosto 2025: {len(citas)}")
    
    # Agrupar por día de la semana
    citas_por_dia = {}
    for cita in citas:
        fecha = datetime.strptime(cita[0], '%Y-%m-%d')
        dia_semana = fecha.strftime('%A')  # Nombre del día
        if dia_semana not in citas_por_dia:
            citas_por_dia[dia_semana] = []
        citas_por_dia[dia_semana].append(cita)
    
    print("\n📅 Citas por día de la semana:")
    for dia, citas_dia in citas_por_dia.items():
        print(f"  {dia}: {len(citas_dia)} citas")
    
    # Verificar específicamente sábados
    sabados = [cita for cita in citas if datetime.strptime(cita[0], '%Y-%m-%d').weekday() == 5]
    print(f"\n🔄 Sábados en agosto 2025: {len(sabados)} citas")
    
    if sabados:
        print("📋 Ejemplos de citas de sábado:")
        for cita in sabados[:3]:
            print(f"  {cita[0]} | {cita[1]} | {cita[2][:20]}... | {cita[3]}")
    else:
        print("❌ No hay citas en sábados")
    
    # Verificar domingos
    domingos = [cita for cita in citas if datetime.strptime(cita[0], '%Y-%m-%d').weekday() == 6]
    print(f"\n🔄 Domingos en agosto 2025: {len(domingos)} citas")
    
    conn.close()

if __name__ == "__main__":
    print("🧪 Verificando todas las citas de agosto 2025...")
    verificar_todas_citas()
    print("\n🌐 Para verificar en el panel:")
    print("   http://localhost:5001/panel") 