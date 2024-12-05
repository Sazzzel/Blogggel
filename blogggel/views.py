from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment, Testimonial
from .forms import CommentForm, TestimonialForm

# Create your views here.


# def PostList(request):
#     testimonials = Testimonial.objects.filter(approved=True).order_by('-created_on')
#     queryset = Post.objects.filter(status=1)
#     post_list = Post.objects.all().order_by('-created_on')  # Adjust as necessary
#     paginate_by = 6
   

#     return render(request, 'blogggel/index.html', {
#     'post_list': post_list,
#     'testimonials': testimonials, 
#     'testimonial_form' : TestimonialForm(),
# })

def PostList(request):
    if request.user.is_authenticated:
        # approved testimonials and unapproved ones authored by the user
        testimonials = Testimonial.objects.filter(
            approved=True
        ) | Testimonial.objects.filter(
            author=request.user, approved=False
        )
    else:
        #only approved testimonials for unauthenticated users
        testimonials = Testimonial.objects.filter(approved=True)

    post_list = Post.objects.all().order_by('-created_on')

    return render(request, 'blogggel/index.html', {
        'post_list': post_list,
        'testimonials': testimonials,
        'testimonial_form': TestimonialForm(),
    })

def add_testimonial(request):

    if request.method == "POST":
        print("Received a POST request")
        testimonial_form = TestimonialForm(data=request.POST)
        if testimonial_form.is_valid():
            testimonial = testimonial_form.save(commit=False)
            testimonial.author = request.user
            testimonial.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Testimonial submitted and awaiting approval.'
            )
        return HttpResponseRedirect(reverse('home'))
    
    testimonial_form = TestimonialForm()
    print("About to render template")

    return render(
        request,
        "blogggel/index.html",
        {
            "testimonials": testimonials,
            "testimonial_form": testimonial_form
        },
    )

def testimonial_delete(request, testimonial_id):
    """
    view to delete testimonial
    """
    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)

    if testimonial.author == request.user:
        testimonial.delete()
        messages.add_message(request, messages.SUCCESS, 'Testimonial deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own testimonial!')

    return HttpResponseRedirect(reverse('home'))

    def comment_edit(request, slug, comment_id):
        """
        view to edit comments
        """
        if request.method == "POST":
            
            comment = get_object_or_404(Testimonial, pk=testimonial_id)
            

            if comment_form.is_valid() and comment.author == request.user:
                testimonial = testimonial_form.save(commit=False)
                testimonial.approved = False
                testimonial.save()
                messages.add_message(request, messages.SUCCESS, 'Testimonial Updated!')
            else:
                messages.add_message(request, messages.ERROR, 'Error updating testimonial')

        return HttpResponseRedirect(reverse('home'))




def post_detail(request, slug):

    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    

    if request.method == "POST":
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    
    comment_form = CommentForm()
    print("About to render template")

    return render(
        request,
        "blogggel/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form
        },
    )

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))