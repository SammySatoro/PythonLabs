def lab11task7():
    countries = {'Russia' : ['Moscow', 'Petersburg', 'Novgorod', 'Kaluga'],
                 'Ukraine' : ['Kiev', 'Donetsk', 'Odessa'],
                 'Japan' : ['Osaka', 'Tokyo', 'Kyoto', 'Hiroshima']}
    cityCount = int(input())
    for i in range(cityCount):
        city = input()
        for country in countries:
            if city in countries[country]:
                print(country)
