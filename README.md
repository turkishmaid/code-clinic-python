# code-clinic-python

LinkedIn Learning Course https://www.linkedin.com/learning/code-clinic-python-2018

> Successful programmers know more than just how to code. They also know how to think about solving problems. Code Clinic is a series of courses where our instructors solve the same problems using different programming languages. Here, Barron Stone works with Python. Barron introduces challenges and provides an overview of his solutions in Python. Challenges include topics such as statistical analysis and accessing peripheral devices.




&nbsp;

## Installation

### Install Python virtual environment

Assumes Python 3.9 installed via homebrew or similar.

```
python3.9 -m venv venv
. venv/bin/activate
python3.9 -m pip install --upgrade pip
pip install -r requirements.txt
```

A `jupyter notebook` server started from that venv will recognize the `venv` as "Python 3 (ipykernel)" without [ipython kernel install](https://medium.com/@eleroy/jupyter-notebook-in-a-virtual-environment-virtualenv-8f3c3448247) when `jupyter` is installed [from within the virtual environment](https://stackoverflow.com/a/59073948/3991164).



### Resources

Download Exercise Files from LinkedIn (no clue about their license, so not in this repo).

Update: Lynda.com [has a repo with the data](https://github.com/lyndadotcom/LPO_weatherdata). Consider including it here...
