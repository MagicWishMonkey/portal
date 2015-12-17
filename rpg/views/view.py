from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from portal.logger import log
from rpg import util



def private(func):
    enabled = False
    def inner(*args, **kwargs):
        request = args[0]
        if not request.user.id and enabled:
            if request.path.lower().startswith("/api/"):
                return View(request).write(
                    {"error": "You do not have permission to access this resource."},
                    status=403
                )

            return View(request).render("unauthorized.html")
        return func(*args, **kwargs)
    return inner


class View(object):
    def __init__(self, request):
        self.request = request
        self.session = request.session

    def login(self, username, password):
        user = authenticate(
            username=username,
            password=password
        )
        auth_login(self.request, user)
        self.session.set_expiry(7200)
        return True

    def redirect(self, uri, **params):
        if uri.find("/") > -1:
            return HttpResponseRedirect(uri)

        endpoint = reverse("rpg:%s" % uri)
        if params:
            buffer = []
            for key in params:
                val = params[key]

                if buffer:
                    buffer.append("&")
                if not val:
                    val = ""
                elif isinstance(val, bool):
                    val = str(val).lower()
                buffer.append("{0}={1}".format(key, val))
            querystring = "".join(buffer)
            endpoint = "{0}?{1}".format(endpoint, querystring)

        return HttpResponseRedirect(endpoint)

    def render(self, template, **kwargs):
        return render_to_response(
            template,
            kwargs,
            context_instance=RequestContext(self.request)
        )

    def write(self, data, **kwargs):
        content_type = kwargs.get('content-type', 'text/html')
        if isinstance(data, (dict, list)):
            content_type = 'application/json'
            data = util.json(data)

        status = kwargs.get("status", 200)
        return HttpResponse(data, content_type=content_type, status=status)

