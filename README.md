# FINAL PROJECT

- [FINAL PROJECT](#final-project)
  - [📕1. หลักการทำงานโดยรวมของ Project](#1-หลักการทำงานโดยรวมของ-project)
  - [📕2. ความสัมพันธ์แบบ One-To-Many](#2-ความสัมพันธ์แบบ-one-to-many)
  - [📕3. Models](#3-models)
  - [📕4. Screen Capture](#4-screen-capture)
  - [📕5. การเชื่อมต่อฐานข้อมูลไปยัง Supabase ใน settings.py](#5-การเชื่อมต่อฐานข้อมูลไปยัง-supabase-ใน-settingspy)
  - [📕6. การเชื่อมต่อไปยัง Vercel](#6-การเชื่อมต่อไปยัง-vercel)
  - [💾 CREDIT](#-credit)

**--------------------------------------------------------------------------------------------------------**
## 📕1. หลักการทำงานโดยรวมของ Project
>**🔺[MYWEBAPPMODEL](https://github.com/Lynnn01/MyWebappModel/blob/main/README.md)**

## 📕2. ความสัมพันธ์แบบ One-To-Many
![enter image description here](https://cdn.discordapp.com/attachments/1026853768505081868/1158259820525269062/2023-10-02_113029.png?ex=651b9904&is=651a4784&hm=96c482497d423cf2ae6c9963e47362752b10e33c6cfbd4e8d647c40d0a026c81&)
>**🔺 ความสัมพันธ์แบบ one-to-many นั้นเป็นความสัมพันธ์ระหว่าง models เช่น พนักงาน 1 คน สามารถมีแผนกได้เพียงแผนกเดียวเท่านั้น แต่ว่าแผนก 1 แผนก สามารถมีพนักงานได้หลายคน**

## 📕3. Models

>**🔻 Model Department**
```py
class Department(models.Model):
    name = models.CharField(max_length=255)
    

    class Meta:
        verbose_name = ("Department")
        verbose_name_plural = ("Departments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed("Department_detail", kwargs={"pk": self.pk})

```
>**🔺 model Department โดยที่ 1 Department สามารถมีได้หลาย Employee**

**--------------------------------------------------------------------------------------------------------**

>**🔻 Model Employee**
```py
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
```
>**🔺 model Employee โดยที่ 1 Employee สามารถมีได้แค่ 1 Department เท่านั้น**