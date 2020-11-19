# iTunes App Store Scraper
This defines a lightweight Python class that can be used to scrape app 
information from the iTunes App Store. It defines a couple of methods that can
be used to get relevant app IDs given a set of parameters, and a couple of 
methods to then scrape data about these app IDs.

Much of this has been adapted from 
[app-store-scraper](https://github.com/facundoolano/app-store-scraper), a 
nodeJS-based scraper that does similar things. But this scraper uses Python.

## Getting started
The following scrapes app details about all apps similar to the first result 
for the 'fortnite' search query:

```python
from itunes_app_scraper.scraper import AppStoreScraper
import asyncio
import pprint

async def main():
    scraper = AppStoreScraper()
    results = await scraper.get_app_ids_for_query("fortnite")
    # similar = await scraper.get_similar_app_ids_for_app(results[0])
    
    async for app in scraper.get_multiple_app_details(results):
        pprint.pprint(app)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

Documentation is not available separately yet, but the code is relatively
simple and you can look in the `scraper.py` file to see what methods are 
available and what their parameters are.

## License
This scraper was developed by the 
[Digital Methods Initiative](https://digitalmethods.net), and is distributed
under the MIT license. See LICENSE for details.