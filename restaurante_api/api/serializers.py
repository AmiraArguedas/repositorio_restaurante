from rest_framework import serializers
from django.utils import timezone
from .models import Roles, Usuario, Menu, HistorialEstados, Pedido, Promocion, DetallePedido, CategoriaMenu, MetodoDePago, MesasEstado, Mesas, Reserva, Notificaciones, Comentarios, Factura


# **************************************************** ROLES - Evans **********************************************
class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'

# validaciones  
    def validate_nombre(self, value):
        if not value.strip():
            raise serializers.ValidationError("El nombre del rol no puede estar vacio.")
        if len(value) < 2:
            raise serializers.ValidationError("El nombre del rol debe tener al menos 3 caracteres.")
    def validate_nombre_rol(self, value):
        if value.lower() not in ['cliente', 'administrador']:
            raise serializers.ValidationError("El rol debe ser 'cliente' o 'administrador'.")
        return value

# **************************************************** USUARIOS - Evans **********************************************
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

# validaciones 

    def validate_nombre(self, value):
        if not value.strip():
            raise serializers.ValidationError("El nombre del usuario no puede estar vacío.")
        return value
    
    def validate_email(self, value):
        if '@' not in value or '.' not in value:
            raise serializers.ValidationError("El correo electrónico no tiene un formato válido.")
        return value
    
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("La contraseña debe contener al menos un número.")
        return value

# **************************************************** MENU - Evans **********************************************
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

# validaciones 

    def validate_nombre(self, value):
        
        if not value.strip():
            raise serializers.ValidationError("El nombre del menú no puede estar vacío.")
        if len(value) < 3:
            raise serializers.ValidationError("El nombre del menú debe tener al menos 3 caracteres.")
        return value 
    
    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio del menú debe ser un valor positivo.")
        return value

    def validate_categoria(self, value):
        if not value.strip():
            raise serializers.ValidationError("La categoría no puede estar vacía.")
        return value

# ******************************************** HISTORIAL ESTADOS - Brayan *****************************************
class HistorialEstadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialEstados
        fields = '__all__'
        
# validaciones 

        def validate_estado(self, value):
            validate_states = ['preparación', 'enviado', 'entregado']
            if value not in validate_states:
                raise serializers.ValidationError("Estado no válido. Opciones: 'preparación', 'enviado', 'entregado'.")
            return value
        
        def cambiar_estado(self, nuevo_estado):
        
            if nuevo_estado not in dict(self.ESTADOS_CHOICES):
                raise ValueError("Estado no válido.")
            self.estado = nuevo_estado
            self.fecha_cambio = timezone.now()
            self.save()


# **************************************************** PEDIDO - Evans **********************************************
class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

# validaciones 

    def validate_precio(self, value):
        if value <= 0:
            raise serializers.values("El precio debe ser mayor a cero")
        return value
      
 # ************************************************** PROMOCION - Rachid *********************************************
class PromocionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocion
        fields = '__all__'

# validaciones 

    def validate(self, attrs):
        if not (0 <= attrs['descuento'] <= 100):
            raise serializers.ValidationError({"descuento": "El descuento debe estar entre 0 y 100."})
        
        if attrs['fecha_vencimiento'] < timezone.now():
            raise serializers.ValidationError({"fecha_vencimiento": "La fecha de vencimiento no puede ser en el pasado."})

        return attrs

# ******************************************** DETALLE PEDIDO - Brayan *****************************************
class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = '__all__'
        read_only_fields = ['detalle_pedido_creado', 'detalle_pedido_actualizado', 'iva', 'total']

    def validate_cantidad(self, value):
        if value <= 0:
            raise serializers.ValidationError("La cantidad debe ser un número positivo.")
        return value

    def validate_subtotal(self, value):
        if value < 0:
            raise serializers.ValidationError("El subtotal no puede ser negativo.")
        return value

    def validate(self, data):
        return data

    def create(self, validated_data):
        iva_percentage = 0.13
        subtotal = validated_data.get('subtotal', 0)
        validated_data['iva'] = subtotal * iva_percentage
        validated_data['total'] = subtotal + validated_data['iva']
        
        return super().create(validated_data)

    def update(self, instance, validated_data):
        iva_percentage = 0.13
        subtotal = validated_data.get('subtotal', instance.subtotal)
        validated_data['iva'] = subtotal * iva_percentage
        validated_data['total'] = subtotal + validated_data['iva']

        return super().update(instance, validated_data)
        
       

# validaciones 

# ******************************************** CATEGORIA MENU - Brayan *****************************************
class CategoriaMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaMenu
        fields = '__all__'

