# email-urls-to-your-pocket-account

This tool sends the top articles from the newspaper 'The Economist' to my Pocket account.
I run on it on my Android phone using the app QPython.

# How it's done :

All the URLs of articles from the print edition can be found each week on : www.economist.com/printedition/.

I'm interested in reading the articles from the section 'Leaders'. This section of the page as a special identifier : id="section-69"
I'm using the Python module BeautifulSoup to parse the HTML content and find the links.

I then send the links to Pocket through my gmail account.

# What you need to do :

- Use a Gmail email address.
- Allow apps to send emails for you, see : https://support.google.com/accounts/answer/6010255?hl=en
- Make sure your Pocket account is linked to the address email you will use to send the links to Pocket.
