from django.db import models

# Create your models here.
class Recipe(models.Model):
    class Meta:
        db_table = "recipe"
    def __str__(self):
        return self.title
    title = models.CharField(max_length=100, null=False)
    img_url = models.ImageField(upload_to='uploads/')#CharField(max_length=200, default='')
    timecost = models.CharField(max_length=30, null=False)
    difficulty = models.CharField(max_length=30, null=False) #SET_NULL:필드값이 사라지면 Null로 바꾼다. null=True일때만 사용할 수 있다
    ingredient = models.TextField(null=False)
    cookstep = models.TextField(null=False)
    ##여기까지 form##
    recipe_author = models.CharField(max_length=100, default='') #User 생기면 ForeignKey로 꼭 바꿔줘야함!!!!!!
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Timecate(models.Model):
    class Meta:
        db_table = "timecost"
    def __str__(self):
        return self.timecost
    timecost = models.CharField(max_length=50, default='')

class Diffcate(models.Model):
    class Meta:
        db_table = "difficulty"
    def __str__(self):
        return self.difficulty
    difficulty = models.CharField(max_length=50, default='')
