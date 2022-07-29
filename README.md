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

## Created for the [PlanetScale](https://planetscale.com/?utm_source=hashnode&utm_medium=hackathon&utm_campaign=announcement_article) x [Hashnode](https://hashnode.com/?source=planetscale_hackathon_announcement) [Hackathon](https://townhall.hashnode.com/planetscale-hackathon?source=projectree_frontend_github)



