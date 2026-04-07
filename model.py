from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    grade = models.IntegerField(default=1)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Enrollment(models.Model):
    student_name = models.CharField(max_length=255)

    def __str__(self):
        return self.student_name


class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.enrollment} - {self.question}"
