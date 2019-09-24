#* * * * * rm /home/febriramadlan/ScoutSuite/scoutsuite-report/scoutsuite-results/*
#* * * * * python3 /home/febriramadlan/ScoutSuite/scout.py gcp --user-account
#* * * * * cp /home/febriramadlan/cloudaudit/apps.py /home/febriramadlan/ScoutSuite/scoutsuite-report/scoutsuite-results/

#rm /home/febriramadlan/ScoutSuite/scoutsuite-report/scoutsuite-results/*; 
rm /home/febriramadlan/scoutsuite-report/scoutsuite-results/*;
echo "y" |  python3 /home/febriramadlan/ScoutSuite/scout.py gcp --user-account; 
cp /home/febriramadlan/scoutsuite-report/scoutsuite-results/scoutsuite_results_gcp-security-research* /home/febriramadlan/scoutsuite-report/scoutsuite-results/file-cloud.json; 
python3 /home/febriramadlan/cloudaudit/apps.py
