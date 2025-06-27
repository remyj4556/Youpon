from django.shortcuts import render, redirect
from .models import List
from .forms import CreateNewList
from django.http import HttpResponseForbidden



def index(request, page_id):
    ls = List.objects.get(id=page_id)

    # if the list (ls) is in the users lists
    if ls not in request.user.list.all():
        return HttpResponseForbidden("You're not allowed to access this list.")
        # the template (html file) passes a dictionary to the function with the information regarding buttons, checkboxes, etc.
        # i.e. {"save":["save"], "c1":["clicked"]}

    if request.method == "POST":

        # check for deletion
        for item in ls.item_set.all():
            if request.POST.get("delete_" + str(item.id)) == "pressed":
                item.delete()
                return redirect(f"/{page_id}")

        if request.POST.get("save") == "save":       # put name of form button in the quotes
            for item in ls.item_set.all():
                item.complete = request.POST.get("c" + str(item.id)) == "clicked"
                item.save()
            return redirect("/mylists") 

        if request.POST.get("newItem"):
            txt = request.POST.get("new")

            # this bool finds if any existing items match new (txt). only allows unique item names in list
            isNotInList = len(ls.item_set.filter(text=txt)) == 0

            if len(txt) > 2 and isNotInList:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid input")

    return render(request, "main/list.html", {"ls": ls})


def home(request):
    return render(request, "main/home.html", {})


def mylists(request):
    form = CreateNewList()

    if request.method == "POST":

        # deleting list objects
        for list in request.user.list.all():
            if request.POST.get("delete_"+str(list.id)) == "pressed":
                list.delete()
                return redirect("mylists")
        
        # creating new list object
        form = CreateNewList(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = List(name=n)
            t.save()
            request.user.list.add(t)
            return redirect(f"/{t.id}")
    
    return render(request, "main/mylists.html", {"form": form})


# here we first call naturalize.py to obtain clean names for user's list of items
# then we call another function (maybe recommend.py) that takes in the clean list and returns list of applicable Coupon objects
# this view then returns this list of Coupons to applicable.html and it presents them as cards
def applicable(request, page_id):
    ls = List.objects.get(id=page_id)

    if ls in request.user.list.all():
        return render(request, "main/applicable.html", {"ls": ls})