class user:
    def __init__(self,name,age,money) -> None:
        self._name=name
        self._age=age
        self.__money=money
    def money(self):
        return self.__money
    
nahin=user("nahin",19,36000)
print(nahin.money())