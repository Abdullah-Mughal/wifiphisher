import mock
import wifiphisher.common.constants as constants


@mock.patch("wifiphisher.common.constants.pyric.pyw")
def test_does_have_mode_0(pyric):
    """
    Test does_have_mode function when interface has mode available
    """
    pyric.getcard.return_value = None
    pyric.devmodes.return_value = ["AP", "monitor"]

    result = constants.does_have_mode("wlan0", "AP")
    message = "Failed to return True when interface had mode available"

    assert result == True, message


@mock.patch("wifiphisher.common.constants.pyric.pyw")
def test_does_have_mode_1(pyric):
    """
    Test does_have_mode function when interface doesn't have mode available
    """
    pyric.getcard.return_value = None
    pyric.devmodes.return_value = ["AP"]

    result = constants.does_have_mode("wlan0", "monitor")
    message = "Failed to return False when interface doesn't have mode available"

    assert result == False, message


@mock.patch("wifiphisher.common.constants.pyric.pyw")
def test_does_have_mode_2(pyric):
    """
    Test does_have_mode function when interface doesn't have mode available
    """
    pyric.getcard.return_value = None
    pyric.devmodes.return_value = ["AP"]

    result = constants.does_have_mode("wlan0", "monitor")
    message = "Failed to return False when interface doesn't have mode available"

    assert result == False, message

@mock.patch("wifiphisher.common.constants.pyric.pyw")
def test_does_have_mode_3(pyric):
    """
    Test does_have_mode function when interface doesn't have mode available
    """
    pyric.getcard.return_value = None
    pyric.devmodes.return_value = ["AP"]

    result = constants.does_have_mode("wlan0", "monitor")
    message = "Failed to return False when interface doesn't have mode available"

    assert result == False, message
