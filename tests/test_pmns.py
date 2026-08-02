"""
Simple test of the PMNS matrix.
"""

import numpy as np

from nuosclab.constants import OscillationParameters
from nuosclab.pmns import PMNSMatrix


# Central values (NuFIT, approximately)
params = OscillationParameters(
    theta12=np.deg2rad(33.44),
    theta13=np.deg2rad(8.57),
    theta23=np.deg2rad(49.2),
    delta_cp=np.deg2rad(197),
    dm21=7.42e-5,
    dm31=2.517e-3,
)

pmns = PMNSMatrix(params)

print("PMNS matrix:")
print(pmns.matrix)

print("\nU†U =")
print(pmns.matrix.conj().T @ pmns.matrix)