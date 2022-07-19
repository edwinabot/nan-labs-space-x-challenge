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
