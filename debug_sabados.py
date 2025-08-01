import requests
import json

def debug_sabados():
    """Depura el problema con las citas de sábado"""
    
    try:
        # Obtener todas las citas
        response = requests.get('http://localhost:5001/api/citas')
        if response.status_code == 200:
            citas = response.json()
            
            print(f"📊 Total de citas: {len(citas)}")
            
            # Verificar citas de sábado específicamente
            sabados_agosto = ['2025-08-02', '2025-08-09', '2025-08-16', '2025-08-23', '2025-08-30']
            
            for fecha in sabados_agosto:
                citas_fecha = [cita for cita in citas if cita['fecha'] == fecha]
                print(f"\n📅 {fecha}: {len(citas_fecha)} citas")
                
                if citas_fecha:
                    for cita in citas_fecha:
                        print(f"  ✅ {cita['hora']} | {cita['nombre']} | {cita['motivo']}")
                else:
                    print(f"  ❌ No hay citas para {fecha}")
            
            # Verificar si hay algún problema con el formato de fecha
            print(f"\n🔍 Verificando formato de fechas...")
            for cita in citas[:5]:  # Primeras 5 citas
                print(f"  Fecha: '{cita['fecha']}' (tipo: {type(cita['fecha'])})")
            
            # Verificar citas de agosto en general
            citas_agosto = [cita for cita in citas if cita['fecha'].startswith('2025-08')]
            print(f"\n📊 Total citas agosto 2025: {len(citas_agosto)}")
            
            # Verificar distribución por días
            from datetime import datetime
            dias_semana = {}
            for cita in citas_agosto:
                fecha = datetime.strptime(cita['fecha'], '%Y-%m-%d')
                dia = fecha.strftime('%A')
                if dia not in dias_semana:
                    dias_semana[dia] = 0
                dias_semana[dia] += 1
            
            print(f"\n📅 Distribución por días de la semana:")
            for dia, count in dias_semana.items():
                print(f"  {dia}: {count} citas")
                
        else:
            print(f"❌ Error al obtener citas: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🔍 Depurando problema con citas de sábado...")
    debug_sabados() 