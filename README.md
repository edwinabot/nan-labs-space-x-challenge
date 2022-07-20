# The Space-x Challenge

The space-x team is designing their next launch to the international space station, they are recluting a group of the elite devs around the world and thought that you are gonna be a good fit. 



Preparations are needed and they want to start organizing their tasks management so they’ve encoment you with your first task. The developer team uses Trello as their task manager app, but their management team (the one that creates the tasks) don’t want to use it, it’s too complicated for them. Is your job to create a bridge between these two teams.



The management team wants an endpoint that they can use to create the tasks, there are 3 flavors this day, but this could change in the future. A task may be:

1.  **An issue:** This represents a business feature that needs implementation, they will provide a short title and a description. All issues gets added to the “To Do” list as unassigned
2.  **A bug:** This represents a problem that needs fixing. They will only provide a description, the title needs to be randomized with the following pattern: bug-{word}-{number}. It doesn't matter that they repeat internally. The bugs should be assigned to a random member of the board and have the “Bug” label.
3.  **A task:** This represents some manual work that needs to be done. It will count with just a title and a category (Maintenance, Research, or Test) each corresponding to a label in trello. 

You need to create a post endpoint that will receive the tasks definition form the management team and create the corresponding cards in Trello [API Introduction](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/) for the team to work with. Here are some examples:

![](https://lh3.googleusercontent.com/tJwah5NQYMbdeLB1zPH7ftZ3Fww8yFNaPQxLxdgS2wDcr6vkTYWTsGrtUxNQbLSKqzBuMk-SltAeEtaEufsu3iuwXRD5352diovLfF1Fz6kuexT0AuYrWmRBZ4dkP4Xe13KG_gPl=s0)


**Expected deliverables:**

Code must be uploaded in a git repository (preferably GitHub).

We need instructions on how to execute the application.

Good luck, have fun!

## Edwin's notes

I decided to base my solution on Django and its ecosystem for this challenge. Combined Django, Django REST Framework, and Django RQ. The reason is that Django allows for speedy prototyping and has decent performance should this grow. My strategy was to focus on rapid prototyping and testability, so I decided to build CI immediately and try to stick to TDD as much as possible. So you'll see GitHub Actions in place and several tests with and without mocks. As the implementation required, I Dockerized the entire solution to integrate with PostgreSQL and Redis.

To run this project, you'll need to install Docker and Docker Compose. Also, you'll need to set the `.env` file following the `.env.example` file at the root of this project. If you have that ready, you can run the project by executing the following:

```bash
$ docker compose up -d
$ docker compose run api python manage.py migrate
```

To run the tests you can execute:

```bash
$ docker compose run api python manage.py test --noinput trello_integration
```

Also, you can test the API with the Postman collections that I included in this repository in the `postman-collections` directory. You can import these in your Postman and play with them.

You have to set your To-Do Trello board with the expected Labels, and you'll need to retrieve that data; I've set up a Postman collection that you can utilize to retrieve them from the Trello API; a note about this process can be read in the Missing Features section.

### Missing Features

I found that we can register callbacks with the Trello API to know about the activity of the cards. It could be helpful to implement some feature that updates the Bugs, Issues, and Tasks with valuable info.

I also thought about storing Trello configurations. Different groups of people could utilize this system with different Trello Boards and accounts, and that would require keeping more user secrets in the database. So, encryption will be necessary for those fields, especially the Trello Token.


I could also have implemented a Django Command in order to retrieve all the requirements, or create them for the Trello Board. Right now, it is a very manual, error-prone process.

### On test coverage

Integration testing with Trello is lacking. Right now, the `test_trello_jobs.py` has almost no validations; test cases act as executors for the different jobs. At the very least, these tests prove the happy path and that the configuration for Trello is working.

API tests in `test_issue_dispatcher.py` could use some Fuzz Testing to look for edge cases derived from unexpected inputs: weird titles and descriptions.

### On Production Readiness

This implementation, to be production ready, requires at least the following:

* Authentication and Authorization, this API does not implement any right now. It could be helpful to use JWT tokens as a first solution.
* Remove secrets from `settings.py` and put them in safe storage, such as AWS Secrets Manager.
* Debug mode is on, it must be set to False in the prod environment.
* It needs a CD pipeline to deploy to different environments, such as staging and production.
