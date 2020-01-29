### Set Up Dictionary Services 

Dictionary services is powered by an Oxford Dictionary API. We use the free tier as the subscription model. To set it up,
follow the steps given below:

1. Visit this [link](https://developer.oxforddictionaries.com/).

2. Click on "Get Your API Key". This should direct you to thier pricing page. Select "Prototype"

3. Fill in the form.
    
    * For the "Application Type" field, select "Bot".
    * For the "Platform" field, select "Desktop".
    * For the "Language" field, select "Python"

4. Ensure that you dont select "I would like to receive email or phone marketing from Oxford University Press.". Accept the 
Terms and Conditions and click on Send. 

5. A confirmation mail will be sent to your registered email address. Click on the link provided. Login into your account 
after redirection.

6. Once the Home Page opens, click on "Credentials". This redirects you to the credentials page.

7. Click on the link under the "Application name" column. This redirects to the credential details page.

8. Copy the App_id, App_key and base_url. Paste it in the keys.json file. 

You are good to go!
