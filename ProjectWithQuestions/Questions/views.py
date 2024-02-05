from django.shortcuts import render, redirect
from .models import Question
from django.db.models import Count


def index(request):
    q1 = Question.objects.all()
    q2 = (Question.objects.values('division', 'company')
          .annotate(company_count=Count('company')).order_by('-company_count'))
    context = {'q1': q1, 'q2': q2}
    if request.method == 'POST':
        form = request.POST
        division = form['select_division']
        company = form['select_company']
        if company == '':
            return redirect('index')
        if company == 'Другое':
            company = form['user_company']
        email = form['user_email']
        text = form['user_question']
        if division not in ["Топливный", "Машиностроительный", "ЯОК"] or text == '':
            return redirect('index')
        Question.objects.create(division=division, company=company, text=text, email=email).save()
        return redirect('index')
    return render(request, 'Questions/index.html', context=context)
