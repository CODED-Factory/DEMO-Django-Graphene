from django.db import models


class Isntructor(models.Model):
    name = models.CharField(max_length=240)
    name_ar = models.CharField(max_length=240)
    bio = models.CharField(max_length=240)
    bio_ar = models.CharField(max_length=240)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=240)
    name_ar = models.CharField(max_length=240)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Bootcamp(models.Model):
    name = models.CharField(max_length=240)
    name_ar = models.CharField(max_length=240)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Cohort(models.Model):
    start_date = models.DateField()
    name = models.CharField(max_length=240)
    name_ar = models.CharField(max_length=240)

    instructors = models.ManyToManyField(
        Isntructor, related_name="cohorts", through="Role")

    def __str__(self):
        return self.name


class Role(models.Model):
    instructor = models.ForeignKey(
        Isntructor, related_name="roles", on_delete=models.CASCADE)
    cohort = models.ForeignKey(Cohort, related_name="roles",
                               on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic
