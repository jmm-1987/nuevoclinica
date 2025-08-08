#!/usr/bin/env python3
"""
Script para probar las correcciones del calendario
"""

from datetime import datetime, timedelta

def test_calendar_fix():
    """Prueba la corrección del calendario"""
    print("=== PRUEBA DE CORRECCIÓN DEL CALENDARIO ===")
    
    # Simular el cálculo corregido del frontend
    display_month = 8  # Agosto
    display_year = 2025
    
    print(f"Mes a mostrar: {display_month}/{display_year}")
    
    # Calcular el primer día del mes
    first_day = datetime(display_year, display_month, 1)
    print(f"Primer día del mes: {first_day.strftime('%Y-%m-%d %A')}")
    
    # Calcular el día de la semana (0=Domingo, 1=Lunes, etc.)
    day_of_week = first_day.weekday()  # 0=Lunes, 1=Martes, etc.
    print(f"Día de la semana del primer día: {day_of_week} (0=Lunes)")
    
    # CORRECCIÓN: Ajustar para que el lunes sea el primer día
    start_date = datetime(display_year, display_month, 1)
    start_date = start_date - timedelta(days=day_of_week)
    
    print(f"Fecha de inicio del calendario: {start_date.strftime('%Y-%m-%d %A')}")
    
    # Generar los primeros días del calendario
    print(f"\nPrimeros días del calendario:")
    for i in range(7):
        current_date = start_date + timedelta(days=i)
        day_name = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'][i]
        print(f"  Día {i}: {current_date.strftime('%Y-%m-%d')} - {day_name}")
    
    # Verificar que el lunes está disponible
    print(f"\n=== VERIFICACIÓN DE LUNES ===")
    august_2025_dates = []
    for day in range(1, 32):  # Agosto tiene 31 días
        fecha = datetime(2025, 8, day)
        if fecha.weekday() < 5:  # Solo días laborables (Lun-Vie)
            fecha_str = fecha.strftime("%Y-%m-%d")
            august_2025_dates.append(fecha_str)
    
    print(f"Fechas laborables de agosto 2025:")
    for fecha in august_2025_dates:
        fecha_obj = datetime.strptime(fecha, '%Y-%m-%d')
        dia_semana = fecha_obj.strftime('%A')
        print(f"  {fecha} - {dia_semana}")

if __name__ == "__main__":
    test_calendar_fix()
