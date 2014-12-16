god
===

God is a process manager that to check whether normal operation process


### How to use?
* Edit the configuration
```
vi god.conf
```

* Running god daemon as background
```
nohup python god.py -c god.conf > /dev/null 2>&1 &
```

* You can run the multiprocess
```
nohup python god.py -c god-apache.conf > /dev/null 2>&1 &
nohup python god.py -c god-nginx.conf > /dev/null 2>&1 &
```

* Add God to rc.local
```
echo 'nohup python god.py -c god-apache.conf > /dev/null 2>&1 &' >> /etc/rc.local
```

### Author
jiasir(Taio Jia) <jiasir@icloud.com>