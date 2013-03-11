from pprint import pprint
import advdupe
from advdupe import Angle, Vector

f = open("warp.txt", "rb")
e2 = f.read()
f.close()

doc = advdupe.AdvDupeDocument()
doc.load("warp_drive.txt")
doc.entities = \
    {27: {'Class': 'generator_energy_wind',
          'EntityMods': {'CollisionGroupMod': 20,
                         'colour': {'Color': {'a': 0,
                                              'b': 255,
                                              'g': 255,
                                              'r': 255},
                                    'RenderFX': 0,
                                    'RenderMode': 0}},
          'Extra_Data': {'extra_bool': False, 'extra_num': 0},
          'LocalAngle': Angle(0.0909501, 89.9128, -0.0158081),
          'LocalPos': Vector(80.7559, -4.10986, 166.567),
          'Model': 'models/ls_models/cloudstrifexiii/windmill/windmill_large.mdl',
          'PhysicsObjects': {0: {'Frozen': True,
                                 'LocalAngle': Angle(0.0909501, 89.9128, 359.984),
                                 'LocalPos': Vector(80.7559, -4.10986, 166.567)}},
          #'SavedParentIdx': 28,
          'Skin': 0,
          'sub_type': 'large_1',
          'type': 'generator_energy_wind'},
     28: {'Class': 'gmod_wire_hoverdrivecontroler',
          'EntityMods': {'CollisionGroupMod': 20,
                         'WireDupeInfo': {'Wires': {}},
                         'colour': {'Color': {'a': 0,
                                              'b': 255,
                                              'g': 255,
                                              'r': 255},
                                    'RenderFX': 0,
                                    'RenderMode': 0}},
          'LocalAngle': Angle(6.33298e-12, 90.028, 1.61349e-06),
          'LocalPos': Vector(9.55664, -4.21143, 131.183),
          'Model': 'models//props_c17/utilityconducter001.mdl',
          'PhysicsObjects': {0: {'Frozen': True,
                                 'LocalAngle': Angle(6.33298e-12, 90.028, 1.61349e-06),
                                 'LocalPos': Vector(9.55664, -4.21143, 131.183)}},
          'Skin': 0},
     70: {'Class': 'gmod_wire_expression2',
          'EntityMods': {'CollisionGroupMod': 20,
                         'WireDupeInfo': {'Wires': {}},
                         'colour': {'Color': {'a': 0,
                                              'b': 255,
                                              'g': 255,
                                              'r': 255},
                                    'RenderFX': 0,
                                    'RenderMode': 0}},
          'LocalAngle': Angle(89.9999, -179.984, 0.0),
          'LocalPos': Vector(20.8682, -11.3804, 131.107),
          'Model': 'models/beer/wiremod/gate_e2.mdl',
          'PhysicsObjects': {0: {'Frozen': True,
                                 'LocalAngle': Angle(89.9999, 0.0162609, 180.0),
                                 'LocalPos': Vector(20.8682, -11.3804, 131.107)}},
          #'SavedParentIdx': 28,
          'Skin': 0,
          '_inputs': {1: {}, 2: {}},
          '_name': 'generic',
          '_original': e2,
          '_outputs': {1: {}, 2: {}},
          '_vars': {}},
     112: {'Class': 'resource_node',
           'EntityMods': {'CollisionGroupMod': 20,
                          'RDDupeInfo': {'cons': {}, 'entities': {}},
                          'colour': {'Color': {'a': 0,
                                               'b': 255,
                                               'g': 255,
                                               'r': 255},
                                     'RenderFX': 0,
                                     'RenderMode': 0}},
           'Extra_Data': {'auto_link': False, 'custom_name': ''},
           'LocalAngle': Angle(2.02307e-07, 90.0, 90.0),
           'LocalPos': Vector(140.024, -4.12451, 131.045),
           'Model': 'models/snakesvx/large_res_node.mdl',
           'PhysicsObjects': {0: {'Frozen': True,
                                  'LocalAngle': Angle(2.02307e-07, 90.0, 90.0),
                                  'LocalPos': Vector(140.024, -4.12451, 131.045)}},
           #'SavedParentIdx': 28,
           'Skin': 0,
           'sub_type': 'large_node',
           'type': 'resource_node'},
     116: {'Class': 'storage_cache',
           'EntityMods': {'CollisionGroupMod': 20,
                          'WireDupeInfo': {'Wires': {}},
                          'colour': {'Color': {'a': 0,
                                               'b': 255,
                                               'g': 255,
                                               'r': 255},
                                     'RenderFX': 0,
                                     'RenderMode': 0}},
           'Extra_Data': {'extra_bool': False, 'extra_num': 0},
           'LocalAngle': Angle(-0.0879669, -89.9837, -90.0002),
           'LocalPos': Vector(21.1484, -4.20947, 131.075),
           'Model': 'models/ce_ls3additional/resource_cache/resource_cache_large.mdl',
           'PhysicsObjects': {0: {'Frozen': True,
                                  'LocalAngle': Angle(-0.0879669, -89.9837, 270.0),
                                  'LocalPos': Vector(21.1484, -4.20947, 131.075)}},
           #'SavedParentIdx': 28,
           'Skin': 0,
           'sub_type': 'large',
           'type': 'storage_cache'}}
