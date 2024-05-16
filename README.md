Create a virtual environment
```
python -m venv venv
```

Activate the virtual environment (Note your command may differ depending on your CLI or OS)
```
venv/Scripts/activate
```


Install the requirements
```
pip install -r requirements.txt
```

Create the **.venv** file inside the root of the project. Use the **.env.sample** as a basis for it and add the secret variable to it.

Run the project. If you did everything correctly, it should print the value of your secret variable.
```
python test.py
```