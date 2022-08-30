from django.shortcuts import render
from django.views.generic import View
# Create your views here.
class centromedicoListView(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'centromedico_list.html', context)
