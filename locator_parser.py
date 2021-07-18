import json
# Opening JSON file

def read_locators(path): # json or cue
    path '../AbletonParser_data/deep_southern_ballad_locators.json'
    with open(path) as json_file:
        locators = json.load(json_file)
        print("Type:", type(locators))
        return locators
    
def cue_to_json(path):
    path '../AbletonParser_data/deep_southern_ballad_locators.json'
    locator_count = 0
    track_id = "no_track_id"
    track,locators,current_locator = {},{},{}

    with open(path) as fp:
        while True:
            line = fp.readline()
            if not line:
                break   
                
            l = line.split()
            if l[0] == 'FILE': # file name
                track_id = " ".join(l[1:-2])
                track['track_id'] = track_id.replace("\"", '')
                continue
            if l[0] == 'TITLE': # locator name
                title = l[1].replace("\"", '') 
                
                current_locator['title'] = l[1].replace("\"", '')
                continue
            if l[0] == 'INDEX': # locator time index
                if current_locator['title'] == '':
                    continue
                locator_count +=1
                current_locator['index'] = "".join(l[2:])
                
                locators['locator_'+str(locator_count)] = current_locator
                current_locator = {}
                continue
            if l[0] == 'TRACK': # useless, skip
                pass
        track['LOCATORS'] = locators
    
    
    json.dump(track,open(path.split['/'][-1].split('.')[0]),"w"),indent=4)
    print(json_object)
