import pandas as pd
from passivetotal import analyzer
analyzer.init()

iplist = pd.read_csv("iplist.txt")
for index, record in iplist.iterrows():
    if "#" in record[0]:
        continue
    else:
        ip = analyzer.IPAddress(record[0])
        print(ip.whois.as_df)

# hostname analysis
#analyzer.Hostname('riskiq.net').resolutions.as_df

