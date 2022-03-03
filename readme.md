# 1.0 Software Setup

Ensure you have python version 3.7 or greater installed on your system, and use this as your default python handle. 

You can determine which python version you are using with the command: 

```
$ python -V
```

And you can determine the location of the python interpreter currently being used with the command:

```
$ which python
```

To change the alias of the python interpreter when running `python` use the following procedure: 

```
$ vim ~/.bashrc
```

Include the line below into the bashrc file (changing the path in qoutes to the one you want):

```
alias python='/c/Users/SeanTedesco/AppData/Local/Programs/Python/Python310/python'
```

Then source the bachrc file to use the changes you just made. 

```
. ~/.bashrc
```


## 1.1 Windows

Please use the following procedure to create your virual environment, activate it, and install all the required packages.

```
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements
```

# 1.2 Mac/Linux

Please use the following procedure to create your virual environment, activate it, and install all the required packages.

```
make clean setup
```


# 2.0 Running the Program

The entry point to the satellite is given in the `main.py` file. Run this to operate the satellite. 


```
python main.py
```
