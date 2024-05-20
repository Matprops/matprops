class CLayouts:
    def __init__(self):
        self.title_locations = {
            "tl": (0, 1.1, "left"),
            "tr": (1, 1.1, "right"),
            "bl": (0, -0.1, "left"),
            "br": (1, -0.1, "right"),
        }

    def set_title_location(self, title_locations):
        """
        Sets the proportional charts' title locations.

        Default value:
            title_locations = {
                "tl": (0, 1.1, "left"),
                "tr": (1, 1.1, "right"),
                "bl": (0, -0.1, "left"),
                "br": (1, -0.1, "right")
            }

        Accepts a dictionary with four values for setting the proportional charts' title locations.
        The dictionary can contain any combination of the following keys: "tl", "tr", "bl", and "br".
        Each key corresponds to a specific title location on the chart.

        Each possible key accepts a tuple of three values:
        - Value 1: x value (float): The x-axis value of the title location.
                  This value should be in the range [0, 1], representing the proportional position along the x-axis.
        - Value 2: y value (float): The y-axis value of the title location.
                  This value should be in the range [0, 1], representing the proportional position along the y-axis.
        - Value 3: alignment (str): The alignment value of the title.
                  This value specifies the alignment of the title relative to its location.

        :param title_locations: A dictionary specifying the locations of the proportional charts' titles.
                                If provided, it should contain keys "tl", "tr", "bl", or "br" with corresponding values
                                as tuples of three values for each title location.

        Example usage:
        >>> set_title_location()
        >>> set_title_location({"tl": (0.5, 0.8, "center"), "tr": (0.9, 0.9, "right")})

        """
        title_configs = {"tl", "tr", "bl", "br"}
        try:
            if isinstance(title_locations, dict):
                unexpected_keys = set(title_locations.keys()) - title_configs
                if unexpected_keys:
                    print("The title_locations contains unexpected keys:", unexpected_keys)
                else:
                    self.title_locations.update(title_locations)
            else:
                print("The variable is not a dictionary.")
        except:
            print("Unexpected error occurred")