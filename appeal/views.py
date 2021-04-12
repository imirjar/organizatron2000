from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Appeal
from .forms import AppealForm, AppealAnswerForm
from .services import appeal_generate_docx, check_bsk_info
from django.db.models import Q


def appeal(request):
    return render(request, 'appeal/appeal.html')

def appeal_create(request):
    # Если POST то получает данные формы и создает экземпляр модели Appeal
    if request.method == 'POST':
    	form = AppealForm(request.POST)
    	if form.is_valid():
    		appeal = Appeal()
    		appeal.appeal_num         = form.cleaned_data['appeal_num']
    		appeal.bsk_number         = form.cleaned_data['bsk_number']
    		appeal.appeal_create_date = form.cleaned_data['appeal_create_date']
    		appeal.appeal_owner_name  = form.cleaned_data['appeal_owner_name']
    		appeal.save()
    		return HttpResponseRedirect('/appeal/appeal_create')
    # Если GET предоставляет форму к заполнению c ссылкой на POST
    else:
        form = AppealForm()
    #Возвращает create.html с определенной формой <form>
    return render(request, 'appeal/create.html', {'form': form})

def appeal_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        context = Appeal.objects.filter(Q(bsk_number__icontains=search_query) | Q(appeal_num__icontains=search_query) | Q(appeal_owner_name__icontains=search_query))
    else:    
        context = Appeal.objects.all()
    return render(request, 'appeal/list.html', {'context': context,})

def appeal_edit(request, appeal_id):
    #Если POST то получает данные формы и переписывает ответ, и уберает подтверждения: правильности ответа и создания docx файла
    appeal = Appeal.objects.get(id=appeal_id)
    bsk_num = (str(appeal.bsk_number)[8:-1])
    info = check_bsk_info(bsk_num)

    bsk_in_black_list = info['black_list']
    bsk_in_send_payment = info['send_payment']
    
    if request.method == 'POST':
        form = AppealAnswerForm(request.POST)
        if form.is_valid():
            appeal.answer       = form.cleaned_data['answer']
            appeal.generated    = False
            appeal.accepted     = False
            appeal.save()
            return HttpResponseRedirect('/appeal/appeal_list')
    # Если GET то предоставляет форму для заполнения ответа
    else:
        form = AppealAnswerForm()
    return render(request, 'appeal/edit.html', {'appeal'            : appeal,
                                                'bsk_num'           : bsk_num,
                                                'form'              : form,
                                                'bsk_in_black_list' : bsk_in_black_list,
                                                'send_payment'      : bsk_in_send_payment,
                                                }
                                                )

def appeal_accept(request, appeal_id):
    appeal = Appeal.objects.get(id=appeal_id)
    appeal.accepted = True
    appeal.save()
    return HttpResponseRedirect('/appeal/appeal_list')

def appeal_generate(request, appeal_id):
    appeal = Appeal.objects.get(id=appeal_id)
    appeal.generated = True
    appeal_generate_docx(appeal)
    appeal.save()
    return HttpResponseRedirect('/appeal/appeal_list')