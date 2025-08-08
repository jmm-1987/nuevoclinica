import requests
import json

def test_servidor():
    print("🧪 TESTEANDO SERVIDOR")
    print("=" * 40)
    
    base_url = "http://localhost:5001"
    
    try:
        # Test 1: Verificar que el servidor esté corriendo
        print("1️⃣ Verificando servidor...")
        response = requests.get(f"{base_url}/", timeout=5)
        if response.status_code == 200:
            print("✅ Servidor funcionando")
        else:
            print(f"❌ Error en servidor: {response.status_code}")
            return
    except requests.exceptions.ConnectionError:
        print("❌ No se puede conectar al servidor")
        print("💡 Asegúrate de que el servidor esté corriendo en http://localhost:5001")
        return
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return
    
    # Test 2: Verificar API de citas
    print("\n2️⃣ Verificando API de citas...")
    try:
        response = requests.get(f"{base_url}/api/citas", timeout=5)
        if response.status_code == 200:
            citas = response.json()
            print(f"✅ API de citas funcionando - {len(citas)} citas encontradas")
            if citas:
                print("📋 Primeras citas:")
                for cita in citas[:3]:
                    print(f"   - {cita['nombre']} ({cita['fecha']} {cita['hora']})")
        else:
            print(f"❌ Error en API de citas: {response.status_code}")
    except Exception as e:
        print(f"❌ Error en API de citas: {str(e)}")
    
    # Test 3: Verificar API de estadísticas
    print("\n3️⃣ Verificando API de estadísticas...")
    try:
        response = requests.get(f"{base_url}/api/estadisticas", timeout=5)
        if response.status_code == 200:
            stats = response.json()
            print("✅ API de estadísticas funcionando")
            print(f"   - Total citas: {stats.get('total_citas', 0)}")
            print(f"   - Pendientes: {stats.get('citas_pendientes', 0)}")
            print(f"   - Confirmadas: {stats.get('citas_confirmadas', 0)}")
        else:
            print(f"❌ Error en API de estadísticas: {response.status_code}")
    except Exception as e:
        print(f"❌ Error en API de estadísticas: {str(e)}")
    
    # Test 4: Verificar panel
    print("\n4️⃣ Verificando panel...")
    try:
        response = requests.get(f"{base_url}/panel", timeout=5)
        if response.status_code == 200:
            print("✅ Panel accesible")
        else:
            print(f"❌ Error en panel: {response.status_code}")
    except Exception as e:
        print(f"❌ Error en panel: {str(e)}")
    
    print("\n🎉 Test completado")

if __name__ == "__main__":
    test_servidor()
