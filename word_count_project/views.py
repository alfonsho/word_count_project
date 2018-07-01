from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'marco': "polo"})

def count(request):

    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    d = {}

    for word in wordlist:
        if word in d.keys():
            d[word] += 1
        elif word not in d.keys():
            d[word] = 1




    return render(request, 'count.html', {'fulltext':fulltext,
                                          'count': len(d.keys()),
                                          'd':d.items()})

def about(request):
    return render(request, 'about.html')