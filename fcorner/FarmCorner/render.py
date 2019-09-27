from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib import messages

def validate_file_size(value):
    filesize= value.size
    
    if filesize > 700000:
        messages.warning("The maximum file size that can be uploaded is 700kb")
    else:
        return value