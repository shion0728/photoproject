from django.shortcuts import render

from django.views.generic import ListView
from .models import BlogPost

from django.shortcuts import render
from transformers import pipeline

class IndexView(ListView):
    template_name = 'index2.html'
    context_object_name = 'orderby_records'
    queryset = BlogPost.objects.order_by('-posted_at')
    
# Create your views here.

def gennsinn(request):
    return render(request, 'gennsinn.html')

def houkai(request):
    return render(request, 'houkai.html')

def apex(request):
    return render(request, 'apex.html')

def daigo5(request):
    return render(request, 'daigo5.html')

def varo(request):
    return render(request, 'varo.html')

def your_template(request):
    return render(request, 'your_template.html')


from django.shortcuts import render

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from django.conf import settings

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def line_webhook(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            handler.handle(body, signature)
        except Exception as e:
            print("Error handling webhook:", e)
        return JsonResponse({'status': 'ok'}, status=200)
    else:
        return JsonResponse({'status': 'failed'}, status=400)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # ユーザーからのメッセージに返信
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="こんにちは！ご質問がありますか？")
    )

from django.shortcuts import render

def line_redirect(request):
    return render(request, 'your_template.html')

# モデルのロード（デプロイでは事前ロードを推奨）
generator = pipeline('text-generation', model='gpt2')

def generate_text(request):
    if request.method == 'POST':
        user_input = request.POST.get('input_text')
        result = generator(user_input, max_length=50, num_return_sequences=1)
        generated_text = result[0]['generated_text']
        return render(request, 'ai_app/result.html', {'generated_text': generated_text})
    return render(request, 'ai_app/input.html')
