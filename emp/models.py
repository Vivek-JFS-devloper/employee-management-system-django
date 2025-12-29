from django.db import models

class Emp(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=200)
    employee_id = models.CharField(max_length=50, unique=True, editable=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=200)
    date_of_joining = models.DateField()

    def save(self, *args, **kwargs):
        if not self.employee_id:
            self.employee_id = self.generate_employee_id()
        super().save(*args, **kwargs)

    def generate_employee_id(self):
        last_emp = Emp.objects.order_by('id').last()

        if last_emp and last_emp.employee_id:
            try:
                last_id = int(last_emp.employee_id.replace('EMP-', ''))
                new_id = last_id + 1
            except ValueError:
                new_id = 1
        else:
            new_id = 1

        return f"EMP-{new_id:03d}"

    def __str__(self):
        return f"{self.name} ({self.employee_id})"
