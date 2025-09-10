programming_dictionary = {
    'bug': 'An error',
    'code': 'instructions',
    'loop': 'doing continously',
}
print(programming_dictionary['bug'])

programming_dictionary['compile'] = 'running program' # Adding new key, value to dic
print(programming_dictionary)

empty_dictionary = {} # creating empty dic

for key in programming_dictionary: # looping through
    print(key)
    print(programming_dictionary[key])

programming_dictionary = {} # wiping dic
print(programming_dictionary)

travel_vlog = { # Nesting dic inside dic
    'France': {'cities_visited': ['Paris', 'Lille', 'Dijon'], 'total_visits': 12},
    'germany': ['berlin', 'kotlin', 'gitlo']
}
print(travel_vlog)

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
print(travel_vlog)

