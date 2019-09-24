#python3
#@author ebi
import json 
import requests
from pprint import pprint

JSON_FILE_NAME = "/home/febriramadlan/scoutsuite-report/scoutsuite-results/file-cloud.json"
def isReadFile(path):
	with open (path) as jsonfile:
		data = jsonfile.read().split("scoutsuite_results =")
		return json.loads(data[1])


def sendNotifToSlack(message):
        webhook_url = 'https://hooks.slack.com/services/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'
        slack_data = {
            'text': message,
            'channel' : "security_cloudaudit",
            'username' : "security_cloudaudit"
        }

        response = requests.post(
            webhook_url, data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'}
        )
        if response.status_code != 200:
            raise ValueError(
                'Request to slack returned an error %s, the response is:\n%s'
                % (response.status_code, response.text)
        )



def main() :
	slack_notif = "```"

	print ("[+] read file ")
	jsonData = isReadFile(JSON_FILE_NAME)
	isServiceList = jsonData['service_list']
	for service in isServiceList:
		isServiceData = jsonData['services'][service]
		findings = jsonData['services'][service]['findings']
		slack_notif += "\n[+] Service : "+service+""
		slack_notif += "\n[+] Data : findings\n"
		for valueFinding in findings:
			# for key in findings[valueFinding]:
			slack_notif += "\n 	*** Dashboard : "+ findings[valueFinding]['dashboard_name']
			slack_notif += "\n 	*** Description : "+ findings[valueFinding]['description']
			slack_notif += "\n 	*** Rationale : "+ findings[valueFinding]['rationale']

	
	project = jsonData['services']['cloudresourcemanager']['projects']
	slack_notif += "\n[+] Data : projects\n"
	usersCount = (jsonData['services']['cloudresourcemanager']['users_count'])
	slack_notif += "\n[+] User Count : " + str(usersCount)
	for listProject in project:
		for i in project[listProject]:
			if "users" in i :
				for usershash in project[listProject]['users']:
					for x in project[listProject]['users'][usershash]:
						slack_notif += "\n-----[+] Email : " + str(project[listProject]['users'][usershash]['name'])
						slack_notif += "\n-----[+] Roles : " + str(project[listProject]['users'][usershash]['roles'])
				break
			else :
				print ("Noting users object ")
				break

	# Get finding for cloudsql
	iamProject = jsonData['services']['iam']['projects']
	slack_notif += "\n[+] Data : projects\n"
	serviceAccountCount = (jsonData['services']['iam']['service_accounts_count'])
	slack_notif += "\n[+] Service Account Count : " + str(serviceAccountCount)
	for listIamProject in iamProject:
		for i in iamProject[listIamProject]:
			if "service_accounts" in i:
				
				for serviceshash in iamProject[listIamProject]['service_accounts']:
					for x in iamProject[listIamProject]['service_accounts'][serviceshash]:
						slack_notif += "\n-----[+] Name : " + str(iamProject[listIamProject]['service_accounts'][serviceshash]['display_name'])
						slack_notif += "\n-----[+] Email : " + str(iamProject[listIamProject]['service_accounts'][serviceshash]['email'])
						slack_notif += "\n-----[+] Keys : " + str(iamProject[listIamProject]['service_accounts'][serviceshash]['keys'])
					break
			else:
				print ("Nothing Services Account Object ")
				break
		
	slack_notif += "\n```"
	sendNotifToSlack(slack_notif)
	print ("Done")

if __name__ == '__main__':
	main()
