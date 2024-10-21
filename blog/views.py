from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Blog, Category
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import CommentForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import ContactForm

#İndex Page Content
def index(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True, is_home=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/index.html", context)

#All Blog Page Content
def blogs(request):
    blog_list = Blog.objects.filter(is_active=True)
    p = Paginator(Blog.objects.filter(is_active=True), 10)
    page = request.GET.get('page')
    blogs = p.get_page(page)
    categories = Category.objects.all()

    return render(request, 'blog/blogs.html',
        {
            'blog_list':blog_list,
            'blogs':blogs,
            'categories':categories
        })

#Blog Detail Page Content
def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comments = blog.comments.filter(active=True)
    new_comment = None
#---Comment Function
    # Comment bloged
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current blog to the comment
            new_comment.blog = blog
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, "blog/blog_detail.html", {   'blog': blog,
                                                        'comments': comments,
                                                        'new_comment': new_comment,
                                                        'comment_form': comment_form})

#Blog Category Page Content
def blogs_by_category(request, slug):
    blogs_category = Category.objects.get(slug=slug).blog_set.filter(is_active=True),
    p = Paginator(Category.objects.get(slug=slug).blog_set.filter(is_active=True), 5)
    page = request.GET.get('page')
    blogs = p.get_page(page)
    categories = Category.objects.all()

    return render(request, 'blog/blogs.html',
        {
            'blogs_category':blogs_category,
            'categories':categories,
            'selected_category':slug,
            'blogs':blogs
        })

#Search Page Content
def search_blog(request):
    search_key = request.GET.get('search', None)
    if search_key:
        blogs = Blog.objects.filter(title__icontains=search_key).distinct()
        if not blogs:
            message = "No results found."
        else:
            message = ""

        context = {
            "categories": Category.objects.all(),
            "blogs": blogs,
            "message": message
        }
        return render(request, 'blog/search.html', context)

#About Page Content
def about(request):
        context = {
           "about":about
        }
        return render(request, "blog/about.html", context)

#Contact Page Content
def contact(request):
        context = {
           "contact":contact
        }
        return render(request, "blog/contact.html", context)

#Contact Form İnformation
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
#-------Contact Form Content
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            html = render_to_string('contact/emails/contactform.html', {
                'name': name,
                'email':email,
                'content':content
            })

#-----------Mail App İnformation
            send_mail('the contact form subject','this is the massage', 'noreply@cartcurt.com',['hakan_@live.com'], html_message=html)
            
#-----------After Sending Message
            return redirect('index')
    
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form
    })