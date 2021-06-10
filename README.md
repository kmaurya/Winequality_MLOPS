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

19. 
    





   
