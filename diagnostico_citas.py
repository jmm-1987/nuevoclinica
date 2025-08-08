import sqlite3
import os
from datetime import datetime

def diagnosticar_problema():
    print("🔍 DIAGNÓSTICO DE CITAS")
    print("=" * 50)
    
    # 1. Verificar si existe la base de datos
    if not os.path.exists("clinica.db"):
        print("❌ La base de datos clinica.db no existe")
        return
    
    print("✅ Base de datos clinica.db existe")
    
    try:
        conn = sqlite3.connect("clinica.db")
        cursor = conn.cursor()
        
        # 2. Verificar si existe la tabla citas
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='citas'")
        if not cursor.fetchone():
            print("❌ La tabla 'citas' no existe")
            print("💡 Solución: Ejecutar el chatbot para inicializar la base de datos")
            return
        
        print("✅ La tabla 'citas' existe")
        
        # 3. Verificar estructura de la tabla
        cursor.execute("PRAGMA table_info(citas)")
        columnas = cursor.fetchall()
        print(f"📋 Estructura de la tabla: {len(columnas)} columnas")
        for col in columnas:
            print(f"   - {col[1]} ({col[2]})")
        
        # 4. Contar citas
        cursor.execute("SELECT COUNT(*) FROM citas")
        total = cursor.fetchone()[0]
        print(f"📊 Total de citas: {total}")
        
        # 5. Mostrar algunas citas de ejemplo
        cursor.execute("SELECT * FROM citas ORDER BY fecha DESC LIMIT 5")
        citas = cursor.fetchall()
        
        if citas:
            print("\n📋 Últimas 5 citas:")
            for cita in citas:
                print(f"   ID: {cita[0]}, Nombre: {cita[1]}, Fecha: {cita[5]}, Hora: {cita[6]}, Estado: {cita[7]}")
        else:
            print("❌ No hay citas en la base de datos")
            print("💡 Solución: Crear algunas citas desde el chatbot")
        
        # 6. Verificar citas por estado
        cursor.execute("SELECT estado, COUNT(*) FROM citas GROUP BY estado")
        estados = cursor.fetchall()
        print("\n📊 Citas por estado:")
        for estado, count in estados:
            print(f"   - {estado}: {count}")
        
        # 7. Verificar citas por fecha
        cursor.execute("SELECT fecha, COUNT(*) FROM citas GROUP BY fecha ORDER BY fecha DESC LIMIT 10")
        fechas = cursor.fetchall()
        print("\n📅 Citas por fecha (últimas 10):")
        for fecha, count in fechas:
            print(f"   - {fecha}: {count} citas")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Error al diagnosticar: {str(e)}")

if __name__ == "__main__":
    diagnosticar_problema()

