
from pxr import Usd, Work

Work.SetConcurrencyLimitArgument(1)

stage = Usd.Stage.OpenMasked('scene.usda', Usd.StagePopulationMask(['/Scene/asset1/mesh_0']))

print "OpenMasked successful"
