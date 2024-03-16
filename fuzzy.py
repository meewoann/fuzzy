import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


Sensor = ctrl.Antecedent(np.arange(20, 200, 0.1), 'Sensor')
MLeft = ctrl.Consequent(np.arange(0, 100, 0.1), 'MLeft')
MRight = ctrl.Consequent(np.arange(0, 100, 0.1), 'MRight')


Sensor['L1'] = fuzz.gaussmf(Sensor.universe, 50, 10)
Sensor['L2'] = fuzz.gaussmf(Sensor.universe, 200, 10)
Sensor['R1'] = fuzz.gaussmf(Sensor.universe, 50, 10)
Sensor['R2'] = fuzz.gaussmf(Sensor.universe, 200, 10)
Sensor['C1'] = fuzz.gaussmf(Sensor.universe, 50, 10)
Sensor['C2'] = fuzz.gaussmf(Sensor.universe, 200, 10)

MLeft['S'] = fuzz.gaussmf(MLeft.universe, 0, 10)
MLeft['R1'] = fuzz.gaussmf(MLeft.universe, 100, 10)
MLeft['R2'] = fuzz.gaussmf(MLeft.universe, 200, 10)
MLeft['B1'] = fuzz.gaussmf(MLeft.universe, -50, 10)
MLeft['B2'] = fuzz.gaussmf(MLeft.universe, -100, 10)

MRight['S'] = fuzz.gaussmf(MRight.universe, 0, 10)
MRight['R1'] = fuzz.gaussmf(MRight.universe, -100, 10)
MRight['R2'] = fuzz.gaussmf(MRight.universe, 100, 10)
MRight['B1'] = fuzz.gaussmf(MRight.universe, -100, 10)
MRight['B2'] = fuzz.gaussmf(MRight.universe, 100, 10)


rule1 = ctrl.Rule(Sensor['C1'] & Sensor['L2'] & Sensor['R2'], (MLeft['S'], MRight['B2']))
rule2 = ctrl.Rule(Sensor['C1'] & Sensor['L1'], (MLeft['B2'], MRight['R1']))
rule3 = ctrl.Rule(Sensor['C1'] & Sensor['R1'], (MLeft['R1'], MRight['B2']))
rule4 = ctrl.Rule(Sensor['L1'] & Sensor['R2'], (MLeft['B2'], MRight['R1']))
rule5 = ctrl.Rule(Sensor['R1'] & Sensor['L2'], (MLeft['R1'], MRight['B2']))


robot_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
robot = ctrl.ControlSystemSimulation(robot_ctrl)
robot.input['Sensor'] = 40
robot.compute()
print('MLeft:', robot.output['MLeft'])
print('MRight:', robot.output['MRight'])


Sensor.view(sim=robot)

