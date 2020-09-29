
import time
import sys
import random

import ibmiotf.application
import ibmiotf.device
import requests


        

#Provide your IBM Watson Device Credentials
organization = "9f49yu" # repalce it with organization ID
deviceType = "sensor" #replace it with device type
deviceId = "430" #repalce with device id
authMethod = "token"
authToken = "1234567890"#repalce with token

def myCommandCallback(cmd):
        
        print("Command received: %s" % cmd.data)        
        if cmd.data['command']=='motoron':
                print("MOTOR ON")
                
                
        if cmd.data['command']=='kukatpallyon':
                print("WATER ON TO KUKATPALLY")
                
                
                #API documentation for sending alerts
                url = "https://www.fast2sms.com/dev/bulk"
                querystring = {"authorization":"IOoA1CzhlQzs76bDEkNC4Jd7qIg6z8ED3CxeRGqKZGYIWd3m9uoBxNwxrzVb","sender_id":"FSTSMS","message":"WATER MANAGEMENT--Water is supplied to your house KUKATPALLY pipeline in 10 min,THANK YOU","language":"english","route":"p","numbers":"phone number"}
                headers = {
                 'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)
        if cmd.data['command']=='asraonagaron':
                print("WATER ON TO AS RAO NAGAR")
                
                
                #API documentation for sending alerts
                url = "https://www.fast2sms.com/dev/bulk"
                querystring = {"authorization":"IOoA1CzhlQzs76bDEkNC4Jd7qIg6z8ED3CxeRGqKZGYIWd3m9uoBxNwxrzVb","sender_id":"FSTSMS","message":"WATER MANAGEMENT--Water is supplied to your house AS RAO NAGAR pipeline in 10 min,THANK YOU","language":"english","route":"p","numbers":"phone number"}
                headers = {
                 'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)
        if cmd.data['command']=='house1bill':
                print("HOUSE 1 BILL HAS BEEN GENERATED")
        if cmd.data['command']=='house2bill':
                print("HOUSE 2 BILL HAS BEEN GENERATED")      
                
        elif cmd.data['command'] == 'motoroff':
            print("MOTOR OFF")
            
            
                
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

deviceCli.connect()



while True:
        
        L = random.randint(0, 1000);
        F = random.randint(0, 100);
        S = random.randint(0, 100);
        
        
       
        data = {'d':{ 'tanklevel' : L, 'flowrate1': F, 'flowrate2': S }}
        u=time.asctime(time.localtime(time.time()))
        print(u)
        

        #print data
        def myOnPublishCallback():
            print ("Published Your Water Tank level = %s %%" % L, "Flow Rate1 = %s %%" % F, "Flow Rate2 = %s %%" % S, "to IBM Watson")

        success = deviceCli.publishEvent("event", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
            
        
        deviceCli.commandCallback = myCommandCallback
        time.sleep(10)
       

      
            







# Disconnect the device and application from the cloud
deviceCli.disconnect()
