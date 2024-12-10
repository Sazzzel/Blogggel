from django import forms
from .models import Comment, Testimonial


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Modify existing field attributes
        self.fields['body'].widget.attrs.update({'class': 'form-control',
                                                'placeholder':
                                                    'Enter your comment'})
        self.fields['body'].label = "Comment:"  # Set the label


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ('job_title', 'text', 'id')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Modify existing field attributes
        self.fields['job_title'].widget.attrs.update({'class': 'form-control',
                                                     'placeholder':
                                                         'Your role...'})
        self.fields['text'].label = "Comment:"  # Set the label
