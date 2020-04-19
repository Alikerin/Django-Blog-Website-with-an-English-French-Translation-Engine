# @Author: Ibrahim Salihu Yusuf <yusuf>
# @Date:   2020-03-20T14:23:12+02:00
# @Email:  sibrahim1396@gmail.com
# @Last modified by:   yusuf
# @Last modified time: 2020-03-25T19:28:13+02:00

from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from .models import Post, Project
from django.views import generic
from django.utils import timezone
from .forms import CommentForm, UserInputForm
from django.shortcuts import render, get_object_or_404
import subprocess, os


class PostList(generic.ListView):
    model = Post
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_list"] = Post.objects.filter(status=1).order_by("-created_on")
        context["heading"] = "Welcome to My Blog"
        context["heading_text"] = "I am an enthusiastic Machine Learning Engineer"
        return context

class ProjectView(generic.ListView):
    model = Project
    template_name = "blog/projects.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_list"] = Project.objects.all()
        context["heading"] = "My Projects"
        context["heading_text"] = "This is a collection of projects I have worked on so far"
        return context

def project_detail_view(request, slug):
    template_name = "blog/project_detail.html"
    context = {}
    context["project"] = get_object_or_404(Project, slug=slug)
    context["heading"] = str(context["project"].title)
    context["heading_text"] = str(context["project"].title)[:15] + "..."
    context["output"] = None
    context["user_input_form"] = UserInputForm()
    if request.method == "POST":
        user_input_form = UserInputForm(data=request.POST)
        context["user_input_form"] = user_input_form
        if user_input_form.is_valid():
            # Create Comment object but don't save to database yet
            new_input = user_input_form.save(commit=False)
            # Assign the current post to the comment
            new_input.project = context["project"]
            # Save the comment to the database
            new_input.save()
            out = subprocess.run(["/home/yusuf/Documents/AMMI-NLP/Labs/Day2_NMT/c.FairSeq/translate-en-fr.sh", request.POST.get("input")], stdout=subprocess.PIPE)
            out = str(out.stdout.decode('utf-8')).rstrip()
            context["output"] = out #user_input_form.input
    return render(request, template_name, context)

def translate(request, slug):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = UserInputForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            # Create Comment object but don't save to database yet
            new_input = form.save(commit=False)
            # Assign the current post to the comment
            new_input.project = get_object_or_404(Project, slug=slug)
            # Save the comment to the database
            new_input.save()
            path = os.path.join(os.getcwd(), "blog/language/translate-en-fr.sh")
            out = subprocess.run([path, request.POST.get("input")], stdout=subprocess.PIPE)
            out = str(out.stdout.decode('utf-8')).rstrip()
            new_input.input = out #user_input_form.input

            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [ new_input, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


class AboutView(generic.TemplateView):
    template_name = "blog/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["heading"] = "About Me"
        context["heading_text"] = "My name is Ibrahim and I Love Machine Intelligence..."
        return context

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = "blog/post_detail.html"
#     context_object_name = ["post", "comments", "new_comment", "comment_form"]
#     def get_queryset(self):
#         """Return the last five published questions."""
#         post = Post.objects.filter(slug=self.kwargs['slug'])[0]
#         comments = post.comments.filter(active=True)
#         new_comment = None
#
#         if self.request.method == "POST":
#             comment_form = CommentForm(data=self.request.POST)
#             if comment_form.is_valid():
#                 # Create Comment object but don't save to database yet
#                 new_comment = comment_form.save(commit=False)
#                 # Assign the current post to the comment
#                 new_comment.post = post
#                 # Save the comment to the database
#                 new_comment.save()
#         else:
#             comment_form = CommentForm()
#
#         return post, comments, new_comment, comment_form

def post_detail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
