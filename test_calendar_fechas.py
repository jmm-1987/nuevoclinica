#!/usr/bin/env python3
"""
Script para diagnosticar el problema de fechas en el calendario del chatbot
"""

from datetime import datetime, timedelta
import sqlite3

def test_calendar_calculation():
    """Prueba el cálculo de fechas del calendario"""
    print("=== DIAGNÓSTICO DEL CALENDARIO ===")
    
    # Simular el cálculo del backend
    today = datetime.now()
    print(f"Fecha actual: {today.strftime('%Y-%m-%d')}")
    
    # Generar fechas disponibles como en el backend
    available_dates = []
    
    # Agregar fechas de agosto 2025
    august_2025_dates = []
    for day in range(1, 32):  # Agosto tiene 31 días
        fecha = datetime(2025, 8, day)
        if fecha.weekday() < 5:  # Solo días laborables (Lun-Vie)
            fecha_str = fecha.strftime("%Y-%m-%d")
            august_2025_dates.append(fecha_str)
    
    # Agregar fechas próximas
    for i in range(1, 31):
        fecha = today + timedelta(days=i)
        if fecha.weekday() < 5:  # Solo días laborables (Lun-Vie)
            fecha_str = fecha.strftime("%Y-%m-%d")
            available_dates.append(fecha_str)
    
    # Combinar y ordenar
    all_dates = august_2025_dates + available_dates
    available_dates = list(set(all_dates))
    available_dates.sort()
    
    print(f"\nFechas disponibles del backend:")
    for fecha in available_dates[:10]:  # Mostrar solo las primeras 10
        fecha_obj = datetime.strptime(fecha, '%Y-%m-%d')
        dia_semana = fecha_obj.strftime('%A')  # Nombre del día
        print(f"  {fecha} - {dia_semana}")
    
    # Simular el cálculo del frontend
    print(f"\n=== CÁLCULO DEL FRONTEND ===")
    
    # Tomar la primera fecha disponible para determinar el mes a mostrar
    if available_dates:
        first_available_date = datetime.strptime(available_dates[0], '%Y-%m-%d')
        display_month = first_available_date.month
        display_year = first_available_date.year
        
        print(f"Mes a mostrar: {display_month}/{display_year}")
        
        # Calcular el primer día del mes
        first_day = datetime(display_year, display_month, 1)
        print(f"Primer día del mes: {first_day.strftime('%Y-%m-%d %A')}")
        
        # Calcular el día de la semana (0=Domingo, 1=Lunes, etc.)
        day_of_week = first_day.weekday()  # 0=Lunes, 1=Martes, etc.
        print(f"Día de la semana del primer día: {day_of_week} (0=Lunes)")
        
        # Calcular el startDate (problema aquí)
        start_date = datetime(display_year, display_month, 1)
        # CORRECCIÓN: Ajustar para que el lunes sea el primer día
        start_date = start_date - timedelta(days=day_of_week)
        
        print(f"Fecha de inicio del calendario: {start_date.strftime('%Y-%m-%d %A')}")
        
        # Generar los primeros días del calendario
        print(f"\nPrimeros días del calendario:")
        for i in range(7):
            current_date = start_date + timedelta(days=i)
            print(f"  Día {i}: {current_date.strftime('%Y-%m-%d %A')}")
    
    # Verificar base de datos
    print(f"\n=== VERIFICACIÓN DE BASE DE DATOS ===")
    try:
        conn = sqlite3.connect("clinica.db")
        cursor = conn.cursor()
        
        cursor.execute('SELECT fecha, hora FROM citas WHERE estado != "cancelada" ORDER BY fecha, hora')
        appointments = cursor.fetchall()
        
        print(f"Total de citas en la base de datos: {len(appointments)}")
        
        if appointments:
            print("Primeras 5 citas:")
            for fecha, hora in appointments[:5]:
                fecha_obj = datetime.strptime(fecha, '%Y-%m-%d')
                dia_semana = fecha_obj.strftime('%A')
                print(f"  {fecha} {hora} - {dia_semana}")
        
        conn.close()
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")

if __name__ == "__main__":
    test_calendar_calculation()
