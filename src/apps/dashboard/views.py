from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from src.apps.auth.models import User
from .models import ShortLink
from .forms import ShortLinkForm, ShortLinkUpdateForm
from .utils import generate_qr_code


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    login_url = '/auth/login/'
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        links = ShortLink.objects.filter(user=user).order_by('-created_at')

        

        context.update({
            'user': user,
            'form': ShortLinkForm(),
            'links': links,
            'total_links': links.count(),
            'total_clicks': sum(link.clicks for link in links),
            'active_links': links.filter(is_active=True).count(),
        })

        return context

    def post(self, request, *args, **kwargs):
        form = ShortLinkForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            ShortLink.create_short_link(user=request.user, original_url=original_url)
            return redirect('dashboard')
        else:
            user = request.user
            links = ShortLink.objects.filter(user=user).order_by('-created_at')
            context = {
                'user': user,
                'form': form,
                'links': links,
                'total_links': links.count(),
                'total_clicks': sum(link.clicks for link in links),
                'active_links': links.filter(is_active=True).count(),
            }
            return render(request, self.template_name, context)


class RedirectShortLinkView(generic.View):
    def get(self, request, short_code, *args, **kwargs):
        try:
            link = ShortLink.objects.get(short_code=short_code)
        except ShortLink.DoesNotExist:
            return render(request, '404.html', status=404)
        if not getattr(link, 'is_active', True):
            return render(request, 'dashboard/inactive_link.html', status=404)
        link.increment_clicks()
        return redirect(link.original_url)


class DeleteShortLinkView(LoginRequiredMixin, generic.View):
    login_url = '/auth/login/'

    def post(self, request, link_id, *args, **kwargs):
        link = get_object_or_404(ShortLink, id=link_id, user=request.user)
        link.delete()
        return redirect('/')
    

class ShortLinkDetailView(LoginRequiredMixin, generic.TemplateView):
    login_url = '/auth/login/'
    template_name = 'dashboard/link_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        link = get_object_or_404(ShortLink, id=kwargs.get('link_id'), user=user)
        context.update({
            'user': user,
            'link': link,
        })
        return context

class GenerateQRCodeView(LoginRequiredMixin, generic.View):
    login_url = '/auth/login/'

    def post(self, request, link_id, *args, **kwargs):
        link = get_object_or_404(ShortLink, id=link_id, user=request.user)
        generate_qr_code(link)
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
class UpdateShortLinkView(LoginRequiredMixin, generic.View):
    login_url = '/auth/login/'

    def post(self, request, link_id, *args, **kwargs):
        link = get_object_or_404(ShortLink, id=link_id, user=request.user)
        form = ShortLinkUpdateForm(request.POST, instance=link)
        print("Form Data:")
        print(form.data)

        if form.is_valid():
            form.save()
        return redirect('dashboard')