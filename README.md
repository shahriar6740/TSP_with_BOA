## Implement Travelling Salesmen Problem(TSP) using Butterfly Optimization Algorithm (BOA)
**This repository is maintained for the group project as part of the requirement of Course: CPSC 5506 - Introduction to Computational Sciences, Winter 2024, MSc in Computational Sciences, Laurentian University, Sudbury, Ontario, Canada. Once the course requirement has been met, there will be no maintenance or support for this repo and will be kept as a legacy project**
<br>
# Environment setup
**Create A Virtual Environment**
To run the project isolated, please install Python version 3.10 or higher. Create a virtual environment and activate it. To create a virtual environment follow the steps:
- Install virtual environment for your python version using:
  ```
  python3 -m pip install virtualenv
  ```
- Now Create a virtual environment with any desired name at your preferred location using:
  ```
  python3 -m venv /path/to/new/virtual_env/<environment_name>
  ```
**Activate the virtual environment**

- <b>Fow windows:</b> <br>
  ```.\<environment_name>\Scripts\activate```
- <b>For Linux/Mac:</b> <br>
  ```source <environment_name>/bin/activate```

# Run the project
- <b>Project Home Directory: </b> Throughout the entire project, `/TSAP_with_BOA` is considered as the project home directory.
- From the project home directory:
  ```cd Implementation```
- Inside the `Implementation` dir, do the following:
  - Now check your virtual environment. If not activated, active on the currnet directory using the mentioned command.
  - Upgrade pip: it is required for the very first-time use of the project:
    ```pip install --upgrade pip```
  - Install All the required packages by running (run this command only once on a new machine/venv):
    ```pip install -r requirements.txt```

- Now enter this command to run Travelling Salesmen problem with Butterfly Optimization Algorithm.
  ```
  python experimental_implementation.py
  ```
# For structured project-like implementation
**RUN**
```
python TSP_main.py
```
And then backtrack each class/function. <br>

Final Report of the project is available [here](https://docs.google.com/document/d/1GV8eV1vXBX2hXU0qtY7MYGdHoHoreN6zfsfpfzBqD4A/edit?usp=sharing) <br>
Final Presentation Slide is available [here](https://docs.google.com/presentation/d/1A0Lu2wP1APy0EfRrgbbs8Y5ncbVd8Ri0qafXFgwd-7M/edit?usp=sharing)
