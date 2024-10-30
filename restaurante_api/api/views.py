from rest_framework import generics, status
from rest_framework.response import Response
from .models import Roles, Usuario, Menu, HistorialEstados, Pedido, Promocion, DetallePedido, CategoriaMenu, MetodoDePago, MesasEstado, Mesas, Reserva, Notificaciones, Comentarios, Factura
from .serializers import RolesSerializer, UsuarioSerializer, MenuSerializer, HistorialEstadosSerializer, PedidoSerializer, PromocionSerializer, DetallePedidoSerializer, CategoriaMenuSerializer, MetodoDePagoSerializer, MesasEstadoSerializer, MesasSerializer, ReservaSerializer, NotificacionesSerializer, ComentariosSerializer, FacturaSerializer
from rest_framework.permissions import IsAuthenticated

# **************************************************** ROLES - Evans **********************************************
# ListCreate
class RolesListCreate(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

# Detail
class RolesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Rol eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)

    
# **************************************************** USUARIOS - Evans **********************************************
# ListCreate  
class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Detail
class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Usuario eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)


# **************************************************** MENU - Evans **********************************************
# ListCreate
class MenuListCreate(generics.ListCreateAPIView):

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Detail
class MenuDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Menú eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)

 
    
# ******************************************** HISTORIAL ESTADOS - Brayan *****************************************
# ListCreate
class HistorialEstadosListCreate(generics.ListCreateAPIView):

    queryset = HistorialEstados.objects.all()
    serializer_class = HistorialEstadosSerializer

# Detail
class HistorialEstadosDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = HistorialEstados.objects.all()
    serializer_class = HistorialEstadosSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Historial de estados eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)

    


# **************************************************** PEDIDO - Evans **********************************************
# ListCreate   
class PedidoListCreate(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

# Detail
class PedidoDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    
    
# ************************************************** PROMOCION - Rachid *********************************************
# ListCreate 
class PromocionListCreate(generics.ListCreateAPIView):

    queryset = Promocion.objects.all()
    serializer_class = PromocionSerializer

# Detail
class PromocionDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Promocion.objects.all()
    serializer_class = PromocionSerializer
    
# ******************************************** DETALLE PEDIDO - Brayan *****************************************
# ListCreate  
class DetallePedidoListCreate(generics.ListCreateAPIView):

    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer

# Detail
class DetallePedidoDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer
    

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Detalle de pedido eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)


# ******************************************** CATEGORIA MENU - Brayan *****************************************
# ListCreate    
class CategoriaMenuListCreate(generics.ListCreateAPIView):

    queryset = CategoriaMenu.objects.all()
    serializer_class = CategoriaMenuSerializer

# Detail

class CategoriaMenuDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = CategoriaMenu.objects.all()
    serializer_class = CategoriaMenuSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Categoría de menú eliminada correctamente.'}, status=status.HTTP_204_NO_CONTENT)

    
    
# ******************************************** METODO DE PAGO - Rachid *****************************************
# ListCreate    
class MetodoDePagoListCreate(generics.ListCreateAPIView):

    queryset = MetodoDePago.objects.all()
    serializer_class = MetodoDePagoSerializer

# Detail

class MetodoDePagoDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = MetodoDePago.objects.all()
    serializer_class = MetodoDePagoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Método de pago eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)

    
# ***************************************** MESAS ESTADO - Amira y Rachid **************************************
# ListCreate  
class MesasEstadoListCreate(generics.ListCreateAPIView):

    queryset = MesasEstado.objects.all()
    serializer_class = MesasEstadoSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Validación adicional para el campo 'estado'
        nombre_estado = request.data.get('nombre_estado')
        if nombre_estado not in ['disponible', 'reservada', 'Disponible', 'Reservada']:
            return Response({'error': "El estado debe ser 'disponible' o 'reservada'"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# Detail
class MesasEstadoDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = MesasEstado.objects.all()
    serializer_class = MesasEstadoSerializer


    def update(self, request, *args, **kwargs):
        # Validación adicional en la actualización
        estado = request.data.get('estado')
        if estado and estado not in ['disponible', 'reservada']:
            return Response({'error': "El estado debe ser 'disponible' o 'reservada'."}, status=status.HTTP_400_BAD_REQUEST)

        return super().update(request, *args, **kwargs)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Estado de mesa eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)
    
# **************************************************** MESAS - Amira **********************************************
# ListCreate     
class MesasListCreate(generics.ListCreateAPIView):

    queryset = Mesas.objects.all()
    serializer_class = MesasSerializer

# Detail
class MesasDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Mesas.objects.all()
    serializer_class = MesasSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Mesa eliminada correctamente.'}, status=status.HTTP_204_NO_CONTENT)
    
# **************************************************** RESERVAS - Rachid **********************************************
# ListCreate   
class ReservaListCreate(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

# Detail
class ReservaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Reserva eliminada correctamente.'}, status=status.HTTP_204_NO_CONTENT)

# ************************************************* Notificaciones - Amira ********************************************
# ListCreate   
class NotificacionesListCreate(generics.ListCreateAPIView):

    queryset = Notificaciones.objects.all()
    serializer_class = NotificacionesSerializer

# Detail
class NotificacionesDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Notificaciones.objects.all()
    serializer_class = NotificacionesSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Notificación eliminada correctamente.'}, status=status.HTTP_204_NO_CONTENT)

# **************************************************** Comentarios - Amira *********************************************
# ListCreate   
class ComentariosListCreate(generics.ListCreateAPIView):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer

# Detail
class ComentariosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Comentario eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)
    
# **************************************************** Factura - Evans **********************************************
# ListCreate   
class FacturaListCreate(generics.ListCreateAPIView):

    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

# Detail
class FacturaDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Factura eliminada correctamente.'}, status=status.HTTP_204_NO_CONTENT)

# ********************************************* Pedidos por Usuarios - Amira ****************************************
class PedidoPorUsuario(generics.ListAPIView):

    serializer_class = PedidoSerializer

    def get_queryset(self):
        usuario_id = self.kwargs['usuario_id']
        return Pedido.objects.filter(id_usuario_id=usuario_id)

# ********************************************* Comentarios por Usuarios - Amira ****************************************
class ComentarioPorUsuario(generics.ListAPIView):

    serializer_class = ComentariosSerializer

    def get_queryset(self):
        usuario_id = self.kwargs['usuario_id']
        return Comentarios.objects.filter(id_usuario_comentarios=usuario_id)