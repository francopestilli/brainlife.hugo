from apscheduler.schedulers.background import BackgroundScheduler as scheduler
import requests
import json
import yaml
import pathlib
import yaml

def gen_md (filepath):
    with open(filepath, 'r') as fp:
        data = json.load(fp)
        # print(data)
        for i in data['response']['award']: 
            url = "https://www.nsf.gov/awardsearch/showAward?AWD_ID="+i['id'] 
            with open('brainlife_lab/brainlife.hugo/content/satelliteprojects/'+i['id']+'.md','w+') as yml:
                yml.write('---\n')
                yaml.dump(i, yml, allow_unicode=True)
                yml.write('url : '+url)
                yml.write('\n---')

if __name__ == "__main__":
    filepath = '/home/ubuntu/brainlife_lab/pestilli-lab--ut-austin/assets/nsf.json'
    gen_md(filepath)