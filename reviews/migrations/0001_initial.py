# Generated by Django 3.2.21 on 2023-11-01 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0012_delete_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_title', models.CharField(default='Default Title', max_length=100)),
                ('name', models.CharField(default='Default Name', max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('service_review', models.TextField(max_length=400, null=True)),
                ('service_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('approved', models.BooleanField(default=False)),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name_plural': 'Reviews',
            },
        ),
    ]
