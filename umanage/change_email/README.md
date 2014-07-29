Change Email
============
App for a user who wants to change their email.

Flow
====
1. Navigate to change email page
2. Enter required fields:
    1. user's password (for authorization purposes) 
    2. new email address
3. On email change request success, send two emails:
    1. send email to current email to notify account of change
    2. send email to the new email address which will provide a link to activate the new email and update the current user's associated email address
        1. Once the link is clicked, if the token is valid (not expired), update the email address and expire the token.