doc.constraints = \
    {1: {'Entity': {1: {'Bone': 0, 'Index': 112}, 2: {'Bone': 0, 'Index': 28}},
         'Type': 'NoCollide'},
     2: {'Entity': {1: {'Bone': 0,
                        'Index': 28,
                        'LPos': Vector(-5.47964, 8.69213, 1.37598)},
                    2: {'Bone': 0,
                        'Index': 0,
                        'LPos': Vector(15.0732, 27.4683, 6.3042),
                        'World': True}},
         'LPos1': Vector(-5.47964, 8.69213, 1.37598),
         'LPos2': Vector(-12940.2, -6529.35, -7199.47),
         'Type': 'AdvBallsocket',
         'forcelimit': 0,
         'nocollide': 1,
         'onlyrotation': 1,
         'torquelimit': 0,
         'xfric': 0,
         'xmax': 180,
         'xmin': -180,
         'yfric': 0,
         'ymax': 180,
         'ymin': -180,
         'zfric': 0,
         'zmax': 180,
         'zmin': -180},
     3: {'Entity': {1: {'Bone': 0, 'Index': 27}, 2: {'Bone': 0, 'Index': 116}},
         'Type': 'Weld',
         'forcelimit': 0,
         'nocollide': True},
     4: {'Entity': {1: {'Bone': 0,
                        'Index': 70,
                        'LPos': Vector(1.20069, -0.328333, 0.731349)},
                    2: {'Bone': 0,
                        'Index': 0,
                        'LPos': Vector(32.8555, 45.8452, 11.1934),
                        'World': True}},
         'LPos1': Vector(1.20069, -0.328333, 0.731349),
         'LPos2': Vector(-12922.4, -6510.97, -7194.58),
         'Type': 'AdvBallsocket',
         'forcelimit': 0,
         'nocollide': 1,
         'onlyrotation': 1,
         'torquelimit': 0,
         'xfric': 0,
         'xmax': 180,
         'xmin': -180,
         'yfric': 0,
         'ymax': 180,
         'ymin': -180,
         'zfric': 0,
         'zmax': 180,
         'zmin': -180},
     5: {'Entity': {1: {'Bone': 0,
                        'Index': 27,
                        'LPos': Vector(-20.9575, 24.0707, 114.07)},
                    2: {'Bone': 0,
                        'Index': 0,
                        'LPos': Vector(-81.6973, -199.431, -71.353),
                        'World': True}},
         'LPos1': Vector(-20.9575, 24.0707, 114.07),
         'LPos2': Vector(-13036.9, -6756.25, -7277.13),
         'Type': 'AdvBallsocket',
         'forcelimit': 0,
         'nocollide': 1,
         'onlyrotation': 1,
         'torquelimit': 0,
         'xfric': 0,
         'xmax': 180,
         'xmin': -180,
         'yfric': 0,
         'ymax': 180,
         'ymin': -180,
         'zfric': 0,
         'zmax': 180,
         'zmin': -180},
     6: {'Entity': {1: {'Bone': 0, 'Index': 70}, 2: {'Bone': 0, 'Index': 116}},
         'Type': 'Weld',
         'deleteonbreak': True,
         'forcelimit': 0,
         'nocollide': True},
     7: {'Entity': {1: {'Bone': 0,
                         'Index': 116,
                         'LPos': Vector(42.091, -35.0312, 25.8903)},
                     2: {'Bone': 0,
                         'Index': 0,
                         'LPos': Vector(-24.9512, -83.6084, -24.9771),
                         'World': True}},
          'LPos1': Vector(42.091, -35.0312, 25.8903),
          'LPos2': Vector(-12980.2, -6640.42, -7230.75),
          'Type': 'AdvBallsocket',
          'forcelimit': 0,
          'nocollide': 1,
          'onlyrotation': 1,
          'torquelimit': 0,
          'xfric': 0,
          'xmax': 180,
          'xmin': -180,
          'yfric': 0,
          'ymax': 180,
          'ymin': -180,
          'zfric': 0,
          'zmax': 180,
          'zmin': -180},
      8: {'Entity': {1: {'Bone': 0, 'Index': 116}, 2: {'Bone': 0, 'Index': 112}},
          'Type': 'Weld',
          'forcelimit': 0,
          'nocollide': True},
      9: {'Entity': {1: {'Bone': 0, 'Index': 70}, 2: {'Bone': 0, 'Index': 28}},
          'Type': 'NoCollide'},
     10: {'Entity': {1: {'Bone': 0, 'Index': 28},
                     2: {'Bone': 0,
                         'Index': 0,
                         'LPos': Vector(-12955.2, -6556.82, -7205.77),
                         'World': True}},
          'Type': 'NoCollide'},
     11: {'Entity': {1: {'Bone': 0, 'Index': 27}, 2: {'Bone': 0, 'Index': 28}},
          'Type': 'NoCollide'},
     12: {'Entity': {1: {'Bone': 0, 'Index': 116}, 2: {'Bone': 0, 'Index': 112}},
          'Type': 'NoCollide'},
     13: {'Entity': {1: {'Bone': 0, 'Index': 28}, 2: {'Bone': 0, 'Index': 116}},
          'Type': 'NoCollide'}}

