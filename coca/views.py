from decimal import Decimal
from django.urls import reverse
from http.client import HTTPResponse
import json
from django.shortcuts import render, redirect
from django.views import View
from django.core.serializers.json import DjangoJSONEncoder

from coca.utility import C_bat, M_Ec1, N_bat, N_panneau
from .models import Appareil, Devis, Devis_Appareil, InformationsInternaute
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

#Function to check if the user with email exist

class checkUserView(View):
    template  = "coca/email-form.html"
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated: 
            logout(request)  # Déconnecte l'utilisateur actuel
        return render(request, 'coca/login.html')

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        user = authenticate(username=email, password=email)
        if user is not None and user.is_active:
            login(request, user)
            return redirect(reverse('appliances'))
        return redirect('user_info', email)


def FromView(request):
    print(request.user)
    return render(request, 'coca/from.html')

class HomeView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'coca/index.html')

    def post(self, request, *args, **kwargs):
        return HTTPResponse('POST request!')
    
class AppliancesView(View):
    def get(self, request, *args, **kwargs):
        appliances = Appareil.objects.all
        context = {
            'appliances':appliances
        }
        print(request.user)
        return render(request, 'coca/appliance.html', context)

    def post(self, request, *args, **kwargs):
        data_appliances = []
        data_qte = []
        data_power = []
        data_hours = []
        # nb = request.POST.get('nombre_appareil')
        for champ, valeur in request.POST.items():
            if champ.startswith('appareil-'):
                data_appliances.append(Appareil.objects.get(pk = valeur))
            if champ.startswith('qte-'):
                data_qte.append(valeur)
            if champ.startswith('power-'):
                data_power.append(valeur)
            if champ.startswith('hour-'):
                data_hours.append(valeur)

        total = 0
        j = 0
        appliances = []
        # print(data_power)

        for i in data_appliances:
          
            total = total + (Decimal(data_power[j]) * Decimal(data_qte[j]) * Decimal(data_hours[j]))
            tmp = {
                'appliance':i,
                'quantity': data_qte[j],
                'power':data_power[j],
                'hour':data_hours[j]
            }
            # print("qte -------------")
            # print(data_qte[j])
            # print("power -------------")
            # print(data_power[j])
            appliances.append(tmp)
            j = j + 1
        print(total)
        internaute = User.objects.get(pk = request.user.id)
        internaute = internaute.internaute
        print(f"--------------------{internaute}")
        total = M_Ec1(total)
        print(f"--------------------{total}")

        # total = Decimal(total)
        devis = Devis.objects.create(internaute_temp = internaute, energie_T = total )

        for appliance in appliances :
            appliance_obj = appliance['appliance']
            qte = appliance['quantity']
            power = appliance['power']
            hour = appliance['hour']
            # energie_T = qte * power * hour
            devis_appareil = Devis_Appareil.objects.create(
                appareil = appliance_obj,
                devis = devis,
                quantite = qte,
                numHours = hour,
                power = power,
                # energie_T=energie_T
            )            
            devis_appareil.save()
        return redirect('get_coast', devis.pk)
        return render(request, 'coca/result_appliance.html')

# A partir des factures:

# class BillsView(View):
#     def get(self, request, *args, **kwargs):

#         return render(request, "coca/bills_coca.html")

#     def post(self, request, *args, **kwargs):
#         data_qte = []
#         total = 0
#         cmpt = 0
#         for champ, valeur in request.POST.items():
#             if champ.startswith('qte-'):
#                 data_qte.append(valeur)
#         for i in data_qte:
#             total +=  int(i)
#             cmpt = cmpt + 1
#         moy = total / cmpt
#         print(moy)

   
        
#         return render(request, 'coca/result_appliance.html')

def Apropos(request):

    return render(request, 'coca/apropos.html')

def Contact(request):
    
    return render(request, 'coca/contact.html')


class InfoUserView(View):
    
    def get(self, request, *args, **kwargs):
        email = kwargs['email']
        context={
            'email':email
        }
        
        return render(request, 'coca/register.html', context)

    def post(self, request, *args, **kwargs):
        email = kwargs['email']
       
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        addres = request.POST.get("addres")
        telephone = request.POST.get("telephone")
        
        country = request.POST.get("country")
        region = request.POST.get("region")
        town = request.POST.get("town")
        user = User.objects.create_user(username=email, password=email)
        data = {
            'nom': nom,
            'prenom':prenom,
            'email':email,
            'addres':addres,
            'telephone':telephone,
            'country': country,
            'region':region,
            'town':town,
            'user':user,

        }
        info_user = InformationsInternaute.objects.create(**data)
        user = authenticate(username=email, password=email)
        login(request, user)
        print(request)

        print(user)
        
        return redirect(reverse('appliances'))
    
class GetCoastView(View):
    def get(self, request, pk, *args, **kwargs):
        high_devis = Devis.objects.get(pk = pk)
        devis = Devis_Appareil.objects.filter(devis = high_devis)
        c_bat = C_bat(high_devis.energie_T)
        N_pan = N_panneau(high_devis.energie_T)
        n_bat = N_bat(c_bat)

        context = {
            'devis':devis,
            'nb_bat':n_bat,
            'c_bat':c_bat,
            'high_devis':high_devis,
            'n_panneau':N_pan
        }

        return render(request, 'coca/invoice.html', context)

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')
def get_appliance_power(request, appliance_id):
    appliance = Appareil.objects.get(pk=appliance_id)
    return JsonResponse({'power': appliance.power})
class RoleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'coca/role.html')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')