from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from .forms import UserRegistrationForm, DepositForm
from .models import UserProfile, BorrowingHistory
from book_app.models import Book
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


def send_mail_to_user(user, subject, template,amount=None):
    message = render_to_string(template, {
        "user": user,
        "amount":amount,
    })
    send_mail = EmailMultiAlternatives(subject, message, to=[user.email])
    send_mail.attach_alternative(message, "text/html")
    send_mail.send()


def register(rq):
    if rq.method == "POST":
        form = UserRegistrationForm(rq.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(rq, user)
            return redirect("profile")
    else:
        form = UserRegistrationForm()
    return render(rq, 'accounts/register.html', {'form': form})


@login_required
def profile(rq):
    user_profile = UserProfile.objects.get(user=rq.user)
    history = BorrowingHistory.objects.filter(user=rq.user)
    return render(rq, 'accounts/profile.html', {'user_profile': user_profile, 'history': history})


@login_required
def deposit(rq):
    if rq.method == 'POST':
        form = DepositForm(rq.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            user_profile = UserProfile.objects.get(user=rq.user)
            user_profile.balance += amount
            user_profile.save()
            send_mail_to_user(user_profile.user,"Deposit Successful","mails/deposit.html",amount)
            return redirect('profile')
    else:
        form = DepositForm()
    return render(rq, 'accounts/deposit.html', {'form': form})


@login_required
def borrow_book(request, book_id):
    book = Book.objects.get(id=book_id)
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.balance >= book.borrowing_price:
        user_profile.balance -= book.borrowing_price
        user_profile.save()
        BorrowingHistory.objects.create(user=request.user, book=book)
        send_mail_to_user(user_profile.user,"Borrowing Successful","mails/borrowing_book.html")
        messages.success(request, 'Book borrowed successfully!')
    else:
        messages.error(request, 'Insufficient balance to borrow this book.')
    return redirect('book_detail', book_id=book_id)



@login_required
def return_book(request, history_id):
    history = BorrowingHistory.objects.get(id=history_id, user=request.user, returned=False)
    if history:
        history.returned = True
        history.save()
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.balance += history.book.borrowing_price
        user_profile.save()
        send_mail_to_user(user_profile.user,"Book returned successfully!","mails/borrowing_book_return.html")
        messages.success(request, 'Book returned successfully!')
    return redirect('profile')



def login_view(rq):
    if rq.method == "POST":
        form=AuthenticationForm(rq,data=rq.POST)
        if form.is_valid():
            user=form.get_user()
            login(rq,user)
            return redirect("profile")
    else:
        form = AuthenticationForm()
    return render(rq, 'accounts/login.html', {'form': form})


@login_required
def logout_view(rq):
    logout(rq)
    return redirect('login')