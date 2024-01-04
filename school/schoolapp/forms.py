
from django import forms
from .models import *


class MyForm(forms.ModelForm):
    materials_provide = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[
        ('notebook', 'Notebook'),
        ('pen', 'Pen'),
        ('exam_peppers', 'Exam Peppers'),
    ])
    class Meta:
        model = UserInform
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')