## Unity
Creating an email list with consent to target with promotional emails is a cost effective way to increase sales. Infact, studies have shown that email
marketing has ~42000% ROI. Unity is a simple seller tool that helps an online store maintain an email list. It consists of a widget installed an online store and a Django application which will provide the ability to manage these new customers.

![Seller Tool](cac-widget.png)

Here is the brief functionality of the seller tool
- A widget pops up on the online store and prompts the store visitor to signup using email address
- The signup data will be sent to an API provided by the Django app (Unity backend)
- The app stores the data in its own model
- The app exposes a view which 
	1.  lists down the emails in the reverse chronological order of their  timestamp
	2. Shows the number of new emails in the current calendar month
- The app sends an email to the seller every Monday and Wednesday including the statistics around the email list

## Installation
-   Install docker, docker-compose
-   Run ```docker-compose up -d --build```
-   The mailing list dashboard is at http://localhost:1337/subscribers/dashboard
-   Test widget page: <project_path>/unity/widgets/test/store.html
-   Check celery task log: ```docker-compose logs -f 'celery'```

