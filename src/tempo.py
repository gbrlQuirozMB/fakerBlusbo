class HombreTemporadaCategoriaEndPoint(APIView):
    def getQuerySet(self, id_temporada):
        try:
            return TemporadaCategoria.objects.all().filter(temporada=id_temporada, genero=2)
        except:
            return None

    def get(self, request, id_temporada):
        queryset = self.getQuerySet(id_temporada)
        serializer = TemporadaCategoriaSerializer(queryset, many=True)
        status = {
            'code': 200,
            'message': 'OK'
        }
        respuesta = {
            'status': status,
            'content': serializer.data
        }
        # if queryset is None:
        if not queryset:
            status['code'] = 200
            status['message'] = 'No existen registros'
            respuesta['content'] = None
        return Response(respuesta, status=status['code'])

class MujerTemporadaCategoriaEndPoint(APIView):
    def getQuerySet(self, id_temporada):
        try:
            return TemporadaCategoria.objects.all().filter(temporada=id_temporada, genero=1)
        except:
            return None

    def get(self, request, id_temporada):
        queryset = self.getQuerySet(id_temporada)
        serializer = TemporadaCategoriaSerializer(queryset, many=True)
        status = {
            'code': 200,
            'message': 'OK'
        }
        respuesta = {
            'status': status,
            'content': serializer.data
        }
        # if queryset is None:
        if not queryset:
            status['code'] = 200
            status['message'] = 'No existen registros'
            respuesta['content'] = None
        return Response(respuesta, status=status['code'])