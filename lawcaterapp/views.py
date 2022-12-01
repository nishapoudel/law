

from .models import Post, Category
from .forms import CommentForm, ContactForm
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from lawcaterapp.forms import ContactForm
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
# Create your views here.

def homepage(request):
    cats = Category.objects.all()
    posts = Post.objects.filter()[0:6]


    # featured = Post.objects.filter(featured=True)
    # latest = Post.objects.order_by('-timestamp')[0:3]
    context= {
        # 'object_list': featured,
        # 'latest': latest,

        'posts':posts,
        'cats':cats,
    }
    return render(request, 'index.html',context)




def team(request):
    return render(request, 'team.html')


# for post detail
def detail(request, slug):


    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    # post= Post.objects.get(slug=slug)
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
    return render(request, 'blog-detail.html', {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

    # context = {
    #     'post': post,
    # }
    # return render(request, 'blog-detail.html', context)

# def Blog (request ):
#     cats = Category.objects.get(cat_id = id)
#     posts=Post.objects.filter(category=cats)
#     posts = Post.objects.filter(categories__in=[category])
#     context = {
#         'cat':cats,
#         'posts': posts,
#     }
#     return render(request, 'blog.html')

#categorywise item
def postByCategory(request,slug):
    cats = Category.objects.all()
    cat=Category.objects.get(slug=slug)
    posts=Post.objects.filter(categories_id=cat)

    page =Paginator(posts, 6)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    # try:
    #     posts_page=all_post.page(page)
    # except PageNotAnInteger:
    #     posts_page = all_post.page(1)
    # except EmptyPage:
    #     posts_page= all_post.page(all_post.num_pages)


    return render(request, "blog.html",{'page':page,'cat':cat, 'posts':posts,'cats':cats})

def contact(request):
    return render(request, 'contact.html')


# def sendmail(request):
#     form = ContactForm(request.POST)
#     if form.is_valid():
#         subject = form.cleaned_data['subject']
#         message = form.cleaned_data['message']
#         sender = form.cleaned_data['sender']
#         cc = form.cleaned_data['cc']
#         recipients = ['urgenlama33@gmail.com']
#         recipients.append(sender)
#         send_mail(subject, message, sender, recipients)
#         return render(request,'home.html')

#     else:
#         form = ContactForm()
#         return render(request,'contact.html',{'form':form})

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         subject = "Website Inquiry"
#         body = {
# 			'first_name': form.cleaned_data['first_name'],
# 			'last_name': form.cleaned_data['last_name'],
# 			'email': form.cleaned_data['email_address'],
# 			'message':form.cleaned_data['message'],
# 			}
#         message = "\n".join(body.values())
#         send_mail(
#             subject,
#             message,
#             ['lawcaters@gmail.com'],
#             fail_silently=False,
#         )

#         return render(request,'contact.html')
#     else:
#         return render(request,'contact.html')
# def sendmail(request):
#     if request.method == 'POST':
#         subject = request.POST.get('subject', '')
#         message = request.POST.get('message', '')
#         from_email = request.POST.get('email', '')
#         send_mail(
#             subject,
#             message,
#             from_email,
#             ['lawcaters@gmail.com'],
#             fail_silently=False,
#         )

#         return render(request,'index.html')
#     else:
#         return render(request,'contact.html')
