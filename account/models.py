from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File

def compress_image(img, file_format='webp', new_width=None, new_height=None):
    image = Image.open(img)
    width, height = image.size
    if new_width and new_height:
        image = image.resize((new_width, new_height))
    elif new_width:
        new_height = int(new_width / width * height)
        image = image.resize((new_width, new_height))
    elif new_height:
        new_width = int(new_height / height * width)
        image = image.resize((new_width, new_height))
    image_io = BytesIO()
    image.save(image_io, format=file_format, optimize=True)
    new_image = File(image_io, name=f"{img.name.split('.')[0]}.{file_format}")
    return new_image

class Employee(models.Model):
    name = models.CharField(max_length=30)
    education = models.CharField(max_length=300)
    location = models.CharField(max_length=100)
    age = models.IntegerField()
    job = models.CharField(max_length=300)
    main_image = models.ImageField(upload_to='images', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.main_image = compress_image(self.main_image,new_width=100)
        super().save(*args,**kwargs)

    @property
    def image_url(self):
        if self.main_image and hasattr(self.main_image, 'url'):
            print(f'==============================={self.main_image.url}')
            return self.main_image.url
        return 'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN'


    def __str__(self):
        return self.name
