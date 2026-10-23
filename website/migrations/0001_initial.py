from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('category', models.CharField(choices=[('automotive', 'Automotive'), ('pasted', 'Pasted / Flat Plate'), ('solar', 'Solar'), ('tubular', 'Tubular & Stationary'), ('ups', 'UPS & Inverter')], max_length=20)),
                ('capacity_ah', models.PositiveIntegerField(blank=True, help_text='Capacity in Ah, if applicable', null=True)),
                ('short_description', models.CharField(max_length=240)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('featured', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('sort_order', models.PositiveIntegerField(default=0)),
            ],
            options={'ordering': ['sort_order', 'name']},
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('product_interest', models.CharField(blank=True, choices=[('', 'Select a product'), ('automotive', 'Automotive'), ('pasted', 'Pasted / Flat Plate'), ('solar', 'Solar'), ('tubular', 'Tubular & Stationary'), ('ups', 'UPS & Inverter')], max_length=20)),
                ('location', models.CharField(blank=True, max_length=160)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_contacted', models.BooleanField(default=False)),
            ],
            options={'ordering': ['-created_at']},
        ),
    ]
