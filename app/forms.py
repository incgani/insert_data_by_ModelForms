from django import forms
from app.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=WebPage
        # fields='__all__'
        fields=['topic_name','name','email']
        labels={'topic_name':'TOPIC NAME','name':'NAME','email':'EMAIL'}
        #widgets={'name':forms.PasswordInput}
       # help_text={'name':'should not be interger'}


class AccessRecordsForm(forms.ModelForm):
    class Meta:
        model=AccessRecords
        fields='__all__'

