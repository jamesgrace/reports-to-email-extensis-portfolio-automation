# reports-to-email-extensis-portfolio-automation
Via the Portfolio REST API , retrieves selected Portfolio Reports and then forwards ( _as an attachment_ ) to selected email recipients. Script includes logging , customizable email notifications , as well as the capability for predetermined scheduling ( _via the Microsoft Windows Task Scheduler_ ).

#### Requirements :
* Extensis Portfolio version 3.6.3 ( _or greater_ ) licensed for the Portfolio API.
* Pyhton 3.x

## Portfolio Instance > Configuration :

#### 1. API TOKEN
* Via the Portfolio Administration ( _:8091_ ) Web interface , select "Users" and either take note of an existing API Token or create a new API Token.
* Via Catalogs > _[ Catalog Name ]_ > Users , verify that API Token has been granted Administrator level Role membership to at least one Catalog ( _required in order to be permitted access to the various REST API Reports_ ).

## Python Script > Configuration :

#### 2. PYTHON SCRIPT
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

