from rest_framework import generics, status
from rest_framework.response import Response
from .models import Roles, Usuario, Menu, HistorialEstados, Pedido, Promocion, DetallePedido, CategoriaMenu, MetodoDePago, MesasEstado, Mesas, Reserva, Notificaciones, Comentarios, Factura
from .serializers import RolesSerializer, UsuarioSerializer, MenuSerializer, HistorialEstadosSerializer, PedidoSerializer, PromocionSerializer, DetallePedidoSerializer, CategoriaMenuSerializer, MetodoDePagoSerializer, MesasEstadoSerializer, MesasSerializer, ReservaSerializer, NotificacionesSerializer, ComentariosSerializer, FacturaSerializer
from rest_framework.permissions import IsAuthenticated

# **************************************************** ROLES - Evans **********************************************
# ListCreate
class RolesListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

# Detail
class RolesDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Usuario eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)


# **************************************************** MENU - Evans **********************************************
# ListCreate
class MenuListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Detail
class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Menú eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)

 
    
# ******************************************** HISTORIAL ESTADOS - Brayan *****************************************
# ListCreate
class HistorialEstadosListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = HistorialEstados.objects.all()
    serializer_class = HistorialEstadosSerializer

# Detail
class HistorialEstadosDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    
    
# ************************************************** PROMOCION - Rachid *********************************************
# ListCreate 
class PromocionListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Promocion.objects.all()
    serializer_class = PromocionSerializer

# Detail
class PromocionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Promocion.objects.all()
    serializer_class = PromocionSerializer
    
# ******************************************** DETALLE PEDIDO - Brayan *****************************************
# ListCreate  
class DetallePedidoListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer

# Detail
class DetallePedidoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer
    

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Detalle de pedido eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)


# ******************************************** CATEGORIA MENU - Brayan *****************************************
# ListCreate    
class CategoriaMenuListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CategoriaMenu.objects.all()
    serializer_class = CategoriaMenuSerializer

# Detail

class CategoriaMenuDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CategoriaMenu.objects.all()
    serializer_class = CategoriaMenuSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Categoría de menú eliminada correctamente.'}, status=status.HTTP_204_NO_CONTENT)

    
    
# ******************************************** METODO DE PAGO - Rachid *****************************************
# ListCreate    
class MetodoDePagoListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MetodoDePago.objects.all()
    serializer_class = MetodoDePagoSerializer

# Detail

class MetodoDePagoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MetodoDePago.objects.all()
    serializer_class = MetodoDePagoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Método de pago eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)

    
# ***************************************** MESAS ESTADO - Amira y Rachid **************************************
# ListCreate  
class MesasEstadoListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MesasEstado.objects.all()
    serializer_class = MesasEstadoSerializer

# Detail
class MesasEstadoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MesasEstado.objects.all()
    serializer_class = MesasEstadoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Estado de mesa eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)
    
# **************************************************** MESAS - Amira **********************************************
# ListCreate     
class MesasListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Mesas.objects.all()
    serializer_class = MesasSerializer

# Detail
class MesasDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    queryset = Notificaciones.objects.all()
    serializer_class = NotificacionesSerializer

# Detail
class NotificacionesDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

# Detail
class FacturaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Factura eliminada correctamente.'}, status=status.HTTP_204_NO_CONTENT)

# ********************************************* Pedidos por Usuarios - Amira ****************************************
class PedidoPorUsuario(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PedidoSerializer

    def get_queryset(self):
        usuario_id = self.kwargs['usuario_id']
        return Pedido.objects.filter(id_usuario_id=usuario_id)

# ********************************************* Comentarios por Usuarios - Amira ****************************************
class ComentarioPorUsuario(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ComentariosSerializer

    def get_queryset(self):
        usuario_id = self.kwargs['usuario_id']
        return Comentarios.objects.filter(id_usuario_comentarios=usuario_id)