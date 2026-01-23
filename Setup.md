*Intrusion Detection and Prevention System (IDPS)*
----------------------------------------------------

This document explains how to set up, run, and test the Intrusion Detection System (IDS) developed using Suricata and Flask.
The project was built as part of an undergraduate academic mini project and focuses on real-time network monitoring and alert visualization.


*1. Project Setup*
-----------------------

*1.1 System Requirements*
---

  Operating System

  Kali Linux (recommended)

  Ubuntu (also supported)

  Required Software

  Suricata

  Python 3

  Flask

  HTML, CSS, JavaScript (for the web interface)

  A modern web browser

*1.2 Installing Suricata*
--

Install Suricata on the Ubuntu/Kali Linux endpoint. 

We tested this process with version 6.0.8 and it can take some time:

#sudo add-apt-repository ppa:oisf/suricata-stable

#sudo apt-get update

#sudo apt-get install suricata -y

*1.3 Suricata Configuration*
--

#cd /tmp/ && curl -LO https://rules.emergingthreats.net/open/suricata-6.0.8/emerging.rules.tar.gz

#sudo tar -xvzf emerging.rules.tar.gz && sudo mv rules/*.rules /etc/suricata/rules/

#sudo chmod 640 /etc/suricata/rules/*.rules

*1.4 Configure (edit) Suricata settings in the /etc/suricata/suricata.yaml file and set the following variables*
--
  **Step 1: Open the Suricata Configuration File**
  #sudo nano /etc/suricata/suricata.yaml

 **Step 2: Configure HOME_NET and EXTERNAL_NET**
  
  Find these lines (they are usually commented out):
  
  #HOME_NET: "<SYSTEM_IP>"
  
  #EXTERNAL_NET: "any"

  Edit them to look like this: 
  
  HOME_NET: "[192.168.1.0/24]"
  
  EXTERNAL_NET: "any"

  **Step 3: Verify the Default Rule Path**
  Find this line:
  
  #default-rule-path: /etc/suricata/rules

  **Step 4: Configure Rule Files**
  Find the rule-files section and configure so that every files which ends with .rules consider as rules

  rule-files:
  - "*.rules"

  **Step 5: Enable Global Statistics**
    Find the stats section.
    
  stats:
  
   enabled: yes (default would be "no", enable it.)

   
  **Step 6: Enable High-Speed Packet Capture (AF-PACKET)**
    Find the af-packet section and configure its interface as your actual network interface.

  af-packet:
  - interface: eth0

 **Step 7: Save and Exit nano**
 
  Press CTRL + O → Enter (save)
  
  Press CTRL + X (exit)    

    
*2. Web Application Setup (Flask)*
-----------------------------------

*2.1 Installing Flask*
--

#pip install flask

*2.2 Create the project folder*
--

#mkdir idps_web_app

#cd idps_web_app

*2.3 Create app.py*
--

#nano app.py 
     
  *paste the flask code*
    
*2.4 Run the web application*
--

#python3 app.py

if the setup is correct, you will see *Running on http://127.0.0.1:5000/*

Now open the browser and go to http://127.0.0.1:5000. You will see your web Dashboard


*3 Creating the GUI*
----------------------

Inside the idps_web_app we will create a new directory named *templates*.

*3.1 Create templates directory*
--

#mkdir templates

*3.2 Create index.html*
--
  
#nano index.html

  *paste the index.html code*

*3.3 Create errorlog.html*
--

#nano errorlog.html

  *paste the error.html code*

Now host the web application and you are good to go!!!!




*4 Operating the IDS*
----------------------


1. Start Suricata:

  #sudo suricata -c /etc/suricata/suricata.yaml -i <network-interface>


2. Access the Web Application:

  Open the browser and navigate to http://<your-ip>:5000.

  Use the GUI to monitor logs in real-time.



3. View Logs:

  Live Monitoring: Logs are read from fast.log.

  Error Logs: Filtered from fast.log for parsing issues.

  Prevent Logs: Custom rules that trigger actions are shown here.



4. Update Rules:

  Add custom rules to /etc/suricata/rules/local.rules. For example:

  alert icmp any any -> any any (msg:"ICMP Echo Request Detected"; sid:1000001; rev:1;)

  Reload Suricata to apply rules:

  #sudo suricata-update  
  #sudo systemctl restart suricata
