import sqlite3
from datetime import datetime

def verificar_citas_por_fecha():
    """Verifica cuántas citas hay en cada fecha de agosto 2025"""
    conn = sqlite3.connect('clinica.db')
    cursor = conn.cursor()
    
    # Obtener todas las citas de agosto 2025
    cursor.execute('''
        SELECT fecha, COUNT(*) as total_citas
        FROM citas 
        WHERE fecha LIKE "2025-08%" 
        GROUP BY fecha
        ORDER BY fecha
    ''')
    resultados = cursor.fetchall()
    
    print("📊 Citas por fecha en agosto 2025:")
    print("=" * 50)
    
    total_citas = 0
    for fecha, count in resultados:
        print(f"📅 {fecha}: {count} citas")
        total_citas += count
    
    print("=" * 50)
    print(f"📊 Total de citas en agosto 2025: {total_citas}")
    
    # Verificar qué fechas tienen 8 o más citas (que serían excluidas del chatbot)
    fechas_ocupadas = [fecha for fecha, count in resultados if count >= 8]
    fechas_disponibles = [fecha for fecha, count in resultados if count < 8]
    
    print(f"\n🔴 Fechas con 8+ citas (ocupadas): {len(fechas_ocupadas)}")
    for fecha in fechas_ocupadas:
        count = next(count for f, count in resultados if f == fecha)
        print(f"  - {fecha}: {count} citas")
    
    print(f"\n🟢 Fechas con <8 citas (disponibles): {len(fechas_disponibles)}")
    for fecha in fechas_disponibles:
        count = next(count for f, count in resultados if f == fecha)
        print(f"  - {fecha}: {count} citas")
    
    conn.close()

if __name__ == "__main__":
    verificar_citas_por_fecha() 