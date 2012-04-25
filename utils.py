# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import View
from django.core.urlresolvers import reverse


class ProtectedView(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedView, self).dispatch(*args, **kwargs)


class AuthorProtectedView(ProtectedView):
    def dispatch(self, *args, **kwargs):
        post = self.get_queryset()

        if not post.author != self.request.user:
            return redirect('access_denied')

        return super(AuthorProtectedView, self).dispatch(*args, **kwargs)
