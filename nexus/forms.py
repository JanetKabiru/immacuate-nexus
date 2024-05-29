from django import forms

class ContactForm(forms.Form):    
    full_name = forms.CharField()    
    email = forms.EmailField()   
    subject = forms.CharField() 
    message = forms.CharField(max_length=700, required=True,
    widget=forms.Textarea(attrs={'id':'floatingTextarea2', 'class':'form-control', 'style':'height: 100px'}))
    
    # reCAPTCHA token
    # token = forms.CharField(
    #     widget=forms.HiddenInput()
    # )

    def normalize_email(self, email):            
        # remove spaces at start and end of the and lowercase email address
        email = email.strip().lower()
        # split email into username and domain information
        username, domain = email.split('@')
        # remove . characters from username
        username = username.replace('.', '')
        #remove everything after +
        username = username.split('+')[0]

        return "%s@%s" % (username, domain)
        
    def clean_email(self):        
        email = self.cleaned_data.get('email')
        email = self.normalize_email(email)


        # with open("nexus/sus_email_providers.txt", 'r') as f:
        #     blacklist = f.read().splitlines()

        # for sus_email in blacklist:
        #     if sus_email in email:                
        #         raise forms.ValidationError("%s is not a valid email address. Kindly try another" % sus_email)

        return email