# Use dev, beta, final to indicate the release type.
VERSION = (0, 1, 2, 'final')


def get_version():
    version = '{0}.{1}'.format(VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '{0}.{1}'.format(version, VERSION[2])
    elif VERSION[3] != 'final':
        version = '{0} {1}'.format(version, VERSION[3])
    return version


def get_short_version():
    return '{0}.{1}'.format(VERSION[0], VERSION[1])
