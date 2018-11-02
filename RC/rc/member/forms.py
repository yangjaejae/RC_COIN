class WebUserCreationForm(UserCreationForm):
    terms = forms.BooleanField(
        label=_('Terms of service'),
        widget=forms.CheckboxInput(
            attrs={
                'required': 'True',
            }
        ),
        error_messages={
            'required': _('You must agree to the Terms of service to sign up'),
        }
    )
    privacy = forms.BooleanField(
        label=_('Privacy policy'),
        widget=forms.CheckboxInput(
            attrs={
                'required': 'True',
            }
        ),
        error_messages={
            'required': _('You must agree to the Privacy policy to sign up'),
        }
    )

    def __init__(self, *args, **kwargs):
        # important to "pop" added kwarg before call to parent's constructor
        self.request = kwargs.pop('request')
        super(UserCreationForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super(WebUserCreationForm, self).save(commit=False)

        if commit:
            user.is_active = False
            user.save()

            # Send user activation mail
            current_site = get_current_site(self.request)
            subject = (_('Welcome To %s! Confirm Your Email') % current_site.name)
            message = render_to_string('registration/user_activate_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': PasswordResetTokenGenerator().make_token(user),
            })
            email = EmailMessage(subject, message, to=[user.email])
            email.send()

        return user