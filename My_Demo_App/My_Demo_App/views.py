from django.http import HttpResponse
import datetime 
def test(requests):
    date = datetime.datetime.now()
    print("hello i am the test function")
    return HttpResponse("<h1>hello</h1>" + str((date)))

def about(requests):
    date = datetime.datetime.now()
    print("hello from about")
    return HttpResponse("<h1>hello from about page</h1>" + str((date)))