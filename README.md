# Django-Fruit-Manager
This is a simple Django project on a local server. It is connected to a PostgreSQL database through pgadmin4. The project has 2 main models: Profile and Fruit. 
The website checks if there is a created profile. If the user hasn't created one, it opens a form which creates an instance of Profile (creates the profile). When the user is logged to his/her account they can ass fruits (instances of the Fruit model). They can also edit and delete their fruits (CRUD operations). 
Another functionality is the profile details page where the user can edit and delete the whole profile. When the profile is deleted, all the fruits dissapear. This is because the relation between the two models through a "ForeignKey".  

The index page:

<img width="650" alt="image" src="https://github.com/Max-Vassilev/Django-Fruit-Manager/assets/106106321/8b402f7b-40af-4d07-99fb-da61a7225ad3">

