# errors.py
# Exception classes for anaconda's storage configuration module.
#
# Copyright (C) 2009  Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.  Any Red Hat trademarks that are incorporated in the
# source code or documentation are not subject to the GNU General Public
# License and may only be used or replicated with the express permission of
# Red Hat, Inc.
#
# Red Hat Author(s): Dave Lehman <dlehman@redhat.com>
#

class StorageError(Exception):
    def __init__(self, *args, **kwargs):
        self.hardware_fault = kwargs.pop("hardware_fault", False)
        super(StorageError, self).__init__(*args, **kwargs)

class NoDisksError(StorageError):
    pass

# Device
class DeviceError(StorageError):
    pass

class DeviceCreateError(DeviceError):
    pass

class DeviceDestroyError(DeviceError):
    pass

class DeviceResizeError(DeviceError):
    pass

class DeviceSetupError(DeviceError):
    pass

class DeviceTeardownError(DeviceError):
    pass

class DeviceUserDeniedFormatError(DeviceError):
    pass

# DeviceFormat
class DeviceFormatError(StorageError):
    pass

class FormatCreateError(DeviceFormatError):
    pass

class FormatDestroyError(DeviceFormatError):
    pass

class FormatSetupError(DeviceFormatError):
    pass

class FormatTeardownError(DeviceFormatError):
    pass

class DMRaidMemberError(DeviceFormatError):
    pass

class MultipathMemberError(DeviceFormatError):
    pass

class FSError(DeviceFormatError):
    pass

class FSResizeError(FSError):
    def __init__(self, message, details):
        FSError.__init__(self, message)
        self.details = details

class LUKSError(DeviceFormatError):
    pass

class MDMemberError(DeviceFormatError):
    pass

class PhysicalVolumeError(DeviceFormatError):
    pass

class SinglePhysicalVolumeError(DeviceFormatError):
    pass

class SwapSpaceError(DeviceFormatError):
    pass

class DiskLabelError(DeviceFormatError):
    pass

class InvalidDiskLabelError(DiskLabelError):
    pass

class DiskLabelCommitError(DiskLabelError):
    pass

# devicelibs
class SwapError(StorageError):
    pass

class SuspendError(SwapError):
    pass

class OldSwapError(SwapError):
    pass

class UnknownSwapError(SwapError):
    pass

class MDRaidError(StorageError):
    pass

class RaidError(StorageError):
    pass

class DMError(StorageError):
    pass

class LVMError(StorageError):
    pass

class CryptoError(StorageError):
    pass

class MPathError(StorageError):
    pass

class LoopError(StorageError):
    pass

class BTRFSError(StorageError):
    pass

class BTRFSValueError(BTRFSError, ValueError):
    pass

# DeviceTree
class DeviceTreeError(StorageError):
    pass

class DeviceNotFoundError(StorageError):
    pass

class UnusableConfigurationError(StorageError):
    """ User has an unusable initial storage configuration. """
    pass

# DeviceAction
class DeviceActionError(StorageError):
    pass

# partitioning
class PartitioningError(StorageError):
    pass

class NotEnoughFreeSpaceError(StorageError):
    pass

# udev
class UdevError(StorageError):
    pass

# fstab
class UnrecognizedFSTabEntryError(StorageError):
    pass

class FSTabTypeMismatchError(StorageError):
    pass

# dasd
class DasdFormatError(StorageError):
    pass

# size
class SizePlacesError(StorageError):
    pass

# probing
class UnknownSourceDeviceError(StorageError):
    pass

# factories
class DeviceFactoryError(StorageError):
    pass
