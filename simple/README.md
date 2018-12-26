#

```
# After ssh into RPI use the following to setup the environment
sudo -sE #These commands need to run as root
apt install git #python-pip had an issue, so install that manually
curl https://bootstrap.pypa.io/get-pip.py | python3 finishes
pip install pipenv
# Then exit and restart your shell session to update your PATH

# Download code from github (this and the rest of the commands should be run as a normal user)
mkdir -p ~/code/github/
cd ~/code/github
git clone git@github.com:gbrayut/hass-mqtt.git
cd hass-mqtt
#Optional set upstream to another local linux system (easier to pull/test code without pushing to github)
git remote add dev username@:/home/username/code/github/hass-mqtt
git branch -u dev/master #Set local master brach to track dev remote instead of origin

# Run script in pipenv shell
cd ~/code/github/hass-mqtt/simple
sudo pipenv shell #starts an interactive shell with required packages
# The above should only take a few minutes to run. Trying without sudo it would stall forever. TODO: fix that
pipenv sync #install packages from lock file. If there is a sha mismatch, run pipenv update
```

# Notes

- Use `pipenv run simple.py` to install dependencies and run program
- Use `pipenv install mypackage` to add packanges.