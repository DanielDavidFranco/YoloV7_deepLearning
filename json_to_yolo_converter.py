import json
import os
import pprint

path ='json_'
file_paths = []
file_names = []
for root, directories, file in os.walk(path):
    for file in file:
        if(file.endswith(".json")):
            filepath = os.path.join(root,file)
            print(filepath)
            file_paths.append(filepath)
            file_names.append(file)
            
for j, file in enumerate(file_paths):
    data = json.load(open(file, 'r'))
    try:
        del data['imageData']
        with open(file, "w") as f:
            json.dump(data, f, indent=1)
    except:
        pass 
            
for j, file in enumerate(file_paths):
    lines = []
    data = json.load(open(file, 'r'))
    #print(data)
    image_width = data['imageWidth']
    image_height = data['imageHeight']
    polygons = data['shapes']
    print("polygons: ")
    pprint.pprint(polygons)
    number_of_tags_in_image = len(polygons)
    #print("number_of_tags_in_image: ", number_of_tags_in_image)
    
    for t in range(number_of_tags_in_image):
        #print(t)
        label = polygons[t]['label']
        id_class = polygons[t]['group_id']
        points = polygons[t]['points']
        #print(label, id_class)
        str_row = str(id_class) + " "
        #print("points: ")
        #pprint.pprint(points)
        number_of_points_of_polygon = len(points)
        print("number_of_points_of_polygon: ", number_of_points_of_polygon)
        
        for i,p in enumerate(points):
            x = p[0] / image_width
            y = p[1] / image_height
            #print(x,y)
            if i!=number_of_points_of_polygon-1:
                added_point_string = str(x) + " " + str(y) + " "
            else:
                added_point_string = str(x) + " " + str(y)
            str_row += added_point_string
        lines.append(str_row)
    print("lines: ")
    #print(lines)
    #print(len(lines))
    pprint.pprint(lines)
    
    with open("yolo_format_/"+file_names[j].replace(".json","")+".txt", "w") as txt_file:
        for row in lines:
            txt_file.write('%s\n' % row)
        txt_file.close()
            
    
    