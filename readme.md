# Slice of the Prizes

Slice of the Prizes is a Python Script designed to enter the ["Slice of the Action" competition hosted by Pizza Express](https://slice-of-the-action.pizzaexpress.com/) the competition ended on the 15th November 2021. (or is due to end depending on when you're reading this :))

The competition T&Cs were worded loosely meaning this script was NOT in breach of them and thus all entries should be valid.
The T&Cs state
```Entries are limited to one per email address. Multiple entries will be rejected.``` no where in the T&Cs does it state a single person cannot have multiple entries.

The competition itself was also built in a manor which does nothing to prevent multiple entries (other than checking that email hasn't been entered before, to their credit they have logic to block people using the gmail dot and plus "tricks")
Other than this - I was able to submit thousands of entries without changing My:
* IP Address
* Full Name
* Date of Birth
* Postcode

It is worth noting there was no anti bot protection such as a captcha set-up.
(Nor any rate limiting that I noticed, on the first day I received 5000+ prize emails where all entries came from the same IP, under the same name and postcode...)

## Outcome
Here is the list of prizes I received

Good prizes:

Prize Name  | Quantity Received
------------- | -------------
Vespa Motorcycle  | 0
Tech Bundle  | 0
Case of Peroni  | 1
Tickets | 1

Worthless vouchers:

Prize Name  | Quantity Received
------------- | -------------
Doughballs  | 30000+
Dessert  | 5000+
Drink  | 5000+

## Installation
Download the script from this repository.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install imap-tools.

```bash
pip install imap-tools
```

## Usage

Configure the variables in the main.py file or delete-bad-prizes.py file
Review the file and adjust anything else if needed to work with your catchall set-up i.e. folder names etc.

Run the script:
Main script (this will generate entries and claim the prizes)
```bash
python3 main.py
```
Clean-up script (delete-bad-prizes.py)
```bash
python3 main.py
```

## Contributing
I don't expect there will be much use for this script as the competition is due to close in a few weeks however I'm releasing it so others can see how poor the security was on this competition. No limit in terms of names, no captcha, no rate limiting etc...

## License
[MIT](https://choosealicense.com/licenses/mit/)
