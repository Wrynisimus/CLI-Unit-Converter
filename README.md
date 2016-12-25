# CLI-Unit-Converter
Included is a debian package which should be installable on all debian based systems, including Ubuntu.
The package will place the Converter.py script in /usr/local/bin along with another script 'converter'.
After installation to run the program just run 'converter'
# Dependencies
Just python3
# Uninstallation
Run sudo rm -r /usr/bin/Converter.py && sudo rm -r /usr/bin/converter
If you installed the application with the debian package go ahead and run apt remove cli-unit-converter just to make sure its not hanging around in any logs or whatevs.
