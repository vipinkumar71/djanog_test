from django.shortcuts import render

# Create your views here.
from travello.models import Destination


def index(request):
    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.img="destination_1.jpg"
    dest1.desc = "The city that never sleeps"
    dest1.price = 700
    dest1.offer=False

    dest2 = Destination()
    dest2.name = "Hyderabad"
    dest2.img="destination_2.jpg"
    dest2.desc = "First Biryani, Then Sherwani"
    dest2.price = 1000
    dest2.offer=True


    dest3 = Destination()
    dest3.name = "Bengaluru"
    dest3.img = "destination_3.jpg"
    dest3.desc = "Beautiful city"
    dest3.price = 1500
    dest3.offer=False
    dests =[dest1,dest2,dest3]
    return render(request, "index.html", {"dests": dests})
