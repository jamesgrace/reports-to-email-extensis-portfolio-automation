import urllib
import urllib.request,urllib.parse,urllib.error
import json
import os
import errno
import datetime
import smtplib
import shutil
import glob


# - - - - - - - - - - - - - - - - - - - - - - - - - - - version 13september2021 - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

SERVER_PROTOCOL = "http" # - - - - "http" or "https"
SERVER_ADDRESS = "localhost"
SERVER_PORT = "8090" # - - - - - - "8090" for http / "9443" for https
API_TOKEN = "TOKEN-"
SESSION_PATH = "D:\\Extensis Portfolio Nightly Reports\\"
SESSION_FOLDER = "Portfolio-Activity_"
DELETE_PREVIOUS = "yes" # - - - "yes" or "no"
REPORTS = ["asset-downloads", "search-terms", "asset-deletions", "asset-uploads"]
# - - - - "asset-deletions", "asset-downloads", "asset-most-downloaded", "asset_most-previewed", "asset-uploads", "file-types", "keyword-statistics", "netpublish-download-frequency", "netpublish-usage", "search-terms"
PREVIOUS_DAYS = "30"
INCLUDE_HEADER = "true"
LOCALE = "en_US"
SMTP_SERVER = "mail.example.com"
SMTP_PORT = 25
EMAIL_FROM = "server_noreply@example.com"
EMAIL_TO = ["recipent1@example.com","recipient2@example.com"]
EMAIL_SUBJECT = '[ Extensis Portfolio ] : Activity Reports for '+str(datetime.datetime.today().strftime("%A , %d %B %Y"))+'...'
EMAIL_BODY = "See the attached Portfolio Activity Reports in TSV ( Tab Separated Value ) format..."

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# --- [ START ] : Delete Prevous Directory - - - - - - - - - - - - - - - - - - - -
#                 Deletes the previous session directory

def deletePreviousDirectory():

	try:
		if DELETE_PREVIOUS.lower() == "yes":
			previousPath = glob.glob(os.path.join(SESSION_PATH, SESSION_FOLDER+"*"))
			for foundDirectory in previousPath:
				print("[ DELETING Previous Session Folder ! ] : [ "+foundDirectory+" ]")
				shutil.rmtree(foundDirectory)

	except OSError:
		if not os.path.isdir(foundDirectory):
			raise

# --- [  END  ] : Delete Previous Directory - - - - - - - - - - - - - - - - - - - -



# --- [ START ] : Create Session Directory - - - - - - - - - - - - - - - - - - - -
#                 Creates the session directory + redirects stdout to session log

def createSessionDirectory():

	from datetime import datetime

	global SESSION_FOLDER
	SESSION_FOLDER = SESSION_FOLDER+datetime.today().strftime('%m-%d-%Y_%H-%M-%S')

	try:
		os.makedirs(SESSION_PATH+SESSION_FOLDER)
	except OSError:
		if not os.path.isdir(SESSION_PATH+SESSION_FOLDER):
			raise

	import sys
	sys.stdout = open(SESSION_PATH+SESSION_FOLDER+'/session_log.txt', 'w')

# --- [  END  ] : Create Session Directory - - - - - - - - - - - - - - - - - - - -



# --- [ START ] : Save Report - - - - - - - - - - - - - - - - - - - -

def saveReport():

	todaysdate = datetime.datetime.today()
	previousdate = todaysdate - datetime.timedelta(days=int(PREVIOUS_DAYS))

	for report in REPORTS:

		save_url = SERVER_PROTOCOL+'://'+SERVER_ADDRESS+':'+SERVER_PORT+'/api/v1/report/'+report+'/?session='+API_TOKEN+'&locale='+LOCALE+'&includeHeader='+INCLUDE_HEADER+'&startingDate='+previousdate.strftime("%Y-%m-%d")+'&endingDate='+todaysdate.strftime("%Y-%m-%d")

		print("[ Saving ! ] : [ "+report+" ]" , "\n")

		try:
			save_response = urllib.request.urlopen(save_url).read()

			with open(os.path.join(SESSION_PATH+SESSION_FOLDER, report+".tsv"), 'wb') as reportfile:
				try:
					reportfile.write(save_response)
				except OSError as error:
					print("[ Save Report ] : [ OS ERROR ! ] =" , error.reason , "\n")

		except urllib.error.URLError as error:
				print("[ Save Report ] : [ URL ERROR ! ] =" , error.reason , "\n")

		print("= - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - =", "\n")

