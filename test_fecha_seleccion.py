from datetime import datetime, date

def test_fecha_seleccion():
    """Prueba la selección de fechas para verificar que no hay desplazamiento"""
    
    print("🧪 Probando selección de fechas...")
    print("=" * 50)
    
    # Fechas de prueba (lunes de agosto 2025)
    fechas_prueba = [
        "2025-08-04",  # Lunes
        "2025-08-11",  # Lunes  
        "2025-08-18",  # Lunes
        "2025-08-25",  # Lunes
        "2025-08-03",  # Domingo
        "2025-08-10",  # Domingo
        "2025-08-17",  # Domingo
        "2025-08-24",  # Domingo
        "2025-08-31",  # Domingo
    ]
    
    for fecha_str in fechas_prueba:
        # Simular la lógica de seleccionarFecha()
        year, month, day = map(int, fecha_str.split('-'))
        fecha_obj = date(year, month, day)
        
        print(f"📅 Fecha seleccionada: {fecha_str}")
        print(f"   Día de la semana: {fecha_obj.strftime('%A')}")
        print(f"   weekday(): {fecha_obj.weekday()} (0=Lunes, 6=Domingo)")
        print(f"   isoweekday(): {fecha_obj.isoweekday()} (1=Lunes, 7=Domingo)")
        print()
    
    print("✅ Verificación:")
    print("   - Si haces clic en un lunes, debe abrir la vista del lunes")
    print("   - Si haces clic en un domingo, debe abrir la vista del domingo")
    print("   - No debe haber desplazamiento de un día")

if __name__ == "__main__":
    test_fecha_seleccion()
    print("\n🌐 Para probar en el panel:")
    print("   http://localhost:5001/panel")
    print("   - Cambia a vista 'Mes'")
    print("   - Navega a agosto de 2025")
    print("   - Haz clic en diferentes días y verifica que abre el día correcto") 