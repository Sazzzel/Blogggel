from django import forms
from .models import Comment, Testimonial 


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ('job_title', 'text', 'id')
 