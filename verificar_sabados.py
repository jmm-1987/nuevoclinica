import sqlite3
from datetime import datetime

def verificar_sabados():
    conn = sqlite3.connect('clinica.db')
    cursor = conn.cursor()
    
    # Obtener citas de sábados en agosto 2025
    cursor.execute('''
        SELECT fecha, hora, nombre, motivo, estado 
        FROM citas 
        WHERE fecha LIKE "2025-08%" 
        AND strftime('%w', fecha) = '6'
        ORDER BY fecha, hora
    ''')
    sabados = cursor.fetchall()
    
    print(f"📊 Citas de sábado en agosto 2025: {len(sabados)}")
    
    if sabados:
        print("\n📅 Citas por sábado:")
        sabados_por_fecha = {}
        for cita in sabados:
            fecha = cita[0]
            if fecha not in sabados_por_fecha:
                sabados_por_fecha[fecha] = []
            sabados_por_fecha[fecha].append(cita)
        
        for fecha, citas in sabados_por_fecha.items():
            print(f"  {fecha}: {len(citas)} citas")
            for cita in citas:
                print(f"    - {cita[1]} | {cita[2]} | {cita[3]}")
    else:
        print("❌ No hay citas en sábados")
    
    conn.close()

if __name__ == "__main__":
    verificar_sabados() 