from django.db import models

# models to manage events
class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_date = models.DateTimeField(auto_now_add=True)
    feature_image = models.ImageField(upload_to="events")
    event_description = models.TextField()
    
    def __str__(self) -> str:
        return self.event_name

    class Meta:
        ordering = ('-event_date',)


class Registration(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.name


class Competition(models.Model):
    name = models.CharField(max_length=200)
    competition_date = models.DateTimeField(auto_now_add=True)
    feature_image = models.ImageField(upload_to = "Competitions")
    competition_description = models.TextField()
    winner_price = models.CharField(max_length=100)
    runner_up_price = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Competition_Registration(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.name