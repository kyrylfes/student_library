from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='media/default_avatar.jpg', upload_to='profile_avatars', blank=True)

    def __str__(self):
        return self.user.username


class Material(models.Model):
    title = models.CharField(max_length=300, verbose_name="Material title")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='own_books')
    readers = models.ManyToManyField(User, through='UserMaterial', related_name='books')
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=None, null=True, blank=True)
    description = models.TextField(max_length=6000, blank=True, null=True)
    material = models.FileField()

    def __str__(self):
        if self.owner is None:
            return f'{self.title}'

        return f'{self.title} - {self.owner.username}'

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'


class UserMaterial(models.Model):
    RATE_CHOICES = (
        (1, 'Погано'),
        (2, 'Норм'),
        (3, 'Норм+'),
        (4, 'Супер'),
        (5, 'Неймовірно')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)

    def __str__(self):
        return f'{self.user.username}: {self.material.title} RATE: {self.rate}'

    class Meta:
        verbose_name = 'UserMaterial'
        verbose_name_plural = 'UserMaterials'
