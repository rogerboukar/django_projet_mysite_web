from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=128)
    created_at = models.DateField(auto_now_add=True)
    progress = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.EmailField()
    object = models.CharField(max_length=128, blank=True)
    message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} {self.lastname} ({self.email})"


class Education(models.Model):
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE, related_name='educations')
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} at {self.institution}"


class Experience(models.Model):
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE, related_name='experiences')
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company}"


class Skill(models.Model):
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Resume(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    summary = models.TextField()

    def __str__(self):
        return self.name

