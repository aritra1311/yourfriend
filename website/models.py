from django.db import models

# slider image for many to many field
class SliderImage(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    image = models.ImageField(
        upload_to='slider-images/', null=False, blank=False)

    def __str__(self):
        return self.name

# Actual Card
class Card(models.Model):
    card_name = models.CharField(max_length=250, null=False, blank=False)
    first_content = models.TextField()
    first_image = models.ImageField(
        upload_to='card-images/', null=False, blank=False)
    second_content = models.TextField()
    sliders = models.ManyToManyField(SliderImage, blank=True)

    def __str__(self):
        return self.card_name

# contact form
class ContactForm(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name

# Card Names
# ================
# Mental        ||
# Campaigns     ||
# Webinar       ||
# Internships   ||