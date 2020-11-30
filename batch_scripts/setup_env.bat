call cd ..
call conda env create -f environment.yml
call conda activate CrownEstateWatch
call ipython kernel install --user --name=CrownEstateWatch
pause