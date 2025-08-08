import requests
import json

def test_servidor():
    """Probar que el servidor esté funcionando correctamente"""
    try:
        base_url = "http://localhost:5000"
        
        print("🔍 Probando conexión al servidor...")
        
        # Probar la página principal
        response = requests.get(f"{base_url}/", timeout=5)
        print(f"✅ Página principal: {response.status_code}")
        
        # Probar la API de citas
        response = requests.get(f"{base_url}/api/citas", timeout=5)
        print(f"✅ API de citas: {response.status_code}")
        
        if response.status_code == 200:
            citas = response.json()
            print(f"📋 Citas encontradas: {len(citas)}")
            if len(citas) > 0:
                print(f"   Primera cita: {citas[0]}")
        else:
            print(f"❌ Error en API de citas: {response.text}")
        
        # Probar la API de estadísticas
        response = requests.get(f"{base_url}/api/estadisticas", timeout=5)
        print(f"✅ API de estadísticas: {response.status_code}")
        
        if response.status_code == 200:
            stats = response.json()
            print(f"📊 Estadísticas: {stats}")
        else:
            print(f"❌ Error en API de estadísticas: {response.text}")
        
        # Probar el panel
        response = requests.get(f"{base_url}/panel", timeout=5)
        print(f"✅ Panel: {response.status_code}")
        
    except requests.exceptions.ConnectionError:
        print("❌ No se puede conectar al servidor. ¿Está ejecutándose?")
        print("💡 Ejecuta: python app_chatbot.py")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_servidor()
