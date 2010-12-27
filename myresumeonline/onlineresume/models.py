from django.db import models

# Create your models here.
class Applicant(models.Model):
    GENDER_CHOICES = (
            (u'M', u'Male'),
            (u'F', u'Female'),
        )

    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    birth_date  = models.DateField()
    gender      = models.CharField(max_length=2, choices=GENDER_CHOICES)
    desc        = models.TextField()


    def __unicode__(self):
            return (self.first_name + self.last_name)

class SkillCategory(models.Model):
    applicant = models.ForeignKey(Applicant)
    title     = models.CharField(max_length=50)

    def __unicode__(self):
            return self.title

class Place(models.Model):
    name    = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city    = models.CharField(max_length=255)
    code    = models.IntegerField()
    website = models.URLField(verify_exists=False,max_length=255)

    def __unicode__(self):
            return self.name

class Education(models.Model):
    applicant  = models.ForeignKey(Applicant)
    desc       = models.TextField()
    place      = models.ForeignKey(Place)
    title      = models.CharField(max_length=50)
    start_time = models.DateField()
    end_time   = models.DateField()

    def __unicode__(self):
            return self.title

class Experience(models.Model):
    applicant  = models.ForeignKey(Applicant)
    desc       = models.TextField()
    place      = models.ForeignKey(Place)
    title      = models.CharField(max_length=50)
    start_time = models.DateField()
    end_time   = models.DateField()

    def __unicode__(self):
            return self.title

class Skill(models.Model):
    applicant = models.ForeignKey(Applicant)
    category  = models.ForeignKey(SkillCategory)
    title     = models.CharField(max_length=50)

    def __unicode__(self):
            return self.title

