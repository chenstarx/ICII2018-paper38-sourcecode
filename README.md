This repository is for the source code and data used in ICII 2018 paper "4G Network for Air-ground Data Transimission: A Drone based Experiment".

If you are interested in our project, you can cite the paper:

```
@INPROCEEDINGS{8539117, 
author={L. {Chen} and Z. {Huang} and Z. {Liu} and D. {Liu} and X. {Huang}}, 
booktitle={2018 IEEE International Conference on Industrial Internet (ICII)}, 
title={4G Network for Air-Ground Data Transmission: A Drone Based Experiment}, 
year={2018}, 
volume={}, 
number={}, 
pages={167-168}, 
keywords={4G mobile communication;aircraft communication;autonomous aerial vehicles;data communication;4G network;air-ground data transmission;remote communication;packet loss;signal strength;low-altitude air-ground communication;drone-based experiment platform;short communication range;frequency 2.4 GHz;Drones;Packet loss;Data communication;Cellular networks;Mobile handsets;Servers;Cellular Network;Drone;Packet Loss Rate;TCP;IoT;4G Network;5G Network}, 
doi={10.1109/ICII.2018.00028}, 
ISSN={}, 
month={Oct},}
```

### Client Folder

The folder contains the Android source code of the client software used in our experiment. You need to download an Android Studio to compile it to any cell phone.

![avatar](http://lukerr.com/image/cellphone.jpg)

PS: you can edit the IP address in the source code to start your own demo.

### Server Folder

The python scripts running in the server are contained in this folder. You can implement the scripts to a cloud server.

**Mongodb is required**

### Data Folder

This folder contains collected data in our experiment. Some data-processing python scripts are also provided.