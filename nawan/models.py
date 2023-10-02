from django.db import models

# Create your models here.

# ประวัติพนักงาน
def history(models: NameError):
    history = models.CharField(max_length=128) # ประวัติพนักงาน

    def __str__(self):
        return self.history


# ข้อมูลส่วนตัวพนักงาน
def history(models: NameError):
    name = models.CharField(max_length=10) # ชื่อ,
    lastname = models.CharField(max_length=128) # นามสกุล,
    gender = models.IntegerField() #เพศ(ชาย / หญิง),
    year = models.IntegerField() # อายุ,
    educationlevel = models.IntegerField() # ระดับการศึกษา(ปวช./ปวส./ปริญญาตรี/สูงกว่าปริญญาตรี)   , 
    departmentofworkunder = models.CharField(max_length=255) # แผนกงานที่สังกัด,
    
    history = models.ForeignKey( history, on_delete=models.CASCADE) # ประวัติพนักงาน

    on_history = models.BooleanField(default=False) # แสดงผลประวัติพนักงาน

    def __str__(self):
        return self.name