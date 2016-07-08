
### Slide Notes

Ryan's lecture notes for each slide are in the [original Google Slides document](https://docs.google.com/a/galvanize.com/presentation/d/1eT1KkCAmcTigXqQy6eMM7NzfVNby_SvASszQySRgcbU/edit?usp=sharing).


### Student Capstone Sprint Planning

Here is a __generic__ list of _stories_ and _tasks_ for a student capstone project. Each student should write stories and tasks that are __specific to their own project__.

```
Data preparation
 - do EDA
 - clean the data
 - transform the data (e.g. put it in matrix-form)
 - package the data-prep code & upload to github
 - document the process & upload to github

Preliminary modeling
 - run a (simple?) learning algorithm on the (subset?) dataset
 - get better results than random guessing
 - pickle the model pipeline
 - validate the model by loading the pickle file
 - package the training and validation code & upload to github
 - document the process & upload to github

EC2 instance to host the API
 - find and launch an appropriate AMI
 - customize the AMI
 - document the process & upload to github

The mock-API
 - design the interface (endpoint, parameters, return values)
 - write mock endpoints
 - write FINAL documentation
 - publish the documentation via flask-swagger and swagger-ui
 - deploy the mock API to AWS
 - test the mock API
 - communicate with WDI partner about where it is and how it works
 - publish the mock-API code to github
 - document the process & upload to github

For-realz modeling
 - find and launch an appropriate AMI
 - customize the AMI
 - upload the data
 - train several models using all the data
 - pickle the trained model pipeline
 - package the code & upload to github
 - document the process & upload to github

Version 1.0.0 API
 - write the code
 - deploy the API alongside the mock-API
 - test the API
 - publish the code to github
 - communicate with WDI partner

Showoff documentation
 - work with WDI partner to finalize the website
 - brainstorm the best way to tell the story
 - write a beautiful README.md for github
 - prepare a slidedeck
```

Students are encouraged to write as many stories as they can! Write the stories and tasks on sticky notes. These stories become the _product backlog_.

Then a _sprint planning meeting_ is held, where the instructor (playing the role of _product owner_) will prioritize the stories and help estimate _story points_ in order to create the _sprint backlog_.

![Product Backlog to Sprint Backlog](images/sprint_planning.png)

After the _sprint backlog_ is created, the student will build themselves a _scrum board_. Here are some example scrum boards:

![Example Scrum Boards](images/student_scrum_board_examples.jpg)


### Suggested Reading

The book, 'Scrum and XP from the Trenches', is free in PDF form.

See: https://www.infoq.com/minibooks/scrum-xp-from-the-trenches-2
