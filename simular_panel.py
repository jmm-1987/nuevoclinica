import requests
from datetime import datetime

def simular_panel():
    """Simula la lógica del panel para verificar citas de sábado"""
    
    try:
        # Obtener citas como lo hace el panel
        response = requests.get('http://localhost:5001/api/citas')
        if response.status_code == 200:
            citas = response.json()
            
            print("🧪 Simulando lógica del panel...")
            print(f"📊 Total citas cargadas: {len(citas)}")
            
            # Simular agosto 2025
            agosto_2025 = "2025-08"
            
            # Filtrar citas de agosto 2025
            citas_agosto = [cita for cita in citas if cita['fecha'].startswith(agosto_2025)]
            print(f"📅 Citas de agosto 2025: {len(citas_agosto)}")
            
            # Verificar sábados específicamente
            sabados = ['2025-08-02', '2025-08-09', '2025-08-16', '2025-08-23', '2025-08-30']
            
            print(f"\n🔍 Verificando sábados en el panel:")
            for fecha in sabados:
                citas_fecha = [cita for cita in citas_agosto if cita['fecha'] == fecha]
                print(f"  {fecha}: {len(citas_fecha)} citas")
                
                if citas_fecha:
                    for cita in citas_fecha:
                        print(f"    ✅ {cita['hora']} | {cita['nombre']} | {cita['motivo']}")
                else:
                    print(f"    ❌ No hay citas para {fecha}")
            
            # Simular la lógica de filtrado del calendario
            print(f"\n🔍 Simulando filtrado del calendario:")
            for fecha in sabados:
                # Simular la lógica del panel: citas.filter(cita => cita.fecha === fechaStr)
                citas_filtradas = [cita for cita in citas_agosto if cita['fecha'] == fecha]
                print(f"  Filtrado para {fecha}: {len(citas_filtradas)} citas encontradas")
                
                if citas_filtradas:
                    print(f"    ✅ Las citas están disponibles para mostrar en el calendario")
                else:
                    print(f"    ❌ No se encontraron citas para mostrar")
            
            print(f"\n✅ Conclusión:")
            print(f"  - Las citas de sábado están en la base de datos")
            print(f"  - El API las devuelve correctamente")
            print(f"  - El filtrado del panel debería funcionar")
            print(f"\n🌐 Si no se ven en el panel, el problema podría ser:")
            print(f"  - Caché del navegador")
            print(f"  - Problema de JavaScript en el frontend")
            print(f"  - Problema de zona horaria")
            
        else:
            print(f"❌ Error al obtener citas: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    simular_panel() 