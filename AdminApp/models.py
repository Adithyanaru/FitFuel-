from django.db import models

# Create your models here.
class Category(models.Model):
    Name=models.CharField(max_length=100)
    Description=models.TextField()
    Image=models.ImageField(upload_to='category')
    def __str__(self):
        return self.Name
class ProductDb(models.Model):
    Pro_Name=models.CharField(max_length=100)
    Pro_Category=models.CharField(max_length=100)
    Pro_Prize=models.IntegerField()
    Pro_Description=models.TextField()
    Pro_Image=models.ImageField(upload_to='product')
    def __str__(self):
        return self.Pro_Name