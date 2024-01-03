def main(link):
    m = Miner(link)
    # m = Miner('https://open.spotify.com/playlist/7lsvxWvgjKhrYdxozfCX2o?si=dZFyaAH0QeKOOhq9-qc9Uw')
    # m = Miner('https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M?si=7HOF1owoRSWQb4UE4bSTdghttps://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M?si=7HOF1owoRSWQb4UE4bSTdg')
    # m = Miner('https://open.spotify.com/playlist/2jpPqqd752TwJccVylOkGu?si=CFRsxXIcTcOamM0GVcjyEg')
    # m = Miner("https://open.spotify.com/user/1votse36w5kojcrxx9305klhd/playlist/5egAP7NR6DOL1pzITmBETv?si=ub6zZwG5RRWqqNCyxWaubA")
    m.scrape()
    songs = m.titles_list
    d = Downloader(songs)