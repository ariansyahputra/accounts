# elementary Account Server
This Webservice is going to manage elementary Accounts and Services. First we will provide daily builds through this service.

## MVP
- [x] Accounts, Registration & GitHub OAuth Login
- [x] Account Page with user information
- [x] Add Stripe Subscriptions to Account Page
- [x] Add Ways to enroll to Stripe Subscription
- [ ] Daily Build Page
- [ ] Make Daily Build Page Subscription/Team only

## Usage
Setup your dev enviroment config by copying `accounts/settings.py.example` to `accounts/settings.py`
If you want to test github OAuth Login you need to provide the OAuth Keys in the `accounts/settings.py` file.

For development use python with a virual environment, to set that up do:

    virtualenv -p python3 .venv
    source ./.venv/bin/activate
    pip install -r requirements.txt
    
You can then run the local development Server with the command:

    ./manage.py runserver
    
`manage.py` is your entry into the django ecosystem, use it to apply migrations, run tests, etc.
