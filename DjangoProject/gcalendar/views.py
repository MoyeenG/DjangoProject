from django.shortcuts import render, render, redirect
from django.http import HttpResponse, JsonResponse

import google.oauth2.credentials
import google_auth_oauthlib.flow

import os
from urllib import parse

import requests

# Create your views here.

def auth(request):
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        '/home/moyeen/Desktop/client_secret.json',
        scopes=['https://www.googleapis.com/auth/calendar'])

    flow.redirect_uri = 'https://127.0.0.1:8000/oauth2callback/redirect'

    authorization_url, state = flow.authorization_url(
        # Enable offline access so that you can refresh an access token without
        # re-prompting the user for permission. Recommended for web server apps.
        access_type='offline',
        # Enable incremental authorization. Recommended as a best practice.
        include_granted_scopes='true')

    return redirect(authorization_url)

def get_token(request):
    #state = request.session['state']
    state = request.GET.get('state')
    print(state)
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        '/home/moyeen/Desktop/client_secret.json',
        scopes=['https://www.googleapis.com/auth/calendar'],
        state=state)
    flow.redirect_uri = "https://127.0.0.1:8000/oauth2callback/redirect"

    authorization_response = request.headers.get('Authorization')

    flow.fetch_token(authorization_response=authorization_response)
    credentials = flow.credentials
    request.session['credentials'] = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes}

