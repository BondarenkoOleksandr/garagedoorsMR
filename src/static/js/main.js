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
    redirect_uri: `https://garagedoors.fun/${redirectUri}`,
    prompt: 'select_account',
    access_type: 'offline',
    scope
  };
  const urlParams = new URLSearchParams(params).toString();

  window.location = `${googleAuthUrl}?${urlParams}`;
};


function sendReqFacebook(){
  const facebookAuthUrl = 'https://www.facebook.com/v12.0/dialog/oauth';
  const redirectUri = 'api/login/facebook/';

  const params = {
    response_type: 'code',
    client_id: '1013078522871763',
    redirect_uri: `https://garagedoors.fun/${redirectUri}`,
    state: "{st=state123abc,ds=123456789}",
    scope: 'email'
  };
  const urlParams = new URLSearchParams(params).toString();

  window.location = `${facebookAuthUrl}?${urlParams}`;
};
