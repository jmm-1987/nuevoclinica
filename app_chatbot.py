from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime, timedelta
import json

app = Flask(__name__)
app.secret_key = 'clinica_dental_secret_key'

DATABASE = "clinica.db"

def init_database():
    """Inicializa la base de datos solo para citas"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Crear tabla solo para citas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS citas (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            email TEXT,
            telefono TEXT,
            motivo TEXT,
            fecha TEXT,
            hora TEXT,
            estado TEXT DEFAULT 'pendiente'
        )
    ''')
    
    conn.commit()
    conn.close()

# Datos de tratamientos hardcodeados
TRATAMIENTOS = [
    {
        'id': 1,
        'nombre': 'Limpieza Dental',
        'descripcion': 'La limpieza dental profesional es un procedimiento fundamental para mantener una salud bucal óptima. Este tratamiento incluye la eliminación completa de sarro, placa bacteriana y manchas superficiales que se acumulan en los dientes y encías. Nuestros higienistas dentales utilizan técnicas avanzadas y equipos especializados para realizar una limpieza profunda que no solo mejora la apariencia de tus dientes, sino que también previene enfermedades periodontales y caries. El proceso incluye pulido dental para dejar una superficie lisa que dificulta la acumulación de bacterias, y aplicación de flúor para fortalecer el esmalte dental. Es recomendable realizarse este tratamiento cada 6 meses para mantener una boca saludable y prevenir problemas futuros.',
        'duracion': '45 minutos',
        'precio': 80.0,
        'antes_despues': 'Eliminación completa de sarro y manchas superficiales, pulido dental profesional y aplicación de flúor protector. Los dientes quedan notablemente más blancos y brillantes, con una sensación de frescura inmediata.',
        'preguntas_frecuentes': '¿Cada cuánto tiempo debo hacerme una limpieza? Cada 6 meses es lo recomendado para mantener una salud bucal óptima. ¿Duele la limpieza? No, es un procedimiento completamente indoloro que solo puede causar una ligera sensibilidad en casos de encías muy sensibles. ¿Cuánto tiempo dura el efecto? Los resultados son inmediatos y se mantienen con una buena higiene dental diaria.',
        'imagen_antes': '/static/img/limpieza_antes.jpg',
        'imagen_despues': '/static/img/limpieza_despues.jpg'
    },
    {
        'id': 2,
        'nombre': 'Empaste Dental',
        'descripcion': 'El empaste dental, también conocido como obturación, es un tratamiento restaurador que se utiliza para tratar las caries dentales. Cuando una caries afecta el esmalte y la dentina del diente, es necesario eliminar el tejido dañado y reemplazarlo con un material de relleno. Utilizamos materiales compuestos de alta calidad que se adaptan perfectamente al color natural de tus dientes, garantizando un resultado estético y funcional. El proceso incluye anestesia local para asegurar tu comodidad, eliminación del tejido cariado, preparación de la cavidad y colocación del empaste. Este tratamiento no solo restaura la función del diente, sino que también previene que la caries se extienda y cause problemas más graves como infecciones o la pérdida del diente.',
        'duracion': '30 minutos',
        'precio': 120.0,
        'antes_despues': 'Restauración completa del diente afectado con material compuesto del color natural. El diente recupera su forma, función y apariencia original, siendo prácticamente indistinguible de los dientes sanos.',
        'preguntas_frecuentes': '¿Duele el empaste? Se aplica anestesia local para evitar cualquier molestia durante el procedimiento. ¿Cuánto dura el empaste? Con una buena higiene dental, los empastes pueden durar entre 5-10 años. ¿Puedo comer después del empaste? Sí, puedes comer normalmente una vez que pase el efecto de la anestesia.',
        'imagen_antes': '/static/img/empaste_antes.jpg',
        'imagen_despues': '/static/img/empaste_despues.jpg'
    },
    {
        'id': 3,
        'nombre': 'Ortodoncia',
        'descripcion': 'La ortodoncia es una especialidad de la odontología que se encarga de corregir la posición de los dientes y la mordida. Utilizamos las técnicas más avanzadas, incluyendo brackets metálicos, brackets estéticos de cerámica, y alineadores transparentes (Invisalign). El tratamiento comienza con un estudio completo que incluye radiografías, fotografías y modelos de tu boca para crear un plan personalizado. Durante el tratamiento, los brackets ejercen una presión suave y constante sobre los dientes, moviéndolos gradualmente a su posición correcta. Este proceso no solo mejora la apariencia de tu sonrisa, sino que también corrige problemas de mordida que pueden causar desgaste dental, problemas de habla y dolores de cabeza. La duración del tratamiento varía según la complejidad del caso, pero generalmente se completa entre 18-24 meses.',
        'duracion': '2 años',
        'precio': 2500.0,
        'antes_despues': 'Corrección completa de la posición dental y alineación de la mordida. Los dientes se mueven gradualmente a su posición ideal, creando una sonrisa perfectamente alineada y una mordida funcional.',
        'preguntas_frecuentes': '¿Cuánto tiempo dura el tratamiento? Entre 18-24 meses dependiendo del caso. ¿Duele la ortodoncia? Puede haber molestias leves los primeros días después de cada ajuste. ¿Puedo comer normalmente? Sí, aunque se recomienda evitar alimentos muy duros o pegajosos.',
        'imagen_antes': '/static/img/ortodoncia_antes.jpg',
        'imagen_despues': '/static/img/ortodoncia_despues.jpg'
    },
    {
        'id': 4,
        'nombre': 'Implante Dental',
        'descripcion': 'El implante dental es la solución más avanzada para reemplazar dientes perdidos. Consiste en la inserción de un tornillo de titanio en el hueso maxilar que actúa como raíz artificial, sobre el cual se coloca una corona dental que restaura completamente la función y apariencia del diente. Utilizamos tecnología de vanguardia y materiales de la más alta calidad para garantizar la durabilidad y biocompatibilidad. El proceso se realiza en varias fases: primero se inserta el implante, luego se espera a que el hueso se integre (osteointegración), y finalmente se coloca la corona. Los implantes son la solución más natural y duradera, ya que se integran perfectamente con el hueso y no requieren el desgaste de dientes adyacentes como los puentes tradicionales.',
        'duracion': '3-6 meses',
        'precio': 1500.0,
        'antes_despues': 'Reemplazo completo del diente perdido con un implante que se integra naturalmente con el hueso. El resultado es un diente que se ve, se siente y funciona exactamente como un diente natural.',
        'preguntas_frecuentes': '¿Es doloroso el implante? Se realiza con anestesia local y es mínimamente invasivo. ¿Cuánto dura un implante? Con los cuidados adecuados, los implantes pueden durar toda la vida. ¿Puedo comer normalmente? Sí, una vez cicatrizado, puedes comer cualquier alimento.',
        'imagen_antes': '/static/img/implante_antes.jpg',
        'imagen_despues': '/static/img/implante_despues.jpg'
    },
    {
        'id': 5,
        'nombre': 'Blanqueamiento',
        'descripcion': 'El blanqueamiento dental profesional es un tratamiento estético que aclara el color de tus dientes de forma segura y efectiva. Utilizamos un gel blanqueador de alta concentración activado con luz LED especializada que penetra en el esmalte dental para eliminar las manchas profundas. El proceso es completamente seguro y está supervisado por profesionales cualificados. El tratamiento se realiza en una sola sesión y los resultados son inmediatos y dramáticos. Es importante destacar que el blanqueamiento solo funciona en dientes naturales y no afecta a empastes, coronas o implantes. Antes del tratamiento, realizamos una limpieza dental para asegurar que el gel blanqueador actúe de manera uniforme en todos los dientes.',
        'duracion': '1 hora',
        'precio': 200.0,
        'antes_despues': 'Aclaramiento significativo del color dental, eliminando manchas y devolviendo el brillo natural a tu sonrisa. Los dientes quedan notablemente más blancos y brillantes, mejorando considerablemente la apariencia de tu sonrisa.',
        'preguntas_frecuentes': '¿Cuánto duran los resultados? Los resultados pueden durar hasta 2 años con cuidados adecuados. ¿Es seguro el blanqueamiento? Sí, es completamente seguro cuando se realiza por profesionales. ¿Puede causar sensibilidad? Puede haber sensibilidad temporal que desaparece en 24-48 horas.',
        'imagen_antes': '/static/img/blanqueamiento_antes.jpg',
        'imagen_despues': '/static/img/blanqueamiento_despues.jpg'
    },

    {
        'id': 7,
        'nombre': 'Corona Dental',
        'descripcion': 'La corona dental es una restauración que cubre completamente un diente dañado o debilitado, devolviéndole su forma, tamaño, fuerza y apariencia original. Utilizamos materiales de alta calidad como porcelana, zirconio o metal-porcelana, dependiendo de la ubicación del diente y las necesidades estéticas del paciente. El proceso incluye la preparación del diente, toma de impresiones digitales, fabricación de la corona en nuestro laboratorio y cementado final. Las coronas no solo restauran la función del diente, sino que también mejoran significativamente su apariencia, siendo prácticamente indistinguibles de los dientes naturales.',
        'duracion': '2-3 semanas',
        'precio': 500.0,
        'antes_despues': 'Restauración completa del diente con una corona que se integra perfectamente con el resto de la dentadura. El diente recupera su función y apariencia natural.',
        'preguntas_frecuentes': '¿Cuánto dura una corona? Con los cuidados adecuados, las coronas pueden durar entre 10-15 años. ¿Duele el proceso? Se realiza con anestesia local. ¿Puedo comer normalmente? Sí, una vez cementada la corona.',
        'imagen_antes': '/static/img/corona_antes.jpg',
        'imagen_despues': '/static/img/corona_despues.jpg'
    }
]

# Datos de ubicaciones hardcodeados
UBICACIONES = [
    {
        'nombre': 'Centro Principal',
        'direccion': 'Calle Mayor 123, Madrid',
        'telefono': '+34 91 123 4567',
        'horarios': 'Lun-Vie: 9:00-18:00, Sáb: 9:00-14:00'
    },
    {
        'nombre': 'Clínica Norte',
        'direccion': 'Avenida de la Paz 45, Madrid',
        'telefono': '+34 91 987 6543',
        'horarios': 'Lun-Vie: 8:00-17:00, Sáb: 8:00-13:00'
    },
    {
        'nombre': 'Clínica Sur',
        'direccion': 'Calle del Sol 78, Madrid',
        'telefono': '+34 91 555 1234',
        'horarios': 'Lun-Vie: 10:00-19:00, Dom: 10:00-14:00'
    }
]

@app.route('/')
def index():
    """Página principal con el chatbot"""
    init_database()
    return render_template('chatbot.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """API para manejar las interacciones del chatbot"""
    data = request.get_json()
    action = data.get('action')
    value = data.get('value')
    
    if action == 'menu_principal':
        return jsonify({
            'type': 'menu',
            'title': '👋 ¡Bienvenido a nuestra clínica dental!',
            'message': 'Selecciona una opción:',
            'options': [
                {'id': 'tratamientos', 'text': '📋 Información de tratamientos', 'icon': '🦷'},
                {'id': 'agendar', 'text': '📅 Agenda tu cita', 'icon': '📅'},
                {'id': 'ubicaciones', 'text': '📍 Ubicaciones', 'icon': '📍'},
                {'id': 'financiacion', 'text': '💰 Información de financiación', 'icon': '💰'}
            ]
        })
    
    elif action == 'tratamientos':
        options = []
        for tratamiento in TRATAMIENTOS:
            options.append({
                'id': f'tratamiento_{tratamiento["id"]}',
                'text': tratamiento['nombre'],
                'icon': '🦷'
            })
        options.append({'id': 'volver', 'text': '🔙 Volver al menú principal', 'icon': '🔙'})
        
        return jsonify({
            'type': 'menu',
            'title': '📋 TRATAMIENTOS DISPONIBLES',
            'message': 'Selecciona un tratamiento para ver más detalles:',
            'options': options
        })
    
    elif action == 'tratamiento_detalle':
        tratamiento_id = int(value.split('_')[1])
        tratamiento = next((t for t in TRATAMIENTOS if t['id'] == tratamiento_id), None)
        
        if tratamiento:
            content = {
                'descripcion': tratamiento['descripcion'],
                'duracion': tratamiento['duracion'],
                'precio': f'{tratamiento["precio"]}€',
                'antes_despues': tratamiento['antes_despues'],
                'preguntas_frecuentes': tratamiento['preguntas_frecuentes'],
                'imagen_antes': tratamiento['imagen_antes'],
                'imagen_despues': tratamiento['imagen_despues']
            }
            
            return jsonify({
                'type': 'detail',
                'title': f'📋 {tratamiento["nombre"]}',
                'content': content,
                'options': [
                    {'id': 'volver_tratamientos', 'text': '🔙 Volver a tratamientos', 'icon': '🔙'}
                ]
            })
    
    elif action == 'agendar':
        return jsonify({
            'type': 'menu',
            'title': '📅 AGENDAR CITA',
            'message': 'Selecciona el motivo de tu visita:',
            'options': [
                {'id': 'revision_periodica', 'text': '🦷 Revisión periódica', 'icon': '🦷'},
                {'id': 'otros_motivos', 'text': '📝 Otros motivos', 'icon': '📝'},
                {'id': 'volver', 'text': '🔙 Volver al menú principal', 'icon': '🔙'}
            ]
        })
    
    elif action == 'revision_periodica':
        return jsonify({
            'type': 'form',
            'title': '📅 Agendar: Revisión Periódica',
            'message': 'Completa tus datos para la revisión periódica:',
            'form_fields': [
                {'id': 'nombre', 'label': '👤 Nombre completo', 'type': 'text', 'required': True},
                {'id': 'email', 'label': '📧 Email', 'type': 'email', 'required': True},
                {'id': 'telefono', 'label': '📞 Teléfono', 'type': 'tel', 'required': True}
            ],
            'motivo': 'Revisión periódica',
            'options': [
                {'id': 'volver_agendar', 'text': '🔙 Volver', 'icon': '🔙'}
            ]
        })
    
    elif action == 'otros_motivos':
        return jsonify({
            'type': 'form',
            'title': '📅 Agendar: Otros Motivos',
            'message': 'Completa tus datos y describe el motivo de tu visita:',
            'form_fields': [
                {'id': 'nombre', 'label': '👤 Nombre completo', 'type': 'text', 'required': True},
                {'id': 'email', 'label': '📧 Email', 'type': 'email', 'required': True},
                {'id': 'telefono', 'label': '📞 Teléfono', 'type': 'tel', 'required': True},
                {'id': 'motivo', 'label': '📝 Describe el motivo de tu visita', 'type': 'textarea', 'required': True}
            ],
            'motivo': 'Otros motivos',
            'options': [
                {'id': 'volver_agendar', 'text': '🔙 Volver', 'icon': '🔙'}
            ]
        })
    
    elif action == 'seleccionar_fecha':
        # Generar fechas disponibles (próximos 30 días laborables)
        today = datetime.now()
        available_dates = []
        
        for i in range(1, 31):
            fecha = today + timedelta(days=i)
            if fecha.weekday() < 5:  # Solo días laborables (Lun-Vie)
                available_dates.append(fecha.strftime("%Y-%m-%d"))
        
        print(f"Seleccionar fecha - Datos recibidos: {data}")
        
        return jsonify({
            'type': 'calendar',
            'title': '📅 Selecciona una fecha',
            'message': 'Elige el día que prefieres para tu cita:',
            'available_dates': available_dates,
            'datos_paciente': data.get('datos_paciente'),
            'motivo': data.get('motivo'),
            'options': [
                {'id': 'volver_datos', 'text': '🔙 Volver', 'icon': '🔙'}
            ]
        })
    
    elif action == 'seleccionar_hora':
        # Horarios disponibles (mañana y tarde)
        available_times = [
            '09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00',
            '16:00', '16:30', '17:00', '17:30', '18:00', '18:30'
        ]
        
        return jsonify({
            'type': 'time_selector',
            'title': '🕐 Selecciona una hora',
            'message': f'Elige la hora que prefieres para el {data.get("fecha")}:',
            'available_times': available_times,
            'datos_paciente': data.get('datos_paciente'),
            'motivo': data.get('motivo'),
            'fecha': data.get('fecha'),
            'options': [
                {'id': 'volver_fecha', 'text': '🔙 Volver', 'icon': '🔙'}
            ]
        })
    
    elif action == 'confirmar_cita':
        datos = data.get('datos_paciente')
        motivo = data.get('motivo')
        if motivo == 'Otros motivos':
            motivo = datos.get('motivo', 'Otros motivos')
        
        # Formatear fecha para mostrar
        fecha_obj = datetime.strptime(data.get('fecha'), '%Y-%m-%d')
        fecha_formateada = fecha_obj.strftime('%d/%m/%Y')
        
        # Datos de confirmación
        confirmation_data = {
            'nombre': datos['nombre'],
            'email': datos['email'],
            'telefono': datos['telefono'],
            'motivo': motivo,
            'fecha': fecha_formateada,
            'hora': data.get('hora')
        }
        
        return jsonify({
            'type': 'confirmation',
            'title': '✅ Confirma tu cita',
            'message': 'Revisa los datos de tu cita antes de confirmar:',
            'confirmation_data': confirmation_data,
            'datos_paciente': datos,
            'motivo': motivo,
            'fecha': data.get('fecha'),
            'hora': data.get('hora'),
            'options': [
                {'id': 'guardar_cita', 'text': '✅ Confirmar cita', 'icon': '✅'},
                {'id': 'volver_hora', 'text': '🔙 Volver', 'icon': '🔙'}
            ]
        })
    
    elif action == 'guardar_cita':
        # Guardar cita en la base de datos
        datos = data.get('datos_paciente')
        motivo = data.get('motivo')
        if motivo == 'Otros motivos':
            motivo = datos.get('motivo', 'Otros motivos')
        
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO citas (nombre, email, telefono, motivo, fecha, hora)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (datos['nombre'], datos['email'], datos['telefono'], 
              motivo, data.get('fecha'), data.get('hora')))
        conn.commit()
        conn.close()
        
        return jsonify({
            'type': 'success',
            'title': '✅ ¡Cita agendada con éxito!',
            'message': f'''<strong>Resumen de tu cita:</strong><br>
👤 Paciente: {datos['nombre']}<br>
📧 Email: {datos['email']}<br>
📞 Teléfono: {datos['telefono']}<br>
📝 Motivo: {motivo}<br>
📅 Fecha: {data.get('fecha')}<br>
🕐 Hora: {data.get('hora')}<br><br>
📧 Recibirás un email de confirmación.<br>
📞 Te llamaremos para confirmar la cita.''',
            'options': [
                {'id': 'menu_principal', 'text': '🏠 Volver al menú principal', 'icon': '🏠'}
            ]
        })
    
    elif action == 'ubicaciones':
        content = ''
        for ubicacion in UBICACIONES:
            content += f'''
            <div class="ubicacion-item">
                <h4>🏥 {ubicacion["nombre"]}</h4>
                <p>📍 {ubicacion["direccion"]}</p>
                <p>📞 {ubicacion["telefono"]}</p>
                <p>🕐 {ubicacion["horarios"]}</p>
            </div>
            '''
        
        return jsonify({
            'type': 'detail',
            'title': '📍 UBICACIONES DE NUESTRAS CLÍNICAS',
            'content': {'html': content},
            'options': [
                {'id': 'volver', 'text': '🔙 Volver al menú principal', 'icon': '🔙'}
            ]
        })
    
    elif action == 'financiacion':
        content = '''
        <div class="financiacion-content">
            <h4>💳 OPCIONES DE PAGO:</h4>
            <ul>
                <li>Pago en efectivo (5% descuento)</li>
                <li>Pago con tarjeta (sin recargo)</li>
                <li>Financiación a 6 meses (sin intereses)</li>
                <li>Financiación a 12 meses (5% intereses)</li>
                <li>Financiación a 24 meses (8% intereses)</li>
            </ul>
            
            <h4>📋 CONDICIONES:</h4>
            <ul>
                <li>Requisito: DNI y justificante de ingresos</li>
                <li>Aprobación inmediata para montos hasta 1.000€</li>
                <li>Para montos superiores: aprobación en 24-48h</li>
                <li>Sin comisión de apertura</li>
                <li>Posibilidad de pago anticipado sin penalización</li>
            </ul>
            
            <h4>❓ PREGUNTAS FRECUENTES:</h4>
            <ul>
                <li>¿Necesito aval? No para montos hasta 2.000€</li>
                <li>¿Puedo pagar antes? Sí, sin penalización</li>
                <li>¿Hay comisiones ocultas? No, todo transparente</li>
            </ul>
        </div>
        '''
        
        return jsonify({
            'type': 'detail',
            'title': '💰 INFORMACIÓN DE FINANCIACIÓN',
            'content': {'html': content},
            'options': [
                {'id': 'volver', 'text': '🔙 Volver al menú principal', 'icon': '🔙'}
            ]
        })
    
    elif action == 'volver':
        return jsonify({
            'type': 'menu',
            'title': '👋 ¡Bienvenido a nuestra clínica dental!',
            'message': 'Selecciona una opción:',
            'options': [
                {'id': 'tratamientos', 'text': '📋 Información de tratamientos', 'icon': '🦷'},
                {'id': 'agendar', 'text': '📅 Agenda tu cita', 'icon': '📅'},
                {'id': 'ubicaciones', 'text': '📍 Ubicaciones', 'icon': '📍'},
                {'id': 'financiacion', 'text': '💰 Información de financiación', 'icon': '💰'}
            ]
        })
    
    return jsonify({'error': 'Acción no reconocida'})

if __name__ == '__main__':
    # Configuración para desarrollo local
    app.run(debug=True, port=5001, host='0.0.0.0') 