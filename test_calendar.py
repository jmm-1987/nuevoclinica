import requests
import json

def test_calendar():
    """Prueba el panel de control para verificar que el calendario empieza en lunes"""
    
    try:
        # Probar acceso al panel
        response = requests.get('http://localhost:5001/panel')
        if response.status_code == 200:
            print("✅ Panel de control accesible")
        else:
            print(f"❌ Error accediendo al panel: {response.status_code}")
            return
        
        # Probar API de citas
        response = requests.get('http://localhost:5001/api/citas')
        if response.status_code == 200:
            citas = response.json()
            print(f"✅ API de citas funcionando - {len(citas)} citas encontradas")
            
            # Mostrar algunas citas de ejemplo
            if citas:
                print("\n📋 Primeras 5 citas:")
                for cita in citas[:5]:
                    print(f"  {cita['fecha']} {cita['hora']} | {cita['nombre'][:20]}... | {cita['motivo']}")
        else:
            print(f"❌ Error en API de citas: {response.status_code}")
        
        # Probar API de estadísticas
        response = requests.get('http://localhost:5001/api/estadisticas')
        if response.status_code == 200:
            stats = response.json()
            print(f"\n📊 Estadísticas:")
            print(f"  Total citas: {stats['total_citas']}")
            print(f"  Pendientes: {stats['citas_pendientes']}")
            print(f"  Confirmadas: {stats['citas_confirmadas']}")
            print(f"  Completadas: {stats['citas_completadas']}")
            print(f"  Canceladas: {stats['citas_canceladas']}")
        else:
            print(f"❌ Error en API de estadísticas: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ No se puede conectar al servidor. Asegúrate de que la aplicación esté ejecutándose.")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    print("🧪 Probando panel de control...")
    test_calendar()
    print("\n🌐 Para ver el panel con calendario que empieza en lunes:")
    print("   http://localhost:5001/panel") 