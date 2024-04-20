# class student:
#     def __init__(self,name,cls,id):
#         self.name=name
#         self.id=id
#         self.cls=cls
        
# nahin=student("nahin","diploma",672751)
# print(nahin)
def call():
    print('calling someone i dont know')
    return 'call done'

class Phone:
    price = 12000
    color = 'blue'
    brand = 'samsung'
    features = ['camera', 'speaker', 'hammer']


    def call(self):
        print('calling someone i know')


my_phone = Phone()
call()