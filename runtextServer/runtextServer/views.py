# myapp/views.py

import os
from django.http import FileResponse, Http404, JsonResponse
from .runningTextManim import generate_manim_video
from .models import Texts

def textrun(request):
    text = request.GET.get('text', 'Бегущая строка на Python')
    try:
        video_path = generate_manim_video(text)
        texts = Texts.objects.create(running_text=text)
        if os.path.exists(video_path):
            return FileResponse(open(video_path, 'rb'), content_type='video/mp4')
        else:
            raise Http404("Video not found")
    except Exception as e:
        raise Http404(f"Error generating video: {str(e)}")

def listOfText(request):
    texts = Texts.objects.all()
    texts_data = [{"text": text.running_text} for text in texts]
    return JsonResponse(texts_data, safe=False)