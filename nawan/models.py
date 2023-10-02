from django.db import models

# Create your models here.

# ประวัติพนักงาน
 history(models.Model):
     history = models.CharField(max_length=128) # ประวัติพนักงาน

    def __str__(self):
        return self. history


# ข้อมูลส่วนตัวพนักงาน
personal information personal informations(models.Model):
    name = models.CharField(max_length=10) # ชื่อ
    last name = models.CharField(max_length=128) # นามสกุล
    gender = models.IntegerField() #เพศ(ชาย / หญิง)
    year = models.IntegerField() # อายุ
    education level = models.IntegerField() # ระดับการศึกษา(ปวช./ปวส./ปริญญาตรี/สูงกว่าปริญญาตรี)    
    department of work under = models.CharField(max_length=255) # แผนกงานที่สังกัด
    
    history = models.ForeignKey( history, on_delete=models.CASCADE) # ประวัติพนักงาน

    on_personal history = models.BooleanField(default=False) # แสดงผลประวัติพนักงาน

    def __str__(self):
        return self.name