z = 14
for i in xrange(1, 11):
    k = 100 + i
    doc.entities[k] = \
        {'Class': 'gmod_wire_latch',
         'EntityMods': {'CollisionGroupMod': 20,
                        'WireDupeInfo': {'Activate': 1,
                                         'Bone1': 0,
                                         'Bone2': 0,
                                         'Ent1': i,
                                         'Ent2': 28,
                                         'NoCollide': 0,
                                         'Wires': {}},
                        'colour': {'Color': {'a': 0,
                                             'b': i,
                                             'g': i,
                                             'r': i},
                                   'RenderFX': 0,
                                   'RenderMode': 0}},
         'LocalAngle': Angle(-89.9075, 99.4048, -99.3771),
         'LocalPos': Vector(21.1123, -11.3745, 145.121),
         'Model': 'models/jaanus/wiretool/wiretool_gate.mdl',
         'PhysicsObjects': {0: {'Frozen': True,
                                'LocalAngle': Angle(-89.9075, 99.4048, 260.623),
                                'LocalPos': Vector(21.1123, -11.3745, 145.121)}},
         #'SavedParentIdx': 28,
         'Skin': 0}
    doc.constraints[z] = \
            {'Entity': {1: {'Bone': 0, 'Index': k}, 2: {'Bone': 0, 'Index': 28}},
             'Type': 'Weld',
             'forcelimit': 0,
             'nocollide': True}
    z = z + 1
    doc.constraints[z] = \
            {'Entity': {1: {'Bone': 0, 'Index': k}, 2: {'Bone': 0, 'Index': 28}},
             'Type': 'NoCollide'}
    z = z + 1
    doc.constraints[z] = \
            {'Entity': {1: {'Bone': 0,
                            'Index': k,
                            'LPos': Vector(1.28624, 1.71482, 1.15996)},
                        2: {'Bone': 0,
                            'Index': 0,
                            'LPos': Vector(10.9111, -27.2788, -4.00244),
                            'World': True}},
             'LPos1': Vector(1.28624, 1.71482, 1.15996),
             'LPos2': Vector(-12944.3, -6584.09, -7209.78),
             'Type': 'AdvBallsocket',
             'forcelimit': 0,
             'nocollide': 1,
             'onlyrotation': 1,
             'torquelimit': 0,
             'xfric': 0,
             'xmax': 180,
             'xmin': -180,
             'yfric': 0,
             'ymax': 180,
             'ymin': -180,
             'zfric': 0,
             'zmax': 180,
             'zmin': -180}
    z = z + 1
doc.dump("warp_drive_10slots.txt")