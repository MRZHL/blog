from django.http import HttpResponse
from TestModel.models import Test

def testdb(request):
    test1 = Test(name="Hua")
    test1.save()

    list = Test.objects.all()
    print(list)

    one = Test.objects.get(id=1)
    one.name = "祝化林"
    one.save()





    return HttpResponse("<p>数据添加成功！</p>")
