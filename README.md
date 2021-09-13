# reports-to-email-extensis-portfolio-automation
Script includes logging , customizable email notifications , as well as the capability for predetermined scheduling ( _via the Microsoft Windows Task Scheduler_ ).

#### Requirements :
* Pyhton 3.x

## Installation Procedure :

#### 1. BATCH FILE CONFIGURATION
* **`reports_to_email.py`**

  * `SESSION_PATH` = `D:\\Extensis Portfolio Nightly Reports\\`
    * Folder location containing individual session folders.
  * `SESSION_FOLDER` = `Portfolio-Activity_`
    * Prepended names of individual session folders.
  * `DELETE_PREVIOUS` = `yes`
    * Delete previous session folder.
  * `REPORTS` = `["asset-downloads", "search-terms", "asset-deletions", "asset-uploads"]`
    * Which reprts to download.
  * `PREVIOUS_DAYS` = `"30"`
    * Number of previous days.
  * `INCLUDE_HEADER` = `"true"`
    * Include report headers.
  * `LOCALE` = `"en_US"`
    * Report localization.
  * `emailserver` = `mail.example.com`
    * Email - Server:
  * `emailto` = `recipient@example.com`
    * Email - To:
  * `emailfrom` = `server_noreply@example.com`
    * Email - From:
  * `emailsubject` = `"Automation Notification: ExifTool Scan Log"`
    * Email - Subject:

:star: Detailed information regarding files that may contain "inflated" `XMP-Photoshop:DocumentAncestors` metadata can be found here : https://prepression.blogspot.com/2017/06/metadata-bloat-photoshopdocumentancestors.html
