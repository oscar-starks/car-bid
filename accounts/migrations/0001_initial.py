# Generated by Django 4.2 on 2023-04-10 12:14

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=300, null=True, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Last name')),
                ('avatar', models.ImageField(blank=True, upload_to='avatar/')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email address')),
                ('phone_number', models.CharField(max_length=45, null=True, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('vat_no', models.CharField(max_length=1000)),
                ('hrb_no', models.CharField(blank=True, max_length=1000, null=True)),
                ('company_reg_no', models.CharField(max_length=1000)),
                ('tax_id_number', models.CharField(max_length=1000)),
                ('identification', models.FileField(upload_to='identification/')),
                ('dealer', models.BooleanField(default=False)),
                ('seller', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]