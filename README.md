# pip-check
Checks the environment has the required pip dependencies for your project

#Install
```bash
git clone https://github.com/Urucas/pip-check.git && cd pip-check
python setup.py install
```

#Usage
Inside your project folder, write a dependencies.json with all the required
dependencies like:
```json
{
  "dependencies": {
    "requests" : "2.7.0",
    "MySQL-python" : "1.2.5",
    "parse" : "1.6.6",
    "parse-rest" : "0.2.20141004",
    "parse-type" : "0.3.4"
  }
}
```
Then **pip-check.py** and install(if required) everything in a simple line

#Requirements
* pip
* setuptools
