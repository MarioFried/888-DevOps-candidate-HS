## Windows

  - Build a Windows server (you can download predeployed windows 2016 ova from here: http://tinyurl.com/sol9vhc)
  - Write Ansible playbook to execute the following, and upload it to your git repo:
      * Install IIS and create a site which serves HTML page with "Hello World"
      * Create a self-signed certificate and bind it to the site you created in the previous bullet on port 443
      * Install dns service and create new zone(you can choose any domain name that you want)
  - Add a record to point the local web server you created, also make sure to create a record to perform dns reverse lookup
  - Add a small exe file or a an image to the web site you created and download it via HTTP(not via HTTPS). Record(sniff) the download session into a pcap file.
  - Filter the download session from the pcap file and create a screenshot, describe the communication steps steps in the session
