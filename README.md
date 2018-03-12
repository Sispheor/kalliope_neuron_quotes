# Kalliope quotes neuron

## Synopsis

Get a random quote from an online collection of quotations by authors, celebrities, and newsmakers.

## Installation
```bash
kalliope install --git-url https://github.com/Sispheor/kalliope_neuron_quotes.git
```

## Options

No option


## Return Values

| Name         | Description             | Type   | sample                                                                                                           |
|--------------|-------------------------|--------|------------------------------------------------------------------------------------------------------------------|
| quote_text   | The quote sentence      | string | People may hear your words, but they feel your attitude.People may hear your words, but they feel your attitude. |
| quote_author | The author of the quote | string | John C. Maxwell                                                                                                  |


## Synapses example

Get a random quote and his author
```yml
- name: "quote"
  signals:
    - order: "give me a quote"
  neurons:
    - quotes:
        say_template: "{{ quote_text }} {{ quote_author }}"
```

The neuron only return sentence in english. If you have installed the [translate neuron](https://github.com/Ultchad/kalliope_neuron_translate), you can use it like the following to get a direct translation.
```yml
- name: "quote"
  signals:
    - order: "give me a quote"
  neurons:
    - quotes:
        kalliope_memory:
          quote_text: "{{ quote_text }}"
    - translate:
        lang_in: "en"
        lang_out: "fr"
        sentence: "{{ kalliope_memory['quote_text'] }}"
        say_template: "{{ result }}"
```

## Notes

> **Note:** This neuron return only sentences in english
