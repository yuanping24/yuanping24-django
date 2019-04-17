from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def index(request):
    post = BlogPost.objects.order_by('pk')[0]
    request.session['addcount'] = [True] * BlogPost.objects.order_by('-pk')[0].pk
    try:
        nextpost = BlogPost.objects.get(pk=post.pk+1)
    except:
        nextpost = None
    posts = BlogPost.objects.order_by('-pk')[:5]
    hotposts = BlogPost.objects.order_by('-readcount')[:5]
    return render(request, "index.html", locals())

def post_blog(request, slug):
    try:
        post = BlogPost.objects.get(slug=slug)
        try:
            add_count = request.session.get('addcount')
        except:
            add_count = [True] * BlogPost.objects.order_by('-pk')[0].pk
        if add_count[post.pk-1]:
            post.readcount += 1
            add_count[post.pk-1] = False
            request.session['addcount'] = add_count
            post.save()
        nextpost_pk = post.pk + 1
        prepost_pk = post.pk - 1
        try:
            nextpost = BlogPost.objects.get(pk=nextpost_pk)
        except:
            nextpost = None
        try:
            prepost = BlogPost.objects.get(pk=prepost_pk)
        except:
            prepost = None
    except:
        post = None
    posts = BlogPost.objects.order_by('-pk')[:5]
    hotposts = BlogPost.objects.order_by('-readcount')[:5]
    return render(request, "post.html", locals())

def google_site_veri(request):
    return render(request, "google294c07ce6293992e.html")