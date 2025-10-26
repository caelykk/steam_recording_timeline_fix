import json
import glob

def main():
    clips_path = "C:\\Program Files (x86)\\Steam\\userdata\\*********\\gamerecordings\\clips" # Paste your path
    timelines = glob.glob(f"{clips_path}\\**\\timelines\\*.json")

    if timelines:
        for timeline in timelines:
            try:
                with open(timeline, encoding='utf-8') as file:
                    data = json.load(file)
                    if type(data['entries']) == dict:
                        fixed_entries = []
                        for key, entries in data['entries'].items():
                            key = ''
                            fixed_entries.append(entries)

                        fixed_data = {
                            "daterecorded": data["daterecorded"],
                            "starttime": data["starttime"],
                            "entries": fixed_entries
                        }


                        with open(timeline, 'w', encoding='utf-8') as output:
                            json.dump(fixed_data, output, indent='\t', ensure_ascii=False)
            except:
                pass



if __name__ == "__main__":
    main()