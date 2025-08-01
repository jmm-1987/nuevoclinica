import sqlite3

def check_citas():
    conn = sqlite3.connect('clinica.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM citas WHERE fecha LIKE "2025-08%"')
    total = cursor.fetchone()[0]
    print(f"Total citas agosto 2025: {total}")
    
    cursor.execute('SELECT fecha, COUNT(*) FROM citas WHERE fecha LIKE "2025-08%" GROUP BY fecha ORDER BY fecha')
    fechas = cursor.fetchall()
    
    print("\nCitas por fecha:")
    for fecha, count in fechas:
        print(f"  {fecha}: {count} citas")
    
    conn.close()

if __name__ == "__main__":
    check_citas() 