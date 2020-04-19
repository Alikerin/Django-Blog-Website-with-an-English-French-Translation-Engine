# @Author: Ibrahim Salihu Yusuf <yusuf>
# @Date:   2020-03-21T10:11:25+02:00
# @Email:  sibrahim1396@gmail.com
# @Last modified by:   yusuf
# @Last modified time: 2020-03-27T12:38:47+02:00
from .models import Comment, UserInput
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment')
        widgets = {
            'comment': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}),
        }

class UserInputForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserInputForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = UserInput
        fields = ('input',)
