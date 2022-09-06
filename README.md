## Package structure

```
.
├── config                        # Config files for internal developer
├── logfile                       # Log files
├── src                           # Source code
│    ├── main.py              
│    ├── functions
│    └── routers
├── templates
├── config.json                   # Configuration file for Customer
└── README.md
```

## Virtual environment

- Creating virtual environment
    ```bash
    $ python3 -m venv venv
    ```

- Activate virtual environment
    ```bash 
    $ venv\Scripts\activate.bat # On Windows
    $ source venv/bin/activate  # On Unix or MacOS
    ```

- Install Optical Character Recognition - [here](https://gitlab.com/GammaRayStudio/DevDoc/-/blob/master/Python/004.PythonOCR.md)
- Install packages
    ```bash
    $ python3 -m pip install -r requirements.txt
    ```


## Run project
```bash
$ ./boot.sh
```
- Interactive API docs: http://127.0.0.1:8000/docs
- Alternative API docs: http://127.0.0.1:8000/redoc



## References
- [Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html)
    - Generate requirements.txt
        ```bash
        $ pip3 freeze > requirements.txt
        ```