# Practice-task

Task management : https://task-api.atlassian.net/jira/software/projects/PT/boards/1

> Task 1:

- Create drf + postgreSQL + docker

> Task 2:

- Implement swagger UI
- Create 2 models: team and parcipinant
- Create endpoints: GET/POST/PUT/DELETE

> Task 3:

- Create Create folder for business logic
- Create CRUD for booking
- Create Validation for booking['POST'] endpoint

> Task 4:

- Create Unit test folder
- Create Unites to testing booking date_from field validation

> Task 5:

- Booking type model must have options setting limit of metting rooms
- Create endpoint get and edit Booking type limits
- Disable create create booking type when limit is reached
- Get a message when trying to create a booking type when the limit is exceeded

> Task 6:

Participant roles:
- Admin - ignores overlapping booking restrictions
- Admin, assistant - when booking can specify the id of another user on whose behalf booking
- User nothing changes

> Task 7:

- Testing endpoints with tst data are all is good working
- Create user Authentication
- Then create booking show what user make this booking

> Task 8:

- Team views update
- Use routers
- Create users endpoints
- Create url team
- Create url participant 
- Update get_xxx_count() function
