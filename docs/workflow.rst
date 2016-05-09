Workflow
--------

It is impossible to create new user via auth-valimo endpoint - only login as existing.

* To start login process - issue POST request against **/api/auth-valimo/** endpoint with phone.

* On success request NodeConductor will create AuthResult object and start login process.
  AuthResult will contain field "message" that will be send to user via mobile.

* To get login process status - issue post request against **/api/auth-valimo/result/** with uuid in request data.
  Check endpoint docs for more details.

* On success login endpoint **/api/auth-valimo/result/** will provide auth token.