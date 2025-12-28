def chai_falvor(flavor="Masala"):
    """Return the falvor of chai"""
    chai="ginger"

    return flavor

print(chai_falvor.__doc__)
print(chai_falvor.__name__)

help(len)

def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samosa.
    :param chai: Number of chai cups(10 rupees each)
    :param samosa: Number of samosas(15 rupees each)
    :return: (total amount, thank you messaege)
    """
    total = chai * 10 + samosa * 15
    return total,"Thank you for visiting!"