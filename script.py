import json

with open('config.json') as infile:
  data = json.load(infile)

if data['playerController']["onJoinCheckWhitelist"] == False:
    data["playerController"]["onJoinCheckWhitelist"] = True
    print('Activation de la whitelist !')
else:
    data["playerController"]["onJoinCheckWhitelist"] = False
    print('Désactivation de la whitelist !')

with open('config.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)