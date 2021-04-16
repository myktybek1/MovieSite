# Generated by Django 3.2 on 2021-04-16 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('description', models.TextField(verbose_name='Информация')),
                ('image', models.ImageField(upload_to='Photo_actor/', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Актер',
                'verbose_name_plural': 'Актеры',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название жанра')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('tagline', models.CharField(max_length=100, verbose_name='Слоган')),
                ('descriptions', models.TextField()),
                ('poster', models.ImageField(blank=True, upload_to='Photo/', verbose_name='фото')),
                ('year', models.DateField()),
                ('country', models.CharField(max_length=255, verbose_name='Страна')),
                ('world_premiere', models.DateField(verbose_name='Примьера в мире')),
                ('budget', models.IntegerField(default=0, help_text='указывать сумму в долларах', verbose_name='Бюджет')),
                ('fees_in_usa', models.IntegerField(default=0, help_text='указывать сумму в долларах', verbose_name='Сборы в США')),
                ('fees_in_world', models.IntegerField(default=0, help_text='указывать сумму в долларах', verbose_name='Сборы в мире')),
                ('url', models.SlugField(max_length=150, unique=True)),
                ('actors', models.ManyToManyField(related_name='film_actor', to='movieslist.Actor', verbose_name='Актеры')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movieslist.category', verbose_name='Категори')),
                ('directors', models.ManyToManyField(related_name='film_director', to='movieslist.Actor', verbose_name='Режиссер')),
                ('genre', models.ManyToManyField(to='movieslist.Genre', verbose_name='Жанры')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0, verbose_name='Значения')),
            ],
            options={
                'verbose_name': 'Звездв рейтинга',
                'verbose_name_plural': 'Звезды рейтинга',
                'ordering': ['-value'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Емайл')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('text', models.TextField(verbose_name='Сообщение')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieslist.movie', verbose_name='Фильм')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50, verbose_name='IP адрес')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieslist.movie', verbose_name='фильм')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieslist.ratingstar', verbose_name='Звезда')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.CreateModel(
            name='MovieShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='Photo_shots/', verbose_name='Изображение')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieslist.movie', verbose_name='Фильм')),
            ],
            options={
                'verbose_name': 'Кадр из фильма',
                'verbose_name_plural': 'Кадры из фильма',
            },
        ),
    ]
