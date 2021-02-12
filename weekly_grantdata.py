from apscheduler.schedulers.background import BackgroundScheduler as scheduler
import requests
import json
import pathlib
def myfn():
    # Insert your requests code here
    print('Hello')
    filepath = '/home/ubuntu/brainlife_lab/pestilli-lab--ut-austin/assets/nsf.json'
    nsf_response = requests.get('https://api.nsf.gov/services/v1/awards.json?keyword="franco+pestilli"&printFields=startDate,expDate,id,title,awardee,agency,awardeeName,piFirstName,piLastName,coPDPI')
    
    # with open('/home/ubuntu/brainlife_lab/brainlife.hugo/themes/brainlife.hugo.theme/static/assets/outputfile.json', 'w') as outf:
    #     json.dump(response.json,outf)        
    # print('written json response')
    pathlib.Path(filepath).write_bytes(nsf_response.content)
sch = scheduler()
sch.add_job(myfn, 'interval', seconds=604800)
sch.start()

# This code will be executed after the sceduler has started
try:
        print('Scheduler started, ctrl-c to exit!')
        while 1:
            # Notice here that if you use "pass" you create an unthrottled loop
            # try uncommenting "pass" vs "input()" and watching your cpu usage.
            # Another alternative would be to use a short sleep: time.sleep(.1)

            pass
            #input()
except KeyboardInterrupt:
        if sch.state:
            sch.shutdown()