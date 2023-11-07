# houdini-codes
Like a barn, except it houses houdini tools, python scripts and other nonsense. 

### vops/windbraker
Evaluates the velocity of a particle and depending on the proximity to a guide 
vector field, it absorbs the potential velocity and slowly blends it in 
it's own velocity. 


### Set parameters to selected nodes
In this example, 4 camera nodes are selected and their iconsize parameter is set to 50
```python
selected = hou.selectedNodes()
for each in selected: 
    each.parm('iconscale').set(50)
```



### [python/scaffolding.py](https://github.com/se-beast-ian/houdini-codes/blob/main/python/scaffolding.py)
Windows > Python Source Editor. Paste the python script and hit apply. 
The python script will create scaffolders (geo nodes) for each object in the list *scaffolding_items*.


