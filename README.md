# extract-binary
Installing the required dependencies:

```
$ wget https://github.com/ReFirmLabs/binwalk/archive/master.zip
$ unzip master.zip
```

```
$ (cd binwalk-master && sudo python setup.py uninstall && sudo python setup.py install)
```


Running the script:

```
$ python main.py FIRMWARE_PATH BINARY_NAME
```
