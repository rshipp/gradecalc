from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    section = models.CharField(max_length=50)
    instructors = models.CharField(max_length=200)

    class Meta:
        abstract = True


class PointsCourse(Course):
    points = models.PositiveIntegerField()


class PercentCourse(Course):
    pass


class Group(models.Model):
    name = models.CharField(max_length=200)
    percent = models.PositiveIntegerField()
    course = models.ForeignKey(PercentCourse)


class Assignment(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        abstract = True


class PointsAssignment(Assignment):
    group = models.ForeignKey(PointsCourse)
    points = models.PositiveIntegerField()


class PercentAssignment(Assignment):
    group = models.ForeignKey(Group)
    percent = models.PositiveIntegerField()
