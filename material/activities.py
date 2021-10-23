import json
def activities(x,activity_id):
    f=open('activities.json','r')
    l=json.load(f)
    f.close()
    dd=[d for d in l if d.get(activity_id)]
    if len(dd)==1:
        ld=dd[0].get(activity_id)
        ddd=[d for d in ld if d.get('value')==x]
        if len(ddd)==1:
            return ddd[0].get('text')
        else:
            return 'WRONG choice'
