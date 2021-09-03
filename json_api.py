import requests
import json 
import time

results =[]
response = requests.get('https://formulae.brew.sh/api/formula.json')
packages_jason = response.json()

t1= time.perf_counter()
for package in packages_jason:
    package_name = package['name']
    package_desc = package['desc']


    package_url =  f'https://formulae.brew.sh/api/formula/{package_name}.json'

    r=requests.get(package_url)
    package_json =r.json()

    #package_str = json.dumps(package_json, indent=2) this line is just to show a jason pacakge in a readable way.

    install_30 = package_json['analytics']['install_on_request']['30d'][package_name]
    install_90 = package_json['analytics']['install_on_request']['90d'][package_name]
    install_365 = package_json['analytics']['install_on_request']['365d'][package_name]

    data ={
        'name': package_name,
        'desc': package_desc,
        'analytics':{
            '30d': install_30,
            '90d': install_90,
            '365d': install_365


        }
    }

    results.append(data)
    time.sleep(response.elapsed.total_seconds())
    print(f'Got {package_name} in {response.elapsed.total_seconds()} seconds')
    
t2=time.perf_counter()
print(f'finished in {t2-t1} seconds')

with open('package_info.json', 'w') as f:
    json.dump(results,f,indent=2)


    #print(package_name, package_desc, install_30, install_90, install_365)
