from audioop import reverse

from django.db import models


class Actor(models.Model):
    """Актеры"""
    name = models.CharField("Имя", max_length=200)
    age = models.IntegerField("Возраст")
    description = models.TextField("Информация")
    image = models.ImageField("Фотография", upload_to='Photo_actor/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актер"
        verbose_name_plural = "Актеры"

class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Название жанра", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Category(models.Model):
    """Категория"""

    name = models.CharField(max_length=250)
    description = models.TextField("Описание")
    url = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Movie(models.Model):
    """Фильм"""

    title = models.CharField('Название', max_length=100)
    tagline = models.CharField('Слоган', max_length=100)
    descriptions = models.TextField()
    poster = models.ImageField('фото', upload_to='Photo/', blank=True)
    year = models.DateField()
    country = models.CharField('Страна', max_length=255)
    directors = models.ManyToManyField(Actor, verbose_name='Режиссер', related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='Актеры', related_name='film_actor')
    genre = models.ManyToManyField(Genre, verbose_name='Жанры')
    world_premiere = models.DateField('Примьера в мире')
    budget = models.IntegerField('Бюджет', default=0, help_text='указывать сумму в долларах')
    fees_in_usa = models.IntegerField('Сборы в США', default=0, help_text='указывать сумму в долларах')
    fees_in_world = models.IntegerField('Сборы в мире', default=0, help_text='указывать сумму в долларах')
    category = models.ForeignKey(Category, verbose_name='Категори', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=150, unique=True)



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class MovieShots(models.Model):
    """Кадры из фильма"""
    title = models.CharField("Заголовок", max_length=255)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to='Photo_shots/')
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильма"


class Review(models.Model):
    """Отзывы"""
    email = models.EmailField("Емайл", blank=True)
    name = models.CharField('Имя', max_length=255)
    text = models.TextField("Сообщение")
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class RatingStar(models.Model):
    """Рейтинш звезды"""
    value = models.IntegerField("Значения", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'Звездв рейтинга'
        verbose_name_plural = 'Звезды рейтинга'
        ordering = ['-value']


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField('IP адрес', max_length=50)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE,
                             verbose_name='Звезда')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              verbose_name='фильм')

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
