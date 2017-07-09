# Anki Add Root Deck Field
Anki provides some [special fields](https://apps.ankiweb.net/docs/manual.html#special-fields) that can be referenced in your notes. In addition to the built-in `Deck` and `Subdeck`, this addon provides access to a `RootDeck` field. It works like this:

```
Deck: Foods::Fruits::Watermelon
Subdeck: Watermelon
RootDeck: Foods
```

Whereas the `Deck` field is always the full string you enter, `RootDeck` will always just be the first. I use it purely for some fancy aesthetics:

![Example Screenshot](/example.png)

the above is for the deck `Code::DistributedSystems`.

## Installation
Copy `add-root-deck-field.py` to your Anki addon folder (Tools > Add-ons > Open Add-ons folder...). Restart Anki.

## Usage
Once installed, `{{RootDeck}}` will be available inside any template.
