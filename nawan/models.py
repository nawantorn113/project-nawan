from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=255)
    

    class Meta:
        verbose_name = ("Department")
        verbose_name_plural = ("Departments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed("Department_detail", kwargs={"pk": self.pk})


class Employee(models.Model):
    gender_choices = [
        ("ชาย", "ชาย"),
        ("หญิง", "หญิง"),
    ]
    qualification_choices = [
        ("ปวช.", "ปวช."),
        ("ปวส.", "ปวส."),
        ("ปริญญาตรี", "ปริญญาตรี"),
        ("สูงกว่าปริญญาตรี", "สูงกว่าปริญญาตรี"),
    ]
    name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    gender = models.CharField(
        max_length=50,
        choices=gender_choices,
        default=1,
    )
    age = models.IntegerField()
    qualification = models.CharField(
        max_length=50,
        choices=qualification_choices,
        default=1,
    )
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed("Employee_detail", kwargs={"pk": self.pk})