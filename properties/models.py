from django.db import models
import uuid


class Property(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)
    path=models.URLField(max_length=200)
    title=models.CharField(max_length=250)
    location=models.CharField(max_length=250)
    image_url=models.URLField(max_length=200)
    price = models.CharField(default="", max_length=20,null=True)
    bathroom=models.CharField(max_length=2000)
    bedroom=models.CharField(max_length=2000)
    area=models.CharField(max_length=2000)
    description=models.CharField(max_length=2000)


    class Meta:
        verbose_name =("property")
        verbose_name_plural =("properties")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("property_detail", kwargs={"pk": self.pk})
