In simple token authentication, we have the power to delete it from the database manually by ourselves.

But in JWT authentication, we have fixed time limit of 5 minutes. after that we can do anything, but in between that 5 mins,we cannot revoke the access token. We can only revoke access by deleting the complete user.

JWT token can be stored in the local storage of browser, not in the database.

Throttling--> it works similar to Authenticationhere but in this feature we have the power to restrict the number of requesnts a user can send. it is important to restrict because if we have open api, there are chances that a bot will send and x number of requests. 
An important example of throttling is Medium.com. they only allow certain number of blog post reads. after that they ask us to create a free account.


**Filtering**
review_user__username=username
they come to 'username' userkey first and then comes to 'reviewuser' userkey.
'review_user' is only used when there is foreign key.
