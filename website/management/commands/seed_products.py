from django.core.management.base import BaseCommand
from website.models import Product

STARTERS = [
    {'name':'IONIQ 150 Ah Battery','category':'tubular','capacity_ah':150,'short_description':'A 150 Ah IONIQ battery shown in the supplied product photos.','description':'The supplied photograph identifies this battery as 150 Ah at 27°C at C10. Confirm the current model datasheet for complete specifications, intended use, dimensions, warranty and charging requirements.','featured':True,'sort_order':1},
    {'name':'IONIQ Automotive Battery Range','category':'automotive','short_description':'Battery options for automotive applications.','description':'Contact IONIQ for current model availability, fitment guidance and verified technical specifications.','featured':True,'sort_order':2},
    {'name':'IONIQ Pasted / Flat Plate Range','category':'pasted','short_description':'Pasted / flat plate battery category featured in the IONIQ brochure.','description':'Ask the team to confirm the available models and their application-specific specifications.','featured':True,'sort_order':3},
    {'name':'IONIQ Solar Battery Range','category':'solar','short_description':'Battery options for solar energy applications.','description':'Share your system requirements with the IONIQ team to check compatible options and current datasheets.','featured':True,'sort_order':4},
    {'name':'IONIQ UPS & Inverter Battery Range','category':'ups','short_description':'Battery solutions for UPS and inverter backup applications.','description':'Model selection depends on load, backup duration, system voltage and usage conditions. Contact IONIQ for guidance.','featured':True,'sort_order':5},
]
class Command(BaseCommand):
    help = 'Create starter catalogue entries if the catalogue is empty.'
    def handle(self, *args, **options):
        if Product.objects.exists():
            self.stdout.write(self.style.WARNING('Products already exist; no starter products added.'))
            return
        for item in STARTERS:
            Product.objects.create(**item)
        self.stdout.write(self.style.SUCCESS(f'Added {len(STARTERS)} starter products.'))
