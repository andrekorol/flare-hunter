import ftplib
from urldl import download
import os.path as path

dirs = []
noaa_url = "ftp.ngdc.noaa.gov"
daily_reports_dir = "STP/swpc_products/daily_reports"
ftp = ftplib.FTP(noaa_url)
ftp.login()

ftp.cwd(daily_reports_dir)
reports = ftp.nlst()
for directory in reports:
    try:
        ftp.cwd("/".join([directory, "2011", "02"]))
        files = ftp.nlst()
        for filename in files:
            if "0216" in filename:
                file_url = "ftp://" + noaa_url + "/".join([ftp.pwd(),
                                                           filename])
                download(file_url, directory)
        ftp.cwd("../../../")
    except ftplib.error_perm:
        pass
    ftp.cwd("/".join([directory, "docs"]))
    doc_files = ftp.nlst()
    for doc in doc_files:
        doc_url = "ftp://" + noaa_url + "/".join([ftp.pwd(), doc])

        download(doc_url, path.join(directory, "docs"))
    ftp.cwd("../../")

ftp.quit()
