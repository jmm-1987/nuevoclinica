#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script simple para limpiar todas las citas de la base de datos
"""

import sqlite3
import os

DATABASE = "clinica.db"

def limpiar_todas_citas():
    """Elimina todas las citas de la base de datos"""
    
    # Verificar si existe la base de datos
    if not os.path.exists(DATABASE):
        print(f"❌ No se encontró la base de datos '{DATABASE}'")
        print("💡 Asegúrate de que la aplicación se haya ejecutado al menos una vez.")
        return
    
    try:
        # Conectar a la base de datos
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # Contar citas antes de eliminar
        cursor.execute('SELECT COUNT(*) FROM citas')
        total_citas = cursor.fetchone()[0]
        
        if total_citas == 0:
            print("📋 No hay citas para eliminar en la base de datos.")
            conn.close()
            return
        
        print(f"📋 Se encontraron {total_citas} citas en la base de datos.")
        print("🗑️  Eliminando todas las citas...")
        
        # Eliminar todas las citas
        cursor.execute('DELETE FROM citas')
        conn.commit()
        
        print(f"✅ Se han eliminado {total_citas} citas de la base de datos.")
        print("🧹 Base de datos limpiada correctamente.")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Error al limpiar la base de datos: {str(e)}")
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    print("🧹 LIMPIADOR RÁPIDO DE BASE DE DATOS")
    print("=" * 40)
    limpiar_todas_citas()
    print("=" * 40)
    input("⏸️  Presiona Enter para salir...")
