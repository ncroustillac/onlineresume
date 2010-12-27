from django.template import Context, loader
from django.core import serializers
from django.http import HttpResponse

def index(request, content='None'):
    if request.is_ajax():
        print "Ajax request"
        from onlineresume.models import Education, Experience
        json_serializer = serializers.get_serializer("json")()
        if content in 'education':
            educations = Education.objects.all()
            t = loader.get_template('onlineresume/content_education.html')
            c = Context({
                        'educations': educations,
                        })
            return HttpResponse(t.render(c))
        elif content in 'experience':
            experiences = Experience.objects.all()
            t = loader.get_template('onlineresume/content_experience.html')
            c = Context({
                        'experiences': experiences,
                        })
            return HttpResponse(t.render(c))
    else:
        print "Http request"
        # have to take care about possible arguments (education, ...)
        from onlineresume.models import Applicant
        applicants = Applicant.objects.get()
        t = loader.get_template('onlineresume/index_home.html')
        c = Context({
                    'applicant': applicants,
                    })
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
