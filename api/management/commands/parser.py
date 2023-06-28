import json
from django.core.management.base import BaseCommand
from rosreestr2coord import Area
from api.models import CadastralPlot
import time
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = "Парсер кадастровых номеров напрямую"

    def add_arguments(self, parser):
        parser.add_argument(
            "file_path",
            type=str,
            help="Путь до JSON файла")

    def handle(self, *args, **options):
        file_path = options["file_path"]
        count_request = 0
        try:
            with open(file_path, "r", encoding="UTF-8") as json_file:
                cadastrals = json.load(json_file)
                for cadastral in cadastrals:
                    area = Area(cadastral["attrs_id"], with_proxy=True)
                    count_request += 1
                    try:
                        geojson_poly = json.loads(area.to_geojson_poly())
                        CadastralPlot.objects.get_or_create(
                            cadastral_number=cadastral["attrs_cn"],
                            short_cadastral_number=cadastral["attrs_id"],
                            address=geojson_poly["properties"]["address"],
                            geometry=geojson_poly["geometry"]
                        )

                    except TypeError:
                        self.stderr.write(
                            f"Cadastral not found: {cadastral['attrs_id']}"
                        )

                    except IntegrityError:
                        continue

                    if count_request==150:
                        time.sleep(180)
                        count_request = 0

        except FileNotFoundError:
            self.stderr.write(f"File not found: {file_path}")
