from rest_framework import serializers
from django.utils import timezone
from datetime import datetime
import re
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
        
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', value):
            raise serializers.ValidationError("Este campo solo debe contener letras y espacios.")
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
    
    def validate_apellido(self, value):
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', value):
            raise serializers.ValidationError("Este campo solo debe contener letras y espacios.")
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
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', value):
            raise serializers.ValidationError("Este campo solo debe contener letras y espacios.")
        return value 
    
    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio del menú debe ser un valor positivo.")
        return value

    def validate_categoria(self, value):
        if not value.strip():
            raise serializers.ValidationError("La categoría no puede estar vacía.")
        return value
    
    def validate_descripcion(self, value):
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', value):
            raise serializers.ValidationError("Este campo solo debe contener letras y espacios.")
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
        read_only_fields = ['detalle_pedido_creado', 'detalle_pedido_actualizado', 'subtotal', 'iva', 'total']

    def validate(self, data):
        cantidad = data.get('cantidad', 1)
        id_menu = data.get('id_menu')
        id_promocion = data.get('id_promocion')
        menu = Menu.objects.get(id=id_menu.id)
        subtotal = menu.precio * cantidad 

        if id_promocion:
            promocion = Promocion.objects.filter(id=id_promocion.id, fecha_vencimiento__gt=datetime.now()).first()
            if promocion:
                descuento = promocion.descuento / 100 
                subtotal = subtotal * (1 - descuento)  
            else:
                raise serializers.ValidationError("La promoción no es válida o ha expirado.")

        tasa_iva = 0.13
        iva = round(subtotal * tasa_iva, 2)

        total = round(subtotal + iva, 2)

        data['subtotal'] = subtotal
        data['iva'] = iva
        data['total'] = total
        return data

    def create(self, validated_data):
        return DetallePedido.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.cantidad = validated_data.get('cantidad', instance.cantidad)
        instance.id_pedido = validated_data.get('id_pedido', instance.id_pedido)
        instance.id_menu = validated_data.get('id_menu', instance.id_menu)
        instance.factura = validated_data.get('factura', instance.factura)
        instance.id_promocion = validated_data.get('id_promocion', instance.id_promocion)

        validated_data = self.validate(validated_data)
        instance.subtotal = validated_data['subtotal']
        instance.iva = validated_data['iva']
        instance.total = validated_data['total']

        instance.save()
        return instance

        
       

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
   
            if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', value):
                raise serializers.ValidationError("Este campo solo debe contener letras y espacios.")
            return value
        
        def validate_descripcion(self, value):
            if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', value):
                raise serializers.ValidationError("Este campo solo debe contener letras y espacios.")
            return value

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
        fields = ['id', 'nombre_estado']
    
    def validate_estado(self, value):
        if value not in ['disponible', 'reservada', 'Disponible', 'Reservada']:
            raise serializers.ValidationError("El estado debe ser 'disponible' o 'reservada'.")
        return value


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