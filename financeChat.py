import sys as system
import re as regularExpression
import numpy as nump


hello_response = ["How is it going? Please let me know how can I help you today about investing."]

name_response = [r"Hello \1, let me know your investment question."]

default_response = [
    "Sorry, but I'm not trained to process your words please retry",
    "Coul'd you rephrase?",
    "Be sure to aks investment questions please", 
    "Bear on me, I'm still training my capabilities let's try again"
    ]

investingComplicated_response = ["It isn’t. It is simple but not easy. A bit like going to the gym. Working out and eating well is harder than doing the right thing."]

start_response = ["The first step is to determine what you want to achieve with your investing, whether it’s in the short-term or long-term. Are you primarily saving for retirement, which means you may not access that money for decades? Or is there some other major goal, like an expensive dream trip, that you’d like to take in a few years? Next, you should think about how hands-on you want to be with your investing. Ask yourself, Do I want to get into the nittygritty, evaluating multiple investments, and agree to do that regularly? Or would I rather set it and forget it?"]

type_response = ["Stocks are probably the most well-known option, but picking and choosing individual companies to invest in is not how most people get involved in the market. Instead, you might want to consider an index fund, which invests in the securities included in indexes like the S&P 500 or NASDAQ.\nBonds—investments in which you loan money to a corporation or government at a fixed interest rate—are another major asset category. They tend to offer lower returns than stocks, but there’s typically also less associated risk because their prices are largely based on the creditworthiness of who’s issuing the bond, as well as the bond’s interest rate, and not market fluctuations.\nGenerally, the longer you have before needing the money, the more risk you may be able take on; this might mean that you hold more stock investments (like stock index funds) in your portfolio. But as you draw closer to withdrawing, the more you may want to skew toward conservative assets, like bonds, because you want to decrease the volatility in your portfolio the closer you get to needing the money.\nBeyond stocks and bonds, there are alternative investments, such as real estate or commodities. You can now consider investing in real estate investment trusts, also known as REITs.\nThe same is true for commodities, like precious metals or oil—you don’t have to buy bars of gold or barrels of oil. You can invest in exchange-traded funds, or ETFs, that track commodity markets. Mutual funds are also a way to incorporate a variety of assets into your portfolio, because they can hold stocks, bonds, real estate and commodities.One of the main reasons to consider investing in commodities is that “they serve as inflation hedges” “During times when there’s higher-than-normal inflation, these investments tend to do pretty well. And the closer [you are] to withdrawing your money, the more inflation becomes a concern.”"]

risk_response = ["Being a master stock-picker may sound sexy, but for most investors, it’s probably a bad idea. Studies show that choosing stocks is almost always a losing proposition—even for the pros. “The risk [versus] reward of owning stocks is simply not in your favor”. Plus, the more you trade stocks, the more likely you are to incur trading fees, which eats into any money you’d make.\nThe bottom line: You don’t have a crystal ball. “I think we are very naïve if we feel like we have the secret to selecting which companies will perform well and which will fail”."]

divers_response = ["In a nutshell, diversification means you don’t have all your eggs in one investing basket, which may help protect you if any part of your portfolio falters.\nFor example, if you invest in just one company whose stock goes bust, then your portfolio will go bust. “If I own 2,000 companies in my portfolio, and 10% go bankrupt, I’m still going to be fine,” Blaylock says. “For me, it comes down to the law of large numbers. I’d rather own small pieces of 2,000 companies than 100% of one company.”\nBeing diversified also applies to the industries and asset classes you invest in. It’s important to consider not only being invested in different sectors of the economy, but also investing in a mix of stocks and bonds. Index funds are one way you might further diversify your portfolio because they can track both stock and bond indexes. Bottom line: The broader your portfolio is, the likelier you are to weather a market storm."]

check_response=["To check and track your portfolio depends—on you. Maybe you get joy from watching the numbers go up or perhaps the ups and downs seriously stress you out. “The frequency is less important than having a set schedule,” Blaylock says. Winkler suggests twice a year, or even once a year may be fine if you’re fairly comfortable with how your portfolio is performing.\nThe key is not to move your investments on a whim just because you see a drop in the stock market or hear that the S&P 500 hit a new record. A good rule of thumb is to consider rebalancing once a year to help ensure that your asset allocation (the percentage of your money dedicated to various types of assets) has not strayed too far from what you’re comfortable with, and if your portfolio is more than 5% off from your model asset allocation, think about making some adjustments.\n“Keep from making reactionary decisions”. “Set aside time to review your investments regularly, but outside that, don’t look at them. Just do it on your schedule.”"]

greet_response = [r"A very good \1 for you too"]

creator_response = ["Juan J. Martínez"]

def response():
	return "HikeTech Bot:"
print(response(), "Hello! I'm the HikeTech Bot and I was created to help you on basic investment questions, what's your name?")
for line in system.stdin:
	line=line.lower()
	if regularExpression.search(r"hello .*",line,regularExpression.I):
		print(response(),nump.random.choice(hello_response))
	elif regularExpression.search(r"(bye|exit|good bye|i'm leaving)",line,regularExpression.I):
       		print(response(),"It was my pleasure to chat with you, have a great day!")
       		break
	elif regularExpression.search(r".*?name is(.*)?",line, regularExpression.I):
	        print(response(),regularExpression.sub(r".*?name is(.*)?",nump.random.choice(name_response),line))
	elif regularExpression.search(r".*?(investing|investment) complicated(.*|\?)?",line, regularExpression.I):
                print(response(),regularExpression.sub(r".*?(investing|investment) complicated(.*|\?)?",nump.random.choice(investingComplicated_response),line))
	elif regularExpression.search(r".*?(get started|start)(.*|\?)?",line, regularExpression.I):
                print(response(),regularExpression.sub(r".*?(get started|start)(.*|\?)?",nump.random.choice(start_response),line))
	elif regularExpression.search(r".*?(type.*?investment)(.*|\?)?",line, regularExpression.I):
                print(response(),regularExpression.sub(r".*?(type.*?investment)(.*|\?)?",nump.random.choice(type_response),line))
	elif regularExpression.search(r".*?(risk)(.*|\?)?",line, regularExpression.I):
                print(response(),regularExpression.sub(r".*?(risk)(.*|\?)?",nump.random.choice(risk_response),line))
	elif regularExpression.search(r".*?(diversifi|diverse)(.*|\?)?",line, regularExpression.I):
                print(response(),regularExpression.sub(r".*?(diversifi|diverse)(.*|\?)?",nump.random.choice(divers_response),line))	
	elif regularExpression.search(r".*?(check|track)(.*|\?)?",line, regularExpression.I): 
		print(response(),regularExpression.sub(r".*?(check|track)(.*|\?)?",nump.random.choice(check_response),line))

	elif regularExpression.search(r".*?good (one|morning|afternoon|evening|night)(.*)?",line,regularExpression.I):
		print(response(),regularExpression.sub(r".*?good (one|morning|afternoon|evening)(.*)?",nump.random.choice(greet_response),line))
	elif regularExpression.search(r".*?your.*?creator(.*|\?)*",line,regularExpression.I):
		print(response(),nump.random.choice(creator_response))
	else:
       		print(response(),nump.random.choice(default_response))
