from PIL import Image
from django.shortcuts import render
from django.http import HttpResponseRedirect
from answersheet.forms import AnswerSheetUploadForm,AnswerKeyUploadForm
from answersheet.models import AnswerSheet, AnswerKey ,test_login_data
from answersheet import ocr_txt_result,summary,para_dir,get_key
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin/')
def uploadAnswerKey(request):
    if request.method == 'POST':
        form = AnswerKeyUploadForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            image = form.cleaned_data['image']
           
            text = ocr_txt_result.detect_document(image).text_annotations[0].description
            AnswerKey.objects.create(
                name=name,
                image=image,
                text=text
            )
            return render(request, 'uploaded.html')

    else:
        form = AnswerKeyUploadForm()

    return render(request, 'upload-answerkey.html', {'form': form})

@login_required(login_url='/admin/')
def uploadAnswerSheet(request):
    if request.method == 'POST':
        form = AnswerSheetUploadForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            image = form.cleaned_data['image']
            key = form.cleaned_data['answerKey']
            ocrtext = ocr_txt_result.detect_document(image).text_annotations[0].description
            sheet_dir=para_dir.create_dir(ocrtext)
            key_txt=key.text
            key_dir=para_dir.create_dir(key_txt)
            print("===========================")
            print(key_dir)
            key_val=get_key.get_key_val(key_dir)
            # key_no1=""
            # for key,value in key_dir:
            #     print("=$=")
            #     print(key)
            #     key_no1=key_no
            #     break
            print("===========================")
            marks = 15*ocr_txt_result.txt_comp(ocrtext, key.text)
            marks=round(marks,2)
            print("=================")
            # summ=summary.txt_summry(ocrtext)
            # for key,value in key_dir:
            #     if key.isnumeric():
            #         key1=key
            #         break
            # print("$$$$$$$$$$$$$$$")
            # print(key1)
            summ=summary.txt_summry(sheet_dir[key_val])
            #ob=AnswerSheet.objects.all()
            #check=[{str(summ)for summ in ob}]

            AnswerSheet.objects.create(
                key=key,
                image=image,
                marks=marks,
                summ=summ,
            )
            return render(request, 'result.html', {'key': key.name, 'summary':summ , 'marks': marks})

    else:
        form = AnswerSheetUploadForm()

    return render(request, 'upload-answersheet.html', {'form': form})

def login_page(request):
    txt=AnswerSheet.objects.all()
    print(txt[AnswerSheet])
    return render(request,'login.html')
def index_page(request):
    return render(request,'index.html')
def render_test_login(request):
    return render(request,'test_login.html')
def test_login_data_table(request):
    print("=================")
    print("++++++++++++++++")
    txt=test_login_data.objects.all()
    print(txt)
    return (request,'test_login_page_data.html')
@login_required(login_url='/admin/')
def home(request):
    return render(request,'upload-answersheet.html')