travel_vlog = [ # Dic inside list
    {
        'Country': 'France',
        'cities_visited': ['Paris', 'Lille', 'Dijon'],
        'total_visits': 12,
    },
    {
        'Country': 'Germany',
        'Cities_Visited': ['Berlin', 'kotlin', 'gitlo'],
        'total_visits': 10,
    }
]

countries = input("Enter the contry to add to the travel vlog: ")
visits = int(input("Enter the number of visits: "))
cities = input("Enter the cities: ")

def update_travel_vlog(travel_vlog, countries, cities, visits):
    travel_vlog.append({
        'Country': countries,
        'Cities_Visited': cities,
        'total_visits': visits
    })

update_travel_vlog(travel_vlog, countries, cities, visits)

print(travel_vlog)