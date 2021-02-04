import json
final_dictionary = {}
final_dictionary['global'] = 'global_sheet'
final_dictionary['alias'] = 'alias_sheet'
final_dictionary['category'] = 'token'
final_dictionary['version'] = 'version'
version = '1.0.1'
print(version)

with open('sample.json','w') as outfile:
  json.dump(final_dictionary,outfile,indent = 4)
