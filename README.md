# Backend Codebase for Projectree

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[**Projectree**](https://projectree.net/) is an open-source tool that helps you create and showcase your projects lists without the hassle of building it yourself. Just add your project details, choose a theme, and generate!


## Routes
- [x] **/auth/register**: User can register and sends user a verification token.
- [x] **/auth/login**: User can log in with the right information.
- [x] **/projectree**: User can create a projectree 
- [x] **​/projectree​/{projectree_id}**: User can view a projectree by ID
- [x] **delete-projectree/{projectree_id}/**: User can delete a projectree by ID 
- [x] **/update-projectree/{projectree_id}/**: User can update a projectree by ID
- [x] **/get-user-projectree**: User can get all projectree for a user
- [x] **/project**: User can create a project
- [x] **/delete-projectr/{projectr_id}/**: User can delete a project by ID
- [x] **/delete-project/{project_id}/**: User can delete a project by ID
- [x] **/publish-projectree/{projectree_id}**: User can publish the projectree by sending the ID
- [x] **/view-publish/{publish_name}**: User can view the publish project by sending the name.


The full API documentation is available here: https://projectree-app.herokuapp.com/docs/


## Prerequisites

1. Clone the repository and run:

 `git clone https://github.com/Sophyia7/projectree-backend`

2. Install all dependencies by running the following command:

`pip install -r requirements.txt`

3. To run the server locally, run the following command:

`python manage.py runserver`

4. Add your changes to the codebase 

5. Add a secret key to your local .env file and use a local database connection to test your changes locally. 

6. Create a new branch with your github username as the name of branch. E.g: 

`git checkout -b Sophyia7`

7. Lastly, push your changes to the branch and create a pull request.


Happy coding! 

## Created for the [PlanetScale](https://planetscale.com/?utm_source=hashnode&utm_medium=hackathon&utm_campaign=announcement_article) x [Hashnode](https://hashnode.com/?source=planetscale_hackathon_announcement) [Hackathon](https://townhall.hashnode.com/planetscale-hackathon?source=projectree_frontend_github)



