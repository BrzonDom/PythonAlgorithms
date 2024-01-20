"""
Dvojrozměrné pole

    Ukázka “pole polí”:
        x = [[0, 1], ['a', True], [1, 1.0, 2, 4]]
        >>> len(x)
        3
        >>> len(x[0])
        2
        >>> x[1][1]
        True
        >>> type(x)
        <class 'list'>
        >>> type(x[0])
        <class 'list'>

    Vytvoření nulové matice o rozměrech 2×3:
        x = []
        for i in range(2):
           x.append([0] * 3)
        >>> print(x)
        [[0, 0, 0], [0, 0, 0]]
"""