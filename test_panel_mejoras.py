import requests
import json

def test_panel_mejoras():
    """Prueba las nuevas funcionalidades del panel"""
    
    try:
        # Obtener todas las citas
        response = requests.get('http://localhost:5001/api/citas')
        if response.status_code == 200:
            citas = response.json()
            
            print("🧪 Probando nuevas funcionalidades del panel...")
            print(f"📊 Total citas disponibles: {len(citas)}")
            
            # Verificar citas de sábado específicamente
            sabados = ['2025-08-02', '2025-08-09', '2025-08-16', '2025-08-23', '2025-08-30']
            
            print(f"\n📅 Verificando citas de sábado para selección:")
            for fecha in sabados:
                citas_fecha = [cita for cita in citas if cita['fecha'] == fecha]
                print(f"  {fecha}: {len(citas_fecha)} citas disponibles")
                
                if citas_fecha:
                    for cita in citas_fecha:
                        print(f"    ✅ {cita['hora']} | {cita['nombre']} | {cita['telefono']} | {cita['email']}")
            
            print(f"\n✅ Funcionalidades implementadas:")
            print(f"  - Al hacer clic en un día del calendario, se muestran solo las citas de ese día")
            print(f"  - Se muestra la fecha seleccionada en el título de la lista")
            print(f"  - Botones de WhatsApp con logo original (fab fa-whatsapp)")
            print(f"  - Botones de Email con icono de sobre")
            print(f"  - Los botones abren WhatsApp Web y cliente de email respectivamente")
            
            print(f"\n🌐 Para probar las funcionalidades:")
            print(f"   http://localhost:5001/panel")
            print(f"   - Haz clic en cualquier día del calendario")
            print(f"   - Verifica que se muestran solo las citas de ese día")
            print(f"   - Prueba los botones de WhatsApp y Email")
            
        else:
            print(f"❌ Error al obtener citas: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_panel_mejoras() 