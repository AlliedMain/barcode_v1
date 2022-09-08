from django import forms
from .models import Subject,Lesson


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('__all__')

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('__all__')
