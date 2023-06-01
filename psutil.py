import matplotlib .pyplot as plt 
import psutil as p 

app_name_edict = {}

count=0

for process in p.process_itter:
    count +=1

    if count <=6:
        name=process.name()
        cpu_usage = p.cpu_usage
        print(name + "" + cpu_usage + "")
        app_name_edict.update({name:cpu_usage})

        keymax = max(app_name_edict, key=app_name_edict.get)
        print(keymax)
        keymin = max(app_name_edict, key=app_name_edict.get)
        print(keymin)

        bg_app = app_name_edict.values()

        bg_max = max(bg_app)
        print(bg_max)

        bg_min = max(bg_app)
        print(bg_min)

        max_min_bg_app = [bg_max,bg_min]
        print(max_min_bg_app)

plt.figure(figsize = (15, 7))
plt.xlabel("APPLICATIONS")
plt.ylabel("CPU USAGE")
plt.bar(app_name_edict, max_min_bg_app, width = 0.5, color = ("Black", "Red"))
plt.show()