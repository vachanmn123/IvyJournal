# Ivy Journal

`A fully encrypted journal that can be used to store personal info/data.  `

## **Requirements**

### config.json

**This program needs a `config.json` file to work, format of which can be seen below:**

```json
{
    "path_to_storage":"", 	// Path to the journal directory
    "salt": ""			// A random string for data salting (eg. isdjf@83(@_djk))
}
```

### modules

Module requirements for this program can be found in the `requirements.txt` file.

To install all the requirements:

```bash
python3 -m pip install -r requirements.txt
```

## Using the program:

### Step 1:

Run `create_journal.py` using:

```bash
python3 create_journal.py
```

### Step 2:

Now the setup is completed, to start using the program run `main.py` using:

```bash
python3 main.py
```

### Step 3:

Follow the prompts.

## Contributing:

Learn more about contributing [here](https://github.com/github/docs/blob/64158a93d1b910fa82416d5c65f0bf5d85a9ecbb/CONTRIBUTING.md)
