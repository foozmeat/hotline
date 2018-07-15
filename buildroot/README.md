This folder contains files to create a custom raspberry pi image for hotline.

To get started run `vagrant up` and then `vagrant ssh` to login to the VM. To build image run the following

```
cd buildroot
/opt/hotline/buildroot/build.sh
make
```

##### References
* https://github.com/enunes/buildroot-external-lima
* https://stackoverflow.com/questions/48212572/add-a-pypi-python-package-to-buildroot
