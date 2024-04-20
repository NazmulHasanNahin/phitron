class calculator:
    brand_name="casio"
    def add(self,num1,num2):
        res=num1+num2
        print(res)
    def subtraction(self,num1,num2):
        res=num2-num1
        print(res)
    def multiply(self,num1,num2):
        res=num2*num1
        print(res)
    def division(self,num1,num2):
        res=num2/num1
        print(res)
    
calc=calculator()
calc.add(10,20)
calc.division(5,30)