from django.db import models

# Create your models here.
class questions(models.Model):
    question = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.question
    
    def get_ans(self):
        return self.Ans.all()

class Answer (models.Model):
    question = models.ForeignKey(questions, related_name="Ans", on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default = False)

    def __str__(self) -> str:
        return f"{self.question.question};{self.answer};{self.is_correct}"