from django.shortcuts import render, redirect
from .models import List
from .forms import CreateNewList


def index(request, page_id):
    ls = List.objects.get(id=page_id)

    # if the list (ls) is in the users lists
    if ls in request.user.list.all():
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
    return render(request,"main/view.html", {})


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


def applicable(request, list_id):
    ls = List.objects.get(id=list_id)

    if ls in request.user.list.all():
        return render(request, "main/applicable.html", {"ls": ls})