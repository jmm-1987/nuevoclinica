import sqlite3

def verificar_citas_agosto():
    conn = sqlite3.connect('clinica.db')
    cursor = conn.cursor()
    
    # Contar total de citas en agosto
    cursor.execute('SELECT COUNT(*) FROM citas WHERE fecha LIKE "2024-08%"')
    total = cursor.fetchone()[0]
    print(f"📊 Total de citas en agosto: {total}")
    
    # Mostrar algunas citas de ejemplo
    cursor.execute('''
        SELECT fecha, hora, nombre, motivo, estado 
        FROM citas 
        WHERE fecha LIKE "2024-08%" 
        ORDER BY fecha, hora 
        LIMIT 10
    ''')
    
    print("\n📋 Primeras 10 citas de agosto:")
    print("-" * 60)
    for fecha, hora, nombre, motivo, estado in cursor.fetchall():
        print(f"{fecha} {hora} | {nombre[:20]}... | {motivo} | {estado}")
    
    conn.close()

if __name__ == "__main__":
    verificar_citas_agosto() 