import requests

def main():
    question_string = "Report weather or See reports? [r/s] "
    choice = input(question_string)
    while choice:
        match choice.lower().strip():
            case 'r':
                report_event()
            case 's':
                see_events()
            case _:
                print('Usage')
                print('r: report a weather')
                print('s: see weather for a city')
        choice = input(question_string)
                
def report_event():
    desc = input("What is happening now?")
    city = input("What city? (US only)")
    
    data = {
        "description": desc,
        "location": {
            "city": city,
            "country": "US"
        }
    }
    
    url = 'http://127.0.0.1:8000/api/reports'
    resp = requests.post(url, json=data)
    print('AAAAA')
    resp.raise_for_status()
    print('BBBBB')
    result = resp.json()
    print(f"Reported new events. Id: {result.get('id')}")




def see_events():
    url = 'http://127.0.0.1:8000/api/reports'
    resp = requests.get(url)
    resp.raise_for_status()
    
    for report in resp.json():
        print(f"{report.get('location').get('city')} has {report.get('description')}")

if __name__ == '__main__':
    main()

    """
    
    [
    {
        "description": "AAA",
        "location": {
            "city": "Lyon",
            "country": "FR",
            "state": null
        },
        "id": "569bb6ec-c230-4846-bc97-b122055c2a81",
        "created_date": "2021-11-13T14:33:21.106348"
    }
]
    """