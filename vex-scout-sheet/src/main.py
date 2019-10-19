import vexdb as v
import json

print('Find event SKU - looks like: RE-VRC-**-****')
print()
thing = input('SKU: ')
print()

numTeams = v.getNumTeams(sku=thing)
teams = v.getTeams(sku=thing, get_all=True)

teams_json = json.dumps(teams)
data = json.loads(teams_json)

print('teams')
for x in range(0, numTeams):
    print(data[x]['number'])
print()
print('organizations')
for x in range(0, numTeams):
    print(data[x]['organization'])