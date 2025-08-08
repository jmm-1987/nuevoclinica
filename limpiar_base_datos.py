#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para limpiar la base de datos de citas de la clínica dental
"""

import sqlite3
import os
from datetime import datetime

DATABASE = "clinica.db"

def conectar_db():
    """Conecta a la base de datos"""
    try:
        conn = sqlite3.connect(DATABASE)
        return conn
    except Exception as e:
        print(f"❌ Error al conectar a la base de datos: {str(e)}")
        return None

def mostrar_citas():
    """Muestra todas las citas en la base de datos"""
    conn = conectar_db()
    if not conn:
        return
    
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM citas ORDER BY fecha, hora')
        citas = cursor.fetchall()
        
        if not citas:
            print("📋 No hay citas en la base de datos.")
            return
        
        print(f"\n📋 Total de citas en la base de datos: {len(citas)}")
        print("=" * 80)
        
        for cita in citas:
            id_cita, nombre, email, telefono, motivo, fecha, hora, estado = cita
            # Formatear fecha para mostrar en formato dd/mm/yyyy
            try:
                fecha_obj = datetime.strptime(fecha, '%Y-%m-%d')
                fecha_formateada = fecha_obj.strftime('%d/%m/%Y')
            except:
                fecha_formateada = fecha
            
            print(f"ID: {id_cita}")
            print(f"👤 Paciente: {nombre}")
            print(f"📧 Email: {email}")
            print(f"📞 Teléfono: {telefono}")
            print(f"📝 Motivo: {motivo}")
            print(f"📅 Fecha: {fecha_formateada}")
            print(f"🕐 Hora: {hora}")
            print(f"📊 Estado: {estado}")
            print("-" * 40)
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Error al mostrar citas: {str(e)}")
        conn.close()

def limpiar_todas_citas():
    """Elimina todas las citas de la base de datos"""
    conn = conectar_db()
    if not conn:
        return
    
    try:
        cursor = conn.cursor()
        
        # Contar citas antes de eliminar
        cursor.execute('SELECT COUNT(*) FROM citas')
        total_citas = cursor.fetchone()[0]
        
        if total_citas == 0:
            print("📋 No hay citas para eliminar.")
            conn.close()
            return
        
        print(f"⚠️  ¿Estás seguro de que quieres eliminar TODAS las {total_citas} citas?")
        confirmacion = input("Escribe 'SI' para confirmar: ")
        
        if confirmacion.upper() == 'SI':
            cursor.execute('DELETE FROM citas')
            conn.commit()
            print(f"✅ Se han eliminado {total_citas} citas de la base de datos.")
        else:
            print("❌ Operación cancelada.")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Error al limpiar citas: {str(e)}")
        conn.close()

def limpiar_citas_por_fecha():
    """Elimina citas de una fecha específica"""
    conn = conectar_db()
    if not conn:
        return
    
    try:
        fecha = input("📅 Introduce la fecha (formato YYYY-MM-DD): ")
        
        # Validar formato de fecha
        try:
            datetime.strptime(fecha, '%Y-%m-%d')
        except ValueError:
            print("❌ Formato de fecha incorrecto. Usa YYYY-MM-DD")
            conn.close()
            return
        
        cursor = conn.cursor()
        
        # Contar citas de esa fecha
        cursor.execute('SELECT COUNT(*) FROM citas WHERE fecha = ?', (fecha,))
        total_citas = cursor.fetchone()[0]
        
        if total_citas == 0:
            print(f"📋 No hay citas para la fecha {fecha}.")
            conn.close()
            return
        
        print(f"⚠️  ¿Estás seguro de que quieres eliminar las {total_citas} citas del {fecha}?")
        confirmacion = input("Escribe 'SI' para confirmar: ")
        
        if confirmacion.upper() == 'SI':
            cursor.execute('DELETE FROM citas WHERE fecha = ?', (fecha,))
            conn.commit()
            print(f"✅ Se han eliminado {total_citas} citas del {fecha}.")
        else:
            print("❌ Operación cancelada.")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Error al limpiar citas por fecha: {str(e)}")
        conn.close()

def limpiar_citas_por_estado():
    """Elimina citas por estado específico"""
    conn = conectar_db()
    if not conn:
        return
    
    try:
        print("📊 Estados disponibles:")
        print("1. pendiente")
        print("2. confirmada")
        print("3. completada")
        print("4. cancelada")
        
        estado = input("📊 Introduce el estado a eliminar: ").lower()
        
        estados_validos = ['pendiente', 'confirmada', 'completada', 'cancelada']
        if estado not in estados_validos:
            print("❌ Estado no válido.")
            conn.close()
            return
        
        cursor = conn.cursor()
        
        # Contar citas de ese estado
        cursor.execute('SELECT COUNT(*) FROM citas WHERE estado = ?', (estado,))
        total_citas = cursor.fetchone()[0]
        
        if total_citas == 0:
            print(f"📋 No hay citas con estado '{estado}'.")
            conn.close()
            return
        
        print(f"⚠️  ¿Estás seguro de que quieres eliminar las {total_citas} citas con estado '{estado}'?")
        confirmacion = input("Escribe 'SI' para confirmar: ")
        
        if confirmacion.upper() == 'SI':
            cursor.execute('DELETE FROM citas WHERE estado = ?', (estado,))
            conn.commit()
            print(f"✅ Se han eliminado {total_citas} citas con estado '{estado}'.")
        else:
            print("❌ Operación cancelada.")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Error al limpiar citas por estado: {str(e)}")
        conn.close()

def limpiar_cita_especifica():
    """Elimina una cita específica por ID"""
    conn = conectar_db()
    if not conn:
        return
    
    try:
        mostrar_citas()
        
        cita_id = input("🆔 Introduce el ID de la cita a eliminar: ")
        
        try:
            cita_id = int(cita_id)
        except ValueError:
            print("❌ ID debe ser un número.")
            conn.close()
            return
        
        cursor = conn.cursor()
        
        # Verificar si la cita existe
        cursor.execute('SELECT * FROM citas WHERE id = ?', (cita_id,))
        cita = cursor.fetchone()
        
        if not cita:
            print(f"❌ No existe una cita con ID {cita_id}.")
            conn.close()
            return
        
        # Mostrar detalles de la cita
        id_cita, nombre, email, telefono, motivo, fecha, hora, estado = cita
        try:
            fecha_obj = datetime.strptime(fecha, '%Y-%m-%d')
            fecha_formateada = fecha_obj.strftime('%d/%m/%Y')
        except:
            fecha_formateada = fecha
        
        print(f"\n📋 Detalles de la cita a eliminar:")
        print(f"👤 Paciente: {nombre}")
        print(f"📅 Fecha: {fecha_formateada}")
        print(f"🕐 Hora: {hora}")
        print(f"📝 Motivo: {motivo}")
        print(f"📊 Estado: {estado}")
        
        confirmacion = input("\n⚠️  ¿Estás seguro de que quieres eliminar esta cita? (SI/NO): ")
        
        if confirmacion.upper() == 'SI':
            cursor.execute('DELETE FROM citas WHERE id = ?', (cita_id,))
            conn.commit()
            print(f"✅ Cita con ID {cita_id} eliminada correctamente.")
        else:
            print("❌ Operación cancelada.")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Error al eliminar cita específica: {str(e)}")
        conn.close()

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 50)
    print("🧹 LIMPIADOR DE BASE DE DATOS - CLÍNICA DENTAL")
    print("=" * 50)
    print("1. 📋 Mostrar todas las citas")
    print("2. 🗑️  Eliminar TODAS las citas")
    print("3. 📅 Eliminar citas por fecha")
    print("4. 📊 Eliminar citas por estado")
    print("5. 🆔 Eliminar cita específica")
    print("6. ❌ Salir")
    print("=" * 50)

def main():
    """Función principal"""
    print("🧹 Bienvenido al limpiador de base de datos de citas")
    
    # Verificar si existe la base de datos
    if not os.path.exists(DATABASE):
        print(f"❌ No se encontró la base de datos '{DATABASE}'")
        print("💡 Asegúrate de que la aplicación se haya ejecutado al menos una vez.")
        return
    
    while True:
        mostrar_menu()
        opcion = input("🔢 Selecciona una opción (1-6): ")
        
        if opcion == '1':
            mostrar_citas()
        elif opcion == '2':
            limpiar_todas_citas()
        elif opcion == '3':
            limpiar_citas_por_fecha()
        elif opcion == '4':
            limpiar_citas_por_estado()
        elif opcion == '5':
            limpiar_cita_especifica()
        elif opcion == '6':
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Inténtalo de nuevo.")
        
        input("\n⏸️  Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
