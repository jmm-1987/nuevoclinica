import sqlite3

def verificar_citas():
    try:
        conn = sqlite3.connect("clinica.db")
        cursor = conn.cursor()
        
        # Verificar si la tabla existe
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='citas'")
        if not cursor.fetchone():
            print("❌ La tabla 'citas' no existe")
            return
        
        # Contar total de citas
        cursor.execute("SELECT COUNT(*) FROM citas")
        total = cursor.fetchone()[0]
        print(f"📊 Total de citas en la base de datos: {total}")
        
        # Mostrar todas las citas
        cursor.execute("SELECT * FROM citas ORDER BY fecha, hora")
        citas = cursor.fetchall()
        
        if citas:
            print("\n📋 Citas encontradas:")
            for cita in citas:
                print(f"ID: {cita[0]}, Nombre: {cita[1]}, Fecha: {cita[5]}, Hora: {cita[6]}, Estado: {cita[7]}")
        else:
            print("❌ No hay citas en la base de datos")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    verificar_citas()

