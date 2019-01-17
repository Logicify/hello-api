# Hello API

An application providing greeting and echo operations via REST API.

## Local deployment

### Initial setup

1. You'll need virtualenv tool, alternatively you can install it with your OS package manager
    ```bash
    pip install virtualenv
    ```
1. Create new virtual environment with python3
    ```bash
    virtualenv -p python3 venv
    ```
1. Activate it
    ```bash
    . venv/bin/activate
    ```
1. Install application requirement into active virtual environment
    ```bash
    pip install -r requirements.txt
    ```

### Run application

Just as for any Django app do

```bash
./manage.py runsever
```

## Docker deployment (production aimed)

You will need to generate a `SECRET_KEY` for Django, see 
[Django doc](https://docs.djangoproject.com/en/2.1/ref/settings/#secret-key) for details on how it's used. **Recommended
length is not less then 50 chars**.

1. Build docker image
    ```bash
    docker build -t impulse1_test .
    ```
    
1. Run container
    ```bash
    docker run -d --name impulse1_test_instance \
       -e SECRET_KEY=${SECRET_KEY} \
       impulse1_test
    ```
    
 1. See `src/impulse1_test/settings_prod.py` for list of supported environment variables
 