# validaciones 
  
        def validate_nombre(self, value):
            if not value.strip():
                raise serializers.ValidationError("El nombre no puede estar vacío.")

# ******************************************** METODO DE PAGO - Rachid *****************************************
class MetodoDePagoSerializer(serializers.ModelSerializer):
     class Meta:
        model = MetodoDePago
        fields = '__all__'

# validaciones 

        def validate_total_compra(self, value):
            if value <= 0:
                raise serializers.ValidationError("El total de la compra debe ser un número positivo.")
            return value

        def validate(self, attrs):
            if attrs.get('tipo_pago') == "":
                raise serializers.ValidationError({"tipo_pago": "El tipo de pago no puede estar vacío."})
            return attrs

# ***************************************** MESAS ESTADO - Amira y Rachid **************************************
class MesasEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MesasEstado
        fields = '__all__'

# validaciones 


# **************************************************** MESAS - Amira **********************************************
class MesasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesas
        fields = '__all__'

# validaciones 

    def validate_capacidad_mesa(self, value): 
        if value <= 0: raise serializers.ValidationError("La capacidad de la mesa debe ser mayor que cero") 
        return value 
    
    def validate_numero_mesa(self, value): 
        if Mesas.objects.filter(numero_mesa=value).exists(): 
            raise serializers.ValidationError("Ya existe una mesa con este número") 
        return value 
    
    def validate_disponibilidad_mesa(self, value): 
        if value.estado == 'Reservada': 
            raise serializers.ValidationError("No se puede agregar una mesa que esté reservada") 
        return value

# **************************************************** RESERVAS - Rachid **********************************************
class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

# validaciones 

    def validate(self, attrs):
        if attrs['fecha_reserva'] < timezone.now():
            raise serializers.ValidationError({"fecha_reserva": "La fecha de reserva no puede ser en el pasado."})
        
        if not Mesas.objects.filter(id=attrs['id_mesa'].id).exists():
            raise serializers.ValidationError({"id_mesa": "La mesa especificada no existe."})

        return attrs

# ************************************************* Notificaciones - Amira ********************************************
class NotificacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificaciones
        fields = '__all__'

# validaciones 

    def validate_mensaje(self, value): 
        if not value: 
            raise serializers.ValidationError("El mensaje no puede estar vacío.") 
        if len(value) > 500: 
            raise serializers.ValidationError("El mensaje no puede exceder los 500 caracteres") 
        return value 
    
    def validate_id_usuario_notificaciones(self, value): 
        if not Usuario.objects.filter(id=value.id).exists(): 
            raise serializers.ValidationError("El usuario especificado no existe") 
        return value 

# **************************************************** Comentarios - Amira ********************************************* 
class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = '__all__'

# validaciones 
    
    def validate_comentario(self, value): 
        if not value: raise serializers.ValidationError("El comentario no puede estar vacío") 
        if len(value) > 500: # Limitar longitud del comentario 
            raise serializers.ValidationError("El comentario no puede exceder los 500 caracteres") 
        return value 
    
    def validate_calificacion(self, value): 
        if value is None: raise serializers.ValidationError("La calificación es obligatoria") 
        if value < 1 or value > 5: raise serializers.ValidationError("La calificación debe estar entre 1 y 5") 
        return value 
    
    def validate_id_usuario_comentarios(self, value): 
        if not Usuario.objects.filter(id=value.id).exists(): 
            raise serializers.ValidationError("Ese usuario no existe") 
        return value 
    
    def validate_id_menu_comentarios(self, value): 
        if not Menu.objects.filter(id=value.id).exists(): 
            raise serializers.ValidationError("El menú especificado no existe") 
        return value

# **************************************************** Factura - Evans **********************************************
class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'
        read_only_fields = ['fecha_emision', 'total_factura']

# validaciones 
        
        def validate_usuario(self, value):
            if value is None:
                raise serializers.ValidationError("El usuario no puede ser nulo")
            return value
        
        def validate_detalles_pedido(self, value):
            if not value.exists():
                raise serializers.ValidationError("Debe haber al menos un detalle de pedido.")
            return value   
        
        def to_representation(self, instance):
            representation = super().to_representation(instance)
            
            total = sum(detalle.total for detalle in instance.detallepedido_set.all())
            representation['total_factura'] = total
            
            return representation

        def create(self, validated_data):
            factura = Factura.objects.create(**validated_data)
            
            factura.total_factura = sum(detalle.total for detalle in factura.detallepedido_set.all())
            factura.save()
            
            return factura     