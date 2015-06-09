# This scraper collects all the AFL agents from the AFLPA website

import scraperwiki
import requests
from bs4 import BeautifulSoup

aflpa = requests.get("http://www.aflplayers.com.au/accredited-agents-list/")

agentsoup = BeautifulSoup(aflpa.content)

agentps = agentsoup.find_all("p")

data = []
for i, a in enumerate(agentps):
	if len(a.find_all("br"))>3:
		if a.find_all("br")[0].previousSibling.strip() == 'New South Wales':
			data.append({"id": i, name": a.find_all("br")[1].nextSibling.strip(), "company": a.find_all("br")[2].nextSibling.strip(), "location": a.find_all("br")[-1].nextSibling.strip().replace(u'\xa0', u' ')}) 
		else:
			data.append({"id": i, "name": a.find_all("br")[0].previousSibling.strip(), "company": a.find_all("br")[1].previousSibling.strip(), "location": a.find_all("br")[-1].nextSibling.strip().replace(u'\xa0', u' ')}) 
		

scraperwiki.sqlite.save(unique_keys=["name","company"], data=data, table_name='agents')
