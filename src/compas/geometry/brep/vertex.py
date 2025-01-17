from compas.data import Data


class BrepVertex(Data):
    """An interface for a Brep Vertex

    Attributes
    ----------
    point : :class:`~compas.geometry.Point`, read_only
        Returns the geometry of this vertex as a 3D point

    """

    # ==============================================================================
    # Properties
    # ==============================================================================

    @property
    def point(self):
        raise NotImplementedError

    # ==============================================================================
    # Constructors
    # ==============================================================================

    @classmethod
    def from_point(cls, point):
        """Creates a Brep vertex from a Point

        Parameters
        ----------
        point: :class:`~compas.geometry.Point`
            The point to create a vertex from

        Returns
        -------
        :class:`~compas.geometry.BrepVertex`
            The created vertex
        """
        raise NotImplementedError
