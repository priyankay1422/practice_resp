from flask import Flask, redirect, session ,url_for
from authlib.integrations.flask_client import OAuth
import os
from datetime import timedelta

app =Flask(__name__)
app.secret_key = 'snd.[fsd]f'
app.config['SESSION_COKIE_NAME']='login-session'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

# oAuth Setup
oauth = OAuth(app)

google = oauth.register(
    name='google',
    client_id="386408878883-elq0l3me8mknn8c5b8igqkd4o80urpnc.apps.googleusercontent.com",
    client_secret= "7pvtWfb35Ef5NDffY_v8vRdg",
    access_token_url='https://accounts.google.com/o/oauth2/token',
    #access_token_url='https://oauth2.googleapis.com/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'openid email profile'},
)

@app.route('/')
def home():
	email=dict(session).get('email',None)
	return f'hello,{email}!'

@app.route('/login')
def login():
    google = oauth.create_client('google')  # create the google oauth client
    redirect_uri = url_for('authorize', _external=True) #
    return google.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
	google=oauth.create_client('google')
	token=google.authorize_access_token()
	resp=google.get('userinfo',token = token)
	user_info=resp.json()
	user = oauth.google.userinfo()
	session['email']=user_info['email']
	session.permanent = True
	return redirect('/') 

@app.route('/logout')
def logout():
	for key in list(session.keys()):
		session.pop(key)
	return redirect('/')
	
if __name__ == '__main__':
     app.run()
