function sendReq(){
  const googleAuthUrl = 'https://accounts.google.com/o/oauth2/v2/auth';
  const redirectUri = 'api/login/google/';

  const scope = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile'
  ].join(' ');

  const params = {
    response_type: 'code',
    client_id: '486436967116-tiadudc1f9rmoj9c94rgp86q5ppks5pb.apps.googleusercontent.com',
    redirect_uri: `http://localhost:8000/${redirectUri}`,
    prompt: 'select_account',
    access_type: 'offline',
    scope
  };
  const urlParams = new URLSearchParams(params).toString();

  window.location = `${googleAuthUrl}?${urlParams}`;
};