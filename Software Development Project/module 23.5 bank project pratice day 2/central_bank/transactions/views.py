# Import necessary modules
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from decimal import Decimal
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView
from transactions.constants import DEPOSIT, WITHDRAWAL, LOAN, LOAN_PAID
from datetime import datetime
from accounts.models import UserBankAccount, BankruptcyStatus
from django.db.models import Sum
from transactions.forms import DepositForm, WithdrawForm, LoanRequestForm
from transactions.models import Transaction


def send_mail_to_user(user,amount ,subject, template,sender_name=None,receiver_name=None):
    message = render_to_string(template, {
        "user": user,
        "amount": amount,
        "sender_name":sender_name,
        "receiver_name":receiver_name,
    })
    send_mail = EmailMultiAlternatives(subject, message, to=[user.email])
    send_mail.attach_alternative(message, "text/html")
    send_mail.send()


class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = 'transactions/transaction_form.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('transaction_report')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title
        })
        return context


class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = 'Deposit'

    def get_initial(self):
        initial = {'transaction_type': DEPOSIT}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount
        account.save(update_fields=['balance'])

        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))} was deposited to your account successfully'
        )
        send_mail_to_user(self.request.user, amount, "Deposit Message", "transactions/deposite_email.html")
        return super().form_valid(form)


class WithdrawMoneyView(TransactionCreateMixin):
    form_class = WithdrawForm
    title = 'Withdraw Money'

    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.template_name)

    @method_decorator(login_required)
    def post(self, request):
        from_account = request.user.account
        amount = Decimal(request.POST.get('amount', 0))

        bankruptcy_status = BankruptcyStatus.objects.first()
        if bankruptcy_status and bankruptcy_status.is_bankrupt:
            messages.error(request, "The bank is bankrupt. Withdrawals are not allowed.")
            return redirect('withdraw_money')

        if from_account.balance >= amount:
            from_account.balance -= amount
            from_account.save(update_fields=['balance'])

            messages.success(request, f'Successfully withdrawn {"{:,.2f}".format(float(amount))} from your account')
            send_mail_to_user(self.request.user, amount, "Withdrawal Message", "transactions/withdrawal_email.html")
        else:
            messages.error(request, "Insufficient funds.")

        return redirect('withdraw_money')


class LoanRequestView(TransactionCreateMixin):
    form_class = LoanRequestForm
    title = 'Request For Loan'

    def get_initial(self):
        initial = {'transaction_type': LOAN}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        current_loan_count = Transaction.objects.filter(
            account=self.request.user.account, transaction_type=3, loan_approve=True).count()
        if current_loan_count >= 3:
            return HttpResponse("You have crossed the loan limits")
        messages.success(
            self.request,
            f'Loan request for {"{:,.2f}".format(float(amount))}$ submitted successfully'
        )
        send_mail_to_user(self.request.user, amount, "Loan request Message", "transactions/loan_rq_email.html")
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class TransactionReportView(LoginRequiredMixin, ListView):
    template_name = 'transactions/transaction_report.html'
    model = Transaction
    balance = 0

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            account=self.request.user.account
        )
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')

        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

            queryset = queryset.filter(
                timestamp__date__gte=start_date, timestamp__date__lte=end_date)
            self.balance = Transaction.objects.filter(
                timestamp__date__gte=start_date, timestamp__date__lte=end_date
            ).aggregate(Sum('amount'))['amount__sum']
        else:
            self.balance = self.request.user.account.balance

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account': self.request.user.account
        })

        return context


class PayLoanView(LoginRequiredMixin, View):
    def get(self, request, loan_id):
        loan = get_object_or_404(Transaction, id=loan_id)
        if loan.loan_approve:
            user_account = loan.account
            if loan.amount < user_account.balance:
                user_account.balance -= loan.amount
                loan.balance_after_transaction = user_account.balance
                user_account.save()
                loan.loan_approved = True
                loan.transaction_type = LOAN_PAID
                loan.save()
                return redirect('transactions:loan_list')
            else:
                messages.error(self.request, "Loan amount is greater than available balance")

        return redirect('loan_list')


class LoanListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/loan_request.html'
    context_object_name = 'loans'

    def get_queryset(self):
        user_account = self.request.user.account
        queryset = Transaction.objects.filter(account=user_account, transaction_type=3)
        return queryset


class TransferAmountView(View):
    template_name = 'transactions/transfer.html'

    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.template_name)

    @method_decorator(login_required)
    def post(self, request):
        from_account = request.user.account
        to_account_no = request.POST.get('to_account_no')
        amount = Decimal(request.POST.get('amount', 0))

        try:
            to_account = UserBankAccount.objects.get(account_no=to_account_no)
        except UserBankAccount.DoesNotExist:
            messages.error(request, "Account not found.")
            return render(request, self.template_name)

        if from_account.balance >= amount:
            from_account.balance -= amount
            to_account.balance += amount

            from_account.save(update_fields=['balance'])
            to_account.save(update_fields=['balance'])

            Transaction.objects.create(
                account=from_account,
                amount=-amount,
                balance_after_transaction=from_account.balance,
                transaction_type=2
            )
            Transaction.objects.create(
                account=to_account,
                amount=amount,
                balance_after_transaction=to_account.balance,
                transaction_type=2
            )
            sender_name = f"{request.user.first_name} {request.user.last_name}"
            receiver_name = f"{to_account.user.first_name} {to_account.user.last_name}"
            send_mail_to_user(request.user, amount, "Money Transfer Message", "transactions/money_transfer_mail.html", sender_name, receiver_name)
            send_mail_to_user(to_account.user, amount, "Money Transfer Received", "transactions/money_received_mail.html", sender_name, receiver_name)
            messages.success(request, "Transfer successful.")
        else:
            messages.error(request, "Insufficient funds.")

        return redirect('transfer_amount')
