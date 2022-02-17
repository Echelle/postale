r"""
Diffraction Grating
-------------------

A diffraction grating class


SiliconGrating
##############
"""

import numpy as np


class SiliconGrating(object):
    """A Silicon diffraction grating object

    Args:
        sigma (scalar): The groove spacing in micron
        groove_top (scalar): The groove top length in micron
        blaze_angle (scalar): The blaze angle in degrees
        apex_angle (scalar): The Si apex angle in degrees (defaults to 70.53)
        wavelength (scalar): The wavelength incident on the grating (defaults to 0.6328 um)
        incidence_angle (scalar): The incidence angle in degrees as measured from the grating normal (default: blaze angle)
        immersion (bool): Whether the groove is illuminated in immersion or not
    """

    def __init__(
        self,
        sigma,
        groove_top,
        blaze_angle,
        apex_angle=70.53,
        incidence_angle=None,
        wavelength=None,
        immersion=0.6328,
    ):

        self.sigma = sigma
        self.groove_top = groove_top
        self.blaze_angle_degrees = blaze_angle
        self.blaze_angle_radians = np.radians(blaze_angle)

        self.apex_angle_degrees = apex_angle
        self.apex_angle_radians = np.radians(apex_angle)

        self.incidence_angle_degrees = incidence_angle
        self.incidence_angle_radians = np.radians(incidence_angle)

        self.wavelength = wavelength

        if immersion:
            raise NotImplementedError

        # The c_angle is the third angle in the groove triangle
        self.c_angle = 180 - blaze_angle - apex_angle

    @property
    def max_m(self):
        """Computes the maximum conceivable diffraction order :math:`m_{\mathrm{max}}`
        """
        max_m = np.floor(2 * self.sigma / self.wavelength)
        return max_m

    def m_vector(self):
        """Return the vector of diffraction orders :math:`[-m_{max}, \cdots, 0, +m_{max}]`

        Note:
        -----
        Some of the diffraction orders will be NaN
        """
        m_vector = np.arange(-self.max_m, self.max_m + 1, 1)
        return m_vector

    def diffracted_angles(self):
        """Apply the grating equation to compute the angle of each diffracted order"""

        theta_m_radians = np.arcsin(
            np.sin(self.incidence_angle_radians)
            - self.m_vector * self.wavelength / self.sigma
        )
