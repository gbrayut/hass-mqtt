#

```bash
# After ssh into RPI use the following to setup the environment
sudo -sE #For now these commands need to run as root (TODO: fix this as it screws up the pipenv)
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
# Can then git pull any commits from your dev machine even before they are pushed to origin

# Run script in pipenv shell
cd ~/code/github/hass-mqtt/simple
sudo pipenv shell #starts an interactive shell with required packages
# The above should only take a few minutes to run. Trying without sudo it would stall forever. TODO: fix that
pipenv sync #install packages from lock file. If there is a sha mismatch, run pipenv update
# If you want to run as non-root, copy+chown the folder from /root/.local/share/virtualenvs/ to /home/$USER/.local/share/virtualenvs/

# Setup systemd user service files https://wiki.archlinux.org/index.php/Systemd/User
mkdir -p ~/.config/systemd/user/ #Make folder where user service files live and symlink file there
ln -s "$HOME/code/github/hass-mqtt/simple/simple-mqtt.service" "$HOME/.config/systemd/user/simple-mqtt.service"
systemctl --user enable simple-mqtt.service #enable the user service file

systemctl --user daemon-reload #after making any changes you make any changes you have to reload the file
systemctl --user status simple-mqtt.service
systemd-analyze verify $HOME/code/github/hass-mqtt/simple/simple-mqtt.service

# Setup current user to view logs
sudo usermod -a -G systemd-journal $USER
newgrp systemd-journal #Reload shell with new group (or just exit and start a new shell)
journalctl --user-unit simple-mqtt.service
```

# Notes

- Use `pipenv shell` to start a shell with the python virtualenv activated
- Use `pipenv run simple.py` to just run the program
- Use `pipenv install mypackage` to add new packanges to the virtualenv
