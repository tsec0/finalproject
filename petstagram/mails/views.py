from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from accounts.models import UserProfile
from mails.forms import MailForm
from mails.models import IsRead, Mail


# @login_required()
# def mail_inbox(request):
#     user = request.user.id
#     context = {
#         'mail': Mail(),
#     }
#     return render(request, 'mail/mail_inbox.html', context)

# Should I create a mailbox or only filter my box. Should I create mailbox form?
@login_required
def mail_inbox(request, pk=None):
    receiver = request.user if pk is None else User.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'mails': receiver.userprofile.mail_set.all(),
        }
        return render(request, 'mail/mail_inbox.html', context)


def persist_mail(request, mail, template_name):
    if request.method == 'GET':
        mail.sender = request.user.username
        form = MailForm(instance=mail)
        context = {
            'form': form,
            'mail': mail,
            'is_read': mail.isread_set.filter(receiver_id=request.user.userprofile.id).exists()
        }
        return render(request, f'mail/{template_name}.html', context)
    else:
        form = MailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mail inbox')  # mail inbox
        context = {
            'form': form,
            'mail': mail,
            'is_read': mail.isread_set.filter(receiver_id=request.user.userprofile.id).exists()
        }
        return render(request, f'mail/{template_name}.html', context)


@login_required()
def preview_mail(request, pk):
    mail = Mail.objects.get(pk=pk)
    return persist_mail(request, mail, 'mail_edit')  # Mail edit template


@login_required()
def create_mail(request):
    mail = Mail()
    return persist_mail(request, mail, 'mail_create')  # Mail create template


@login_required
def delete_mail(request, pk):
    mail = Mail.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'mail': mail,
        }
        return render(request, 'mail/mail_delete.html', context)  # Mail delete template
    else:
        mail.delete()
        return redirect('mail inbox')  # inbox


@login_required()
def is_read(request, pk):
    read = IsRead.objects.filter(receiver_id=request.user.userprofile.id, mail_id=pk)
    if read:
        read.delete()
    else:
        mail = Mail.objects.get(pk=pk)
        read = IsRead(isread=str(pk), receiver=request.user.userprofile)
        read.mail = mail
        read.save()
    return redirect('edit mail', pk)  # inbox
