from django.contrib.auth.decorators import login_required
from django.http import (HttpResponse, HttpResponseNotFound,
                         HttpResponseBadRequest, HttpResponseServerError)