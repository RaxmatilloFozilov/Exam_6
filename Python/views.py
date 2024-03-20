from django.shortcuts import render,redirect
from .models import Topic,Item
from .forms import ItemForm,TopicForm

def topic_list(request):
    topics = Topic.objects.all()
    return render(request, "tajriba.html", {'topics': topics})
def user_list(request):

    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pswd')
        remember = request.POST.get('remember')


        return redirect('success')
    else:
        # If it's not a POST request, render the form template
        return render(request, 'learn-html.html')

    # return render(request, 'learn-html.html')

def table_list(request):
    return render(request, 'jadval.html')


def item_list(request):
    items = Item.objects.all()
    return render(request, 'crud/item_list.html', {'items': items})

def item_detail(request, pk):
    item = Item.objects.get(pk=pk)
    return render(request, 'crud/item_detail.html', {'item': item})

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'crud/item_form.html', {'form': form})

def item_update(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'crud/item_form.html', {'form': form})

def item_delete(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'crud/item_confirm_delete.html', {'item': item})


