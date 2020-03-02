import pandas as pd
# containers_url = 'https://api.data.amsterdam.nl/afval/v1/containers/?detailed=1&format=csv&page_size=15000'
containers_url = 'https://api.data.amsterdam.nl/afval/v1/containers/?detailed=1&format=csv'
wells_url = 'https://api.data.amsterdam.nl/afval/v1/wells/?format=csv'
container_types_url = 'https://api.data.amsterdam.nl/afval/v1/containertypes/?format=csv'

print("Starting import...")

# Grab containers and create a smaller more relevant list. Fields can be added later.
container_list = pd.read_csv(containers_url)
print("Cleaning containers")
containers = container_list[['id', 'active', 'address', 'owner.name', 'owner.id', 'container_type.id', 'well.geometrie.type', 'waste_name', 'waste_type', 'well.id', 'well.geometrie.coordinates.0', 'well.geometrie.coordinates.1']]
containers = containers.rename(columns={
    'id': 'container_id',
    'owner.name': 'buurt',
    'owner.id': 'owner_id',
    'container_type.id': 'container_type_id',
    'well.geometrie.type': 'well_type',
    'well.id': 'well_id',
    'latitude': 'well.geometrie.coordinates.0',
    'longitude': 'well.geometrie.coordinates.1'
}).set_index('container_id')
containers.to_csv('data/containers.csv')

print("Importing wells")
well_list = pd.read_csv(wells_url)
print("Cleaning wells")
wells = well_list[['id', 'stadsdeel', 'buurt_code', 'geometrie.type']]
wells = wells.rename(columns={'id': 'well_id', 'geometry.type': 'well_type'}).set_index('well_id')
wells.to_csv('data/wells.csv')

print("Importing container types")
container_types = pd.read_csv(container_types_url)
print("Cleaning container types")
container_types = container_types[['id', 'name', 'volume', 'weight']]
container_types = container_types.rename(columns={
    'id': 'container_type_id'
}).set_index('container_type_id')
container_types.to_csv('data/container_types.csv')
