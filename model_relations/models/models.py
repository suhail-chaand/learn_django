from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Cuisine(models.Model):
    CUISINE_CHOICES = [
            ('Indian','Indian'),
            ('Chinese','Chinese'),
            ('Italian','Italian'),
            ('Mexican','Mexican')
        ]

    cuisine = models.CharField(choices=CUISINE_CHOICES, default='Indian', max_length=20)
    dishes = models.TextField()

class Restaurant(models.Model):
    
    
    #One-To-One relation: 
    # A place can have only one resturant
    # A restuarant can only be at one place 
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    #ManyToMany relation:
    # A restuarant can offer MANY cuisine
    # A cuisine can be offered at MANY restuarants
    cuisine = models.ManyToManyField(Cuisine)

    def __str__(self):
        return self.place.name

class Waiter(models.Model):
    name = models.CharField(max_length=60)
    
    #Many-To-One relation:
    # A restuarant can have MANY waiters
    # A waiter can only work at ONE restuarant
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)