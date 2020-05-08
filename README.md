# FASYS

Uses face_recognition module to scan faces and stores the known faces (for which model is trained) in a CSV format (file name = "latest.csv" ) , which can be send to required email address using smtplib and email module. And all this functionality is packed into a simple GUI made out of Tkinter module.

# Modules/Dependencies
1. Base64 module
2. Pandas module
3. Python CSV Module
4. Tkinter module
5. The smtplib module
6. The email package
7. face_recognition module

# How to configure?
To configure send mail function you will have to create an email / or use an existing email.
Create App Password for your email(you can referto https://support.google.com/mail/answer/185833?hl=en)
After that Enter your email address and app password in "sendmail.py" at the mentioned places. 

# How to use ?
1. Install all dependencies.
2. Execute G1.py file.

"latest.csv" file will be the final result created.
After every face recognition session, latest.csv file will be overwritten.
Hence store it/send mail after every face scan/recognition (attendance session) 

# Functions in run.py

* `train(<filename to store data>.json)`

* To scan faces:
    1. Load training data: `load_train_data(<filename>)` this will return `kfe` and `kfn`
    2. Scan faces data: `scan_faces(kfe, kfn)`

# Additional notes :
* software key is 1234
* press q to quit from attendace mode then click on close(cross or X) face scan window.
* be in frame for 2 seconds to capture attendance
* only jpg, png  image supported
*  "latest.csv" file will be the final result created.
    After every face recognition session, latest.csv file will be overwritten.
    Hence store it/send mail after every face scan/recognition (attendance session)


# For Testing

* To train data from local data folder:
`python run.py -t <Filename To Store Training Data to>.json`

* To scan faces:
`python run.py -s <Filname to pick training data from>.json`
# FASYS
