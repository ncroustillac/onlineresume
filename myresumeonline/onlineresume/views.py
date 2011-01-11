from django.template import Context, loader
from django.core import serializers
from django.http import HttpResponse

def index(request, content='home'):
    if request.is_ajax():
        print "Ajax request"
        from onlineresume.models import Education, Experience
        json_serializer = serializers.get_serializer("json")()
        if content in 'education':
            educations = Education.objects.all()
            c = Context({
                        'educations': educations,
                        })
        elif content in 'experience':
            experiences = Experience.objects.all()
            c = Context({
                        'experiences': experiences,
                        })
        t = loader.get_template('onlineresume/content_'+content+'.html')
        return HttpResponse(t.render(c))
    else:
        print "Http request"
        from onlineresume.models import Applicant, Education, Experience
        applicants = Applicant.objects.get()
        if content in 'education':
            educations = Education.objects.all()
            c = Context({
                        'educations': educations,
                        })
        elif content in 'experience':
            experiences = Experience.objects.all()
            c = Context({
                        'experiences': experiences,
                        })
        elif content in 'home':
            experiences = Experience.objects.all()
            educations = Education.objects.all()
            c = Context({
                        'educations': educations,
                        'experiences': experiences,
                        })
        else:
            c = Context()
        t = loader.get_template('onlineresume/content_wrapper.html')
        c['applicant'] = applicants
        c['content'] = 'onlineresume/content_'+content+'.html'
        return HttpResponse(t.render(c))

def education(request):
    if request.is_ajax():
        print "Ajax request"
        t = loader.get_template('onlineresume/content_education.html')
        c = Context({
                    'educations': educations,
                    })
        return HttpResponse(t.render(c))
    else:
        from onlineresume.models import Applicant, Education
        applicants = Applicant.objects.get()
        educations = Education.objects.all()
        t = loader.get_template('onlineresume/index_education.html')
        c = Context({
                    'applicant' : applicants,
                    'educations': educations,
                    })
        return HttpResponse(t.render(c))

def experience(request):
    if request.is_ajax():
        from onlineresume.models import Experience
        datas = serializers.serialize('json', Experience.objects.all(), ensure_ascii=False)
        return HttpResponse(datas, 'application/javascript')
    else:
        from onlineresume.models import Applicant, Experience
        applicants  = Applicant.objects.get()
        experiences = Experience.objects.all()
        t = loader.get_template('onlineresume/education.html')
        c = Context({
                    'applicant'   : applicants,
                    'experiences' : experiences,
                    })
        return HttpResponse(t.render(c))
