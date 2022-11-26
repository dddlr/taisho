from django.core.management.base import BaseCommand, CommandError
from tsmc.models import Initial, Final, Character
import csv

# Assumption: Order is
# 01. Character
# 02. Initial
# 03. Tone
# 04. Final
# 05. Openness (1 = open, 2 = closed)
# 06. Division
# 07. Jiyun only?
# 08. From outside Jiyun/Chengyun?
# 09. More common variant?
# 10. Gloss
# 11. Notes

DRY_RUN = True

class Command(BaseCommand):
    help = 'Batch add characters to database from a CSV spreadsheet.'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        if DRY_RUN:
            print("Dry run. Change the DRY_RUN variable in the code to False \
                  to update the database.")

        with open(options['path']) as csvfile:
            # data = csv.reader(csvfile)
            data = csv.reader(csvfile)
            for i, row in enumerate(data):
                if i == 0:  # Skip the header row
                    continue
                assert len(row) == 11
                character, initial, tone, final, openness, division, jiyun_only, \
                outside_jiyun_chengyun, more_common_variant, gloss, note = row

                initial_key = Initial.objects.get(name=initial)
                final_key = Final.objects.get(name=final)
                character = Character(
                    char=character,
                    initial_key=initial_key,
                    final_key=final_key,
                    tone=tone,
                    openness=openness,
                    division=int(division),
                    gloss=gloss,
                    note=note,
                    variant=more_common_variant,
                    jiyun_only=bool(jiyun_only),
                    external=bool(outside_jiyun_chengyun),

                )

                if DRY_RUN:
                    print(f"[dry run] adding {character}")
                else:
                    print(f"Adding {character}")
                    character.save()
