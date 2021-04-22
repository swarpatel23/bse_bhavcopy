crontab -l > jobs.txt
echo "0 18 * * * $(which python) $(pwd)/cron.py" >> jobs.txt
crontab jobs.txt