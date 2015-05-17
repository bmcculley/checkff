#!/usr/bin/python
from BeautifulSoup import BeautifulSoup
import urlparse, argparse

def grablatest():
	#https://www.mozilla.org/en-US/firefox/all/
	html = open("all.html").read()
	soup = BeautifulSoup(html)

	enTd = soup.find("tr", {"id" : "en-US"})
	enDl = enTd.find("td", {"class" : "download linux64"})

	dlLk = enDl.find("a").get("href")
	parts = urlparse.urlparse(dlLk)
	prodStr = urlparse.parse_qs(parts.query)["product"]
	return prodStr[0].split("-")[1]

def main():
	parser = argparse.ArgumentParser(description='Find out if firefox needs an update.')
	parser.add_argument("installedV", metavar="N", type=str, nargs="+",
                       help="Which version is currently installed?")

	args = parser.parse_args()

	print args.installedV[0] == grablatest()

main()