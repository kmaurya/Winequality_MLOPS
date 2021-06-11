1. Created environment
    conda create -n environment_name
   
2. Activate environment
    conda activate environment_name
   
3. Create a requirements.txt file
    fsutil file createnew requirements.txt 0
   
4. Add required library to the requirements.txt file
    sklearn
    dvc
    dvc[gdrive]
   
5. Installed requirements
    pip install -r requirements.txt
   
6. Create a template file
    fsutil file createnew template.py 0

7. Added dirs required for the project

8. Copy the data to data_given folder. You can get data from 
    https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing
   
9. Do git init

10. Do dvc init

11. Do dvc add data_given/winequality.csv

12. Do git add . to move files to staging area

13. Do git commit -m "First commit"

14. Create a git hub repository

15. Do git remote add origin your repo link
    for eg.: git remote add origin https://github.com/kmaurya/Winequality_MLOPS.git
    
16. Do git branch -M main

17. Do git push -u origin main

18. Lets beign for actual code

19. Update the params.yaml file with the configuration paths and values

20. Commit your changes using 
    git add .
    git commit -m "Updated params.yaml"
    git push -u origin main
    
21. Create a new file under src folder get_data.py which will contain code to get the data
    fsutil file createnew src\get_data.py 0

22. Write the code to get data 

23. Create load_data.py file in src where we will be adding data in raw folder
    fsutil file createnew src\load_data.py 0

24, Run the file and check that raw folder should be updated with winequality.csv file

25. Now add stages in the dvc.yaml file. Stages are nothing but it is a pipeline 
    We have given the first stage name as load_data
    
26. After adding the cmd, deps and outs we will run the pipeline using command
    dvc repro
    
27. After running this command dvc.lock file is created, and it tracks the record if there is some change in the file 
    then it reruns again and create new hash value else the hash value remains the same.
    
28. Create a new file split_data.py to split data set into training and testing instances
    fsutil file createnew src\split_data.py 0
    
29. Add the code to the split_data.py

30. Create stage 2 in dvc.yaml

31. Run dvc repro

Successfully we have implemented two stages i.e. two pipelines created

32. Push your code 

33. Create a new file for training now 
    fsutil file createnew src\train_and_evaluate.py 0
    
34. Write the code for training and add as pipeline for stage in dvc.yaml

35. Create a folder reports 
    mkdir report
    
36. Create a file params.json file and scores.json
        fsutil file createnew report/params.json 0
        fsutil file createnew report/scores.json 0
    
37. We need not worry about what is to be added it will automatically be updated by the dvc pipelines.

38 Do dvc repo 

39. All the metrics related scores and params are updated after running above command.

40. Now let's check whether dvc is tracking the metrics or not. Run below command:
    dvc metrics show
    
41. We can also track the differences from past 
    dvc metrics diff
    
42. Push the code to github now

43. Let's do some experiement with the params to check the tracking of model.
    Let's change the params value passed to model in params.yaml file
    
44. Do dvc repro

45. Let's compare the previously generated and newly generated metrics using 
    dvc metrics diff
    
46. You can rollback to any previous stage using git checkout and the commit id.

Now that we have basic code implementation done. Lets look into over the testing part.

47. Install tox and pytest library

What is tox
tox is mainly used as a command line tool and needs a tox.ini or a tool.tox section in pyproject.toml containing the 
configuration.
tox can be used for ...
        creating development environments
        running static code analysis and test tools
        automating package builds
        running tests against the package built by tox
        checking that packages install correctly with different Python versions/interpreters
        unifying Continuous Integration and command line based testing
        building and deploying project documentation
        releasing a package to PyPI or any other platform

48. Let's create tox.ini file now in the root directory

49. Add environment list and command to the tox file

50. Create a directory tests which will contain testcases
    mkdir tests
    
51. Add a file conftest.py, __init__.py and test_config.py to tests folder
    fsutil file createnew tests/conftest.py 0
    fsutil file createnew tests/test_config.py 0
    fsutil file createnew tests/__init__.py 0

52. You can write the test cases in test_config.py file. Note that the testcases must start with test

53. Now create setup.py file which will help virtual env created by tox to identify the code package.
     fsutil file createnew setup.py 0
    
54. Add code in setup file.

55. Let's install the package created in setup.py
    pip install -e .
    
56. Use of doing this is src will be treated as package here and you will be able to import it


    
    


    











   
