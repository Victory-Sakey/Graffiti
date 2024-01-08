# views.py
from .models import ContactFormSubmission , JoinCommunitySubmission
from .forms import ContactForm , JoinCommunityForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse


def Graffiti(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            
            person_email = form.cleaned_data['email']
            person_name = form.cleaned_data['name']
            person = ContactFormSubmission.objects.create(email=person_email, name=person_name)
            person.save()
            subject = 'Thank You for Contacting Us! (From Graffiti)'
            message = f"""
Hello {person.name},

Thank you for reaching out to us! We have received your message and appreciate the time you took to contact us.

Our team is reviewing your inquiry, and you can expect to hear back from us soon. We aim to respond within 3 to 4 days.

If your matter is urgent, please feel free to call us at +2348117869512.

Once again, thank you for considering us, and we look forward to assisting you.

Best regards,
Victory Sakey
Backend Developer
Graffiti Website

"""
            configured_email = settings.EMAIL_HOST_USER
            receiver = [person.email , settings.EMAIL_HOST_USER]
            
            send_mail(subject,message,configured_email,receiver,fail_silently=False)

         
            response_data = {
                'message': f"We've sent you an email, {person.name}, Thank you for contacting us!"
            }             
            return JsonResponse(response_data)


    else:
        form = ContactForm()

    return render(request, 'Graffiti.html', {'form': form})

'''
def Subscribe(request):
    if request.method == 'POST':
        subscribe = SubscribeForm(request.POST)
        if subscribe.is_valid:
            subscribe.save()

            reply = {
                "Your Submission was successful 😌"
            }

            return JsonResponse(reply)
    else:
            subscribe = SubscribeForm()
            return render(request, 'Graffiti.html', {'subscribe': subscribe})'''

def JoinCommunity(request):
    if request.method == 'POST':
        JcForm = JoinCommunityForm(request.POST)
        if JcForm.is_valid():
            jc_email = JcForm.cleaned_data['email']
            jc_name = JcForm.cleaned_data['name']
            jc_phone_number = JcForm.cleaned_data['Phone_number']
            jc = JoinCommunitySubmission.objects.create(email=jc_email, name=jc_name, Phone_number=jc_phone_number)
            jc.save()
            subject = "Welcome to Graffiti's Community!"
            message = f"""
Hi {jc.name},

On behalf of our entire community, I want to extend a warm welcome and express our gratitude for joining us.

Your presence adds tremendous value to our community, and we are excited to have you on board. We are currently in the process of expanding and actively working towards bringing more like-minded individuals into our community.

As we continue to grow, we will keep you updated on our progress and developments. Rest assured, once we have achieved our goal of bringing more people on board, we will be in touch with you again to discuss the next steps.

Thank you once again for being a part of our community. If you have any questions or if there's anything you'd like to share, feel free to reach out. We look forward to building a vibrant and engaging community together.

Best regards,
Victory Sakey
Backend Developer
Graffiti Website
"""
            configured_email = settings.EMAIL_HOST_USER
            receiver = [jc.email , settings.EMAIL_HOST_USER]
            
            send_mail(subject,message,configured_email,receiver,fail_silently=False)
                      
           
            return HttpResponseRedirect(reverse('Graffiti:Success', args=[jc_name]))


    else:
        JcForm = JoinCommunityForm()
    return render(request, 'JoinCommunity.html', {'JcForm': JcForm})

def Success(request, jc_name):
    success_name = jc_name
    success = success_name
    return render(request, 'success.html' , {'success': success})