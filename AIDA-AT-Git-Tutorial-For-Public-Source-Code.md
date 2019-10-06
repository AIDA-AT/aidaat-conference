Dear researchers,

Wellcome to AIDAAT Conference,

Here is the simple tutorial how you public your source-code to AIDA-AT, after your paper have been accepted.

# *** Requirements ***

1. Knowlegde in Git.
2. Github account. 

Watch these video to get overview about git and github : 

https://www.youtube.com/watch?v=sz6zfrQpCQg (What is Git | What is GitHub | Git Tutorial | GitHub Tutorial | Devops Tutorial | Edureka)

https://www.youtube.com/watch?v=xuB1Id2Wxak (GitHub Learning Lab: Introduction to GitHub Walkthrough)

You can explore more from reference resources:
- https://www.datacamp.com/courses/introduction-to-git-for-data-science
- https://lab.github.com/githubtraining/introduction-to-github
- google for more :-D


# Step by step

1. Go to AIDA-AT Conference GitHub repo : https://github.com/aidaat/aidaat-conference

2. Fork it to your git,


3. Clone the forked git repo to your local machine:
    For example, suppose this is my forked-repo from AIDA-AT, I will clone it to my local machine:
    
    ``` cd ~ ```  # go to home directory, or your working space.
    
    ``` git clone git@github.com:aidaat/aidaat-conference.git ```
    
4. Go to the clone repo directory, add your working results (source-code, pictures, documenation for reproduce experiments):
    
    ``` cd aidaat-conference/AIDA-AT2020 ```
    
    ``` git pull origin master ``` # make sure you get the latest updates.
    
    ## create a new branch for your work
    
    ``` git checkout -b <your-branch-name> ```
    
    `<your-branch-name>` should be short, clear and informative, follow this pattern `aida-at-2020-paper-id-xxx`, where xxx is your accepted paper ID.
    
    In my case, it will be: ``` git checkout -b aida-at-2020-paper-id-000 ```
    
    ## go to your paper ID folder, for example in my case: `PID_000`
    
    ## copy all your source code, sample data to this folder
    
    `BE NOTICED THAT: YOU MUST WORK INSIDE YOUR FOLDER BELONG TO YOUR PAPER ID ONLY, DO NOT CHANGE ANYTHING OUTSIDE YOUR PAPER ID FOLDER`
    
    ## add and commit your works
    
    ``` git add PID_000/ ```
    
    ``` git commit -m "<aida-at-2020-paper-id-xxx>" ```
    In my case: ``` git commit -m "aida-at-2020-paper-id-000"```
    
    ``` git push origin <your-branch-name> ```
    In my case: ``` git push origin aida-at-2020-paper-id-000 ```
    
5. Goto your forked repo on Github, create the pull-request to AIDA-AT follow these pictures below:
    
    <picture>
    
    <picture>
    
6. Wait for reviews & feedbacks from AIDA-AT staffs, then it will be merged to AIDA-AT repo.


Thank for your attention!

    
    
    
