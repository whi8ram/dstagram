from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import redirect
# Create your views here.
from .models import Photo

def photo_list(request):
    # 보여줄 사진 데이터
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos':photos})

class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    def form_vaild(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})