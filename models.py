from django.db import models

DIVISION_CHOICE = (
    ('Barisal','Barisal'),
    ('Chittagong','Chittagong'),
    ('Dhaka','Dhaka'),
    ('Khulna','Khulna'),
    ('Mymensingh','Mymensingh'),
    ('Rajshahi','Rajshahi'),
    ('Rangpur','Rangpur'),
    ('Sylhet','Sylhet'),
    ('Cumilla','Cumilla'),
)


class BiodataModel(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    division = models.CharField(choices=DIVISION_CHOICE , max_length=50)
    city = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    siblings = models.PositiveIntegerField()
    profile_image = models.ImageField(upload_to='profileimg', blank=True)
    my_file = models.FileField(upload_to='doc', blank=True)

    def __str__(self):
        return self.name