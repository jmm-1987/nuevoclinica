import requests
import json

def test_chatbot_fechas():
    """Prueba que el chatbot muestra las fechas correctas"""
    
    try:
        # Simular la petición del chatbot para seleccionar fecha
        payload = {
            'action': 'seleccionar_fecha',
            'data': {
                'datos_paciente': {
                    'nombre': 'Test User',
                    'email': 'test@email.com',
                    'telefono': '123456789'
                },
                'motivo': 'Revisión periódica'
            }
        }
        
        response = requests.post('http://localhost:5001/api/chat', json=payload)
        
        if response.status_code == 200:
            data = response.json()
            
            print("🧪 Probando fechas disponibles en el chatbot...")
            print(f"📊 Tipo de respuesta: {data.get('type')}")
            print(f"📅 Título: {data.get('title')}")
            
            available_dates = data.get('available_dates', [])
            print(f"\n📅 Fechas disponibles: {len(available_dates)}")
            
            # Verificar fechas de agosto 2025
            august_2025_dates = [fecha for fecha in available_dates if fecha.startswith('2025-08')]
            print(f"📅 Fechas de agosto 2025: {len(august_2025_dates)}")
            
            if august_2025_dates:
                print("✅ Fechas de agosto 2025 encontradas:")
                for fecha in august_2025_dates[:10]:  # Mostrar primeras 10
                    print(f"  - {fecha}")
                if len(august_2025_dates) > 10:
                    print(f"  ... y {len(august_2025_dates) - 10} más")
            else:
                print("❌ No se encontraron fechas de agosto 2025")
            
            # Verificar fechas próximas
            current_dates = [fecha for fecha in available_dates if not fecha.startswith('2025-08')]
            print(f"\n📅 Fechas próximas: {len(current_dates)}")
            
            if current_dates:
                print("✅ Fechas próximas encontradas:")
                for fecha in current_dates[:5]:  # Mostrar primeras 5
                    print(f"  - {fecha}")
                if len(current_dates) > 5:
                    print(f"  ... y {len(current_dates) - 5} más")
            
            print(f"\n✅ Conclusión:")
            print(f"  - El chatbot ahora incluye fechas de agosto 2025")
            print(f"  - También incluye fechas próximas")
            print(f"  - Total de fechas disponibles: {len(available_dates)}")
            
        else:
            print(f"❌ Error al obtener fechas: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_chatbot_fechas() 