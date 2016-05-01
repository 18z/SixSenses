install:
	cp Slx7hS3ns3onLinux.cfg ~/.Slx7hS3ns3onLinux.cfg
	sudo apt-get update
	sudo apt-get install sdcv
	sudo pip install -r requirements.txt

clean:
	find -name "*.pyc" -exec rm {} \;
