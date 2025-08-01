import requests
import json

def test_sabados_panel():
    """Prueba que las citas de sábado se muestran en el panel"""
    
    try:
        # Obtener todas las citas
        response = requests.get('http://localhost:5001/api/citas')
        if response.status_code == 200:
            citas = response.json()
            
            # Filtrar citas de sábado (agosto 2025)
            sabados = [cita for cita in citas if 
                      cita['fecha'].startswith('2025-08') and 
                      cita['fecha'] in ['2025-08-02', '2025-08-09', '2025-08-16', '2025-08-23', '2025-08-30']]
            
            print(f"📊 Citas de sábado encontradas en el panel: {len(sabados)}")
            
            if sabados:
                print("\n📅 Citas por sábado:")
                sabados_por_fecha = {}
                for cita in sabados:
                    fecha = cita['fecha']
                    if fecha not in sabados_por_fecha:
                        sabados_por_fecha[fecha] = []
                    sabados_por_fecha[fecha].append(cita)
                
                for fecha, citas_fecha in sabados_por_fecha.items():
                    print(f"  {fecha}: {len(citas_fecha)} citas")
                    for cita in citas_fecha:
                        print(f"    - {cita['hora']} | {cita['nombre']} | {cita['motivo']}")
                
                print(f"\n✅ Las citas de sábado están disponibles en el panel")
                print("🌐 Verifica en: http://localhost:5001/panel")
                print("   - Cambia a vista 'Mes'")
                print("   - Navega a agosto 2025")
                print("   - Los sábados deberían mostrar las citas")
            else:
                print("❌ No se encontraron citas de sábado en el panel")
                
        else:
            print(f"❌ Error al obtener citas: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🧪 Verificando citas de sábado en el panel...")
    test_sabados_panel() 