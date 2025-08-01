from datetime import datetime, date

def test_calendar_alignment():
    """Prueba la alineación del calendario mensual"""
    
    # Probar con agosto de 2025
    test_date = datetime(2025, 8, 1)
    
    print(f"🧪 Probando alineación del calendario para: {test_date.strftime('%B %Y')}")
    print("=" * 60)
    
    # Calcular el primer día del mes
    primer_dia_mes = date(test_date.year, test_date.month, 1)
    ultimo_dia_mes = date(test_date.year, test_date.month + 1, 1) - date.resolution
    
    print(f"📅 Primer día del mes: {primer_dia_mes} ({primer_dia_mes.strftime('%A')})")
    print(f"📅 Último día del mes: {ultimo_dia_mes} ({ultimo_dia_mes.strftime('%A')})")
    
    # Calcular espacios en blanco (lógica del calendario)
    primer_dia_semana = primer_dia_mes.weekday()  # 0=lunes, 6=domingo
    print(f"📊 Día de la semana del primer día: {primer_dia_semana} ({primer_dia_mes.strftime('%A')})")
    
    # Aplicar la lógica del calendario
    if primer_dia_semana == 6:  # Domingo (6 en weekday())
        espacios_blanco = 6
    else:
        espacios_blanco = primer_dia_semana
    
    print(f"📊 Espacios en blanco calculados: {espacios_blanco}")
    
    # Verificar que el primer día del mes cae en la posición correcta
    posicion_primer_dia = espacios_blanco + 1
    print(f"📊 Posición del primer día en el calendario: {posicion_primer_dia}")
    
    # Mostrar los primeros días del calendario
    print("\n📋 Primeros días del calendario:")
    for i in range(7):
        if i < espacios_blanco:
            print(f"  Día {i+1}: [Espacio en blanco]")
        elif i == espacios_blanco:
            print(f"  Día {i+1}: {primer_dia_mes.day} (Primer día del mes)")
        else:
            dia_mes = i - espacios_blanco + 1
            print(f"  Día {i+1}: {dia_mes}")
    
    # Verificar que los lunes están en la posición correcta
    print("\n🔍 Verificación de lunes:")
    lunes_agosto = [4, 11, 18, 25]  # Lunes de agosto 2025
    
    for lunes in lunes_agosto:
        fecha_lunes = date(2025, 8, lunes)
        # Calcular en qué posición del calendario cae este lunes
        # Primero calculamos cuántos días han pasado desde el primer día del mes
        dias_desde_inicio = (fecha_lunes - primer_dia_mes).days
        # Luego calculamos la posición en el calendario
        posicion_calendario = espacios_blanco + dias_desde_inicio + 1
        # Calculamos en qué semana y día de la semana cae
        semana = (posicion_calendario - 1) // 7 + 1
        dia_semana = ((posicion_calendario - 1) % 7) + 1
        
        print(f"  {fecha_lunes}: Posición {posicion_calendario} (Semana {semana}, Día {dia_semana})")
    
    print("\n✅ Si los lunes aparecen en la columna 1, el calendario está alineado correctamente")

if __name__ == "__main__":
    test_calendar_alignment()
    print("\n🌐 Para verificar en el panel:")
    print("   http://localhost:5001/panel")
    print("   - Cambia a vista 'Mes'")
    print("   - Navega a agosto de 2025")
    print("   - Verifica que los lunes (4, 11, 18, 25) están en la primera columna") 