# This file was auto-generated by Fern from our API Definition.

import typing
from .password_credential_response import PasswordCredentialResponse
from .credit_card_credential_response import CreditCardCredentialResponse

CredentialResponseCredential = typing.Union[PasswordCredentialResponse, CreditCardCredentialResponse]
