from rest_framework.views import APIView
from .models import CadastralPlot
from .serializers import CadastralPlotSerializer
from django.http import JsonResponse
from rosreestr2coord import Area
import json
from django.db.utils import IntegrityError
from rest_framework.renderers import JSONRenderer


class CadastralPlotView(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request, cadastral_number):
        try:
            cadastral_plot = CadastralPlot.objects.get(
                cadastral_number=cadastral_number)
            serialize_cadastral_plot = CadastralPlotSerializer(cadastral_plot)
            return JsonResponse(serialize_cadastral_plot.data)

        except CadastralPlot.DoesNotExist:
            try:
                geojson_poly = Area(cadastral_number).to_geojson_poly()
                geojson_cadstral_plot = json.loads(geojson_poly)
                cadastral_plot = CadastralPlot.objects.create(
                    cadastral_number=geojson_cadstral_plot['properties']['cn'],
                    short_cadastral_number=geojson_cadstral_plot['properties']['id'],
                    geometry=geojson_cadstral_plot['geometry'],
                    address=geojson_cadstral_plot['properties']['address']
                )
                serialize_cadstral_plot = CadastralPlotSerializer(cadastral_plot)

                return JsonResponse(serialize_cadstral_plot.data)

            except TypeError:
                return JsonResponse({
                    'status': 'Not found'
                })

            except IntegrityError:
                return JsonResponse({
                    'status': 'This cadastral number already exists in the database'
                })

    def post(self, request, cadastral_number):
        try:
            geojson_poly = Area(cadastral_number).to_geojson_poly()
            geojson_cadstral_plot = json.loads(geojson_poly)
            cadastral_plot = CadastralPlot.objects.create(
                cadastral_number=geojson_cadstral_plot['properties']['cn'],
                short_cadastral_number=geojson_cadstral_plot['properties']['id'],
                geometry=geojson_cadstral_plot['geometry'],
                address=geojson_cadstral_plot['properties']['address']
            )
            serialize_cadstral_plot = CadastralPlotSerializer(cadastral_plot)

            return JsonResponse(serialize_cadstral_plot.data)

        except TypeError:
            return JsonResponse({
                'status': 'Not found'
            })

        except IntegrityError:
            return JsonResponse({
                'status': 'This cadastral number already exists in the database'
            })
