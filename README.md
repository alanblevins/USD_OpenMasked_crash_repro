Repro files for Stage.OpenMasked crash
======================================

In USD 0.8.4, 0.8.5, and possibly earlier versions, Stage.OpenMasked
will crash when masking to an instanced Prim and using multiple threads.

scene.usda declares two prims (asset1 and asset2) that reference sphere.usdc, 
which contains many Mesh prims below an Xform. asset1 sets instanceable as
true, asset2 does not.

crash.py demonstrates the issue:
```python
from pxr import Usd
stage = Usd.Stage.OpenMasked('scene.usda', Usd.StagePopulationMask(['/Scene/asset1/mesh_0']))

print "OpenMasked successful"
```

When masking to a Prim that is an instance, USD will crash most of the time.

Masking to the same Prim in asset2 does not crash (nocrash_not_instance.py):
```python
from pxr import Usd
stage = Usd.Stage.OpenMasked('scene.usda', Usd.StagePopulationMask(['/Scene/asset2/mesh_0']))

print "OpenMasked successful"
```

Also, limiting USD to a single thread will avoid the crash when masking to
the instanced Prim (nocrash_one_thread.py):
```python
from pxr import Usd, Work

Work.SetConcurrencyLimitArgument(1)

stage = Usd.Stage.OpenMasked('scene.usda', Usd.StagePopulationMask(['/Scene/asset1/mesh_0']))

print "OpenMasked successful"
```