# --- [  END  ] : Save Report - - - - - - - - - - - - - - - - - - - -



# --- [ START ] : Send Email - - - - - - - - - - - - - - - - - - - -

def sendEmail():

	from email.mime.base import MIMEBase
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
	from email import encoders

	try:
		msg = MIMEMultipart()
		msg['Subject'] = EMAIL_SUBJECT
		msg['From'] = EMAIL_FROM
		msg['To'] = ','.join(EMAIL_TO)

		body = EMAIL_BODY
		body = MIMEText(body)
		msg.attach(body)

		for file in os.listdir(SESSION_PATH+SESSION_FOLDER):
			if file.endswith('.tsv'):
				path = os.path.join(SESSION_PATH+SESSION_FOLDER, file)
				tsv = MIMEBase('text', 'tab-separated-values')

				with open(path, 'rb') as fp:
					tsv.set_payload(fp.read())
				tsv.add_header('Content-Disposition', 'attachment', filename=file)
				encoders.encode_base64(tsv)
				msg.attach(tsv)

		mailserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
#		mailserver.set_debuglevel(1)
		mailserver.ehlo()
		mailserver.sendmail(msg['From'],EMAIL_TO,msg.as_string())
		mailserver.quit()

	except smtplib.SMTPResponseException as e:
		print('SMTP Error Code ' , e.smtp_code , '; SMTP Error Message : ' , e.smtp_error , '\n')


# --- [  END  ] : Send Email - - - - - - - - - - - - - - - - - - - -



# --- [ START ] : Test Email - - - - - - - - - - - - - - - - - - - -

def testEmail():

	from email.mime.text import MIMEText
	from email.mime.multipart import MIMEMultipart

	try:
		msg = MIMEMultipart()
		msg['Subject'] = EMAIL_SUBJECT
		msg['From'] = EMAIL_FROM
		msg['To'] = EMAIL_TO

		body = EMAIL_BODY
		body = MIMEText(body)
		msg.attach(body)

		mailserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
		mailserver.set_debuglevel(1)
		mailserver.ehlo()
		mailserver.sendmail(msg['From'],msg['To'],msg.as_string())
		mailserver.quit()

	except smtplib.SMTPResponseException as e:
		print('SMTP Error Code ' , e.smtp_code , '; SMTP Error Message : ' , e.smtp_error , '\n')

# --- [  END  ] : Test Email - - - - - - - - - - - - - - - - - - - -



# --- [ START ] : Logout - - - - - - - - - - - - - - - - - - - -
#                 Session logout. Note that this is not normally
#                 needed as there is no connection limit nor
#                 timeout for RESTful API connections - - - - -

def Logout():

	logout_url = SERVER_PROTOCOL+'://'+SERVER_ADDRESS+':'+SERVER_PORT+'/api/v1/auth/logout?session='+API_TOKEN
	logout_data = urllib.parse.urlencode({}).encode("utf-8")
	request = urllib.request.Request(logout_url, logout_data)
	request.add_header('Accept', 'application/json, text/plain, */*')
	request.add_header('Content-Type', 'application/json;charset=UTF-8')

	try:
		logout_response = urllib.request.urlopen(request).read()

	except urllib.error.URLError as error:
		print("[ Logout ] : [ ERROR ! ] =" , error.reason , "\n")

	else:
		print("[ Logout ] : [ - Session Logout Successful - ]" , "\n")

# --- [  END  ] : Logout - - - - - - - - - - - - - - - - - - - -



deletePreviousDirectory()

createSessionDirectory()

saveReport()

#testEmail()

sendEmail()

Logout()
