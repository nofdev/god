god
===

God is a daemon guard that to check whether normal operation process


### How to use?
* Edit the configuration
```
vi god.conf
```

* Running god daemon as background
```
python god.py -c god.conf > /dev/null 2>&1 &
```

* You can run the multiprocess
```
python god.py -c god-apache.conf > /dev/null 2>&1 &
python god.py -c god-nginx.conf > /dev/null 2>&1 &
```

* Add God to rc.local
```
echo 'python god.py -c god-apache.conf > /dev/null 2>&1 &' >> /etc/rc.local
```

### Author
jiasir(Taio Jia) <jiasir@icloud.com>