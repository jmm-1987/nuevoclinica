#!/usr/bin/env python3
"""
Script para probar el servidor y las correcciones del calendario
"""

import requests
import json

def test_calendar_api():
    """Prueba la API del calendario"""
    print("=== PRUEBA DE LA API DEL CALENDARIO ===")
    
    # URL del servidor
    base_url = "http://localhost:5000"
    
    try:
        # Probar que el servidor esté funcionando
        print("1. Probando conexión al servidor...")
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            print("✅ Servidor funcionando correctamente")
        else:
            print(f"❌ Error del servidor: {response.status_code}")
            return
        
        # Probar la API de chat para obtener fechas disponibles
        print("\n2. Probando API de chat para fechas disponibles...")
        
        # Simular datos de un paciente
        datos_paciente = {
            'nombre': 'Test User',
            'email': 'test@example.com',
            'telefono': '123456789'
        }
        
        chat_data = {
            'action': 'seleccionar_fecha',
            'datos_paciente': datos_paciente,
            'motivo': 'Revisión periódica'
        }
        
        response = requests.post(f"{base_url}/api/chat", json=chat_data)
        
        if response.status_code == 200:
            data = response.json()
            print("✅ API de chat funcionando")
            print(f"Tipo de respuesta: {data.get('type')}")
            
            if data.get('type') == 'calendar':
                available_dates = data.get('available_dates', [])
                print(f"Fechas disponibles: {len(available_dates)}")
                
                if available_dates:
                    print("Primeras 10 fechas disponibles:")
                    for fecha in available_dates[:10]:
                        print(f"  {fecha}")
                    
                    # Verificar que hay lunes disponibles
                    lunes_count = 0
                    for fecha in available_dates:
                        # Convertir fecha a objeto datetime para verificar el día
                        from datetime import datetime
                        fecha_obj = datetime.strptime(fecha, '%Y-%m-%d')
                        if fecha_obj.weekday() == 0:  # 0 = Lunes
                            lunes_count += 1
                    
                    print(f"\nLunes disponibles: {lunes_count}")
                    if lunes_count > 0:
                        print("✅ Los lunes están disponibles")
                    else:
                        print("❌ No hay lunes disponibles")
                else:
                    print("❌ No hay fechas disponibles")
            else:
                print(f"❌ Respuesta inesperada: {data}")
        else:
            print(f"❌ Error en la API de chat: {response.status_code}")
            print(f"Respuesta: {response.text}")
        
        # Probar la API de citas
        print("\n3. Probando API de citas...")
        response = requests.get(f"{base_url}/api/citas")
        
        if response.status_code == 200:
            citas = response.json()
            print(f"✅ API de citas funcionando - {len(citas)} citas encontradas")
            
            if citas:
                print("Primeras 3 citas:")
                for cita in citas[:3]:
                    print(f"  {cita.get('fecha')} {cita.get('hora')} - {cita.get('nombre')}")
        else:
            print(f"❌ Error en la API de citas: {response.status_code}")
        
    except requests.exceptions.ConnectionError:
        print("❌ No se pudo conectar al servidor. Asegúrate de que esté ejecutándose.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_calendar_api()
