"""
pmns.py

Construction of the PMNS mixing matrix.
"""

import numpy as np

from .constants import OscillationParameters


class PMNSMatrix:
    """
    PMNS matrix constructor
    """

    def __init__(self, parameters: OscillationParameters):
        self._parameters = parameters
        self._matrix = self._build_matrix()

    @property
    def parameters(self) -> OscillationParameters:
        """
        Oscillation parameters used to construct the PMNS matrix
        """
        return self._parameters

    @property
    def matrix(self) -> np.ndarray:
        """
        Return the PMNS matrix
        """
        return self._matrix

    def _build_matrix(self) -> np.ndarray:
        """
        Build the PMNS matrix.

        Returns
        -------
        numpy.ndarray
            Complex 3x3 PMNS matrix
        """

        theta12 = self._parameters.theta12
        theta13 = self._parameters.theta13
        theta23 = self._parameters.theta23

        delta_cp = self._parameters.delta_cp

        c12 = np.cos(theta12)
        s12 = np.sin(theta12)

        c13 = np.cos(theta13)
        s13 = np.sin(theta13)

        c23 = np.cos(theta23)
        s23 = np.sin(theta23)

        exp_plus = np.exp(1j * delta_cp)
        exp_minus = np.exp(-1j * delta_cp)

        R12 = np.array(
    [
        [c12,  s12, 0],
        [-s12, c12, 0],
        [0,    0,   1],
    ],
    dtype=complex,
)

        U13 = np.array(
    [
         [c13, 0, s13 * exp_minus],
         [0,   1, 0],
         [-s13 * exp_plus, 0, c13],
    ],
    dtype=complex,
)

        R23 = np.array(
    [
       [1, 0, 0],
       [0, c23, s23], 
       [0, -s23, c23],
    ], 
    dtype=complex,
)

        U = R23 @ U13 @ R12
        return U