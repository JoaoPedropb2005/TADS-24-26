import pandas as pd
 
def create_example():
    """

    Return data
    """
    data = pd.DataFrame({
        "product": ["café", "guaraná", "pastel" ],
        "price": [6, 5, 7],
        "quantity": [20, 10, 15]
    })

    return data