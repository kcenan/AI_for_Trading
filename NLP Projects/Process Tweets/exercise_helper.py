from bs4 import BeautifulSoup
import requests

def get_tweets():
    
    # Get HTML data
    html_data = requests.get('https://twitter.com/AIForTrading1', params = {'count':'28'}).text

    # Create a BeautifulSoup Object
    page_content = BeautifulSoup(html_data, 'lxml')

    # Find all the <div> tags that have a class="js-tweet-text-container" attribute
    tweets = page_content.find_all('div', class_='js-tweet-text-container')
    
    # Create empty list to hold all out tweets
    all_tweets = []

    # Add each tweet to all_tweets. Use the .strip() method rto eturn a copy of
    # the string with the leading and trailing characters removed.
    for tweet in tweets:
        all_tweets.append(tweet.p.get_text().strip())
        
    # Workaround
    all_tweets = ['The Long-Term Stock Exchange Is Worth a Shot', 'Predicting Stock Performance with Natural Language Deep Learning', 'Comcast Acquiring Time Warner Cable In All Stock Deal Worth $45.2 Billion', 'Facebook stock drops more than 20% after revenue forecast misses', 'Facebook Buying WhatsApp for $16B in Cash and Stock Plus $3B in RSUs', 'Netflix’s ‘death cross’ is the third for FAANG stocks and Nasdaq Composite is next', 'After Yesterday’s Signs of Recovery, Crypto Markets See Drastic Losses', 'MF Sees Australia Risks Tilt to Downside on China, Trade War', 'Bitcoin Cash Clash Is Costing Billions With No End in Sight', 'SEC Crypto Settlements Spur Expectations of Wider ICO Crackdown', 'Nissan’s Drama Looks a Lot Like a Palace Coup', 'Yahoo Finance has apparently killed its API', 'Tesla Tanks After Goldman Downgrades to Sell', 'Goldman Sachs to Open a Bitcoin Trading Operation', 'Tax-Free Bitcoin-To-Ether Trading in US to End Under GOP Plan', 'Goldman Sachs Is Setting Up a Cryptocurrency Trading Desk', 'Robinhood stock trading app confirms $110M raise at $1.3B valuation', 'How I made $500k with machine learning and high frequency trading', "Tesla's Finance Team Is Losing Another Top Executive", 'Finance sites erroneously show Amazon, Apple, other stocks crashing', 'Jeff Bezos Says He Is Selling $1 Billion a Year in Amazon Stock to Finance Race to Space', 'US government commits to publish publicly financed software under Free Software licenses', 'The dream life is having your luggage first out of the carousel each time.', 'Stocks Sink as Apple, Facebook Pace the Tech Wreck: Markets Wrap', "Elon Musk's SpaceX Cuts Loan Deal by $500 Million", 'Nvidia Stock Falls Another 12%', 'Anything is possible in this world! Exhibit A: Creation of a sequel to Superbabies.', 'Elon Musk forced to step down as chairman, TSLA short all the way!']

    return all_tweets