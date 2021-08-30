from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='employees/', null=True)
    position = models.CharField(max_length=100)
    type_of_works = models.TextField()
    state = models.OneToOneField(to='employees.State', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name + ' - ' +self.position


class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Review(models.Model):
    STARS = (
        (1, 'Very bad'),
        (2, 'Bad'),
        (3, 'Normal'),
        (4, 'Good'),
        (5, 'Excellent'),
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    pub_date = models.DateField(auto_now_add=True)
    text = models.TextField()
    rating = models.IntegerField(choices=STARS, default=STARS[4])

    def __str__(self):
        return self.name + ' - ' + self.text[:35] + self.employee.name