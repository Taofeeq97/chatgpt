from django.shortcuts import render
import random
import os
from django.conf import settings


def index(request):
    # Get a list of all the images in the static/img folder
    img_folder = os.path.join(settings.STATIC_ROOT, 'img')
    img_list = os.listdir(img_folder)
    img_list = [i for i in img_list if i.endswith('.jpg')]

    # Select a random image from the list
    random_img = random.choice(img_list)

    # Add the image to the context dictionary
    context = {'random_img': random_img}

    # Render the index.html template with the context
    return render(request, 'index.html', context)
