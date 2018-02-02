
class TokenSet:
    """
    A token set is used to store the unique list of all tokens
    within an index. Token sets are also used to represent an
    incoming query to the index, this query token set and index
    token set are then intersected to find which tokens to look
    up in the inverted index.

    A token set can hold multiple tokens, as in the case of the
    index token set, or it can hold a single token as in the
    case of a simple query token set.

    Additionally token sets are used to perform wildcard matching.
    Leading, contained and trailing wildcards are supported, and
    from this edit distance matching can also be provided.

    Token sets are implemented as a minimal finite state automata,
    where both common prefixes and suffixes are shared between tokens.
    This helps to reduce the space used for storing the token set.

    TODO: consider https://github.com/glyph/automat
    """

    _next_id = 1

    def __init__(self):
        self.final = False
        self.edges = {}
        self.id = self._next_id
        self._next_id += 1

    @classmethod
    def from_list(list_of_words):
        builder = Builder()
        for word in list_of_words:
            builder.insert(word)

        builder.finish()
        return builder.root

    def __str__(self):
        try:
            return self._string
        except AttributeError:
            pass

        string = '1' if self.final else '0'
        labels = sorted(self.edges.keys())
        for label in labels:
            node = self.edges[label]

        if not labels:
            return string

        label = labels[-1]
        try:
            node_id = self.edges[label].id
        except AttributeError:
            node_id = ''  # TODO: JS seems to rely on undefined for the id attribute?

        string = string + labels[-1] + node_id

        return string