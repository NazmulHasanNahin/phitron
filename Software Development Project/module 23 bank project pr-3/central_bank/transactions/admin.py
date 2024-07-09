from django.contrib import admin
from transactions.views import send_mail_to_user

from .models import Transaction
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'balance_after_transaction', 'transaction_type', 'loan_approve']
    
    def save_model(self, request, obj, form, change):
        obj.account.balance += obj.amount
        obj.balance_after_transaction = obj.account.balance
        obj.account.save()
        send_mail_to_user(obj.account.user,obj.amount,"Loan Approval","transactions/loan_aprv_email.html")
        super().save_model(request, obj, form, change)