from anki.hooks import addHook

def _addRootDeckField(fields, *args):
    fields["RootDeck"] = fields["Deck"].split("::")[0]
    return fields

addHook("mungeFields", _addRootDeckField)
