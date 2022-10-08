<h2> pywish API </h2>
API for pywish social network.

<h3> Installation guide for Linux/GNU OS </h3>

1) Install all required solutions. Replace 'apt' with
   your distribution package manager.
   ```commandline
   sudo apt update && sudo apt upgrade
   sudo apt install -y git python3-venv python3-pip vim
   git clone https://github.com/pkozhem/pywish.git
   cd pywish
   ```
2) Create and activate virtual environment.
   ```commandline
   python3 -m venv venv
   source venv/bin/activate
   ```
3) Set up your environment variables in
   _.env.template_ file.
   ```commandline
   vim .env.template
   cp .env.template .env
   ```
4) Install all dependencies.
   ```commandline
   pip install -r requirements.txt
   ```
5) Run up locally via.
   ```commandline
   python3 manage.py runserver
   ```