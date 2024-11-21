from django.db import models


class OurBoy(models.Model):
    photo = models.ImageField(
        upload_to='cats/our_boys'
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


class OurGirl(models.Model):
    photo = models.ImageField(
        upload_to='cats/our_girls/'
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


class Kitten(models.Model):
    photo = models.ImageField(
        upload_to='cats/kittens'
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


'''
    1. Photo
    2. Name
    3. Registration
    4. Color
    5. Date of Birth
    6. Blood Type
    7. Research (Genetic)
    8. Research (Blood)
'''