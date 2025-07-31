import requests
import json

def test_calendar_endpoint():
    """Prueba el endpoint del calendario"""
    url = "http://localhost:5001/api/chat"
    
    # Datos de prueba
    data = {
        "action": "seleccionar_fecha",
        "datos_paciente": {
            "nombre": "Test User",
            "email": "test@example.com",
            "telefono": "123456789"
        },
        "motivo": "Revisión periódica"
    }
    
    try:
        response = requests.post(url, json=data)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("Respuesta del servidor:")
            print(json.dumps(result, indent=2, ensure_ascii=False))
            
            if 'available_dates' in result:
                print(f"\nFechas disponibles: {len(result['available_dates'])}")
                print("Primeras 10 fechas:")
                for i, date in enumerate(result['available_dates'][:10]):
                    print(f"  {i+1}. {date}")
            else:
                print("ERROR: No se encontraron fechas disponibles en la respuesta")
        else:
            print(f"Error: {response.text}")
            
    except Exception as e:
        print(f"Error al conectar: {e}")

if __name__ == "__main__":
    test_calendar_endpoint() 