## AT commands

```
AT // auto-baud
AT+CLVL? // query volume level -- +CLVL: n
AT+CLVL=n // set volume
```
```
ATE0 // disable echo
AT+COPS? // show carrier
AT+CSQ // show signel strength

AT+CHFA=0 // Switch audio to 3.5mm jack
AT+CHFA=1 // Switch audio to AUX
```
#### Texting
```
AT+CMGF=1 // text mode
AT+CMGS="nnnnnn" // send CR followed by chr(26) control-z
```

#### Phone
```
ATDnnnnnnn;
ATH // hang up
```
#### Network connection
```
AT+CFUN=1 // full functionality
AT+CGATT=1
AT+SAPBR=3,1,"Contype","GPRS"
AT+SAPBR=3,1,"APN","wholesale" 
AT+SAPBR=1,1 
AT+SAPBR=2,1  // shows the IP address
AT+SAPBR=0,1 // close
```
#### NTP
```
AT+CNTPCID=1
AT+CNTP="pool.ntp.org",0  // GMT
AT+CNTP // Wait for CNTP response
AT+CCLK? // show local time
```

#### Diagnostic
```
AT+CLDTMF=1,"1,5,0,3,8,1,6,3,0,0,8",80 // Generate DTMF
AT+CENG=1 // switch on engineering mode
AT+CENG? // show cell connections
AT+STTONE=1,20,5000 // dialtone 5s
AT+CPAS // phone status: 0:ready, 3:ringing 4:call in progress
```

#### RJ9
```
Red     Speaker Ground
Green   Speaker +

Black   Mic ?
Yellow  Mic ?
```

#### 3.5mm cable
```

Tip     Red    Left
Ring    White  Right
Ring    Green  Ground
Sleeve  Black  Mic
```

