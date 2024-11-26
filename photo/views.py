from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import PhotoPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import PhotoPost
from django.views.generic import DetailView
from django.views.generic import DeleteView
# Create your views here.
class IndexView(ListView):
    template_name='index.html'
    queryset = PhotoPost.objects.order_by('-posted_at')
    paginate_by = 9

@method_decorator(login_required, name='dispatch')
class CreatePhotoView(CreateView):
    form_class = PhotoPostForm
    template_name = "post_photo.html"
    success_url = reverse_lazy('photo:post_done')
    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    template_name = 'post_success.html'
    
class CategoryView(ListView):
    template_name ='index.html'
    paginate_by = 9
    def get_queryset(self):
        category_id = self.kwargs['category']
        categorys = PhotoPost.objects.filter(
            category=category_id).order_by('-posted_at')
        return categorys
    
class UserView(ListView):
    template_name = 'index.html'
    paginate_by = 9
    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = PhotoPost.objects.filter(
            user=user_id).order_by('-posted_at')
        return user_list
    
class DetailView(DetailView):
    template_name = 'detail.html'
    model = PhotoPost
    
class MypageView(ListView):
    template_name = 'mypage.html'
    paginate_by = 9
    def get_queryset(self):
        queryset = PhotoPost.objects.filter(
            user=self.request.user).order_by('-posted_at')
        return queryset

class PhotoDeleteView(DeleteView):
    model = PhotoPost
    template_name = 'photo_delete.html'
    success_url = reverse_lazy('photo:mypage')
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
from django.shortcuts import render
from transformers import pipeline

# モデルのロード（デプロイでは事前ロードを推奨）
generator = pipeline('text-generation', model='gpt2')

def generate_text(request):
    if request.method == 'POST':
        user_input = request.POST.get('input_text')
        result = generator(user_input, max_length=50, num_return_sequences=1)
        generated_text = result[0]['generated_text']
        return render(request, 'ai_app/result.html', {'generated_text': generated_text})
    return render(request, 'ai_app/input.html')