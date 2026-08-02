
"""
# constants.py

# Physical constants and neutrino oscillation parameters

# References

# ----------
# - NuFIT 6.x
- Particle Data Group (PDG)
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class OscillationParameters:
    """
    Standard three-flavour neutrino oscillation parameters-
    Angles are in radians
    Mass splittings are in eV^2
    """
    theta12: float
    theta13: float
    theta23: float

    delta_cp: float

    dm21: float
    dm31: float