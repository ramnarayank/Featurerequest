# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from .models import Clients,FeatureReq
from .forms import CreateFeatureReq


def index(request):
    all_clients = Clients.objects.all()
    if request.method == "POST":

        form =CreateFeatureReq(request.POST)

        if form.is_valid():
            form.save(commit=False)
            for req in FeatureReq.objects.filter(
                    clients__name = form.cleaned_data['clients'],
                    clientpriority__gte = form.cleaned_data['clientpriority']):
                    req.clientpriority = req.clientpriority + 1
                    req.save()
        form.save()
        return redirect('app_feature_request:home')


    else:
        form = CreateFeatureReq()
    context = {'all_clients': all_clients, 'form': form}
    return render(request, 'app_feature_request/index.html', context)




