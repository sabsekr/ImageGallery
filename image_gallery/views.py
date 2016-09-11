from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, render
from django.template import RequestContext
from django.views import generic
from django.views.generic import FormView
from image_gallery.forms import ImageUploadForm
from image_gallery.models import Photo

"""
The view contain the logic necessary to return a response to a Web request.
"""

"""
The IndexView returns all saved Photo objects from the database. A page to represent a list of objects.
"""
class IndexView(generic.ListView):
    template_name = "image_gallery/index.html"
    context_object_name = "photo_list"

    """
    Returns the queryset that will be used to retrieve the object that this view will display.
    """
    def get_queryset(self):
        return Photo.objects.all()

"""
The ShowPhotoView is a view which operates and displays the Photo object. The Photo model
is passed to the template's context
"""

class ShowPhotoView(generic.DetailView):
    model = Photo
    template_name = "image_gallery/show_photo.html"



"""
Handles uploading of the images.
"""
def upload_pic(request):

    """
    :param request: the Web request
    :return: Combines a given template with a given context dictionary and
    returns an HttpResponse object with that rendered text.
    """
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_photo = Photo(image_upload=request.FILES['image_upload'], tag_text=request.POST['tag_text'])
            new_photo.save()
            """
             Redirect to the image list after POST
            """
            return HttpResponseRedirect(reverse('upload_pic'))
    else:
        form = ImageUploadForm()  # A empty, unbound form

        # Render list page with the documents and the form
    context = {'form': form}
    return render(request, 'image_gallery/add.html', context)


# def add(request):
#     #    return HttpResponse("You are adding a photo.")
