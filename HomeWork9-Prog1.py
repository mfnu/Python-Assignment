'''-----------------------------------------------------------------------------------------------------
Author: Madhulika
Program: Home Work 9 Program 1.
Description: 4 psutil readings and displaying in web page.
Version: 1
Date: 6/12/2015
-----------------------------------------------------------------------------------------------------'''
import psutil, datetime
from wsgiref.simple_server import make_server

def hello_world_app(environ,start_response):

    message=""
    status = '200 ok'
    headers = [('Content-type', 'html; charset=utf-8')]
    start_response(status,headers)
    
    #1 psutil parameter
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    print("\nBOOT TIME:", boot_time)
    

    #2 psutil parameter
    cpu_util = psutil.cpu_percent(interval=1, percpu=True)
    i=1
    print("\nCPU UTILIZATION:")
    for cpu in cpu_util:
        print("CPU {} : {}% ---".format(i, cpu))
        i+=1

    #3 psutil parameter
    mem = psutil.virtual_memory()
    availablemem=psutil.avail_virtmem()
    #4 psutil parameter
    usedmem=psutil.used_phymem()
    #5 psutil parameter
    usedper=mem.percent
    THRESHOLD = 100 * 1024 * 1024  # 100MB
    

    message +="<TABLE border=10> <TR> <TD> BOOT TIME</TD><TD>"+boot_time+"</TD></TR>"
    #message +="<TR><TD>CPU UTILIZATION</TD><TD><TABLE BORDER =2><TR><TD>CPU1</TD><TD>VAL</TD></TR><TR><TD>CPU2</TD><TD>VAL</TD></TR><TR><TD>CPU3</TD><TD>VAL</TD></TR></TABLE></TD></TR>"
    message +="<TR> <TD> AVAILABLE MEMORY </TD><TD>"+str(availablemem)+"</TD></TR>"
    message +="<TR> <TD> USED MEMORY </TD><TD>"+str(usedmem)+"</TD></TR>"
    message +="<TR> <TD> USED PERCENT </TD><TD>"+str(usedper)+"</TD></TR></TABLE>"
    return[bytes(message,'utf-8')]

httpd=make_server('',8000,hello_world_app)
print("Serving on port 8000...")
httpd.serve_forever()

