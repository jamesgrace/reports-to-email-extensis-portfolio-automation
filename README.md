# reports-to-email-extensis-portfolio-automation
Via the Portfolio REST API , retrieves selected Portfolio Reports and then forwards ( _as attachements_ ) to selected email receipents. Script includes logging , customizable email notifications , as well as the capability for predetermined scheduling ( _via the Microsoft Windows Task Scheduler_ ).

#### Requirements :
* Extensis Portfolio version 3.6.3 ( _or greater_ )
* Pyhton 3.x

## Installation Procedure :

#### 1. CONFIGURATION
* **`reports_to_email.py`**

  * `SESSION_PATH` = `"D:\\Extensis Portfolio Nightly Reports\\"`
    * Base folder location containing individual session folders.
  * `SESSION_FOLDER` = `"Portfolio-Activity_"`
    * Folder name indentifier prepedned to individual session folders.
  * `DELETE_PREVIOUS` = `"yes"`
    * Delete previous session folder ?
  * `REPORTS` = `["asset-downloads", "search-terms", "asset-deletions", "asset-uploads"]`
    * Which speciifc reports to download.
  * `PREVIOUS_DAYS` = `"30"`
    * Number of previous days.
  * `INCLUDE_HEADER` = `"true"`
    * Include report headers ?
  * `LOCALE` = `"en_US"`
    * Report localization.
  * `SMTP_SERVER` = `"mail.example.com"`
    * Email - Server:
  * `SMTP_PORT` = `25`
    * Email - Port: 
  * `EMAIL_FROM` = `"server_noreply@example.com"`
    * Email - From:
  * `EMAIL_TO` = `["recipent1@example.com","recipient2@example.com"]`
    * Email - To:
  * `EMAIL_SUBJECT` = `[ Extensis Portfolio ] : Activity Reports for`
    * Email - Subject:
  * `EMAIL_BODY` = `"See the attached Portfolio Activity Reports in TSV ( Tab Separated Value ) format.."`
    * Email - Body:
