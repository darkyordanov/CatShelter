from django.db import models


class Cat(models.Model):
    
    class Meta:
        abstract = True

    photo = models.ImageField(
        upload_to='cats/photos/'
    )
    
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    
    registration = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    
    color = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    
    date_of_birth = models.DateField()
    
    blood_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    
    research_genetic = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    
    research_blood = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    
    modified_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self) -> str:
        return self.name


class OurBoy(Cat):
    photo = models.ImageField(
        upload_to='cats/our_boys/'
    )


class OurGirl(Cat):
    photo = models.ImageField(
        upload_to='cats/our_girls/'
    )


class Kitten(Cat):
    photo = models.ImageField(
        upload_to='cats/kittens/'
    )