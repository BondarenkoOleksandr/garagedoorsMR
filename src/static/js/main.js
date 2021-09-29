function sendReq(){
  const googleAuthUrl = 'https://accounts.google.com/o/oauth2/v2/auth';
  const redirectUri = 'api/login/google/';

  const scope = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile'
  ].join(' ');

  const params = {
    response_type: 'code',
    client_id: '551586915430-tqjp7rsp2thrsp71sr9s3ukkb8nkf8eu.apps.googleusercontent.com',
    redirect_uri: `http://localhost:8008/${redirectUri}`,
    prompt: 'select_account',
    access_type: 'offline',
    scope
  };
  const urlParams = new URLSearchParams(params).toString();

  window.location = `${googleAuthUrl}?${urlParams}`;
};