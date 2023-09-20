import pickle
import sklearn
import numpy

with open(r'C:\Users\MANAN\Desktop\Manan Shah\VIT\Events\HackBattle\doofenshmirtz-hackbattle\models\kmeans_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def get_hotspots():
    with open(r'C:\Users\MANAN\Desktop\Manan Shah\VIT\Events\HackBattle\doofenshmirtz-hackbattle\models\structure_coordinates.pkl', 'rb') as coords_file:
        coords = pickle.load(coords_file)
        coords = coords.tolist()
        for i in coords:
            x = i[0]
            y = i[1]
            i[0] = y
            i[1] = x
        print(coords)
    return coords

get_hotspots()


