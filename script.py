# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def convert_damage_to_float(input):
    if input[0] != "D":
        if input[-1] == "M":
            return float(input[:(len(input)-1)])*1000000
        elif input[-1] == "B":
            return float(input[:(len(input)-1)])*1000000000
    else:
        return input

# To test function uncomment lines below.
#print(convert_damage_to_float("Damages not recorded"))
#print(convert_damage_to_float("100M"))
#print(convert_damage_to_float("1.42B"))


# write your construct hurricane dictionary function here:
def hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricanes = {}
    for i in range(len(names)):
        hurricanes[names[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": damages[i], "Deaths": deaths[i]}
    return hurricanes

# To test function uncomment line below.
#print(hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths))


# write your construct hurricane by year dictionary function here:
def year_dictionary(dictionary):
    hurricanes_by_year = {}
    name_list = dictionary.keys()
    for name in name_list:
        current_year = dictionary[name].get("Year")
        if hurricanes_by_year.get(current_year, False) == False:
            hurricanes_by_year[current_year] = [dictionary[name]]
        else:
            (hurricanes_by_year.get(current_year)).append([dictionary[name]])
    return hurricanes_by_year

# To test function uncomment line below.
#print(year_dictionary(hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths)))


# write your count affected areas function here:
def count_affected_areas(dictionary):
    canes_by_area = {}
    name_list = dictionary.keys()
    for name in name_list:
        current_area_list = (dictionary[name].get("Areas Affected"))
        for area in current_area_list:
            if canes_by_area.get(area, False) == False:
                canes_by_area[area] = 1
            else:
                canes_by_area[area] += 1
    return canes_by_area

# To test function uncomment line below.
#print(count_affected_areas(hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths)))


# write your find most affected area function here:
def most_affected_area(dictionary):
    area_list = list(dictionary.keys())
    count_list = list(dictionary.values())
    most = -1
    most_index = -1
    for i in range(len(dictionary)):
        if count_list[i] > most:
            most = count_list[i]
            most_index = i
    area_most = area_list[most_index]
    count_most = count_list[most_index]
    return [area_most, count_most]

# To test function uncomment line below.
#print(most_affected_area(count_affected_areas(hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths))))


# write your greatest number of deaths function here:
def greatest_deaths(dictionary):
    most_deaths = -1
    most_name = ["default"]
    for names in dictionary:
        cane = dictionary.get(names)
        deaths = cane.get("Deaths", -1)
        if deaths > most_deaths:
            most_deaths = deaths
            most_name[0] = cane
    return [most_name[0].get("Name"), most_deaths]

# To test function uncomment line below.
#print(greatest_deaths(hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths)))


# write your categorize by mortality function here:
def mortality_ratings(dictionary):
    mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for names in dictionary:
        cane = dictionary.get(names)
        deaths = cane.get("Deaths", -1)
        if deaths > 10000:
            mortality[5].append(cane)
        elif deaths > 1000:
            mortality[4].append(cane)
        elif deaths > 500:
            mortality[3].append(cane)
        elif deaths > 100:
            mortality[2].append(cane)
        elif deaths > 0:
            mortality[1].append(cane)
        else:
            mortality[0].append(cane)
    return mortality

# To test function uncomment line below.
#print(mortality_ratings(hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths)))


# write your greatest damage function here:
def greatest_damage(dictionary):
    most_damage = -1
    most_name = ["default"]
    for names in dictionary:
        cane = dictionary.get(names)
        damage = cane.get("Damage", 0)
        damage_float = convert_damage_to_float(damage)
        if isinstance(damage_float, str) == False:
            if damage_float > most_damage:
                most_damage = damage_float
                most_name[0] = cane.get("Name")
    return [most_name, most_damage]

# To test function uncomment line below.
#print(greatest_damage(hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths)))


# write your categorize by damage function here:
def damage_ratings(dictionary):
    damages = {"Damages not recorded": [], 0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for names in dictionary:
        cane = dictionary.get(names)
        damage = cane.get("Damage", -1)
        damage_float = convert_damage_to_float(damage)
        if damage_float == "Damages not recorded":
            damages["Damages not recorded"].append(cane)
        elif damage_float > 50000000000:
            damages[5].append(cane)
        elif damage_float > 10000000000:
            damages[4].append(cane)
        elif damage_float > 1000000000:
            damages[3].append(cane)
        elif damage_float > 100000000:
            damages[2].append(cane)
        elif damage_float > 0:
            damages[1].append(cane)
        else:
            damages[0].append(cane)
    return damages

# To test function uncomment line below.
#print(damage_ratings(hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths)))