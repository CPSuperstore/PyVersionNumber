"""
This module contains the definition of the VersionNumber class
"""
import typing
import warnings


class VersionNumber:
    """
    This class represents a single version number in the Semantic format (MAJOR, MINOR, PATCH)
    See https://semver.org/ for more details on this standard
    """
    def __init__(self, major: typing.Union[str, int], minor: int = None, patch: int = None):
        """
        The constructor for the version number
        :param major: Backwards incompatible changes,
                      or a string containing the version number in the format x.x.x OR x.x
        :param minor: Backwards compatible functionality changes
        :param patch: Backwards compatible bug fixes
        """
        self.major = major
        self.minor = minor
        self.patch = patch

        # if the user passed in a string, unpack the string into the 3 variables
        # it is assumed that the string is in the format x.x.x OR x.x
        if isinstance(major, str):
            try:
                self.major, self.minor, self.patch = major.split(".")
            except ValueError:
                try:
                    self.major, self.minor = major.split(".")
                    self.patch = 0
                except ValueError:
                    raise ValueError("The version number string must be in the format x.x.x OR x.x")

        # ensure the 3 variables are integers
        try:
            self.major = int(self.major)
            self.minor = int(self.minor)
            self.patch = int(self.patch)
        except ValueError:
            raise ValueError("All three values (major, minor, and patch) must be integers!")

        # ensure the 3 variables are greater than or equal to 0
        if self.major < 0:
            warnings.warn("Semantic versioning does not allow MAJOR to be less than 0")

        if self.minor < 0:
            warnings.warn("Semantic versioning does not allow MINOR to be less than 0")

        if self.patch < 0:
            warnings.warn("Semantic versioning does not allow PATCH to be less than 0")

    def __repr__(self):
        return "{}.{}.{}".format(
            self.major, self.minor, self.patch
        )

    def __eq__(self, other):
        if isinstance(other, VersionNumber):
            return self.major == other.major and \
                   self.minor == other.minor and \
                   self.patch == other.patch

        return self.raise_type_error(other)

    def __ne__(self, other):
        if isinstance(other, VersionNumber):
            return self.major != other.major or \
                   self.minor != other.minor or \
                   self.patch != other.patch

        return self.raise_type_error(other)

    def __lt__(self, other):
        if isinstance(other, VersionNumber):
            if self.major < other.major:
                return True
            elif self.major > other.major:
                return False

            if self.minor < other.minor:
                return True
            elif self.minor > other.minor:
                return False

            if self.patch < other.patch:
                return True
            elif self.patch > other.patch:
                return False

            return False

        return self.raise_type_error(other)

    def __gt__(self, other):
        if isinstance(other, VersionNumber):
            if self.major > other.major:
                return True
            elif self.major < other.major:
                return False

            if self.minor > other.minor:
                return True
            elif self.minor < other.minor:
                return False

            if self.patch > other.patch:
                return True
            elif self.patch < other.patch:
                return False

            return False

        return self.raise_type_error(other)

    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return self == other or self > other

    def __add__(self, other):
        if isinstance(other, VersionNumber):
            return VersionNumber(
                self.major + other.major,
                self.minor + other.minor,
                self.patch + other.patch
            )

        return self.raise_type_error(other)

    def __sub__(self, other):
        if isinstance(other, VersionNumber):
            return VersionNumber(
                self.major - other.major,
                self.minor - other.minor,
                self.patch - other.patch
            )

        return self.raise_type_error(other)

    def __mul__(self, other):
        if isinstance(other, VersionNumber):
            return VersionNumber(
                self.major * other.major,
                self.minor * other.minor,
                self.patch * other.patch
            )

        return self.raise_type_error(other)

    def __truediv__(self, other):
        if isinstance(other, VersionNumber):
            return VersionNumber(
                self.major // other.major,
                self.minor // other.minor,
                self.patch // other.patch
            )

        return self.raise_type_error(other)

    def __mod__(self, other):
        if isinstance(other, VersionNumber):
            return VersionNumber(
                self.major % other.major,
                self.minor % other.minor,
                self.patch % other.patch
            )

        return self.raise_type_error(other)

    def __floordiv__(self, other):
        return self / other

    def __pow__(self, power, modulo=None):
        if isinstance(power, VersionNumber):
            return VersionNumber(
                self.major ** power.major,
                self.minor ** power.minor,
                self.patch ** power.patch
            )

        return self.raise_type_error(power)

    def raise_type_error(self, other):
        """
        Raises a type error if the provided type is incompatible with the VersionNumber class
        """
        raise TypeError("Can not compare type '{}' with type '{}'".format(
            self.__class__.__name__, other.__class__.__name__
        ))

    @property
    def in_development(self) -> bool:
        """
        Returns if the version number indicates the product is in development (MAJOR = 0)
        """
        return self.major == 0
