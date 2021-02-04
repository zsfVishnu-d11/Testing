final_dictionary = {}
final_dictionary['global'] = 'global_sheet'
final_dictionary['alias'] = 'alias_sheet'
final_dictionary['category'] = 'token'
final_dictionary['version'] = 'version'

print(version)

with open(ROOT_DIR+'/../jsons/' + token + '.json','w') as outfile:
  json.dump(final_dictionary,outfile,indent = 4)
