# Automatically execute the UDP broadcast IP script on startup


# IPBroadcast.py
>Place it at the desired path


<br><br/><br><br><br>

# Prepare a startup service file
>Create a service file：

```
sudo nano /etc/systemd/system/startup-script.service

```

>Copy and paste the following content

```
[Unit]
Description=Startup Script Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/your_script.py
Restart=always
User=root
Group=root
Environment=PATH=/usr/bin:/usr/local/bin
WorkingDirectory=/path/to/your_script_directory

[Install]
WantedBy=multi-user.target

```
>>WorkingDirectory refers to the directory where your Python script is located. Please replace /path/to/your_script_directory with the actual path to your script.



>Reload the systemd daemon
```
sudo systemctl daemon-reload
```

> Enable it to run on startup
```
sudo systemctl enable startup-script.service

```

>Start the service immediately
```
sudo systemctl start startup-script.service

```

