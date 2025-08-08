import requests
import json

def test_inicio():
    """Probar que la aplicación arranque correctamente con el index"""
    try:
        base_url = "http://localhost:5000"
        
        print("🔍 Probando inicio de la aplicación...")
        
        # Probar la página principal (debería ser index.html)
        response = requests.get(f"{base_url}/", timeout=5)
        print(f"✅ Página principal (/): {response.status_code}")
        
        if response.status_code == 200:
            # Verificar que el contenido sea el index
            if "Clínica Dental" in response.text and "Chatbot de Citas" in response.text:
                print("✅ Contenido correcto: Página de entrada principal")
            else:
                print("❌ Contenido incorrecto: No es la página de entrada")
        
        # Probar el chatbot
        response = requests.get(f"{base_url}/chatbot", timeout=5)
        print(f"✅ Chatbot (/chatbot): {response.status_code}")
        
        # Probar el panel
        response = requests.get(f"{base_url}/panel", timeout=5)
        print(f"✅ Panel (/panel): {response.status_code}")
        
        print("\n📋 Resumen de rutas:")
        print("   / → Página de entrada principal (index.html)")
        print("   /chatbot → Chatbot de citas")
        print("   /panel → Panel de administración")
        
        print("\n💡 Para acceder a la aplicación:")
        print("   http://localhost:5000/")
        
    except requests.exceptions.ConnectionError:
        print("❌ No se puede conectar al servidor. ¿Está ejecutándose?")
        print("💡 Ejecuta: python app_chatbot.py")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_inicio()
