import os
import cadquery as cq
from cq_server.ui import UI, show_object


height = 50.0
width = 50.0
depth = 50.0

r = cq.Workplane("front").box(depth,height,width)

r = r + cq.Workplane('top').text("YX / Top", 8, 26)
r = r + cq.Workplane('bottom').text("XY / Bottom", 8, 26)
r = r + cq.Workplane('front').text("ZX / Front", 8, 26)
r = r + cq.Workplane('back').text("XZ / Back", 8, 26)
r = r + cq.Workplane('left').text("ZY / Left", 8, 26)
r = r + cq.Workplane('right').text("YZ / Right", 8, 26)





r = r.rotate((0, 0, 0), (1, 0, 0), 90)
volume = r.findSolid().Volume()
print(f"Total Object volume is: {volume} , Approx. Print Time (100% infill): {volume / 429.6 / 60} hours")
cq.exporters.export(r,"test/test.step")
cq.exporters.export(r,"test/test.stl")
cq.exporters.export(r,"test/test.svg")
cq.exporters.export(r,"test/test.json", tolerance=0.01, angularTolerance=0.1, exportType=cq.exporters.ExportTypes.TJS)
cq.exporters.export(r,"test/test.vrml", tolerance=0.01, angularTolerance=0.1)

r = r.rotate((0, 0, 0), (1, 0, 180), 0)
show_object(r)


