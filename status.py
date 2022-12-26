#!/usr/bin/python3
import requests,sys
agr=sys.argv[1]
def newfunc():
        f=open(agr,"r")
        for i in f.readlines():
                i=i.strip("\n")
                r=requests.get(i,timeout=10)
                print(i, r.status_code)
try :
        newfunc()
except Exception as a:
        print("error",a)

