# Django-Fruit-Manager
This is a simple Django project on a local server. It is connected to a PostgreSQL database through pgadmin4. The project has 2 main models: Profile and Fruit. 
The website checks if there is a created profile. If the user hasn't created one, it opens a form which creates an instance of Profile (creates the profile). When the user is logged to his/her account they can ass fruits (instances of the Fruit model). They can also edit and delete their fruits (CRUD operations). 
Another functionality is the profile details page where the user can edit and delete the whole profile. When the profile is deleted, all the fruits dissapear. This is because the relation between the two models through a "ForeignKey".  
All the buttons in the header are functional. They appear in all of the pages because I used HTML page inheritance. So all of the pages extend the base page and inherit the header and the footer. 

The "index" page:

<img width="700" alt="image" src="https://github.com/Max-Vassilev/Django-Fruit-Manager/assets/106106321/8b402f7b-40af-4d07-99fb-da61a7225ad3">

The "create user" page:

<img width="700" alt="image" src="https://github.com/Max-Vassilev/Django-Fruit-Manager/assets/106106321/c3edb571-be4d-478d-92a2-2ff8c6c8f659">

The "profile dashboard" without any fruits:

<img width="700" alt="image" src="https://github.com/Max-Vassilev/Django-Fruit-Manager/assets/106106321/d837cfbd-b84c-49a5-bf6f-dc3e349b100e">

The "add fruit" functionality":

<img width="700" alt="image" src="https://github.com/Max-Vassilev/Django-Fruit-Manager/assets/106106321/9945608b-f933-4650-ba55-af723a962f2b">


The "profile dashboard" with added fruits:

<img width="700" alt="image" src="https://github.com/Max-Vassilev/Django-Fruit-Manager/assets/106106321/7d9ae663-e49d-4567-9d0e-1d52b05a860f">


"Fruit details" page:

<img width="700" alt="image" src="https://github.com/Max-Vassilev/Django-Fruit-Manager/assets/106106321/960b4fca-f848-47f8-8e9b-e2d401c73276">

"Fruit edit":

<img width="700" alt="image" src="https://github.com/Max-Vassilev/Django-Fruit-Manager/assets/106106321/a04a0d8e-2740-4709-8d2a-4d6a19bc83f2">

"Fruit delete":

<img width="700" alt="image" src="https://github.com/Max-Vassilev/Django-Fruit-Manager/assets/106106321/be11d2af-7d11-42ef-940d-dbde8f352858">




