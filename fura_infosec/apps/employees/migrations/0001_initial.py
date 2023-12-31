# Generated by Django 4.2.4 on 2023-08-25 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=100, verbose_name='Департамент')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_name', models.CharField(max_length=10, verbose_name='Устройство')),
                ('device_lic', models.CharField(choices=[('YES', 'Да'), ('NO', 'Нет')], default='NO', max_length=3, verbose_name='Лицензия устройства')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos_name', models.CharField(max_length=100, verbose_name='Должность')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=15, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('middlename', models.CharField(max_length=30, verbose_name='Отчество')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('phone', models.PositiveIntegerField(blank=True, unique=True, verbose_name='Телефон')),
                ('user_lic', models.CharField(choices=[('YES', 'Да'), ('NO', 'Нет')], default='NO', max_length=3, verbose_name='Лицензия пользователя')),
                ('status', models.CharField(choices=[('YES', 'Да'), ('NO', 'Нет')], default='NO', max_length=3, verbose_name='Статус отслеживания')),
                ('dossier', models.CharField(choices=[('YES', 'Да'), ('NO', 'Нет')], default='NO', max_length=3, verbose_name='Досье сотрудника')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='department', to='employees.department')),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='device', to='employees.device')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='position', to='employees.position')),
            ],
        ),
    ]
