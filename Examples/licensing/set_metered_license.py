import os

from groupdocs.search import Metered

def set_metered_license():
    public_key = os.environ.get("GROUPDOCS_METERED_PUBLIC_KEY")
    private_key = os.environ.get("GROUPDOCS_METERED_PRIVATE_KEY")

    # Skip the call until real keys are supplied
    if not (public_key and private_key):
        print("Set GROUPDOCS_METERED_PUBLIC_KEY and GROUPDOCS_METERED_PRIVATE_KEY to apply a metered license.")
        return

    # Apply the metered keys before using any search features
    Metered().set_metered_key(public_key, private_key)
    print("Quantity:", Metered.get_consumption_quantity())
    print("Credit:", Metered.get_consumption_credit())

if __name__ == "__main__":
    set_metered_license()